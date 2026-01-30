import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cortex - Domine o Comportamento Humano",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- ESTILO PREMIUM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    html, body, .stApp {
        background: linear-gradient(135deg, #020930 0%, #BE90E3 100%) !important;
    }
    
    /* Container Principal */
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    /* HERO SECTION */
    .hero {
        padding: 80px 20px;
        text-align: center;
    }
    
    .hero h1 {
        color: #FFFFFF;
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0 0 20px 0;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        color: #666;
        font-size: 1.3rem;
        margin-bottom: 30px;
        line-height: 1.6;
    }

    .hero-subtitle strong {
        color: #FFFFFF;
    }
    
    .hero-cta {
        display: inline-block;
        background: linear-gradient(90deg, #FFB800 0%, #EDAB00 100%);
        color: white;
        padding: 18px 40px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1.1rem;
        text-decoration: none;
        cursor: pointer;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        box-shadow: 0 10px 30px rgba(55, 208, 135, 0.3);
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(55, 208, 135, 0.4);
    }
    
    /* PROBLEMA */
    .problem-section {
        background: white;
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
    }
    
    .problem-section h2 {
        color: #952791;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 800;
    }
    
    .problem-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        margin-bottom: 30px;
    }
    
    @media (max-width: 768px) {
        .problem-grid {
            grid-template-columns: 1fr;
        }
    }
    
    .problem-item {
        padding: 30px;
        background: rgba(55, 208, 135, 0.08);
        border-radius: 12px;
        border-left: 5px solid #37D087;
    }
    
    .problem-item h3 {
        color: #37D087;
        font-size: 1.2rem;
        margin: 0 0 15px 0;
        font-weight: 700;
    }
    
    .problem-item p {
        color: #666;
        line-height: 1.6;
        margin: 0;
    }
    
    /* SOLUÇÃO */
    .solution-section {
        background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
        border-left: 5px solid #37D087;
    }

    .urgency-text {
    font-size: 2.0rem;
}
    
    .solution-section h2 {
        color: #952791;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 800;
    }
    
    .quote-box {
        background: white;
        padding: 40px;
        border-radius: 12px;
        border-left: 5px solid #37D087;
        margin-bottom: 40px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .quote-text {
        color: #952791;
        font-size: 1.3rem;
        font-weight: 700;
        line-height: 1.6;
        margin: 0;
    }
    
    .quote-highlight {
        color: #37D087;
        font-style: italic;
    }
    
    /* BENEFÍCIOS */
    .benefits-section {
        padding: 60px 20px;
        margin: 40px 0;
    }
    
    .benefits-section h2 {
        color: #952791;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 800;
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
    }
    
    .benefit-card {
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        text-align: center;
        border-top: 4px solid #37D087;
    }
    
    .benefit-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
    }
    
    .benefit-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    
    .benefit-card h3 {
        color: #952791;
        font-size: 1.2rem;
        margin: 0 0 15px 0;
        font-weight: 700;
    }
    
    .benefit-card p {
        color: #666;
        line-height: 1.6;
        margin: 0;
        font-size: 0.95rem;
    }
    
    /* MICROLEARNING */
    .microlearning-section {
        background: linear-gradient(135deg, #F3E5F5 0%, #FCE4EC 100%);
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
    }
    
    .microlearning-section h2 {
        color: #952791;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 800;
    }
    
    .microlearning-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
    }
    
    .microlearning-item {
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .microlearning-item h3 {
        color: #952791;
        font-size: 1.1rem;
        margin: 0 0 10px 0;
        font-weight: 700;
    }
    
    .microlearning-item p {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.6;
        margin: 0;
    }
    
    /* PROVA SOCIAL */
    .social-proof {
        background: white;
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        text-align: center;
    }
    
    .social-proof h2 {
        color: #952791;
        font-size: 2.2rem;
        margin-bottom: 50px;
        font-weight: 800;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
        margin-bottom: 50px;
    }
    
    .stat-card {
        padding: 30px;
        background: white;
        border-radius: 12px;
        border: 2px solid #37D087;
    }
    
    .stat-number {
        color: #37D087 !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        line-height: 1 !important;
        display: block !important;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.95rem;
        margin: 10px 0 0 0;
    }
    
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
    }
    
    .testimonial-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #37D087;
    }
    
    .stars {
        color: #FFD700;
        font-size: 1.2rem;
        margin-bottom: 15px;
    }
    
    .testimonial-text {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 15px;
        font-style: italic;
    }
    
    .testimonial-author {
        color: #952791;
        font-weight: 700;
        font-size: 0.9rem;
    }
    
    /* O QUE VOCÊ PERDE */
    .loses-section {
        background: linear-gradient(135deg, #FFE8E8 0%, #FFF5F5 100%);
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
        border-left: 5px solid #FF6B6B;
    }
    
    .loses-section h2 {
        color: #FF6B6B;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 800;
    }
    
    .loses-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
    }
    
    .lose-item {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .lose-item h3 {
        color: #FF6B6B;
        font-size: 1.1rem;
        margin: 0 0 10px 0;
        font-weight: 700;
    }
    
    .lose-item p {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.6;
        margin: 0;
    }
    
    /* FAQ */
    .faq-section {
        padding: 60px 20px;
        margin: 40px 0;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 255, 254, 0.95) 100%);
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    }
    
    .faq-section h2 {
        color: #952791;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 60px;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    
    .faq-item {
        background: white;
        border-radius: 16px;
        padding: 0;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #37D087;
        transition: all 0.3s ease;
        overflow: hidden;
    }
    
    .faq-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(55, 208, 135, 0.2);
        border-left-color: #39D7FE;
    }
    
    .faq-item[open] {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0FFFE 100%);
    }
    
    .faq-question {
        color: #952791;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 25px;
        margin: 0;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 15px;
        transition: all 0.3s ease;
        list-style: none;
    }
    
    .faq-question::before {
        content: '';
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #37D087 0%, #39D7FE 100%);
        border-radius: 50%;
        color: white;
        font-weight: 800;
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    
    .faq-item:nth-of-type(1) .faq-question::before {
        content: '1';
    }
    
    .faq-item:nth-of-type(2) .faq-question::before {
        content: '2';
    }
    
    .faq-item:nth-of-type(3) .faq-question::before {
        content: '3';
    }
    
    .faq-item:nth-of-type(4) .faq-question::before {
        content: '4';
    }
    
    .faq-item:nth-of-type(5) .faq-question::before {
        content: '5';
    }
    
    .faq-item:nth-of-type(6) .faq-question::before {
        content: '6';
    }
    
    .faq-answer {
        color: #555;
        font-size: 0.95rem;
        line-height: 1.8;
        padding: 0 25px 25px 80px;
        border-top: 2px solid #37D087;
        margin-top: 0;
        display: none;
    }
    
    .faq-item[open] .faq-answer {
        display: block;
        animation: slideDown 0.3s ease;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .faq-answer strong {
        color: #37D087;
        font-weight: 800;
    }
    
    /* CTA FINAL */
    .final-cta {
        background: linear-gradient(90deg, #39D7FE 0%, #39D7FE 100%);
        padding: 80px 20px;
        text-align: center;
        border-radius: 16px;
        margin: 60px 0;
    }
    
    .final-cta h2 {
        color: white;
        font-size: 2.5rem;
        margin: 0 0 20px 0;
        font-weight: 800;
    }
    
    .final-cta p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    .final-cta-btn {
        display: inline-block;
        background: white;
        color: #37D087;
        padding: 18px 50px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1.1rem;
        text-decoration: none;
        cursor: pointer;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .final-cta-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* DEMO SECTION */
    .demo-section {
        background: #FAE4EE;
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        text-align: center;
    }
    
    .demo-section h2 {
        color: #952791;
        font-size: 2.2rem;
        margin-bottom: 30px;
        font-weight: 800;
    }
    
    .demo-btn {
        display: inline-block;
        background: linear-gradient(90deg, #37D087 0%, #37D087 100%);
        color: white;
        padding: 16px 40px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        text-decoration: none;
        cursor: pointer;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .demo-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(55, 208, 135, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.9rem;
        padding: 40px 20px;
        border-top: 1px solid #e0e0e0;
        margin-top: 60px;
    }
    
    .footer a {
        color: #952791;
        text-decoration: none;
    }
    
    .footer a:hover {
        text-decoration: underline;
    }
    
    /* ===== CHECKOUT STYLES ===== */
    .checkout-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 20px;
        background: white !important;
    }
    
    /* Header */
    .header {
        text-align: center;
        margin-bottom: 50px;
    }
    
    .header h1 {
        color: #952791;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
    }
    
    .header p {
        color: #666;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    
    /* Urgência */
    .urgency-banner {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E72 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 700;
        font-size: 1rem;
    }
    
    /* Grid de Produtos */
    .products-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 50px;
    }
    
    @media (max-width: 768px) {
        .products-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Card de Produto */
    .product-card {
        background: white;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
    }
    
    .product-card.featured {
        border: 2px solid #37D087;
        background: linear-gradient(135deg, #FFFFFF 0%, #F0FFFE 100%);
    }
    
    .product-card.featured::before {
        content: "MAIS POPULAR";
        display: block;
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        width: fit-content;
        margin: -50px 0 20px 0;
        letter-spacing: 0.05em;
    }
    
    .product-title {
        color: #952791;
        font-size: 1.5rem;
        font-weight: 800;
        margin: 0 0 15px 0;
    }
    
    .product-description {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 25px;
    }
    
    .price {
        font-size: 2.5rem;
        color: #952791;
        font-weight: 800;
        margin: 20px 0;
    }
    
    .price-small {
        font-size: 0.9rem;
        color: #999;
        margin-bottom: 25px;
    }
    
    .features-list {
        list-style: none;
        padding: 0;
        margin: 25px 0;
    }
    
    .features-list li {
        color: #666;
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
        display: flex;
        align-items: center;
    }
    
    .features-list li:last-child {
        border-bottom: none;
    }
    
    .features-list li::before {
        content: "✓";
        color: #37D087;
        font-weight: 800;
        margin-right: 12px;
        font-size: 1.2rem;
    }
    
    .btn-checkout {
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: white;
        border: none;
        padding: 16px 32px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 20px;
    }
    
    .btn-checkout:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(55, 208, 135, 0.3);
    }
    
    /* Order Bump */
    .order-bump {
        background: linear-gradient(135deg, #FFF9E6 0%, #FFFBF0 100%);
        border: 2px solid #FFD700;
        border-radius: 16px;
        padding: 30px;
        margin: 40px 0;
        position: relative;
    }
    
    .order-bump::before {
        content: "⚡ OFERTA RELÂMPAGO";
        position: absolute;
        top: -15px;
        left: 20px;
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.05em;
    }
    
    .order-bump h3 {
        color: #952791;
        font-size: 1.3rem;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    .order-bump p {
        color: #666;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .bump-price {
        font-size: 1.8rem;
        color: #952791;
        font-weight: 800;
        margin: 15px 0;
    }
    
    .bump-original {
        text-decoration: line-through;
        color: #999;
        font-size: 0.9rem;
        margin-right: 10px;
    }
    
    .bump-savings {
        background: #FFD700;
        color: #333;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    
    /* Responsivo */
    @media (max-width: 768px) {
        .hero h1 {
            font-size: 2.2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .benefits-section h2,
        .microlearning-section h2,
        .social-proof h2,
        .loses-section h2,
        .faq-section h2,
        .final-cta h2 {
            font-size: 1.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="container">
        <div class="hero">
            <h1>🧬 A Cortex é a primeira plataforma desenvolvida exclusivamente ao ensinamento do comportamento humano</h1>
            <p class="hero-subtitle">
                <br>
    <strong style="font-size: 2.0rem;">Junte-se a mais de 15 mil pessoas que dominam as táticas das 22 maiores autoridades globais em psicologia e linguagem corporal.</strong>
            </p>
            <a href="#produtos" class="hero-cta-link">
            <button class="hero-cta">
                ⚡ Começar Agora
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- MICROLEARNING ---
st.markdown("""
    <div class="container">
        <div class="microlearning-section">
            <h2>🧬 Microlearning + Neurociência = Aprendizado Real</h2>
            <p style="text-align: center; color: #666; font-size: 1.05rem; margin-bottom: 40px; line-height: 1.8;">
                Cada módulo é projetado com base em como o cérebro realmente aprende. Não é coincidência que você vai reter o conhecimento.
            </p>
            <div class="microlearning-grid">
                <div class="microlearning-item">
                    <h3>🔗 Links cerebrais</h3>
                    <p>Cada conceito é conectado a exemplos reais. Seu cérebro cria conexões mais fortes e memória duradoura.</p>
                </div>
                <div class="microlearning-item">
                    <h3>🌊 Modo difuso</h3>
                    <p>Atividades que ativam o modo difuso do cérebro. Você aprende enquanto relaxa, não através de força bruta.</p>
                </div>
                <div class="microlearning-item">
                    <h3>⏱️ Sessões curtas</h3>
                    <p>15-20 minutos por dia. Seu cérebro absorve melhor em sessões curtas e focadas do que em maratonas.</p>
                </div>
                <div class="microlearning-item">
                    <h3>🔄 Repetição espaçada</h3>
                    <p>Conceitos são revisitados em intervalos ótimos. Você não esquece. Conhecimento fica para sempre.</p>
                </div>
                <div class="microlearning-item">
                    <h3>✍️ Atividades práticas</h3>
                    <p>Fazer é o melhor jeito de aprender. Cada dia tem exercícios que consolidam o conhecimento.</p>
                </div>
                <div class="microlearning-item">
                    <h3>🎓 Baseado em estudo</h3>
                    <p>Tudo segue as melhores práticas de neurociência e psicologia cognitiva (Paul Ekman, Joe Navarro, Cialdini e muito mais). Todo conteúdo sempre estará citando de onde vem a base. Aprendizado que funciona.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- PROVA SOCIAL ---
st.markdown("""
    <div class="container">
        <div class="social-proof">
            <h2>📊 Nossos resultados em números</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <p class="stat-number">15.000+</p>
                    <p class="stat-label">Usuários ativos</p>
                </div>
                <div class="stat-card">
                    <p class="stat-number">4.9★</p>
                    <p class="stat-label">Avaliação média</p>
                </div>
                <div class="stat-card">
                    <p class="stat-number">92%</p>
                    <p class="stat-label">Taxa de conclusão</p>
                </div>
            </div><h3 style="color: #952791; font-size: 1.8rem; margin-top: 50px; margin-bottom: 30px; font-weight: 800;">Mais do que estatísticas, somos feitos de histórias reais:</h3>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                        <img class="testimonial-photo"
                         src="https://raw.githubusercontent.com/Gm0ur4/cortex-landing/main/ricardo_depoimento.png">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <p class="testimonial-text">
                        "Eu sempre achei que linguagem corporal não importava muito, mas a prática me provou o contrário. Usei a técnica de leitura de bloqueios numa reunião e percebi que o cliente ia recusar o preço antes dele abrir a boca. Ajustei o tom na hora e consegui fechar o contrato. É bizarro o quanto a gente é cego para esses sinais."
                    </p>
                    <div class="testimonial-author">Ricardo Murata</div>
                </div>
                <div class="testimonial-card">
                 <img class="testimonial-photo"
                         src="https://raw.githubusercontent.com/Gm0ur4/cortex-landing/main/luiza_depoimento">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <p class="testimonial-text">
                        "O que eu mais gostei é que não tem enrolação. Eu leio o conteúdo no ônibus e já chego no escritório testando. É muito direto ao ponto: a plataforma entrega o módulo e em minutos você já entende por que aquela pessoa age de tal forma. Valeu cada centavo pela praticidade."
                    </p>
                    <div class="testimonial-author">Luiza Sabino</div>
                </div>
                <div class="testimonial-card">
                        <img class="testimonial-photo"
                         src="https://raw.githubusercontent.com/Gm0ur4/cortex-landing/main/fernanda_depoimento">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <p class="testimonial-text">
                        "Parece que agora eu vejo o mundo em câmera lenta. Você começa a notar as microexpressões e entende as intenções reais das pessoas, não só o que elas dizem. Mudou totalmente a forma como eu me posiciono em conversas difíceis. Minha única reclamação é não ter descoberto isso antes kkkk"
                    </p>
                    <div class="testimonial-author">Fernanda Zerbini</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)


# --- PROBLEMA ---
st.markdown("""
    <div class="container">
        <div class="problem-section">
            <h2>Sua jornada de 21 dias:</h2>
            <div class="problem-grid">
                <div class="problem-item">
                    <h3>🏁 Fase 1: Persuasão e vendas (Dia 01 ao 05)</h3>
                    <p>Nesta fase, você desbloqueia as chaves da comunicação persuasiva. O objetivo é que, já na primeira semana, você consiga aplicar gatilhos mentais em negociações e conversas casuais para notar uma mudança imediata na aceitação das suas ideias.</p>
                </div>
                <div class="problem-item">
                    <h3>🔍 Fase 2: Leitura de pessoas e linguagem corporal (Dia 06 ao 10)</h3>
                    <p>Aqui é onde você "abre os olhos". Você aprenderá a decodificar microexpressões e gestos involuntários. É o módulo que o Ricardo (nosso aluno) usou para ler o fechamento de corpo do cliente e garantir o contrato.</p>
                </div>
                <div class="problem-item">
                    <h3>🧠 Fase 3: Controle emocional e resiliência (Dia 11 ao 15)</h3>
                    <p>Não adianta ler os outros se você não domina a si mesmo. Esta fase foca em manter a calma sob pressão e usar a resiliência como arma em ambientes hostis ou discussões acaloradas. Você aprende a não reagir, mas a agir com estratégia.</p>
                </div>
                <div class="problem-item">
                    <h3>👑 Fase 4: Liderança e influência social (Dia 16 ao 21)</h3>
                    <p>A fase final consolida tudo. Você aprenderá como projetar uma presença de liderança que comanda o ambiente sem precisar dizer uma palavra. É o ajuste final para você se tornar a pessoa mais influente em qualquer grupo social ou profissional.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- DEMO ---
st.markdown("""
    <div class="container">
        <div class="demo-section">
            <h2>🎥 Veja como funciona</h2>
            <p style="color: #666; font-size: 1.05rem; margin-bottom: 30px; line-height: 1.8;">
                Quer ver um exemplo de como é um parte de um dia? Clique abaixo para acessar uma demonstração gratuita.Sem necessidade de cadastro. Acesso imediato.
            </p>
            <a href="https://aprendizadocortexdemo.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button class="demo-btn" style="cursor: pointer;">
                👀 Ver demonstração gratuita
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CTA ANTES DO FAQ ---
st.markdown("""
<div class="container">
    <div style="text-align:center; margin: 40px 0;">
        <a <a href="#produtos" class="hero-cta-link" style="text-decoration:none;">
            <button class="hero-cta">
                ⚡ Começar Agora
            </button>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FAQ PREMIUM ---
st.markdown("""
<div class="container">
<div class="faq-section">
<h2>❓ Perguntas Frequentes</h2>
<details class="faq-item">
<summary class="faq-question">É seguro realizar a compra?</summary>
<div class="faq-answer">Sim. Toda a compra é processada pela <strong>Eduzz</strong>, uma das plataformas de pagamentos e educação mais seguras e reconhecidas do Brasil. Nenhum dado sensível passa por nós, tudo ocorre diretamente no ambiente da Eduzz, com <strong>criptografia, certificados de segurança e antifraude</strong>. Além disso, você sempre pode verificar a URL do checkout, confirmar que está no domínio oficial da Eduzz e pesquisar sobre a empresa para garantir total transparência.</div>
</details>
<details class="faq-item">
<summary class="faq-question">Por onde acesso a Cortex?</summary>
<div class="faq-answer">Você pode acessar nossa plataforma de qualquer lugar pelo navegador: <strong>celular, computador, tablet ou qualquer dispositivo com internet</strong>, sem instalações complicadas. É 100% online e funciona perfeitamente em qualquer lugar.</div>
</details>
<details class="faq-item">
<summary class="faq-question">Como funciona a IA?</summary>
<div class="faq-answer">O Chat IA é treinado com os principais conceitos de comportamento humano de todas as nossas fontes. Você descreve uma situação (um conflito, uma dificuldade pessoal) e a IA: <strong>Analisa seus padrões comportamentais, faz um diagnóstico personalizado, oferece soluções práticas, cria um plano de ação</strong> e tira todas suas dúvidas sobre a mente humana. Tudo baseado em ciência. Tudo prático. É como ter um <strong>especialista em comportamento humano disponível 24/7</strong> para ajudar você.</div>
</details>
<details class="faq-item">
<summary class="faq-question">O que vou aprender?</summary>
<div class="faq-answer">Nosso conteúdo foi escolhido com base no que as pessoas mais procuram sobre o assunto: <strong>Persuasão, leitura de pessoas, linguagem corporal, controle emocional, influência social, resiliência com inteligência emocional, vendas com persuasão</strong> + um conteúdo bônus final no formato intensivo surpresa. Tudo prático e aplicável imediatamente.</div>
</details>
<details class="faq-item">
<summary class="faq-question">Existe algum tipo de suporte?</summary>
<div class="faq-answer">Com certeza! Desde o primeiro acesso, você recebe <strong>instruções completas de orientação</strong> que explica como a plataforma funciona. Caso precise de qualquer tipo de assistência, oferecemos <strong>suporte humano rápido</strong>, garantindo que você nunca fique travado ou perdido durante o processo.</div>
</details>
<details class="faq-item">
<summary class="faq-question">Posso fazer no meu ritmo?</summary>
<div class="faq-answer">Claro! Você pode usar a Cortex no seu próprio ritmo, porque ela se adapta à sua <strong>disponibilidade e ao seu momento de vida</strong>. Não existem aulas extensas, vídeos obrigatórios ou sequências fixas. A plataforma personaliza as explicações e orientações conforme você evolui, para que cada interação gere resultado independentemente da frequência.</div>
</details>
</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# ===== CHECKOUT INTEGRADO COM FUNDO BRANCO =====
# ============================================================

# ===== CHECKOUT =====

# Âncora para rolar até aqui
st.markdown('<div id="produtos"></div>', unsafe_allow_html=True)

# Urgência
st.markdown("""
    <div class="urgency-banner">
        <span class="urgency-text">⏰ OFERTA ESPECIAL DE CAMPANHA!</span>
    </div>
    """, unsafe_allow_html=True)


# Produtos
st.markdown('<div class="products-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="product-card">
<h3 class="product-title">Plataforma de aprendizado Cortex</h3>

<p class="product-description">
Aprenda os princípios fundamentais do comportamento humano através de 21 dias de atividades práticas e transformadoras.
</p>

<div class="price">R$44,90</div>
<p class="price-small">Acesso vitalício</p>

<ul class="features-list">
<li>21 dias de aprendizado puro</li>
<li>Diversas atividades práticas para aplicação imediata</li>
<li>Conteúdo baseado em comportamento humano</li>
<li>Acesso vitalício à plataforma</li>
<li>Atualizações futuras incluídas</li>
<li>Suporte humano todos os dias</li>
</ul>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia', '_blank')">
Quero acessar agora
</button>
</div>""", unsafe_allow_html=True)


with col2:
    st.markdown("""<div class="product-card featured">
<h3 class="product-title">Plataforma de aprendizado Cortex + Ultra Cortex (PDF)</h3>

<p class="product-description">
Além da plataforma de aprendizado, o Ultra Cortex é o seu manual tático para o dia a dia. São mais de 50 análises de comportamento e scripts de reação prontos para você consultar no celular, exatamente na hora em que precisar identificar uma mentira, desarmar um conflito ou fechar um negócio.
</p>

<div class="price">R$ 79,90</div>
<p class="price-small">Acesso vitalício a ambos</p>

<ul class="features-list">
<li>Plataforma de aprendizado e tudo que ela oferece</li>
<li>Leitura rápida de microexpressões e emoções</li>
<li>Táticas aplicáveis imediatamente na vida real</li>
<li>Técnicas práticas de influência e persuasão</li>
<li>Detecção de mentiras e sinais de desconforto</li>
<li>Controle de ambiente e posições de poder</li>
</ul>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia-completo', '_blank')">
Garantir a experiência completa
</button>
</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# Order Bump
st.markdown("""<div class="order-bump">
<h3>🤖 Adicione somente a Ultra Cortex por R$ 59,90</h3>

<p>
Caso queira, adicione somente o Ultra Cortex com planos de ação e diversas técnicas da inteligência humana.
</p>

<div class="bump-price">
R$ 59,90
<span class="bump-original">R$ 79,90</span>
<span class="bump-savings">-25% OFF</span>
</div>

<p style="color: #666; margin: 15px 0;">
✓ Consulta rápida para decisões sob pressão<br>
✓ Criação instantânea de conexão e autoridade<br>
✓ Scripts prontos para negociações e conversas difíceis<br>
✓ Consulta rápida para decisões sob pressão<br>
✓ Manual direto ao ponto
</p>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia-chat', '_blank')">
Adicionar Chat IA Agora
</button>
</div>""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2026 Cortex IA. Todos os direitos reservados.</p>
    </div>
</div>""", unsafe_allow_html=True)
