
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vikas Kumar - Front-End Developer</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

    <style>
        /* --- CORE VARIABLES --- */
        :root {
            --bg-dark: #050505;
            --primary-gold: #ffbd39;
            --primary-glow: rgba(255, 189, 57, 0.5);
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-white: #ffffff;
            --text-grey: #a9adb8;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-grey);
            font-family: 'Poppins', sans-serif;
            overflow-x: hidden;
            position: relative;
        }

        #particles-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: radial-gradient(circle at center, #11111d 0%, #000000 100%);
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            color: var(--text-white);
            font-weight: 700;
        }

        a {
            text-decoration: none;
            transition: 0.4s ease;
        }

        .btn-custom {
            background: linear-gradient(45deg, var(--primary-gold), #ffca2c);
            color: #000;
            border-radius: 50px;
            padding: 12px 35px;
            font-weight: 600;
            border: none;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 0 20px var(--primary-glow);
            position: relative;
            overflow: hidden;
            z-index: 1;
            transition: all 0.3s ease;
        }

        .btn-custom::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, #fff, rgba(255, 255, 255, 0.5));
            transition: left 0.5s ease;
            z-index: -1;
        }

        .btn-custom:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px var(--primary-glow);
            color: #000;
        }

        .btn-custom:hover::before {
            left: 100%;
        }

        .btn-custom:active {
            transform: translateY(-2px) scale(1.02);
        }

        .navbar {
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(15px);
            padding: 15px 0;
            border-bottom: 1px solid var(--glass-border);
        }

        .navbar-brand {
            font-size: 26px;
            font-weight: 800;
            color: #fff !important;
        }

        .navbar-brand span {
            color: var(--primary-gold);
        }

        .nav-link {
            color: #fff !important;
            margin-left: 20px;
            font-size: 14px;
            text-transform: uppercase;
            position: relative;
        }

        .nav-link {
            position: relative;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary-gold);
            transition: width 0.3s ease;
        }

        .nav-link:hover {
            color: var(--primary-gold) !important;
            text-shadow: 0 0 10px var(--primary-glow);
        }

        .nav-link.active {
            color: var(--primary-gold) !important;
        }

        .nav-link.active::after {
            width: 100%;
        }

        .hero-section {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-section .floating-icon {
            position: absolute;
        }

        .hero-content h1 {
            font-size: 70px;
            margin-bottom: 15px;
        }

        .hero-content h1 span {
            color: transparent;
            background: linear-gradient(to right, var(--primary-gold), #fff);
            -webkit-background-clip: text;
            text-shadow: 0 0 20px var(--primary-glow);
        }

        .typed-text {
            color: var(--primary-gold);
            font-weight: 600;
        }

        .section-title {
            text-align: center;
            margin-bottom: 70px;
            position: relative;
        }

        .section-title h2 {
            font-size: 40px;
            text-transform: uppercase;
            z-index: 2;
            position: relative;
        }

        .section-title span {
            font-size: 90px;
            color: rgba(255, 255, 255, 0.03);
            position: absolute;
            top: -45px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            font-weight: 900;
        }

        .section-title::after {
            display: none;
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
            padding: 40px 30px;
            border-radius: 15px;
            transition: 0.4s;
            height: 100%;
        }

        .glass-card:hover {
            transform: translateY(-10px);
            border-color: var(--primary-gold);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }

        .resume-box {
            position: relative;
            padding-left: 30px;
            margin-bottom: 40px;
            border-left: 2px solid rgba(255, 255, 255, 0.1);
        }

        .resume-box::before {
            content: '';
            position: absolute;
            left: -9px;
            top: 0;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--bg-dark);
            border: 2px solid var(--primary-gold);
            box-shadow: 0 0 10px var(--primary-glow);
        }

        .year {
            font-size: 14px;
            font-weight: 700;
            color: var(--primary-gold);
            background: rgba(255, 189, 57, 0.1);
            display: inline-block;
            padding: 4px 15px;
            border-radius: 20px;
            margin-bottom: 10px;
        }

        .process-item {
            text-align: center;
            position: relative;
            padding: 20px;
        }

        .process-circle {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            border-radius: 50%;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            color: var(--primary-gold);
            transition: 0.4s;
        }

        .glass-card:hover .process-circle {
            background: var(--primary-gold);
            color: #000;
            box-shadow: 0 0 20px var(--primary-glow);
        }

        .step-count {
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 60px;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.03);
            line-height: 1;
            pointer-events: none;
        }

        .service-icon {
            font-size: 45px;
            color: var(--primary-gold);
            margin-bottom: 25px;
        }

        .progress {
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin-bottom: 25px;
        }

        .progress-bar {
            background: var(--primary-gold);
            box-shadow: 0 0 10px var(--primary-glow);
        }

        .portfolio-item {
            border-radius: 15px;
            overflow: hidden;
            position: relative;
            margin-bottom: 30px;
            height: 300px;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            transition: 0.4s;
        }

        .portfolio-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: 0.5s;
        }

        .portfolio-item:hover {
            border-color: var(--primary-gold);
            box-shadow: 0 10px 40px rgba(255, 189, 57, 0.3);
        }

        .portfolio-item:hover img {
            transform: scale(1.1);
        }

        .portfolio-overlay {
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.9);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: 0.4s;
        }

        .portfolio-item:hover .portfolio-overlay {
            opacity: 1;
        }

        .portfolio-content {
            text-align: center;
            padding: 20px;
        }

        .portfolio-content h4 {
            color: var(--primary-gold);
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        .portfolio-content p {
            color: #fff;
            margin-bottom: 15px;
        }

        .portfolio-tech {
            display: flex;
            gap: 8px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .portfolio-tech span {
            padding: 5px 15px;
            background: rgba(255, 189, 57, 0.2);
            border: 1px solid var(--primary-gold);
            border-radius: 20px;
            font-size: 12px;
            color: var(--primary-gold);
        }

        .form-control {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            color: #fff;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .form-control:focus {
            background: rgba(255, 255, 255, 0.05);
            border-color: var(--primary-gold);
            box-shadow: none;
            color: #fff;
        }

        .form-control::placeholder {
            color: #9ca3af;
            opacity: 1;
        }

        .form-control::-webkit-input-placeholder {
            color: #9ca3af;
        }

        .form-control::-moz-placeholder {
            color: #9ca3af;
        }

        .text-muted {
            color: #9ca3af !important;
        }

        .cursor {
            width: 20px;
            height: 20px;
            border: 2px solid var(--primary-gold);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transition: all 0.2s ease;
            transform: translate(-50%, -50%);
        }

        .cursor.hover {
            width: 40px;
            height: 40px;
            border-color: #00ffff;
            background: rgba(0, 255, 255, 0.1);
        }

        .cursor-follower {
            width: 8px;
            height: 8px;
            background: var(--primary-gold);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            transition: all 0.15s ease;
        }

        .cursor-follower.hover {
            width: 15px;
            height: 15px;
            background: #00ffff;
        }

        .education-timeline {
            position: relative;
            padding: 20px 0;
        }

        .edu-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 25px;
            backdrop-filter: blur(10px);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .edu-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, var(--primary-gold), #ffca2c);
            border-radius: 0 10px 10px 0;
        }

        .edu-card:hover {
            transform: translateX(10px);
            border-color: var(--primary-gold);
            box-shadow: 0 15px 40px rgba(255, 189, 57, 0.2);
        }

        .edu-year {
            position: absolute;
            top: 20px;
            right: 25px;
            background: linear-gradient(135deg, var(--primary-gold), #ffca2c);
            color: #000;
            padding: 8px 15px;
            border-radius: 25px;
            font-size: 12px;
            font-weight: 700;
            box-shadow: 0 5px 15px rgba(255, 189, 57, 0.3);
        }

        .edu-content {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .edu-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary-gold), #ffca2c);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 8px 25px rgba(255, 189, 57, 0.3);
            transition: 0.3s;
        }

        .edu-icon i {
            font-size: 24px;
            color: #000;
        }

        .edu-card:hover .edu-icon {
            transform: scale(1.1) rotate(5deg);
            box-shadow: 0 12px 35px rgba(255, 189, 57, 0.5);
        }

        .edu-details h4 {
            color: #fff;
            font-size: 18px;
            font-weight: 700;
            margin: 0 0 8px 0;
            line-height: 1.3;
        }

        .edu-institute {
            color: var(--primary-gold);
            font-size: 14px;
            font-weight: 600;
            margin: 0 0 10px 0;
        }

        .edu-grade {
            color: #9ca3af;
            font-size: 13px;
            margin: 0;
        }

        .edu-grade span {
            color: var(--primary-gold);
            font-weight: 700;
        }

        .skill-tag {
            display: inline-block;
            background: rgba(255, 189, 57, 0.1);
            border: 1px solid rgba(255, 189, 57, 0.3);
            color: var(--primary-gold);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 8px;
            transition: all 0.3s ease;
        }

        .skill-tag:hover {
            background: var(--primary-gold);
            color: #000;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 189, 57, 0.3);
        }

        /* Skills Marquee */
        .skills-marquee {
            position: absolute;
            bottom: 64px;
            left: 0;
            width: 100%;
            height: 80px;
            overflow: hidden;
            display: flex;
            align-items: center;
            border-top: 1px solid rgba(255, 189, 57, 0.2);
            border-bottom: 1px solid rgba(255, 189, 57, 0.2);
        }

        .marquee-track {
            display: flex;
            align-items: center;
            animation: scroll 25s linear infinite;
            width: max-content;
        }

        .skill-item {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-right: 80px;
            padding: 15px 25px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50px;
            border: 1px solid rgba(255, 189, 57, 0.2);
            transition: 0.3s;
        }

        .skill-item:hover {
            background: rgba(255, 189, 57, 0.1);
            border-color: var(--primary-gold);
            transform: translateY(-5px);
        }

        .skill-icon {
            font-size: 32px;
            flex-shrink: 0;
        }

        .skill-name {
            color: #fff;
            font-weight: 600;
            font-size: 16px;
            white-space: nowrap;
        }

        .skill-icon.fa-html5 {
            color: #e34f26;
        }

        .skill-icon.fa-css3-alt {
            color: #1572b6;
        }

        .skill-icon.fa-js {
            color: #f7df1e;
        }

        .skill-icon.fa-react {
            color: #61dafb;
        }

        .skill-icon.fa-figma {
            color: #f24e1e;
        }

        .skill-icon.fa-bootstrap {
            color: #7952b3;
        }

        @keyframes scroll {
            0% {
                transform: translateX(0);
            }

            100% {
                transform: translateX(-50%);
            }
        }

        /* Experience Badge Animation */
        @keyframes floatBadge {

            0%,
            100% {
                transform: translateY(0px) rotate(0deg);
            }

            25% {
                transform: translateY(-10px) rotate(2deg);
            }

            50% {
                transform: translateY(-5px) rotate(0deg);
            }

            75% {
                transform: translateY(-15px) rotate(-2deg);
            }
        }

        @keyframes pulseBadge {

            0%,
            100% {
                box-shadow: 0 10px 20px rgba(255, 189, 57, 0.3), 0 0 0 0 rgba(255, 189, 57, 0.4);
            }

            50% {
                box-shadow: 0 15px 30px rgba(255, 189, 57, 0.5), 0 0 0 10px rgba(255, 189, 57, 0.1);
            }
        }

        @keyframes glowText {

            0%,
            100% {
                text-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            }

            50% {
                text-shadow: 0 0 15px rgba(255, 189, 57, 0.8), 0 0 25px rgba(255, 189, 57, 0.4);
            }
        }

        .experience-badge {
            animation: floatBadge 4s ease-in-out infinite, pulseBadge 2s ease-in-out infinite;
            transition: all 0.3s ease;
        }

        .experience-badge:hover {
            animation-play-state: paused;
            transform: translateY(-20px) scale(1.1) rotate(5deg) !important;
            box-shadow: 0 20px 40px rgba(255, 189, 57, 0.6) !important;
        }

        .experience-badge h3 {
            animation: glowText 3s ease-in-out infinite;
        }

        .experience-badge p {
            animation: glowText 3s ease-in-out infinite 0.5s;
        }

        @keyframes shimmer {
            0% {
                transform: translateX(-100%) rotate(45deg);
            }

            100% {
                transform: translateX(200%) rotate(45deg);
            }
        }

        /* Responsive Design */
        @media(max-width: 1200px) {
            .hero-content h1 {
                font-size: 60px;
            }

            .section-title h2 {
                font-size: 35px;
            }

            .section-title span {
                font-size: 80px;
            }
        }

        @media(max-width: 992px) {
            .hero-content h1 {
                font-size: 50px;
            }

            .section-title h2 {
                font-size: 30px;
            }

            .section-title span {
                font-size: 70px;
            }

            .about-img-wrapper {
                margin-bottom: 40px;
            }

            .experience-badge {
                width: 120px !important;
                height: 120px !important;
                bottom: -20px !important;
                right: -20px !important;
            }

            .experience-badge h3 {
                font-size: 28px !important;
            }

            .experience-badge p {
                font-size: 12px !important;
            }
        }

        @media(max-width: 768px) {
            .hero-content h1 {
                font-size: 40px;
            }

            .hero-content h3 {
                font-size: 20px;
            }

            .section-title h2 {
                font-size: 28px;
            }

            .section-title span {
                font-size: 60px;
                top: -35px;
            }

            .section-title {
                margin-bottom: 50px;
            }

            .navbar-brand {
                font-size: 22px;
            }

            .nav-link {
                margin-left: 10px;
                font-size: 13px;
            }

            .skills-marquee {
                height: 60px;
            }

            .skill-item {
                padding: 10px 20px;
                margin-right: 40px;
            }

            .skill-icon {
                font-size: 24px;
            }

            .skill-name {
                font-size: 14px;
            }

            .glass-card {
                padding: 30px 20px;
            }

            .service-icon {
                font-size: 35px;
                margin-bottom: 20px;
            }

            .edu-card {
                padding: 20px;
                margin-bottom: 20px;
            }

            .edu-content {
                flex-direction: column;
                text-align: center;
                gap: 15px;
            }

            .edu-icon {
                width: 50px;
                height: 50px;
            }

            .edu-icon i {
                font-size: 20px;
            }

            .edu-details h4 {
                font-size: 16px;
            }

            .edu-institute {
                font-size: 13px;
            }

            .edu-grade {
                font-size: 12px;
            }

            .edu-year {
                position: static;
                display: inline-block;
                margin-bottom: 15px;
                font-size: 11px;
                padding: 6px 12px;
            }

            .experience-badge {
                display: none;
            }

            .cursor,
            .cursor-follower {
                display: none;
            }
        }

        @media(max-width: 576px) {
            .hero-content h1 {
                font-size: 32px;
                margin-bottom: 10px;
            }

            .hero-content h3 {
                font-size: 18px;
            }

            .hero-content h4 {
                font-size: 14px;
            }

            .section-title h2 {
                font-size: 24px;
            }

            .section-title span {
                font-size: 50px;
                top: -30px;
            }

            .btn-custom {
                padding: 10px 25px;
                font-size: 12px;
            }

            .glass-card {
                padding: 25px 15px;
            }

            .service-icon {
                font-size: 30px;
            }

            .portfolio-item {
                height: 250px;
            }

            .portfolio-content h4 {
                font-size: 1.2rem;
            }

            .portfolio-content p {
                font-size: 14px;
            }

            .portfolio-tech span {
                font-size: 10px;
                padding: 3px 10px;
            }

            .edu-card {
                padding: 15px;
            }

            .edu-details h4 {
                font-size: 14px;
            }

            .edu-institute {
                font-size: 12px;
            }

            .edu-grade {
                font-size: 11px;
            }

            .skills-marquee {
                bottom: 40px;
                height: 50px;
            }

            .skill-item {
                padding: 8px 15px;
                margin-right: 30px;
            }

            .skill-icon {
                font-size: 20px;
            }

            .skill-name {
                font-size: 12px;
            }
        }

        @media(max-width: 480px) {
            .container {
                padding-left: 15px;
                padding-right: 15px;
            }

            .hero-content h1 {
                font-size: 28px;
            }

            .section-title h2 {
                font-size: 22px;
            }

            .section-title span {
                font-size: 45px;
            }

            .glass-card {
                padding: 20px 10px;
            }

            .edu-content {
                gap: 10px;
            }

            .edu-icon {
                width: 45px;
                height: 45px;
            }

            .edu-icon i {
                font-size: 18px;
            }

            .edu-details h4 {
                font-size: 13px;
            }

            .portfolio-item {
                height: 200px;
            }

            .skills-marquee {
                height: 45px;
            }

            .skill-item {
                padding: 6px 12px;
                margin-right: 25px;
            }

            .skill-icon {
                font-size: 18px;
            }

            .skill-name {
                font-size: 11px;
            }

            .skill-tag {
                font-size: 10px;
                padding: 4px 8px;
            }
        }

        /* Landscape Mobile */
        @media(max-height: 500px) and (orientation: landscape) {
            .hero-section {
                height: auto;
                min-height: 100vh;
                padding: 100px 0 50px;
            }

            .skills-marquee {
                position: relative;
                bottom: auto;
                margin-top: 30px;
            }
        }

        /* Touch Device Optimizations */
        @media(hover: none) and (pointer: coarse) {
            .glass-card:hover {
                transform: none;
            }

            .edu-card:hover {
                transform: none;
            }

            .btn-custom:hover {
                transform: none;
            }

            .portfolio-item:hover img {
                transform: none;
            }

            .portfolio-overlay {
                opacity: 1;
                background: rgba(0, 0, 0, 0.7);
            }
        }
    </style>
</head>

<body>

    <div class="cursor"></div>
    <div class="cursor-follower"></div>

    <canvas id="particles-canvas"></canvas>

    <nav class="navbar navbar-expand-lg fixed-top">
        <div class="container">
            <a class="navbar-brand" href="#">Vikas<span>.</span></a>
            <button class="navbar-toggler bg-secondary" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="#skills">Skills</a></li>
                    <li class="nav-item"><a class="nav-link" href="#resume">Resume</a></li>

                    <li class="nav-item"><a class="nav-link" href="#portfolio">Portfolio</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <section id="home" class="hero-section">
        <div class="hero-content" data-aos="zoom-in" data-aos-duration="1200">
            <h4>HELLO WORLD!</h4>
            <h1>I am <span class="text-gradient">Vikas Kumar</span></h1>
            <h3 class="mb-4 text-white">I'm a <span class="typed-text"></span></h3>
            <div class="mt-4" style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <a href="#contact" class="btn btn-custom">Hire Me</a>
                <!-- <a href="#resume" class="btn btn-custom"
                    style="background: transparent; color: white; border: 1px solid white;">Download CV</a> -->
            </div>
        </div>

        <!-- Skills Marquee -->
        <div class="skills-marquee">
            <div class="marquee-track">
                <div class="skill-item">
                    <i class="skill-icon fab fa-html5"></i>
                    <span class="skill-name">HTML5</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-css3-alt"></i>
                    <span class="skill-name">CSS3</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-js"></i>
                    <span class="skill-name">JavaScript</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-react"></i>
                    <span class="skill-name">React.js</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-figma"></i>
                    <span class="skill-name">Figma</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-bootstrap"></i>
                    <span class="skill-name">Bootstrap</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-html5"></i>
                    <span class="skill-name">HTML5</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-css3-alt"></i>
                    <span class="skill-name">CSS3</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-js"></i>
                    <span class="skill-name">JavaScript</span>
                </div>
                <div class="skill-item">
                    <i class="skill-icon fab fa-react"></i>
                    <span class="skill-name">React.js</span>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="py-5" style="position: relative; overflow: hidden; margin: 120px 0;">
        <div class="container">
            <div class="section-title" data-aos="fade-up">
                <span>About</span>
                <h2>About Me</h2>
            </div>
            <div class="row align-items-center g-5">
                <div class="col-lg-5" data-aos="fade-right">
                    <div style="position: relative; perspective: 1000px;">
                        <div style="position: relative; transform-style: preserve-3d; transition: 0.6s;"
                            class="about-img-wrapper">
                            <div
                                style="position: absolute; inset: -20px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 30px; filter: blur(30px); opacity: 0.2; z-index: -1;">
                            </div>
                            <img src="profile3.jpg" alt="Vikas Kumar"
                                style="width: 100%; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); border: 3px solid var(--primary-gold);">
                            <div class="experience-badge"
                                style="position: absolute; bottom: -30px; right: -30px; width: 150px; height: 150px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-direction: column; box-shadow: 0 10px 20px rgba(255, 189, 57, 0.3); border: 5px solid var(--bg-dark); cursor: pointer;">
                                <h3 style="color: #000; font-size: 36px; font-weight: 900; margin: 0; line-height: 1;">
                                    12 +</h3>
                                <p
                                    style="color: #000; font-size: 14px; font-weight: 600; margin: 0; text-transform: uppercase;">
                                    Years</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7" data-aos="fade-left">
                    <div style="padding-left: 30px;">
                        <h3 style="color: #fff; font-size: 36px; margin-bottom: 20px; font-weight: 800;">                            
                            Front-End Developer 
                            <span style="color: var(--primary-gold);">&</span> Sr. UI/UX Designer
                        </h3>
                        <p style="color: #d1d5db; font-size: 18px; line-height: 1.8; margin-bottom: 25px;">
                            Hello! I'm <span style="color: var(--primary-gold); font-weight: 700;">Vikas Kumar</span>, 
                            a passionate Front-End Developer & Sr. UI/UX Designer with <span style="color: var(--primary-gold); font-weight: 700;">12+ years</span> 
                            of experience in creating stunning and responsive web applications, building scalable, responsive, and accessible web, mobile, and tablet applications for enterprise and consumer-facing products. Proven track record of delivering high-impact solutions for global clients including Kuwait Petroleum Corporation, KPMG, Protiviti, Boubyan Bank, and Eureka.
                        </p>

                        <p style="color: #d1d5db; font-size: 16px; line-height: 1.8; margin-bottom: 30px;">
                            Specialized in <span style="color: var(--primary-gold);">React.js, Tailwind CSS, modern JavaScript,</span> and <span style="color: var(--primary-gold);">component-driven UI architecture</span>, with a strong foundation in <span style="color: var(--primary-gold);">human-centered modern UX design</span>. Adept at translating complex business requirements and user insights into elegant, high-performance interfaces that balance <span style="color: var(--primary-gold);">visual excellence, usability, and speed.</span>
                        </p>

                        <p style="color: #d1d5db; font-size: 16px; line-height: 1.8; margin-bottom: 30px;">
                            Experienced across the full UI lifecycle—from <span style="color: var(--primary-gold);">user research, personas, wireframes, and interactive prototypes</span> to <span style="color: var(--primary-gold);">production-ready front-end implementation</span> within <span style="color: var(--primary-gold);">Agile and CI/CD environments.</span> Known for strong stakeholder collaboration, clean design systems, and delivering pixel-perfect UIs that scale efficiently.
                        </p>


                            
                        <div class="row g-4 mb-4">
                            <div class="col-md-6">
                                <div style="padding: 20px; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 15px; backdrop-filter: blur(10px); transition: 0.3s;"
                                    onmouseover="this.style.borderColor='var(--primary-gold)'; this.style.transform='translateX(10px)';"
                                    onmouseout="this.style.borderColor='var(--glass-border)'; this.style.transform='translateX(0)';">
                                    <div style="display: flex; align-items: center; gap: 15px;">
                                        <i class="fas fa-envelope"
                                            style="font-size: 28px; color: var(--primary-gold);"></i>
                                        <div>
                                            <p
                                                style="margin: 0; font-size: 12px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">
                                                Email</p>
                                            <a href="mailto:vikas.vikaskumar.kumar19@gmail.com"
                                                style="margin: 0; color: #fff; font-weight: 600; font-size: 13px; display: block;">vikas.vikaskumar.kumar19@gmail.com</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div style="padding: 20px; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 15px; backdrop-filter: blur(10px); transition: 0.3s;"
                                    onmouseover="this.style.borderColor='var(--primary-gold)'; this.style.transform='translateX(10px)';"
                                    onmouseout="this.style.borderColor='var(--glass-border)'; this.style.transform='translateX(0)';">
                                    <div style="display: flex; align-items: center; gap: 15px;">
                                        <i class="fas fa-phone"
                                            style="font-size: 28px; color: var(--primary-gold);"></i>
                                        <div>
                                            <p
                                                style="margin: 0; font-size: 12px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">
                                                Phone</p>
                                            <a href="tel:+919634528413"
                                                style="margin: 0; color: #fff; font-weight: 600; font-size: 14px; display: block;">+91
                                                9634528413</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div style="padding: 20px; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 15px; backdrop-filter: blur(10px); transition: 0.3s;"
                                    onmouseover="this.style.borderColor='var(--primary-gold)'; this.style.transform='translateX(10px)';"
                                    onmouseout="this.style.borderColor='var(--glass-border)'; this.style.transform='translateX(0)';">
                                    <div style="display: flex; align-items: center; gap: 15px;">
                                        <i class="fas fa-map-marker-alt"
                                            style="font-size: 28px; color: var(--primary-gold);"></i>
                                        <div>
                                            <p
                                                style="margin: 0; font-size: 12px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">
                                                Location</p>
                                            <p style="margin: 0; color: #fff; font-weight: 600; font-size: 14px;">
                                                Berhampur, Ghaziabad, India</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div style="padding: 20px; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 15px; backdrop-filter: blur(10px); transition: 0.3s;"
                                    onmouseover="this.style.borderColor='var(--primary-gold)'; this.style.transform='translateX(10px)';"
                                    onmouseout="this.style.borderColor='var(--glass-border)'; this.style.transform='translateX(0)';">
                                    <div style="display: flex; align-items: center; gap: 15px;">
                                        <i class="fas fa-briefcase"
                                            style="font-size: 28px; color: var(--primary-gold);"></i>
                                        <div>
                                            <p
                                                style="margin: 0; font-size: 12px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">
                                                Experience</p>
                                            <p style="margin: 0; color: #fff; font-weight: 600; font-size: 14px;">12 +
                                                Years</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <a href="#contact" class="btn btn-custom">Let's Talk <i class="fas fa-arrow-right ms-2"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="services" class="container py-5" style="margin: 120px auto;">
        <div class="section-title" data-aos="fade-up">
            <span>Services</span>
            <h2>What I Do</h2>
        </div>
        <div class="row g-4">
            <div class="col-md-4" data-aos="fade-up">
                <div class="glass-card text-center">
                    <div class="service-icon"><i class="fas fa-laptop-code"></i></div>
                    <h4 style="position: relative;">Front-End Developer
                        <span
                            style="position: absolute; bottom: -8px; left: 50%; transform: translateX(-50%); width: 40px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h4>
                    <p>Building responsive websites using HTML5, CSS3, JavaScript, React, and Tailwind CSS.</p>
                </div>
            </div>
            <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
                <div class="glass-card text-center">
                    <div class="service-icon"><i class="fas fa-pencil-ruler"></i></div>
                    <h4 style="position: relative;">Sr. UI/UX Designer
                        <span
                            style="position: absolute; bottom: -8px; left: 50%; transform: translateX(-50%); width: 40px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h4>
                    <p>Designing beautiful user interfaces and prototypes using Figma and Adobe tools.</p>
                </div>
            </div>
            <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
                <div class="glass-card text-center">
                    <div class="service-icon"><i class="fas fa-rocket"></i></div>
                    <h4 style="position: relative;">Responsive Design
                        <span
                            style="position: absolute; bottom: -8px; left: 50%; transform: translateX(-50%); width: 40px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h4>
                    <p>Creating mobile-friendly designs that work seamlessly across all devices.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="skills" class="container py-5" style="margin: 120px auto;">
        <div class="section-title" data-aos="fade-up">
            <span>Skills</span>
            <h2>My Expertise</h2>
        </div>
        <div class="row g-4">
            
             <div class="col-lg-12 col-md-12" data-aos="fade-up" data-aos-delay="100">
                <div class="glass-card">
                    <!-- <h5 class="text-white mb-3" style="position: relative;"><i class="fas fa-desktop text-warning me-2"></i>Operating Systems
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5> -->
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">Team Leadership & Development</span>
                        <span class="skill-tag">Project Management</span>
                        <span class="skill-tag">UI UX Information Architecture</span>
                        <span class="skill-tag">Agile & Scrum Methodologies</span>
                        <span class="skill-tag">Cross-functional Collaboration</span>
                        <span class="skill-tag">Wireframeing & Prototyping</span>                        
                        <span class="skill-tag">Debugging/Testing</span>
                        <span class="skill-tag">XD/Photoshop/Illustrator</span>
                        <span class="skill-tag">Figma/Zeplin/Sketch</span>
                        <span class="skill-tag">HTML/CSS/JS/jQuery</span>
                        <span class="skill-tag">UI Frameworks (Bootstrap, Angular, MVC .NET, PHP, Wordpress)</span>

                    </div>
                </div>
            </div>

            
            <!-- Operating Systems -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="100">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fas fa-desktop text-warning me-2"></i>Operating Systems
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">Windows</span>
                        <span class="skill-tag">Linux</span>
                        <span class="skill-tag">macOS</span>
                    </div>
                </div>
            </div>

            <!-- Web Technologies -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="200">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fas fa-code text-warning me-2"></i>Web Technologies
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">HTML5</span>
                        <span class="skill-tag">CSS3</span>
                        <span class="skill-tag">JavaScript</span>
                        <span class="skill-tag">jQuery</span>
                        <span class="skill-tag">Bootstrap</span>
                        <span class="skill-tag">Sass</span>
                        <span class="skill-tag">Tailwind CSS</span>
                        <span class="skill-tag">Semantic UI</span>
                    </div>
                </div>
            </div>

            <!-- Frameworks & Libraries -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="300">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fab fa-react text-warning me-2"></i>Frameworks & Libraries
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">AngularJS</span>
                        <span class="skill-tag">ReactJS</span>
                        <span class="skill-tag">UI Integration</span>
                        <span class="skill-tag">Frameworks (Bootstrap, Angular, MVC .NET, PHP, Wordpress)</span>
                    </div>
                </div>
            </div>

            <!-- UI/UX Design & Prototyping -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="400">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fab fa-figma text-warning me-2"></i>UI/UX Design & Prototyping
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">Figma</span>
                        <span class="skill-tag">Adobe Photoshop</span>
                        <span class="skill-tag">Adobe Illustrator</span>
                        <span class="skill-tag">Adobe XD</span>
                        <span class="skill-tag">CorelDRAW</span>
                        <span class="skill-tag">UI Mockups</span>
                        <span class="skill-tag">Interactive Prototyping</span>
                        <span class="skill-tag">Responsive Layout Design</span>
                        <span class="skill-tag">User Interface Design</span>
                        <span class="skill-tag">Strategy & vision presentations</span>
                        <span class="skill-tag">User Research</span>
                        <span class="skill-tag">Wireframes & mock ups</span>
                        <span class="skill-tag">App UI Design</span>
                        <span class="skill-tag">Prototyping using Adobe XD & Invision</span>
                        <span class="skill-tag">Interactive ow with HTML/ CSS/JS/jQuery</span>                        
                    </div>
                </div>
            </div>

            <!-- Development Tools -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="500">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fas fa-tools text-warning me-2"></i>Development Tools
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">Sublime Text</span>
                        <span class="skill-tag">Notepad++</span>
                        <span class="skill-tag">Visual Studio Code</span>
                        <span class="skill-tag">Visual Studio</span>
                        <span class="skill-tag">Cursor AI</span>
                        <span class="skill-tag">GitHub Copilot</span>
                    </div>
                </div>
            </div>

            <!-- AI Skills -->
            <div class="col-lg-6 col-md-6" data-aos="fade-up" data-aos-delay="600">
                <div class="glass-card">
                    <h5 class="text-white mb-3" style="position: relative;"><i
                            class="fas fa-robot text-warning me-2"></i>AI Skills
                        <span
                            style="position: absolute; bottom: -5px; left: 0; width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                    </h5>
                    <div class="skill-tags" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="skill-tag">Prompt Writing</span>
                        <span class="skill-tag">AI-Assisted Development</span>
                        <span class="skill-tag">Cursor AI</span>
                        <span class="skill-tag">GitHub Copilot</span>
                        <span class="skill-tag">ChatGPT</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="resume" class="container py-5" style="margin: 120px auto;">
        <div class="section-title" data-aos="fade-up">
            <span>Resume</span>
            <h2>My Journey</h2>
        </div>
        <div class="row g-5">
            <!-- Left Side: Circular Timeline for Education -->
             <div class="col-lg-12" data-aos="fade-left">
                <h3 class="mb-5 text-white" style="font-size: 28px; position: relative;"><i
                        class="fas fa-briefcase text-warning me-3"></i>Experience
                    <span
                        style="position: absolute; bottom: -8px; left: 0; width: 60px; height: 3px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                </h3>
                <div>
                    <div style="position: relative; padding-left: 100px; margin-bottom: 35px;">
                        <div
                            style="position: absolute; left: 0; top: 0; width: 75px; height: 75px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #000; box-shadow: 0 5px 20px rgba(255, 189, 57, 0.4);">
                            01</div>
                        <div style="background: var(--glass-bg); border-left: 4px solid var(--primary-gold); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid var(--glass-border); transition: 0.3s;"
                            onmouseover="this.style.transform='translateX(5px)'; this.style.borderColor='var(--primary-gold)';"
                            onmouseout="this.style.transform='translateX(0)'; this.style.borderColor='var(--glass-border)';">
                            <div
                                style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                                <h4 style="color: #fff; margin: 0; font-size: 20px;">Sr. Front-End Developer / Sr. UI/UX
                                    Designer</h4>
                                <!-- <span
                                    style="background: var(--primary-gold); color: #000; padding: 5px 15px; border-radius: 20px; font-size: 11px; font-weight: 700; white-space: nowrap;">2022
                                    - Present</span> -->
                            </div>
                            <p
                                style="color: var(--primary-gold); font-weight: 600; margin-bottom: 8px; font-size: 15px;">
                                Intigate Technology Pvt. Ltd.
                            </p>
                            <p>JAN 2013 - PRESENT, NOIDA</p>
                            <p style="color: #9ca3af; margin: 0; line-height: 1.6; font-size: 14px;">I lead a team to
                                design new inte ace & mockups then develop
                                front end pages & maintaining style guides. I create wireframes,
                                prototypes a er clients brie ng. I closely work on market
                                research to get a be er ux. Conveying concepts and providing design direction to the
                                team
                                through renderings, images and e ective wri en and verbal
                                communication; Lead the team designing the overall graphic
                                image including creating concept design layout and illustrations</p>
                        </div>
                    </div>

                    <div style="position: relative; padding-left: 100px; margin-bottom: 35px;">
                        <div
                            style="position: absolute; left: 0; top: 0; width: 75px; height: 75px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #000; box-shadow: 0 5px 20px rgba(255, 189, 57, 0.4);">
                            02</div>
                        <div style="background: var(--glass-bg); border-left: 4px solid var(--primary-gold); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid var(--glass-border); transition: 0.3s;"
                            onmouseover="this.style.transform='translateX(5px)'; this.style.borderColor='var(--primary-gold)';"
                            onmouseout="this.style.transform='translateX(0)'; this.style.borderColor='var(--glass-border)';">
                            <h4 style="color: #fff; margin: 0 0 12px 0; font-size: 20px;">Hivish Technology Pvt. Ltd.
                            </h4>
                            <p>JAN 2012 - DEC 2012, DELHi</p>
                            <p
                                style="color: var(--primary-gold); font-weight: 600; margin-bottom: 8px; font-size: 15px;">
                                Front-End Developer</p>
                            <p style="color: #9ca3af; margin: 0; line-height: 1.6; font-size: 14px;">Redesigning and
                                develop websites, Product branding - Business
                                cards, displays, collateral, brochures. Responsive web designing using HTML, CSS,
                                Javascript Bootstrap.
                            </p>
                        </div>
                    </div>

                    <div style="position: relative; padding-left: 100px;">
                        <div
                            style="position: absolute; left: 0; top: 0; width: 75px; height: 75px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #000; box-shadow: 0 5px 20px rgba(255, 189, 57, 0.4);">
                            03</div>
                        <div style="background: var(--glass-bg); border-left: 4px solid var(--primary-gold); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid var(--glass-border); transition: 0.3s;"
                            onmouseover="this.style.transform='translateX(5px)'; this.style.borderColor='var(--primary-gold)';"
                            onmouseout="this.style.transform='translateX(0)'; this.style.borderColor='var(--glass-border)';">
                            <h4 style="color: #fff; margin: 0 0 12px 0; font-size: 20px;">VT Info Net</h4>
                            <p>MAR 2011 - DEC 2011, DELHi</p>
                            <p
                                style="color: var(--primary-gold); font-weight: 600; margin-bottom: 8px; font-size: 15px;">
                                Web Designer</p>
                            <p style="color: #9ca3af; margin: 0; line-height: 1.6; font-size: 14px;">Redesigning and
                                develop websites, business cards, displays,
                                collateral. Responsive web designing using HTML, CSS,
                                Javascript Bootstrap.</p>
                        </div>
                    </div>
                </div>
            </div>
           

            <!-- Right Side: Layout 5 for Experience -->
              <div class="col-lg-12 mb-5" data-aos="fade-right">
                <h3 class="mb-5 text-white" style="font-size: 28px; position: relative;">
                    <i class="fas fa-graduation-cap text-warning me-3"></i>Education
                    <span
                        style="position: absolute; bottom: -8px; left: 0; width: 60px; height: 3px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                </h3>

                <div class="education-timeline">
                    <!-- BCA -->
                    <div class="edu-card" data-aos="fade-up" data-aos-delay="100">
                        <div class="edu-year">2010-11</div>
                        <div class="edu-content">
                            <div class="edu-icon">
                                <i class="fas fa-graduation-cap"></i>
                            </div>
                            <div class="edu-details">
                                <h4>Diploma in Web Designing</h4>
                                <p class="edu-institute">Flas'n Media Institute</p>
                                <!-- <div class="edu-grade">CGPA: <span>7.81</span></div> -->
                            </div>
                        </div>
                    </div>

                    <!-- 12th HSC -->
                    <div class="edu-card" data-aos="fade-up" data-aos-delay="200">
                        <div class="edu-year">2009</div>
                        <div class="edu-content">
                            <div class="edu-icon">
                                <i class="fas fa-book"></i>
                            </div>
                            <div class="edu-details">
                                <h4>Higher Secondary Certificate</h4>
                                <p class="edu-institute">Agroha Inter Collage</p>
                                <!-- <div class="edu-grade">Percentage: <span>80.57%</span></div> -->
                            </div>
                        </div>
                    </div>

                    <!-- 10th SSC -->
                    <div class="edu-card" data-aos="fade-up" data-aos-delay="300">
                        <div class="edu-year">2007</div>
                        <div class="edu-content">
                            <div class="edu-icon">
                                <i class="fas fa-school"></i>
                            </div>
                            <div class="edu-details">
                                <h4>Higher Secondary Certificate</h4>
                                <p class="edu-institute">Agroha Inter Collage</p>
                                <!-- <div class="edu-grade">Percentage: <span>65.57%</span></div> -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            
        </div>
    </section>

    <section id="portfolio" class="container py-5" style="margin: 120px auto;">
        <div class="section-title" data-aos="fade-up">
            <span>Portfolio</span>
            <h2>Featured Works</h2>
        </div>
        <div class="row g-4">
            <div class="col-md-4" data-aos="zoom-in">
                <div class="portfolio-item">
                    <img src="https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&h=600&fit=crop"
                        alt="Chatalott">
                    <div class="portfolio-overlay">
                        <div class="portfolio-content">
                            <h4 style="position: relative;">Chatalott
                                <span
                                    style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                            </h4>
                            <p>Contact & Productivity Management System</p>
                            <div class="portfolio-tech">
                                <span>HTML5</span>
                                <span>CSS3</span>
                                <span>JavaScript</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4" data-aos="zoom-in" data-aos-delay="100">
                <div class="portfolio-item">
                    <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&h=600&fit=crop"
                        alt="BBOYO Real Estate">
                    <div class="portfolio-overlay">
                        <div class="portfolio-content">
                            <h4 style="position: relative;">BBOYO Real Estate
                                <span
                                    style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                            </h4>
                            <p>Property Listing & Management Platform</p>
                            <div class="portfolio-tech">
                                <span>React.js</span>
                                <span>CSS3</span>
                                <span>Figma</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4" data-aos="zoom-in" data-aos-delay="200">
                <div class="portfolio-item">
                    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=600&fit=crop"
                        alt="Web Design">
                    <div class="portfolio-overlay">
                        <div class="portfolio-content">
                            <h4 style="position: relative;">E-Commerce Design
                                <span
                                    style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                            </h4>
                            <p>Modern online shopping interface</p>
                            <div class="portfolio-tech">
                                <span>React</span>
                                <span>Tailwind</span>
                                <span>Figma</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="py-5" style="position: relative; margin: 120px 0;">
        <div class="container">
            <div class="section-title" data-aos="fade-up">
                <span>Contact</span>
                <h2>Get in Touch</h2>
            </div>
            <div class="row g-4 mb-5">
                <div class="col-md-4" data-aos="fade-up">
                    <div class="glass-card text-center"
                        style="padding: 40px 20px; position: relative; overflow: hidden;">
                        <div
                            style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 50%; filter: blur(60px); opacity: 0.15;">
                        </div>
                        <div
                            style="width: 80px; height: 80px; margin: 0 auto 25px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(255, 189, 57, 0.3); transform: rotate(45deg);">
                            <i class="fas fa-phone"
                                style="font-size: 32px; color: #000; transform: rotate(-45deg);"></i>
                        </div>
                        <h4 style="color: #fff; margin-bottom: 15px; font-size: 22px; position: relative;">Phone
                            <span
                                style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                        </h4>
                        <a href="tel:+919634528413"
                            style="color: #9ca3af; margin: 0; font-size: 16px; display: block; transition: 0.3s;"
                            onmouseover="this.style.color='var(--primary-gold)';"
                            onmouseout="this.style.color='#9ca3af';">+91 9634528413</a>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
                    <div class="glass-card text-center"
                        style="padding: 40px 20px; position: relative; overflow: hidden;">
                        <div
                            style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 50%; filter: blur(60px); opacity: 0.15;">
                        </div>
                        <div
                            style="width: 80px; height: 80px; margin: 0 auto 25px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(255, 189, 57, 0.3); transform: rotate(45deg);">
                            <i class="fas fa-envelope"
                                style="font-size: 32px; color: #000; transform: rotate(-45deg);"></i>
                        </div>
                        <h4 style="color: #fff; margin-bottom: 15px; font-size: 22px; position: relative;">Email
                            <span
                                style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                        </h4>
                        <a href="mailto:vikas.vikaskumar.kumar19@gmail.com"
                            style="color: #9ca3af; margin: 0; font-size: 16px; word-break: break-word; display: block; transition: 0.3s;"
                            onmouseover="this.style.color='var(--primary-gold)';"
                            onmouseout="this.style.color='#9ca3af';">vikas.vikaskumar.kumar19@gmail.com</a>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
                    <div class="glass-card text-center"
                        style="padding: 40px 20px; position: relative; overflow: hidden;">
                        <div
                            style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 50%; filter: blur(60px); opacity: 0.15;">
                        </div>
                        <div
                            style="width: 80px; height: 80px; margin: 0 auto 25px; background: linear-gradient(135deg, var(--primary-gold), #ffca2c); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(255, 189, 57, 0.3); transform: rotate(45deg);">
                            <i class="fab fa-linkedin-in"
                                style="font-size: 32px; color: #000; transform: rotate(-45deg);"></i>
                        </div>
                        <h4 style="color: #fff; margin-bottom: 15px; font-size: 22px; position: relative;">LinkedIn
                            <span
                                style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%); width: 30px; height: 2px; background: linear-gradient(90deg, var(--primary-gold), transparent);"></span>
                        </h4>
                        <a href="https://linkedin.com/in/imvikaskt" target="_blank" rel="noopener noreferrer"
                            style="color: #9ca3af; margin: 0; font-size: 16px; display: block; transition: 0.3s;"
                            onmouseover="this.style.color='var(--primary-gold)';"
                            onmouseout="this.style.color='#9ca3af';">linkedin.com/in/imvikaskt</a>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <footer
        style="background: linear-gradient(180deg, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.95) 100%); border-top: 1px solid rgba(255, 189, 57, 0.1); position: relative; overflow: hidden;">
        <div
            style="position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, var(--primary-gold), transparent);">
        </div>
        <div class="container py-5">
            <div class="row g-4">
                <div class="col-lg-4 col-md-6">
                    <h3 style="color: #fff; font-size: 32px; font-weight: 800; margin-bottom: 20px;">Vikas<span
                            style="color: var(--primary-gold);">.</span></h3>
                    <p style="color: #9ca3af; line-height: 1.8; margin-bottom: 25px;">Sr. Front-End Developer & Sr. UI/UX
                        Designer passionate about creating beautiful and functional web experiences.</p>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h5
                        style="color: #fff; font-size: 18px; font-weight: 700; margin-bottom: 25px; position: relative; padding-bottom: 10px;">
                        Quick Links
                        <span
                            style="position: absolute; bottom: 0; left: 0; width: 40px; height: 2px; background: var(--primary-gold);"></span>
                    </h5>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 12px;"><a href="#home"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>Home</a></li>
                        <li style="margin-bottom: 12px;"><a href="#about"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>About</a></li>
                        <li style="margin-bottom: 12px;"><a href="#services"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>Services</a></li>
                        <li style="margin-bottom: 12px;"><a href="#portfolio"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>Portfolio</a></li>
                        <li style="margin-bottom: 12px;"><a href="#contact"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>Contact</a></li>
                    </ul>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5
                        style="color: #fff; font-size: 18px; font-weight: 700; margin-bottom: 25px; position: relative; padding-bottom: 10px;">
                        Services
                        <span
                            style="position: absolute; bottom: 0; left: 0; width: 40px; height: 2px; background: var(--primary-gold);"></span>
                    </h5>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 12px;"><a href="#"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right" style="font-size: 10px; margin-right: 8px;"></i>Web
                                Development</a></li>
                        <li style="margin-bottom: 12px;"><a href="#"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right" style="font-size: 10px; margin-right: 8px;"></i>UI/UX
                                Design</a></li>
                        <li style="margin-bottom: 12px;"><a href="#"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right"
                                    style="font-size: 10px; margin-right: 8px;"></i>Responsive Design</a></li>
                        <li style="margin-bottom: 12px;"><a href="#"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right" style="font-size: 10px; margin-right: 8px;"></i>React
                                Development</a></li>
                        <li style="margin-bottom: 12px;"><a href="#"
                                style="color: #9ca3af; font-size: 15px; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)'; this.style.paddingLeft='5px';"
                                onmouseout="this.style.color='#9ca3af'; this.style.paddingLeft='0';"><i
                                    class="fas fa-chevron-right" style="font-size: 10px; margin-right: 8px;"></i>Figma
                                Design</a></li>
                    </ul>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5
                        style="color: #fff; font-size: 18px; font-weight: 700; margin-bottom: 25px; position: relative; padding-bottom: 10px;">
                        Contact Info
                        <span
                            style="position: absolute; bottom: 0; left: 0; width: 40px; height: 2px; background: var(--primary-gold);"></span>
                    </h5>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 15px; display: flex; align-items: start; gap: 12px;">
                            <i class="fas fa-map-marker-alt"
                                style="color: var(--primary-gold); font-size: 16px; margin-top: 3px;"></i>
                            <span style="color: #9ca3af; font-size: 15px; line-height: 1.6;">Berhampur, Ghaziabad, India</span>
                        </li>
                        <li style="margin-bottom: 15px; display: flex; align-items: start; gap: 12px;">
                            <i class="fas fa-phone"
                                style="color: var(--primary-gold); font-size: 16px; margin-top: 3px;"></i>
                            <a href="tel:+919634528413"
                                style="color: #9ca3af; font-size: 15px; line-height: 1.6; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)';"
                                onmouseout="this.style.color='#9ca3af';">+91 9634528413</a>
                        </li>
                        <li style="margin-bottom: 15px; display: flex; align-items: start; gap: 12px;">
                            <i class="fas fa-envelope"
                                style="color: var(--primary-gold); font-size: 16px; margin-top: 3px;"></i>
                            <a href="mailto:vikas.vikaskumar.kumar19@gmail.com"
                                style="color: #9ca3af; font-size: 15px; line-height: 1.6; word-break: break-word; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)';"
                                onmouseout="this.style.color='#9ca3af';">vikas.vikaskumar.kumar19@gmail.com</a>
                        </li>
                        <li style="margin-bottom: 15px; display: flex; align-items: start; gap: 12px;">
                            <i class="fab fa-linkedin-in"
                                style="color: var(--primary-gold); font-size: 16px; margin-top: 3px;"></i>
                            <a href="https://linkedin.com/in/imvikaskt" target="_blank" rel="noopener noreferrer"
                                style="color: #9ca3af; font-size: 15px; line-height: 1.6; transition: 0.3s;"
                                onmouseover="this.style.color='var(--primary-gold)';"
                                onmouseout="this.style.color='#9ca3af';">linkedin.com/in/imvikaskt</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding: 25px 0; background: rgba(0,0,0,0.5);">
            <div class="container">
                <p style="margin: 0; color: #9ca3af; font-size: 15px; text-align: center;">&copy; 2026 <span
                        style="color: var(--primary-gold); font-weight: 600;">Vikas Kumar</span>. All Rights Reserved.
                    | Designed with <i class="fas fa-heart" style="color: var(--primary-gold);"></i> by Vikas</p>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="https://unpkg.com/typed.js@2.0.16/dist/typed.umd.js"></script>

    <script>
        AOS.init({ duration: 1000, once: true });

        var typed = new Typed('.typed-text', {
            strings: ['Front-End Developer.', 'UI/UX Designer.', 'Web Designer.'],
            typeSpeed: 50, backSpeed: 30, loop: true
        });

        // Background Particles
        const canvas = document.getElementById("particles-canvas");
        const ctx = canvas.getContext("2d");
        canvas.width = window.innerWidth; canvas.height = window.innerHeight;
        let particlesArray = [];

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2;
                this.speedX = (Math.random() * 1) - 0.5;
                this.speedY = (Math.random() * 1) - 0.5;
            }
            update() {
                this.x += this.speedX; this.y += this.speedY;
                if (this.x > canvas.width || this.x < 0) this.speedX = -this.speedX;
                if (this.y > canvas.height || this.y < 0) this.speedY = -this.speedY;
            }
            draw() {
                ctx.fillStyle = "rgba(255, 189, 57, 0.5)";
                ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2); ctx.fill();
            }
        }
        function init() { for (let i = 0; i < 80; i++) particlesArray.push(new Particle()); }
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particlesArray.length; i++) {
                particlesArray[i].update(); particlesArray[i].draw();
                for (let j = i; j < particlesArray.length; j++) {
                    const dx = particlesArray[i].x - particlesArray[j].x;
                    const dy = particlesArray[i].y - particlesArray[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 100) {
                        ctx.strokeStyle = `rgba(255, 189, 57, ${0.1 - dist / 1000})`;
                        ctx.beginPath(); ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                        ctx.lineTo(particlesArray[j].x, particlesArray[j].y); ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animate);
        }
        init(); animate();
        window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });

        // Custom Cursor
        const cursor = document.querySelector('.cursor');
        const cursorFollower = document.querySelector('.cursor-follower');

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';

            setTimeout(() => {
                cursorFollower.style.left = e.clientX + 'px';
                cursorFollower.style.top = e.clientY + 'px';
            }, 100);
        });

        // Cursor hover effect on clickable elements
        const hoverElements = document.querySelectorAll('a, button, .btn, .glass-card, .portfolio-item, input, textarea');
        hoverElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.classList.add('hover');
                cursorFollower.classList.add('hover');
            });
            el.addEventListener('mouseleave', () => {
                cursor.classList.remove('hover');
                cursorFollower.classList.remove('hover');
            });
        });

        // Smooth Scroll on Menu Click and All Links
        document.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener('click', function (e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId !== '#') {
                    e.preventDefault();
                    const targetSection = document.querySelector(targetId);
                    if (targetSection) {
                        const navbarHeight = document.querySelector('.navbar').offsetHeight;
                        const targetPosition = targetSection.offsetTop - navbarHeight - 20;
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                }
            });
        });

        // Scroll Spy - Active Menu on Scroll
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (window.pageYOffset >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) {
                    link.classList.add('active');
                }
            });
        });


    </script>
</body>

</html>
