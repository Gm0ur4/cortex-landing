<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Cortex - Domine o Comportamento Humano em 21 dias. Aprenda os princípios fundamentais do comportamento humano através de atividades práticas.">
    <meta name="theme-color" content="#952791">
    <title>Cortex - Domine o Comportamento Humano em 21 Dias</title>
    
    <style>
        /* ==================== RESET E VARIÁVEIS ==================== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #1a1a2e;
            --primary-light: #16213e;
            --secondary: #0f3460;
            --accent: #e94560;
            --accent-light: #f39c12;
            --success: #27ae60;
            --danger: #c0392b;
            --light-bg: #f8f9fa;
            --light-bg-2: #ecf0f1;
            --white: #FFFFFF;
            --text-dark: #1a1a2e;
            --text-gray: #555555;
            --text-light: #888888;
            --border-light: #d5d8dc;
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
            --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.12);
            --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.15);
            --transition: all 0.3s ease;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            background: #ffffff;
            color: var(--text-gray);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* ==================== CONTAINER E LAYOUT ==================== */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .section {
            padding: 80px 20px;
        }

        @media (max-width: 768px) {
            .section {
                padding: 50px 20px;
            }
        }

        /* ==================== TIPOGRAFIA ==================== */
        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            color: var(--primary);
            line-height: 1.2;
            letter-spacing: -0.02em;
            margin-bottom: 20px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        h2 {
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 40px;
            text-align: center;
            position: relative;
            padding-bottom: 20px;
        }

        h2::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-light) 100%);
            border-radius: 2px;
        }

        h3 {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 15px;
        }

        p {
            font-size: 1rem;
            line-height: 1.8;
            color: var(--text-gray);
        }

        strong {
            color: var(--text-dark);
            font-weight: 700;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2.2rem;
            }

            h2 {
                font-size: 1.8rem;
            }
        }

        /* ==================== BOTÕES ==================== */
        .btn {
            display: inline-block;
            padding: 16px 40px;
            border: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            text-decoration: none;
            cursor: pointer;
            transition: var(--transition);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            text-align: center;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--accent) 0%, #d63447 100%);
            color: var(--white);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(233, 69, 96, 0.4);
        }

        .btn-white {
            background: var(--white);
            color: var(--secondary);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .btn-white:hover {
            transform: scale(1.05);
        }

        .btn-block {
            width: 100%;
            display: block;
        }

        /* ==================== HERO SECTION ==================== */
        .hero {
            text-align: center;
            padding: 100px 20px 80px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: var(--white);
            border-radius: 0;
            margin-bottom: 0;
        }

        .hero h1 {
            margin-bottom: 20px;
        }

        .hero-subtitle {
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 40px;
            line-height: 1.8;
        }

        .hero-subtitle strong {
            color: var(--accent-light);
        }

        .hero-cta {
            display: inline-block;
        }

        /* ==================== PROVA SOCIAL RÁPIDA ==================== */
        .social-proof-quick {
            background: var(--white);
            padding: 60px 20px;
            margin: -40px 20px 40px 20px;
            border-radius: 16px;
            box-shadow: var(--shadow-md);
            position: relative;
            z-index: 10;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 0;
        }

        .stat-card {
            padding: 30px;
            background: var(--white);
            border-radius: 12px;
            border: 2px solid var(--accent);
            text-align: center;
            transition: var(--transition);
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(233, 69, 96, 0.15);
        }

        .stat-number {
            color: var(--accent);
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .stat-label {
            color: var(--text-gray);
            font-size: 0.95rem;
        }

        /* ==================== PROBLEMA ==================== */
        .problem-section {
            background: var(--white);
            padding: 60px 20px;
            margin: 40px 0;
            border-radius: 16px;
            box-shadow: var(--shadow-md);
            border-top: 4px solid var(--danger);
        }

        .problem-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }

        .problem-item {
            padding: 30px;
            background: #fafafa;
            border-radius: 12px;
            border-left: 5px solid var(--danger);
            transition: var(--transition);
        }

        .problem-item:hover {
            background: #f5f5f5;
            box-shadow: var(--shadow-md);
        }

        .problem-item h3 {
            color: var(--danger);
            margin-bottom: 15px;
        }

        /* ==================== SOLUÇÃO ==================== */
        .solution-section {
            background: linear-gradient(135deg, var(--light-bg-2) 0%, var(--light-bg) 100%);
            padding: 60px 20px;
            margin: 40px 0;
            border-radius: 16px;
            border-left: 5px solid var(--accent);
        }

        .quote-box {
            background: var(--white);
            padding: 40px;
            border-radius: 12px;
            border-left: 5px solid var(--accent);
            margin-bottom: 30px;
            box-shadow: var(--shadow-md);
        }

        .quote-text {
            color: var(--primary);
            font-size: 1.3rem;
            font-weight: 700;
            line-height: 1.8;
        }

        .quote-highlight {
            color: var(--accent);
            font-style: italic;
        }

        /* ==================== BENEFÍCIOS ==================== */
        .benefits-section {
            padding: 60px 20px;
            margin: 40px 0;
        }

        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }

        .benefit-card {
            background: var(--white);
            padding: 40px;
            border-radius: 12px;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            text-align: center;
            border-top: 4px solid var(--accent);
        }

        .benefit-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
            border-top-color: var(--secondary);
        }

        .benefit-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        .benefit-card h3 {
            margin-bottom: 15px;
        }

        .benefit-card p {
            font-size: 0.95rem;
            color: var(--text-gray);
        }

        /* ==================== O QUE VOCÊ PERDE ==================== */
        .loses-section {
            background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
            padding: 60px 20px;
            margin: 40px 0;
            border-radius: 16px;
            border-left: 5px solid var(--danger);
        }

        .loses-section h2 {
            color: var(--primary);
        }

        .loses-section h2::after {
            background: linear-gradient(90deg, var(--danger) 0%, #a93226 100%);
        }

        .loses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }

        .lose-item {
            background: var(--white);
            padding: 25px;
            border-radius: 12px;
            box-shadow: var(--shadow-sm);
        }

        .lose-item h3 {
            color: var(--danger);
            margin-bottom: 10px;
        }

        .lose-item p {
            font-size: 0.9rem;
        }

        /* ==================== MICROLEARNING ==================== */
        .microlearning-section {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            padding: 60px 20px;
            margin: 40px 0;
            border-radius: 16px;
            color: var(--white);
        }

        .microlearning-section h2 {
            color: var(--white);
        }

        .microlearning-section h2::after {
            background: var(--accent-light);
        }

        .microlearning-section > .container > p {
            color: rgba(255, 255, 255, 0.9);
        }

        .microlearning-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }

        .microlearning-item {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 12px;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            border-left: 4px solid var(--accent);
        }

        .microlearning-item:hover {
            transform: translateY(-3px);
            background: var(--white);
        }

        .microlearning-item h3 {
            margin-bottom: 10px;
            color: var(--primary);
        }

        .microlearning-item p {
            font-size: 0.9rem;
        }

        /* ==================== CHECKOUT ==================== */
        .checkout-section {
            padding: 80px 20px;
            background: var(--white);
            margin: 40px 0;
            border-radius: 16px;
            box-shadow: var(--shadow-lg);
            border-top: 4px solid var(--accent);
        }

        .checkout-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .checkout-header h2 {
            margin-bottom: 15px;
        }

        .checkout-header p {
            font-size: 1.1rem;
            color: var(--text-gray);
            max-width: 600px;
            margin: 0 auto;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            margin-bottom: 50px;
        }

        .product-card {
            background: var(--white);
            border: 2px solid var(--border-light);
            border-radius: 12px;
            padding: 40px;
            transition: var(--transition);
            position: relative;
        }

        .product-card.featured {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(233, 69, 96, 0.1);
            transform: scale(1.05);
        }

        .product-card.featured::before {
            content: "⭐ MAIS POPULAR";
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(90deg, var(--accent) 0%, #d63447 100%);
            color: var(--white);
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.05em;
            white-space: nowrap;
        }

        .product-card:hover {
            box-shadow: var(--shadow-lg);
        }

        .product-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 15px;
        }

        .product-description {
            color: var(--text-gray);
            margin-bottom: 25px;
            line-height: 1.8;
        }

        .price {
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--accent);
            margin-bottom: 5px;
        }

        .price-small {
            color: var(--text-light);
            font-size: 0.9rem;
            margin-bottom: 25px;
        }

        .features-list {
            list-style: none;
            margin: 25px 0;
        }

        .features-list li {
            color: var(--text-gray);
            padding: 12px 0;
            border-bottom: 1px solid var(--border-light);
            display: flex;
            align-items: center;
            font-size: 0.95rem;
        }

        .features-list li:last-child {
            border-bottom: none;
        }

        .features-list li::before {
            content: "✓";
            color: var(--accent);
            font-weight: 800;
            margin-right: 12px;
            font-size: 1.2rem;
        }

        .btn-checkout {
            background: linear-gradient(135deg, var(--accent) 0%, #d63447 100%);
            color: var(--white);
            border: none;
            padding: 16px 32px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            width: 100%;
            transition: var(--transition);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 20px;
            text-decoration: none;
            display: block;
            text-align: center;
        }

        .btn-checkout:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        }

        /* ==================== ORDER BUMP ==================== */
        .order-bump {
            background: linear-gradient(135deg, #f8f9fa 0%, #ecf0f1 100%);
            border: 2px solid var(--accent-light);
            border-radius: 16px;
            padding: 40px;
            margin: 50px 0;
            position: relative;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .order-bump::before {
            content: "⚡ OFERTA RELÂMPAGO";
            position: absolute;
            top: -15px;
            left: 20px;
            background: linear-gradient(90deg, var(--accent-light) 0%, #e67e22 100%);
            color: var(--white);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.05em;
        }

        .order-bump h3 {
            color: var(--primary);
            font-size: 1.3rem;
            margin-top: 15px;
            margin-bottom: 15px;
        }

        .order-bump p {
            color: var(--text-gray);
            line-height: 1.8;
            margin-bottom: 15px;
        }

        .bump-price {
            font-size: 1.8rem;
            color: var(--accent);
            font-weight: 800;
            margin: 20px 0;
        }

        .bump-original {
            text-decoration: line-through;
            color: var(--text-light);
            font-size: 0.9rem;
            margin-right: 10px;
        }

        .bump-savings {
            background: var(--accent-light);
            color: var(--white);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 700;
        }

        .bump-features {
            color: var(--text-gray);
            margin: 20px 0;
            line-height: 1.8;
        }

        .bump-features p {
            margin: 8px 0;
            font-size: 0.95rem;
        }

        /* ==================== BÔNUS ==================== */
        .bonus-section {
            background: linear-gradient(135deg, var(--light-bg-2) 0%, var(--light-bg) 100%);
            border-radius: 16px;
            padding: 40px;
            margin: 50px 0;
            border-left: 5px solid var(--accent);
        }

        .bonus-section h3 {
            color: var(--primary);
            font-size: 1.5rem;
            margin-bottom: 25px;
            font-weight: 800;
        }

        .bonus-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 20px;
        }

        .bonus-icon {
            font-size: 1.5rem;
            margin-right: 15px;
            min-width: 30px;
        }

        .bonus-content h4 {
            color: var(--primary);
            margin: 0 0 5px 0;
            font-size: 1rem;
            font-weight: 700;
        }

        .bonus-content p {
            color: var(--text-gray);
            margin: 0;
            font-size: 0.9rem;
        }

        /* ==================== DEPOIMENTOS ==================== */
        .testimonials-section {
            padding: 60px 20px;
            margin: 40px 0;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }

        .testimonial-card {
            background: var(--white);
            padding: 30px;
            border-radius: 12px;
            box-shadow: var(--shadow-md);
            border-left: 5px solid var(--accent);
            transition: var(--transition);
        }

        .testimonial-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-lg);
        }

        .stars {
            color: var(--accent-light);
            font-size: 1.2rem;
            margin-bottom: 15px;
        }

        .testimonial-text {
            color: var(--text-gray);
            font-size: 0.95rem;
            line-height: 1.8;
            margin-bottom: 15px;
            font-style: italic;
        }

        .testimonial-author {
            color: var(--primary);
            font-weight: 700;
            font-size: 0.9rem;
        }

        .testimonial-role {
            color: var(--text-light);
            font-size: 0.85rem;
        }

        /* ==================== FAQ ==================== */
        .faq-section {
            padding: 60px 20px;
            margin: 40px 0;
        }

        .faq-item {
            background: var(--white);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 15px;
            box-shadow: var(--shadow-sm);
            cursor: pointer;
            transition: var(--transition);
        }

        .faq-item:hover {
            box-shadow: var(--shadow-md);
        }

        .faq-question {
            color: var(--primary);
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .faq-toggle {
            font-size: 1.5rem;
            transition: var(--transition);
        }

        .faq-item.active .faq-toggle {
            transform: rotate(180deg);
        }

        .faq-answer {
            color: var(--text-gray);
            font-size: 0.95rem;
            line-height: 1.8;
            display: none;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid var(--border-light);
        }

        .faq-item.active .faq-answer {
            display: block;
        }

        /* ==================== CTA FINAL ==================== */
        .final-cta {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            padding: 80px 20px;
            text-align: center;
            border-radius: 16px;
            margin: 60px 0;
        }

        .final-cta h2 {
            color: var(--white);
            margin-bottom: 20px;
        }

        .final-cta h2::after {
            background: var(--accent-light);
        }

        .final-cta p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.2rem;
            margin-bottom: 30px;
            line-height: 1.8;
        }

        /* ==================== URGÊNCIA ==================== */
        .urgency-banner {
            background: linear-gradient(135deg, var(--accent) 0%, #d63447 100%);
            color: var(--white);
            padding: 15px 20px;
            text-align: center;
            font-weight: 700;
            font-size: 1rem;
            border-radius: 8px;
            margin-bottom: 30px;
            animation: pulse 2s infinite;
            box-shadow: 0 8px 24px rgba(233, 69, 96, 0.2);
        }

        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.8;
            }
        }

        .timer {
            display: inline-block;
            background: var(--accent-light);
            color: var(--white);
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 700;
            margin-left: 10px;
            font-size: 0.9rem;
        }

        /* ==================== FOOTER ==================== */
        footer {
            text-align: center;
            color: var(--text-light);
            font-size: 0.9rem;
            padding: 40px 20px;
            border-top: 1px solid var(--border-light);
            margin-top: 60px;
        }

        footer {
            background: var(--primary);
            color: rgba(255, 255, 255, 0.8);
        }

        footer a {
            color: var(--accent-light);
            text-decoration: none;
            transition: var(--transition);
        }

        footer a:hover {
            text-decoration: underline;
        }

        /* ==================== RESPONSIVIDADE ==================== */
        @media (max-width: 768px) {
            .product-card.featured {
                transform: scale(1);
            }

            .products-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 60px 20px 40px;
            }

            .section {
                padding: 50px 20px;
            }

            .order-bump {
                margin: 30px 0;
            }

            .urgency-banner {
                font-size: 0.9rem;
            }

            .timer {
                display: block;
                margin-left: 0;
                margin-top: 10px;
            }
        }

        /* ==================== ACESSIBILIDADE ==================== */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation: none !important;
                transition: none !important;
            }
        }

        /* ==================== SCROLL REVEAL ==================== */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: var(--transition);
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <!-- ==================== HERO SECTION ==================== -->
    <section class="hero">
        <div class="container">
            <h1>🧠 A Cortex é a primeira plataforma desenvolvida para te ensinar comportamento humano em 21 dias</h1>
            <p class="hero-subtitle">
                Somos pioneiros a dar o fim em cursos chatos e PDFs intermináveis.<br>
                <strong>São mais de 15.000 alunos absorvendo o conhecimento dos 22 maiores best-sellers do mundo</strong>
            </p>
            <a href="#checkout" class="btn btn-primary">⚡ Começar Agora</a>
        </div>
    </section>

    <!-- ==================== PROVA SOCIAL RÁPIDA ==================== -->
    <section class="section">
        <div class="container">
            <div class="social-proof-quick">
                <div class="stats-grid">
                    <div class="stat-card">
                        <p class="stat-number">15.000+</p>
                        <p class="stat-label">Usuários ativos</p>
                    </div>
                    <div class="stat-card">
                        <p class="stat-number">98%</p>
                        <p class="stat-label">Taxa de satisfação</p>
                    </div>
                    <div class="stat-card">
                        <p class="stat-number">21</p>
                        <p class="stat-label">Dias para transformação</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== PROBLEMA ==================== -->
    <section class="section">
        <div class="container">
            <div class="problem-section">
                <h2>❌ Qual o problema dos demais que tentam ensinar?</h2>
                <div class="problem-grid">
                    <div class="problem-item">
                        <h3>📚 Sobrecarga de informação</h3>
                        <p>Existem milhares de livros sobre comportamento humano. Qual ler? Por onde começar? Você fica perdido entre teorias complexas e informações contraditórias.</p>
                    </div>
                    <div class="problem-item">
                        <h3>⏰ Tempo desperdiçado</h3>
                        <p>Ler 7.000 páginas leva meses. Assistir cursos chatos leva semanas. Você quer resultados AGORA, não em 6 meses.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== SOLUÇÃO ==================== -->
    <section class="section">
        <div class="container">
            <div class="solution-section">
                <h2>✅ Aprenda com quem é especialista no assunto</h2>
                <div class="quote-box">
                    <p class="quote-text">
                        Você não precisa ler mais de 7.000 páginas para dominar a mente humana. 
                        <span class="quote-highlight">A Cortex já processou, filtrou e organizou o ouro de cada mestre da inteligência humana para você aplicar hoje mesmo.</span>
                    </p>
                </div>
                <p style="text-align: center; color: var(--text-gray); font-size: 1.05rem; line-height: 1.8; margin-top: 30px;">
                    A Cortex é um <strong>programa de 21 dias</strong> com atividades práticas que te ensinam os princípios fundamentais 
                    do comportamento humano. Sem teoria chata. Sem PDFs gigantes. Apenas <strong>o essencial para você aplicar e transformar sua vida.</strong>
                </p>
            </div>
        </div>
    </section>

    <!-- ==================== BENEFÍCIOS ==================== -->
    <section class="section">
        <div class="container">
            <h2>🎯 Características principais</h2>
            <div class="benefits-grid">
                <div class="benefit-card reveal">
                    <div class="benefit-icon">⚡</div>
                    <h3>Aprenda no tempo perfeito</h3>
                    <p>Não em 6 meses. Não em 1 ano. Em apenas 21 dias você terá os conhecimentos que levaria meses para ler em livros e cursos.</p>
                </div>
                <div class="benefit-card reveal">
                    <div class="benefit-icon">🎯</div>
                    <h3>100% prático</h3>
                    <p>Cada dia tem atividades que você faz. Sem teoria chata. Sem vídeos longos. Pura aplicação.</p>
                </div>
                <div class="benefit-card reveal">
                    <div class="benefit-icon">🧠</div>
                    <h3>Baseado em ciência</h3>
                    <p>Todos os conceitos vêm das melhores referências mundiais sobre comportamento humano. Você aprende só o que realmente funciona.</p>
                </div>
                <div class="benefit-card reveal">
                    <div class="benefit-icon">💡</div>
                    <h3>Aplique imediatamente</h3>
                    <p>Aprenda uma técnica e use no mesmo dia. Com seus relacionamentos, no trabalho, em casa. Resultados reais.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== O QUE VOCÊ PERDE ==================== -->
    <section class="section">
        <div class="container">
            <div class="loses-section">
                <h2>⚠️ Quem não entende comportamento humano está à mercê de:</h2>
                <div class="loses-grid">
                    <div class="lose-item">
                        <h3>😔 Relações superficiais</h3>
                        <p>Sem entender comportamento, você fica preso em conflitos. Relacionamentos que poderiam ser incríveis viram frustrantes.</p>
                    </div>
                    <div class="lose-item">
                        <h3>📉 Baixa produtividade</h3>
                        <p>Se não compreende suas próprias motivações, você procrastina. Fica preso em padrões que te impedem de avançar.</p>
                    </div>
                    <div class="lose-item">
                        <h3>💔 Insegurança constante</h3>
                        <p>Sem autoconhecimento? Você fica inseguro. Duvida de si mesmo. Deixa oportunidades passarem.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== MICROLEARNING ==================== -->
    <section class="section">
        <div class="container">
            <div class="microlearning-section">
                <h2>🧬 Microlearning + Neurociência = Aprendizado Real</h2>
                <p style="text-align: center; color: var(--text-gray); font-size: 1.05rem; margin-bottom: 40px; line-height: 1.8;">
                    Cada módulo é projetado com base em como o cérebro realmente aprende. Não é coincidência que você vai reter o conhecimento.
                </p>
                <div class="microlearning-grid">
                    <div class="microlearning-item reveal">
                        <h3>🔗 Links cerebrais</h3>
                        <p>Cada conceito é conectado a exemplos reais. Seu cérebro cria conexões mais fortes e memória duradoura.</p>
                    </div>
                    <div class="microlearning-item reveal">
                        <h3>🌊 Modo difuso</h3>
                        <p>Atividades que ativam o modo difuso do cérebro. Você aprende enquanto relaxa, não através de força bruta.</p>
                    </div>
                    <div class="microlearning-item reveal">
                        <h3>⏱️ Sessões curtas</h3>
                        <p>15-20 minutos por dia. Seu cérebro absorve melhor em sessões curtas e focadas do que em maratonas.</p>
                    </div>
                    <div class="microlearning-item reveal">
                        <h3>🔄 Repetição espaçada</h3>
                        <p>Conceitos são revisitados em intervalos ótimos. Você não esquece. Conhecimento fica para sempre.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== CHECKOUT ==================== -->
    <section class="section" id="checkout">
        <div class="container">
            <div class="checkout-section">
                <div class="checkout-header">
                    <h2>🎁 Escolha seu plano agora</h2>
                    <p>Acesso vitalício a todo o conteúdo. Pagamento único. Sem mensalidades. Comece sua transformação hoje mesmo.</p>
                </div>

                <div class="urgency-banner">
                    ⏰ OFERTA ESPECIAL DE CAMPANHA!
                    <span class="timer" id="timer">Expira em: <span id="countdown">3 dias</span></span>
                </div>

                <div class="products-grid">
                    <!-- Plano 1 -->
                    <div class="product-card">
                        <h3 class="product-title">Plataforma Cortex</h3>
                        <p class="product-description">
                            Aprenda os princípios fundamentais do comportamento humano através de 21 dias de atividades práticas e transformadoras.
                        </p>
                        <div class="price">R$ 39,90</div>
                        <p class="price-small">Acesso vitalício</p>
                        <ul class="features-list">
                            <li>21 dias de aprendizado puro</li>
                            <li>Atividades práticas para aplicação imediata</li>
                            <li>Conteúdo baseado em comportamento humano</li>
                            <li>Acesso vitalício à plataforma</li>
                            <li>Atualizações futuras incluídas</li>
                            <li>Suporte humano todos os dias</li>
                        </ul>
                        <a href="https://seulink.eduzz.com/cortex-ia" target="_blank" class="btn-checkout">Quero acessar agora</a>
                    </div>

                    <!-- Plano 2 (Destacado) -->
                    <div class="product-card featured">
                        <h3 class="product-title">Cortex + Chat IA</h3>
                        <p class="product-description">
                            Aprenda e receba análises comportamentais personalizadas com nossa IA especializada. A melhor combinação para transformação.
                        </p>
                        <div class="price">R$ 79,90</div>
                        <p class="price-small">Acesso vitalício a ambos</p>
                        <ul class="features-list">
                            <li>Acesso a todo aprendizado da plataforma</li>
                            <li>Chat IA com análise comportamental</li>
                            <li>Plano de ação customizado</li>
                            <li>Análise de padrões comportamentais</li>
                            <li>Diagnóstico personalizado</li>
                            <li>Suporte prioritário 24/7</li>
                        </ul>
                        <a href="https://seulink.eduzz.com/cortex-ia-completo" target="_blank" class="btn-checkout">Garantir a experiência completa</a>
                    </div>
                </div>

                <!-- ORDER BUMP -->
                <div class="order-bump">
                    <h3>🤖 Adicione somente a IA por apenas R$ 59,90</h3>
                    <p>
                        Caso queira, adicione somente nossa IA com análise comportamental e receba diagnósticos personalizados, planos de ação e acompanhamento contínuo.
                    </p>
                    <div class="bump-price">
                        R$ 59,90
                        <span class="bump-original">R$ 79,90</span>
                        <span class="bump-savings">-25% OFF</span>
                    </div>
                    <div class="bump-features">
                        <p>✓ Análise de padrões comportamentais</p>
                        <p>✓ Diagnóstico personalizado</p>
                        <p>✓ Soluções para problemas específicos</p>
                        <p>✓ Plano de ação customizado</p>
                        <p>✓ Acesso vitalício</p>
                    </div>
                    <a href="https://seulink.eduzz.com/cortex-ia-chat" target="_blank" class="btn-checkout">Adicionar Chat IA Agora</a>
                </div>

                <!-- BÔNUS -->
                <div class="bonus-section">
                    <h3>🎁 Bônus exclusivos inclusos</h3>
                    <div class="bonus-item">
                        <div class="bonus-icon">📚</div>
                        <div class="bonus-content">
                            <h4>Acesso vitalício</h4>
                            <p>Todo o conteúdo, incluindo suas atualizações, estará disponível para ver e revisar quando quiser.</p>
                        </div>
                    </div>
                    <div class="bonus-item">
                        <div class="bonus-icon">🤖</div>
                        <div class="bonus-content">
                            <h4>Acesso ao Chat IA (se escolher o plano completo)</h4>
                            <p>Seu assistente pessoal de inteligência emocional e comportamento humano 24h por dia, 7 dias por semana.</p>
                        </div>
                    </div>
                    <div class="bonus-item">
                        <div class="bonus-icon">📖</div>
                        <div class="bonus-content">
                            <h4>Suporte rápido e humano</h4>
                            <p>Suporte para responder todas as suas dúvidas, com atendimento de um time de especialistas.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== DEPOIMENTOS ==================== -->
    <section class="section">
        <div class="container">
            <h2>💬 O que dizem nossos clientes</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card reveal">
                    <div class="stars">★★★★★</div>
                    <p class="testimonial-text">
                        "Cortex mudou completamente minha forma de ver relacionamentos. Em 21 dias aprendi mais do que em anos tentando sozinho. Recomendo para todos!"
                    </p>
                    <p class="testimonial-author">Marina Silva</p>
                    <p class="testimonial-role">Psicóloga</p>
                </div>
                <div class="testimonial-card reveal">
                    <div class="stars">★★★★★</div>
                    <p class="testimonial-text">
                        "Nunca pensei que seria tão prático. As atividades diárias são incríveis e realmente funcionam. Minha produtividade aumentou 300%."
                    </p>
                    <p class="testimonial-author">Carlos Mendes</p>
                    <p class="testimonial-role">Empreendedor</p>
                </div>
                <div class="testimonial-card reveal">
                    <div class="stars">★★★★★</div>
                    <p class="testimonial-text">
                        "A IA do Cortex é absurda. Consegui resolver conflitos que tinha há anos. Melhor investimento que já fiz em desenvolvimento pessoal."
                    </p>
                    <p class="testimonial-author">Juliana Costa</p>
                    <p class="testimonial-role">Gerente de Projetos</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== FAQ ==================== -->
    <section class="section">
        <div class="container">
            <h2>❓ Perguntas Frequentes</h2>
            <div class="faq-section">
                <div class="faq-item">
                    <div class="faq-question">
                        <span>Como funciona o acesso à plataforma?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Após a compra, você recebe um email com suas credenciais de acesso. Você pode acessar a plataforma de qualquer dispositivo (computador, tablet, smartphone) a qualquer hora do dia. O acesso é vitalício, então você pode fazer o programa quantas vezes quiser.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Posso acessar em múltiplos dispositivos?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Sim! Você pode acessar sua conta de qualquer dispositivo. Recomendamos começar no computador para melhor experiência, mas você pode continuar no celular ou tablet quando estiver fora de casa.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Quanto tempo preciso dedicar por dia?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Apenas 15-20 minutos por dia. Cada módulo é projetado para ser concluído em uma única sessão. Você pode fazer no seu próprio ritmo, mas recomendamos seguir a sequência de 21 dias para melhores resultados.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>E se eu não gostar? Há garantia?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Oferecemos garantia de satisfação de 30 dias. Se você não ficar satisfeito com o programa, devolvemos 100% do seu dinheiro, sem perguntas. Queremos que você tenha confiança total na sua compra.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Como funciona o Chat IA?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        O Chat IA é um assistente especializado em comportamento humano. Você pode fazer perguntas sobre situações específicas, pedir análises de padrões comportamentais e receber planos de ação personalizados. Funciona 24/7 e está disponível sempre que você precisar.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Preciso ter conhecimento prévio?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Não! O programa é projetado para iniciantes. Começamos do zero e vamos construindo seu conhecimento passo a passo. Não importa seu background, você conseguirá acompanhar perfeitamente.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Como é o suporte?</span>
                        <span class="faq-toggle">▼</span>
                    </div>
                    <div class="faq-answer">
                        Temos um time de especialistas disponível todos os dias para responder suas dúvidas. Você pode nos contatar por email em suporte@inteligenciacortex.com.br e responderemos em até 24 horas. Clientes do plano Cortex + IA têm suporte prioritário 24/7.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==================== CTA FINAL ==================== -->
    <section class="section">
        <div class="container">
            <div class="final-cta">
                <h2>Pronto para dominar o comportamento humano?</h2>
                <p>
                    Não deixe essa oportunidade passar. Junte-se a mais de 15.000 pessoas que já transformaram suas vidas com Cortex.
                </p>
                <a href="#checkout" class="btn btn-white">⚡ Começar Agora</a>
            </div>
        </div>
    </section>

    <!-- ==================== FOOTER ==================== -->
    <footer>
        <div class="container">
            <p>&copy; 2024 Inteligência Cortex. Todos os direitos reservados.</p>
            <p>
                <a href="mailto:suporte@inteligenciacortex.com.br">Contato</a> • 
                <a href="#">Política de Privacidade</a> • 
                <a href="#">Termos de Uso</a>
            </p>
        </div>
    </footer>

    <!-- ==================== JAVASCRIPT ==================== -->
    <script>
        // ==================== COUNTDOWN TIMER ====================
        function initCountdown() {
            const targetDate = new Date();
            targetDate.setDate(targetDate.getDate() + 3);

            function updateCountdown() {
                const now = new Date().getTime();
                const distance = targetDate.getTime() - now;

                if (distance < 0) {
                    document.getElementById('countdown').textContent = 'Oferta expirada';
                    return;
                }

                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

                document.getElementById('countdown').textContent = `${days}d ${hours}h ${minutes}m`;
            }

            updateCountdown();
            setInterval(updateCountdown, 60000);
        }

        // ==================== FAQ ACCORDION ====================
        function initFAQ() {
            const faqItems = document.querySelectorAll('.faq-item');

            faqItems.forEach(item => {
                item.addEventListener('click', function() {
                    this.classList.toggle('active');
                });
            });
        }

        // ==================== SCROLL REVEAL ====================
        function initScrollReveal() {
            const reveals = document.querySelectorAll('.reveal');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1
            });

            reveals.forEach(reveal => {
                observer.observe(reveal);
            });
        }

        // ==================== SMOOTH SCROLL ====================
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // ==================== INIT ====================
        document.addEventListener('DOMContentLoaded', function() {
            initCountdown();
            initFAQ();
            initScrollReveal();
        });
    </script>
</body>
</html>
