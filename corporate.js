/* Scroll reveals are progressive enhancement: content stays visible without JS. */
(() => {
    if (!('IntersectionObserver' in window) || !Element.prototype.animate) return;
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    const active = new Set();
    const staged = new WeakMap();
    const targets = new Set();
    const group = (selector, direction = 'up', stagger = 85) => {
        document.querySelectorAll(selector).forEach((element, index) => {
            if (targets.has(element)) return;
            targets.add(element);
            staged.set(element, {direction, delay:(index % 3) * stagger});
        });
    };
    document.querySelectorAll('main > section:not(#home)').forEach(section => {
        section.querySelectorAll('.section-title > span, .section-title > h2, .section-title > p').forEach((element,index) => {
            targets.add(element);
            staged.set(element, {direction:'up', delay:index * 100});
        });
    });
    group('.about-portrait', 'left');
    group('.about-story > .eyebrow, .about-story > h3, .about-story > p, .about-pillar, .about-signoff', 'right');
    group('.service-flip, .process-grid > article, #portfolio .row > div');
    group('.training-panel .col-lg-7 > :not(.training-features), .training-features > li');
    group('.training-summary > :not(.training-stats), .training-stat', 'right');
    group('#contact .row > div, .corporate-footer .row > div, .footer-bottom');
    const reveal = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            reveal.unobserve(entry.target);
            entry.target.dataset.revealed = 'true';
            if (reduced.matches || document.body.classList.contains('motion-paused')) return;
            const {direction, delay} = staged.get(entry.target);
            const distance = innerWidth < 600 ? 22 : 36;
            const start = direction === 'left' ? '-' + distance + 'px 0' :
                direction === 'right' ? distance + 'px 0' : '0 ' + distance + 'px';
            const animation = entry.target.animate([
                {opacity:0, translate:start},
                {opacity:1, translate:'0 0'}
            ], {duration:850, delay, easing:'cubic-bezier(.16,1,.3,1)', fill:'backwards'});
            active.add(animation);
            animation.finished.then(() => active.delete(animation)).catch(() => active.delete(animation));
        });
    }, {threshold:.08, rootMargin:'0px 0px -25px 0px'});
    targets.forEach(element => reveal.observe(element));
    const finishMotion = () => {
        if (!reduced.matches && !document.body.classList.contains('motion-paused')) return;
        active.forEach(animation => animation.finish());
        active.clear();
    };
    reduced.addEventListener('change', finishMotion);
    new MutationObserver(finishMotion).observe(document.body, {attributes:true, attributeFilter:['class']});
    // Keyboard navigation must never land on an invisible, delayed element.
    document.addEventListener('focusin', event => {
        active.forEach(animation => {
            if (animation.effect.target.contains(event.target)) animation.finish();
        });
    });
})();

// Keep navigation and admissions accessible on desktop and mobile.
const navigation = document.getElementById('navbarNav');
document.querySelectorAll('#navbarNav a[href^="#"]').forEach(link => {
    link.addEventListener('click', () => {
        if (window.bootstrap && navigation.classList.contains('show')) {
            bootstrap.Collapse.getOrCreateInstance(navigation).hide();
        }
    });
});
const applicationModal = document.getElementById('trainingModal');
applicationModal.addEventListener('shown.bs.modal', () => {
    document.getElementById('trainingName').focus();
});
applicationModal.addEventListener('show.bs.modal', () => {
    if (window.bootstrap && navigation.classList.contains('show')) {
        bootstrap.Collapse.getOrCreateInstance(navigation).hide();
    }
});
const navLinks = document.querySelectorAll('.nav-link');
const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        navLinks.forEach(link => {
            const current = link.getAttribute('href') === '#' + entry.target.id;
            link.classList.toggle('active', current);
            if (current) link.setAttribute('aria-current', 'location');
            else link.removeAttribute('aria-current');
        });
    }
}, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
document.querySelectorAll('main > section[id]').forEach(section => observer.observe(section));

/* Flip cards: hover, touch and keyboard share one accessible state. */
document.querySelectorAll('.service-flip').forEach(card => {
    const front = card.querySelector('.service-front');
    const back = card.querySelector('.service-back');
    const open = card.querySelector('.flip-open');
    const close = card.querySelector('.flip-close');
    const flip = (active, moveFocus = false) => {
        card.classList.toggle('is-flipped', active);
        front.inert = active;
        back.inert = !active;
        front.setAttribute('aria-hidden', String(active));
        back.setAttribute('aria-hidden', String(!active));
        open.setAttribute('aria-expanded', String(active));
        if (moveFocus) (active ? close : open).focus({preventScroll:true});
    };
    card.addEventListener('pointerenter', event => {
        if (event.pointerType === 'mouse' && matchMedia('(hover:hover)').matches) flip(true);
    });
    card.addEventListener('pointerleave', () => {
        if (!card.contains(document.activeElement)) flip(false);
    });
    card.addEventListener('focusout', () => {
        requestAnimationFrame(() => {
            if (!card.contains(document.activeElement) && !card.matches(':hover')) flip(false);
        });
    });
    open.addEventListener('click', () => flip(true, true));
    close.addEventListener('click', () => flip(false, true));
    card.addEventListener('keydown', event => {
        if (event.key === 'Escape') { flip(false, true); event.stopPropagation(); }
    });
});

/* Reuse the application form, with the selected service included in email. */
applicationModal.addEventListener('show.bs.modal', event => {
    const service = event.relatedTarget?.dataset.service;
    const form = applicationModal.querySelector('form');
    const title = document.getElementById('trainingModalTitle');
    const intro = applicationModal.querySelector('.modal-body > p');
    const experience = document.getElementById('trainingExperience');
    const experienceLabel = applicationModal.querySelector('label[for="trainingExperience"]');
    const interest = form.querySelector('input[name="course"],input[name="interest"]');
    interest.name = service ? 'interest' : 'course';
    interest.value = service || 'UI/UX Design - 3 Months / 90 Days';
    form.querySelector('[name="_subject"]').value = service ? 'New Enquiry: ' + service : 'New UI/UX Training Course Application';
    title.textContent = service ? 'Apply for ' + service : 'Apply for UI/UX Training';
    intro.textContent = service ? 'Share your details and a little about your goals. We will contact you to discuss ' + service + '.' : 'Start your 90-day design journey. Share your details and we will contact you about the course.';
    experience.required = !service;
    experienceLabel.textContent = service ? 'Design Experience (Optional)' : 'Design Experience *';
    applicationModal.querySelector('label[for="trainingMessage"]').textContent = service ? 'Project Details or Questions (Optional)' : 'Questions or Learning Goals (Optional)';
    document.getElementById('trainingMessage').placeholder = service ? 'Tell us about your project, goals or requirements' : 'Tell us what you would like to learn';
    form.querySelector('p.small').textContent = service ? 'By submitting, you agree to be contacted about your enquiry. Your details will be sent securely through FormSubmit.' : 'By submitting, you agree to be contacted about this course. Your details will be sent securely through FormSubmit.';
});

/* A bounded particle field, paused off-screen and when reduced motion is enabled. */
(() => {
    const hero = document.querySelector('.corporate-hero');
    const canvas = document.getElementById('hero-particles');
    const context = canvas.getContext('2d');
    if (!context) return;
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
    const pauseButton = document.querySelector('.motion-toggle');
    let width = 0, height = 0, points = [], frame = 0, lastTime = 0;
    let visible = true, manualPause = false;
    const draw = () => {
        context.clearRect(0, 0, width, height);
        points.forEach((point, i) => {
            context.beginPath();
            context.arc(point.x, point.y, point.size, 0, Math.PI * 2);
            context.fillStyle = 'rgba(255,199,95,.55)';
            context.fill();
            for (let j = i + 1; j < points.length; j++) {
                const other = points[j];
                const distance = Math.hypot(point.x - other.x, point.y - other.y);
                if (distance < 125) {
                    context.strokeStyle = 'rgba(255,189,57,' + ((1 - distance / 125) * .13) + ')';
                    context.beginPath();
                    context.moveTo(point.x, point.y);
                    context.lineTo(other.x, other.y);
                    context.stroke();
                }
            }
        });
    };
    const resize = () => {
        width = hero.clientWidth;
        height = hero.clientHeight;
        const scale = Math.min(devicePixelRatio || 1, 2);
        canvas.width = Math.round(width * scale);
        canvas.height = Math.round(height * scale);
        context.setTransform(scale, 0, 0, scale, 0, 0);
        points = Array.from({length:width < 600 ? 24 : 55}, () => ({
            x:Math.random()*width, y:Math.random()*height,
            dx:(Math.random()-.5)*.25, dy:(Math.random()-.5)*.25, size:Math.random()*1.3+.5
        }));
        draw();
    };
    const tick = time => {
        const delta = Math.min((time - lastTime) / 16.67 || 1, 2);
        lastTime = time;
        points.forEach(point => {
            point.x += point.dx * delta; point.y += point.dy * delta;
            if (point.x < 0 || point.x > width) point.dx *= -1;
            if (point.y < 0 || point.y > height) point.dy *= -1;
        });
        draw();
        frame = requestAnimationFrame(tick);
    };
    const sync = () => {
        cancelAnimationFrame(frame); frame = 0;
        const paused = manualPause || reducedMotion.matches || document.hidden;
        document.body.classList.toggle('motion-paused', paused);
        if (!paused && visible) { lastTime = performance.now(); frame = requestAnimationFrame(tick); }
    };
    pauseButton.addEventListener('click', () => {
        manualPause = !manualPause;
        pauseButton.setAttribute('aria-pressed', String(manualPause));
        pauseButton.querySelector('span').textContent = manualPause ? 'Resume motion' : 'Pause motion';
        pauseButton.querySelector('i').className = manualPause ? 'fas fa-play' : 'fas fa-pause';
        sync();
    });
    new ResizeObserver(resize).observe(hero);
    new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }).observe(hero);
    document.addEventListener('visibilitychange', sync);
    reducedMotion.addEventListener('change', sync);
    resize(); sync();
})();
