/* Shared interactions for the homepage and the India career guide. */
(() => {
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    const header = document.querySelector('.navbar');
    const menu = document.getElementById('navbarNav');
    document.querySelectorAll('#navbarNav a').forEach(link => link.addEventListener('click', () => {
        if (menu?.classList.contains('show') && window.bootstrap) bootstrap.Collapse.getOrCreateInstance(menu).hide();
    }));
    const links = [...document.querySelectorAll('#navbarNav .nav-link')].filter(link => link.getAttribute('href').startsWith('#'));
    const sections = links.map(link => document.getElementById(link.hash.slice(1))).filter(Boolean);
    let queued = false;
    const syncNav = () => {
        queued = false;
        if (!sections.length) return;
        const position = scrollY + (header?.offsetHeight || 90) + 80;
        let current = sections[0];
        sections.forEach(section => { if (section.offsetTop <= position) current = section; });
        if (scrollY + innerHeight >= document.documentElement.scrollHeight - 4) current = sections[sections.length - 1];
        links.forEach(link => {
            const selected = link.hash === '#' + current.id;
            link.classList.toggle('active', selected);
            if (selected) link.setAttribute('aria-current', 'location');
            else link.removeAttribute('aria-current');
        });
    };
    addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(syncNav); } }, {passive:true});
    addEventListener('resize', syncNav);
    addEventListener('load', syncNav);
    syncNav();

    if ('IntersectionObserver' in window) {
        const counts = new IntersectionObserver(entries => entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            counts.unobserve(entry.target);
            const el = entry.target, target = Number(el.dataset.count), suffix = el.dataset.suffix || '';
            el.dataset.counted = 'true';
            if (reduced.matches || document.body.classList.contains('motion-paused')) return;
            const start = performance.now();
            const step = time => {
                const progress = Math.min((time - start) / 1200, 1);
                el.textContent = Math.round(target * (1 - Math.pow(1-progress, 3))) + suffix;
                if (progress < 1 && !reduced.matches && !document.body.classList.contains('motion-paused')) requestAnimationFrame(step);
                else el.textContent = target + suffix;
            };
            requestAnimationFrame(step);
        }), {threshold:.5});
        document.querySelectorAll('[data-count]').forEach(el => counts.observe(el));
        const reveals = new IntersectionObserver(entries => entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            reveals.unobserve(entry.target);
            if (!reduced.matches && !document.body.classList.contains('motion-paused') && entry.target.animate) {
                entry.target.animate([{opacity:0,translate:'0 24px'},{opacity:1,translate:'0 0'}], {duration:750,easing:'cubic-bezier(.16,1,.3,1)'});
            }
        }), {threshold:.08});
        document.querySelectorAll('.student-project,.testimonial-card,.placement-strip,.contact-form-card,.contact-info-panel,.coaching-stats,.founder-quote,.guide-page .fade-up').forEach(el => reveals.observe(el));
    }

    const caseNames = ["Mobile commerce","Daily habits","Travel discovery","Learning platform","Finance dashboard","Community app"];
    const briefs = [
        ['Find the right product faster','Map the browse-to-checkout journey, compare category navigation and design clear product and cart states.','Show your research questions, information architecture and an accessible checkout prototype.'],
        ['Help a new habit feel achievable','Explore reminder preferences, build an onboarding flow and design progress feedback without pressure.','Present a task flow, a small component set and your usability-test plan.'],
        ['Make trip planning easier to compare','Organise destinations, dates and saved options; explain how filters help travellers make a decision.','Demonstrate search, empty states and a mobile booking prototype.'],
        ['Help learners find their next lesson','Investigate course discovery, progress visibility and how learners return to unfinished work.','Build a course dashboard with reusable cards and a clear lesson flow.'],
        ['Turn complex numbers into useful information','Prioritise essential account information and explore clear labels, readable charts and transaction states.','Explain hierarchy, accessibility choices and the limitations of the concept.'],
        ['Make it easier to join a community','Map discovery, joining and posting, considering moderation and member privacy from the beginning.','Document personas, interaction states and a prototype of the core journey.']
    ];
    const dialog = document.getElementById('caseStudyDialog');
    let caseTrigger;
    if (dialog) {
        document.querySelectorAll('[data-case]').forEach(link => link.addEventListener('click', event => {
            event.preventDefault();
            const index = Number(link.dataset.case);
            caseTrigger = link;
            document.getElementById('caseStudyTitle').textContent = caseNames[index];
            const image = document.getElementById('caseStudyImage');
            image.src = 'g_img_0' + (index + 1) + '.png';
            image.alt = caseNames[index] + ' design reference';
            const body = document.getElementById('caseStudyBody');
            body.replaceChildren();
            ['The challenge','Suggested approach','Portfolio deliverable'].forEach((heading, n) => {
                const title = document.createElement('h3');
                title.textContent = heading;
                const text = document.createElement('p');
                text.textContent = briefs[index][n];
                body.append(title, text);
            });
            dialog.showModal();
        }));
        dialog.querySelector('.case-close').addEventListener('click', () => dialog.close());
        dialog.querySelector('.case-academy').addEventListener('click', () => dialog.close());
        dialog.addEventListener('close', () => caseTrigger?.focus({preventScroll:true}));
        dialog.addEventListener('click', event => {
            const box = dialog.getBoundingClientRect();
            if (event.target === dialog && (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom)) dialog.close();
        });
    }

    document.querySelectorAll('[data-enquiry]').forEach(form => {
        form.noValidate = true;
        const status = form.querySelector('.form-status');
        const submit = form.querySelector('[type="submit"]');
        const ready = form.querySelector('.whatsapp-ready');
        const originalSubmit = submit.innerHTML;
        let sending = false;
        const message = (text, state) => {
            status.textContent = text;
            status.dataset.state = state;
        };
        const fields = () => [...form.querySelectorAll('input:not([type="hidden"]), textarea, select')];
        const validate = () => {
            let firstInvalid;
            fields().forEach(field => {
                field.setCustomValidity('');
                if (typeof field.value === 'string' && field.tagName !== 'SELECT') field.value = field.value.trim();
                if (field.name === 'phone' && field.value && !/^\+?[\d \-]+$/.test(field.value)) field.setCustomValidity('Enter a valid phone number.');
                if (field.name === 'phone' && field.value && (field.value.replace(/\D/g,'').length < 10 || field.value.replace(/\D/g,'').length > 15)) field.setCustomValidity('Enter a phone number with 10 to 15 digits.');
                if (field.name === 'name' && field.value && field.value.length < 2) field.setCustomValidity('Please enter your full name.');
                const valid = field.checkValidity();
                field.setAttribute('aria-invalid', String(!valid));
                let error = form.querySelector('#' + field.id + '-error');
                if (!error && field.id) {
                    error = document.createElement('small');
                    error.id = field.id + '-error';
                    error.className = 'field-error';
                    field.after(error);
                }
                if (error) {
                    field.setAttribute('aria-describedby', error.id);
                    error.textContent = valid ? '' : field.validationMessage;
                }
                if (!valid && !firstInvalid) firstInvalid = field;
            });
            if (firstInvalid) {
                message('Please check the highlighted fields.', 'error');
                firstInvalid.focus();
                return false;
            }
            return true;
        };
        const whatsappURL = data => {
            const lines = ['Hello, I would like to enquire about ' + (data.get('interest') || data.get('course') || form.dataset.source) + '.'];
            ['name','phone','email','experience','message'].forEach(key => {
                if (data.get(key)) lines.push(key.charAt(0).toUpperCase() + key.slice(1) + ': ' + data.get(key));
            });
            return 'https://wa.me/917983744423?text=' + encodeURIComponent(lines.join('\n'));
        };
        const prepareWhatsApp = data => {
            ready.href = whatsappURL(data);
            ready.hidden = false;
            return ready.href;
        };
        form.querySelector('.whatsapp-submit').addEventListener('click', () => {
            if (!validate()) return;
            const url = prepareWhatsApp(new FormData(form));
            message('Your message is ready. Review it in WhatsApp and press Send. No email has been sent by this action.', 'ready');
            window.open(url, '_blank', 'noopener,noreferrer');
        });
        form.addEventListener('input', event => {
            if (event.target.setCustomValidity) event.target.setCustomValidity('');
            if (sending) return;
            submit.disabled = false;
            submit.innerHTML = originalSubmit;
            status.textContent = '';
            ready.hidden = true;
        });
        form.addEventListener('submit', async event => {
            event.preventDefault();
            if (sending || !validate()) return;
            const data = new FormData(form);
            data.set('page', location.href.split('#')[0]);
            prepareWhatsApp(data);
            sending = true;
            submit.disabled = true;
            submit.textContent = 'Sending…';
            message('Submitting your enquiry…', 'loading');
            const controller = new AbortController();
            const timeout = setTimeout(() => controller.abort(), 25000);
            try {
                const response = await fetch('https://formsubmit.co/ajax/vikas.vikaskumar.kumar19@gmail.com', {
                    method:'POST', body:data, headers:{Accept:'application/json'}, signal:controller.signal
                });
                const result = await response.json();
                if (!response.ok || !(result.success === true || result.success === 'true')) throw new Error('Submission not accepted');
                message('Thank you! Your request has been submitted. You can also continue the conversation on WhatsApp.', 'success');
                submit.textContent = 'Submitted';
            } catch (error) {
                message('We could not confirm your email submission. Your details are still here—please retry or continue on WhatsApp.', 'error');
                submit.disabled = false;
                submit.innerHTML = originalSubmit;
            } finally {
                clearTimeout(timeout);
                sending = false;
            }
        });
    });
})();

