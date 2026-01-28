import streamlit as st
from datetime import datetime, timedelta
import time

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Cortex - Domine o Comportamento Humano",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== CORES PROFISSIONAIS PREMIUM ====================
COLORS = {
    "primary": "#1a1a2e",
    "primary_light": "#16213e",
    "secondary": "#0f3460",
    "accent": "#e94560",
    "accent_light": "#f39c12",
    "success": "#27ae60",
    "danger": "#c0392b",
    "light_bg": "#f8f9fa",
    "light_bg_2": "#ecf0f1",
    "white": "#FFFFFF",
    "text_dark": "#1a1a2e",
    "text_gray": "#555555",
    "text_light": "#888888",
    "border_light": "#d5d8dc",
}

# ==================== CSS PROFISSIONAL ====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* RESET */
    html, body, .stApp {{
        background: #ffffff !important;
        color: {COLORS['text_gray']};
    }}
    
    /* CONTAINER */
    .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}
    
    /* ==================== HERO SECTION ==================== */
    .hero {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_light']} 100%);
        padding: 100px 20px 80px;
        text-align: center;
        border-radius: 0;
        color: white;
        margin-bottom: -40px;
        position: relative;
        z-index: 1;
    }}
    
    .hero h1 {{
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 20px;
        line-height: 1.2;
        letter-spacing: -0.02em;
    }}
    
    .hero-subtitle {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.3rem;
        margin-bottom: 40px;
        line-height: 1.8;
    }}
    
    .hero-subtitle strong {{
        color: {COLORS['accent_light']};
    }}
    
    /* ==================== PROVA SOCIAL RÁPIDA ==================== */
    .social-proof-quick {{
        background: white;
        padding: 60px 20px;
        margin: 0 20px 40px 20px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        position: relative;
        z-index: 10;
    }}
    
    .stat-card {{
        padding: 30px;
        background: white;
        border-radius: 12px;
        border: 2px solid {COLORS['accent']};
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .stat-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(233, 69, 96, 0.15);
    }}
    
    .stat-number {{
        color: {COLORS['accent']};
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 10px;
    }}
    
    .stat-label {{
        color: {COLORS['text_gray']};
        font-size: 0.95rem;
    }}
    
    /* ==================== SEÇÕES GERAIS ==================== */
    .section {{
        padding: 60px 20px;
        margin: 40px 0;
        border-radius: 16px;
    }}
    
    .section-white {{
        background: white;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }}
    
    .section-light {{
        background: linear-gradient(135deg, {COLORS['light_bg_2']} 0%, {COLORS['light_bg']} 100%);
    }}
    
    .section-dark {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_light']} 100%);
        color: white;
    }}
    
    .section-dark h2 {{
        color: white;
    }}
    
    .section-dark h2::after {{
        background: {COLORS['accent_light']} !important;
    }}
    
    /* ==================== TÍTULOS ==================== */
    h2 {{
        color: {COLORS['primary']};
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 40px;
        position: relative;
        padding-bottom: 20px;
    }}
    
    h2::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, {COLORS['accent']} 0%, {COLORS['accent_light']} 100%);
        border-radius: 2px;
    }}
    
    h3 {{
        color: {COLORS['primary']};
        font-weight: 700;
        margin-bottom: 15px;
    }}
    
    /* ==================== PROBLEMA ==================== */
    .problem-item {{
        padding: 30px;
        background: #fafafa;
        border-radius: 12px;
        border-left: 5px solid {COLORS['danger']};
        transition: all 0.3s ease;
    }}
    
    .problem-item:hover {{
        background: #f5f5f5;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }}
    
    .problem-item h3 {{
        color: {COLORS['danger']};
    }}
    
    /* ==================== QUOTE BOX ==================== */
    .quote-box {{
        background: white;
        padding: 40px;
        border-radius: 12px;
        border-left: 5px solid {COLORS['accent']};
        margin-bottom: 30px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }}
    
    .quote-text {{
        color: {COLORS['primary']};
        font-size: 1.3rem;
        font-weight: 700;
        line-height: 1.8;
    }}
    
    .quote-highlight {{
        color: {COLORS['accent']};
        font-style: italic;
    }}
    
    /* ==================== BENEFIT CARD ==================== */
    .benefit-card {{
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        transition: all 0.3s ease;
        text-align: center;
        border-top: 4px solid {COLORS['accent']};
    }}
    
    .benefit-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
        border-top-color: {COLORS['secondary']};
    }}
    
    .benefit-icon {{
        font-size: 2.5rem;
        margin-bottom: 15px;
    }}
    
    .benefit-card p {{
        color: {COLORS['text_gray']};
        font-size: 0.95rem;
    }}
    
    /* ==================== LOSES SECTION ==================== */
    .lose-item {{
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }}
    
    .lose-item h3 {{
        color: {COLORS['danger']};
        margin-bottom: 10px;
    }}
    
    .lose-item p {{
        font-size: 0.9rem;
    }}
    
    /* ==================== MICROLEARNING ==================== */
    .microlearning-item {{
        background: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        transition: all 0.3s ease;
        border-left: 4px solid {COLORS['accent']};
    }}
    
    .microlearning-item:hover {{
        transform: translateY(-3px);
        background: white;
    }}
    
    .microlearning-item h3 {{
        color: {COLORS['primary']};
    }}
    
    .section-dark .microlearning-item p {{
        color: {COLORS['text_gray']};
    }}
    
    /* ==================== CHECKOUT ==================== */
    .checkout-section {{
        background: white;
        padding: 80px 20px;
        margin: 40px 0;
        border-radius: 16px;
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
        border-top: 4px solid {COLORS['accent']};
    }}
    
    .product-card {{
        background: white;
        border: 2px solid {COLORS['border_light']};
        border-radius: 12px;
        padding: 40px;
        transition: all 0.3s ease;
        position: relative;
    }}
    
    .product-card.featured {{
        border-color: {COLORS['accent']};
        box-shadow: 0 0 0 3px rgba(233, 69, 96, 0.1);
        transform: scale(1.05);
    }}
    
    .product-card.featured::before {{
        content: "⭐ MAIS POPULAR";
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(90deg, {COLORS['accent']} 0%, #d63447 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.05em;
        white-space: nowrap;
    }}
    
    .product-card:hover {{
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
    }}
    
    .product-title {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {COLORS['primary']};
        margin-bottom: 15px;
    }}
    
    .product-description {{
        color: {COLORS['text_gray']};
        margin-bottom: 25px;
        line-height: 1.8;
    }}
    
    .price {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {COLORS['accent']};
        margin-bottom: 5px;
    }}
    
    .price-small {{
        color: {COLORS['text_light']};
        font-size: 0.9rem;
        margin-bottom: 25px;
    }}
    
    .features-list {{
        list-style: none;
        padding: 0;
        margin: 25px 0;
    }}
    
    .features-list li {{
        color: {COLORS['text_gray']};
        padding: 12px 0;
        border-bottom: 1px solid {COLORS['border_light']};
        display: flex;
        align-items: center;
        font-size: 0.95rem;
    }}
    
    .features-list li:last-child {{
        border-bottom: none;
    }}
    
    .features-list li::before {{
        content: "✓";
        color: {COLORS['accent']};
        font-weight: 800;
        margin-right: 12px;
        font-size: 1.2rem;
    }}
    
    /* ==================== BOTÕES ==================== */
    .btn-primary {{
        background: linear-gradient(135deg, {COLORS['accent']} 0%, #d63447 100%);
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
        box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        display: inline-block;
    }}
    
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(233, 69, 96, 0.4);
    }}
    
    .btn-checkout {{
        background: linear-gradient(135deg, {COLORS['accent']} 0%, #d63447 100%);
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
        text-decoration: none;
        display: block;
        text-align: center;
    }}
    
    .btn-checkout:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
    }}
    
    /* ==================== ORDER BUMP ==================== */
    .order-bump {{
        background: linear-gradient(135deg, {COLORS['light_bg_2']} 0%, {COLORS['light_bg']} 100%);
        border: 2px solid {COLORS['accent_light']};
        border-radius: 16px;
        padding: 40px;
        margin: 50px 0;
        position: relative;
    }}
    
    .order-bump::before {{
        content: "⚡ OFERTA RELÂMPAGO";
        position: absolute;
        top: -15px;
        left: 20px;
        background: linear-gradient(90deg, {COLORS['accent_light']} 0%, #e67e22 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.05em;
    }}
    
    .order-bump h3 {{
        color: {COLORS['primary']};
        font-size: 1.3rem;
        margin-top: 15px;
        margin-bottom: 15px;
    }}
    
    .order-bump p {{
        color: {COLORS['text_gray']};
        line-height: 1.8;
        margin-bottom: 15px;
    }}
    
    .bump-price {{
        font-size: 1.8rem;
        color: {COLORS['accent']};
        font-weight: 800;
        margin: 20px 0;
    }}
    
    .bump-original {{
        text-decoration: line-through;
        color: {COLORS['text_light']};
        font-size: 0.9rem;
        margin-right: 10px;
    }}
    
    .bump-savings {{
        background: {COLORS['accent_light']};
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 700;
    }}
    
    /* ==================== BÔNUS ==================== */
    .bonus-section {{
        background: linear-gradient(135deg, {COLORS['light_bg_2']} 0%, {COLORS['light_bg']} 100%);
        border-radius: 16px;
        padding: 40px;
        margin: 50px 0;
        border-left: 5px solid {COLORS['accent']};
    }}
    
    .bonus-section h3 {{
        color: {COLORS['primary']};
        font-size: 1.5rem;
        margin-bottom: 25px;
        font-weight: 800;
    }}
    
    .bonus-item {{
        display: flex;
        align-items: flex-start;
        margin-bottom: 20px;
    }}
    
    .bonus-icon {{
        font-size: 1.5rem;
        margin-right: 15px;
        min-width: 30px;
    }}
    
    .bonus-content h4 {{
        color: {COLORS['primary']};
        margin: 0 0 5px 0;
        font-size: 1rem;
        font-weight: 700;
    }}
    
    .bonus-content p {{
        color: {COLORS['text_gray']};
        margin: 0;
        font-size: 0.9rem;
    }}
    
    /* ==================== DEPOIMENTOS ==================== */
    .testimonial-card {{
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        border-left: 5px solid {COLORS['accent']};
        transition: all 0.3s ease;
    }}
    
    .testimonial-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
    }}
    
    .stars {{
        color: {COLORS['accent_light']};
        font-size: 1.2rem;
        margin-bottom: 15px;
    }}
    
    .testimonial-text {{
        color: {COLORS['text_gray']};
        font-size: 0.95rem;
        line-height: 1.8;
        margin-bottom: 15px;
        font-style: italic;
    }}
    
    .testimonial-author {{
        color: {COLORS['primary']};
        font-weight: 700;
        font-size: 0.9rem;
    }}
    
    .testimonial-role {{
        color: {COLORS['text_light']};
        font-size: 0.85rem;
    }}
    
    /* ==================== FAQ ==================== */
    .faq-item {{
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }}
    
    .faq-question {{
        color: {COLORS['primary']};
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 10px;
        cursor: pointer;
    }}
    
    .faq-answer {{
        color: {COLORS['text_gray']};
        font-size: 0.95rem;
        line-height: 1.8;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid {COLORS['border_light']};
    }}
    
    /* ==================== CTA FINAL ==================== */
    .final-cta {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_light']} 100%);
        padding: 80px 20px;
        text-align: center;
        border-radius: 16px;
        margin: 60px 0;
    }}
    
    .final-cta h2 {{
        color: white;
        margin-bottom: 20px;
    }}
    
    .final-cta h2::after {{
        background: {COLORS['accent_light']} !important;
    }}
    
    .final-cta p {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        margin-bottom: 30px;
        line-height: 1.8;
    }}
    
    /* ==================== URGÊNCIA ==================== */
    .urgency-banner {{
        background: linear-gradient(135deg, {COLORS['accent']} 0%, #d63447 100%);
        color: white;
        padding: 15px 20px;
        text-align: center;
        font-weight: 700;
        font-size: 1rem;
        border-radius: 8px;
        margin-bottom: 30px;
        box-shadow: 0 8px 24px rgba(233, 69, 96, 0.2);
    }}
    
    .timer {{
        display: inline-block;
        background: {COLORS['accent_light']};
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 700;
        margin-left: 10px;
        font-size: 0.9rem;
    }}
    
    /* ==================== FOOTER ==================== */
    .footer {{
        background: {COLORS['primary']};
        color: rgba(255, 255, 255, 0.8);
        text-align: center;
        font-size: 0.9rem;
        padding: 40px 20px;
        margin-top: 60px;
    }}
    
    .footer a {{
        color: {COLORS['accent_light']};
        text-decoration: none;
        transition: all 0.3s ease;
    }}
    
    .footer a:hover {{
        text-decoration: underline;
    }}
    
    /* ==================== RESPONSIVIDADE ==================== */
    @media (max-width: 768px) {{
        .hero h1 {{
            font-size: 2.2rem;
        }}
        
        .hero-subtitle {{
            font-size: 1rem;
        }}
        
        h2 {{
            font-size: 1.8rem;
        }}
        
        .product-card.featured {{
            transform: scale(1);
        }}
        
        .timer {{
            display: block;
            margin-left: 0;
            margin-top: 10px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# ==================== HERO SECTION ====================
st.markdown("""
    <div class="hero">
        <h1>🧠 A Cortex é a primeira plataforma desenvolvida para te ensinar comportamento humano em 21 dias</h1>
        <p class="hero-subtitle">
            Somos pioneiros a dar o fim em cursos chatos e PDFs intermináveis.<br>
            <strong>São mais de 15.000 alunos absorvendo o conhecimento dos 22 maiores best-sellers do mundo</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# Hero CTA
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("""
        <a href="#checkout" style="text-decoration: none;">
            <button class="btn-primary" style="width: 100%;">⚡ Começar Agora</button>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================== PROVA SOCIAL RÁPIDA ====================
st.markdown("""
    <div class="social-proof-quick">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px;">
            <div class="stat-card">
                <div class="stat-number">15.000+</div>
                <div class="stat-label">Usuários ativos</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">98%</div>
                <div class="stat-label">Taxa de satisfação</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">21</div>
                <div class="stat-label">Dias para transformação</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==================== PROBLEMA ====================
st.markdown("""
    <div class="section section-white">
        <h2>❌ Qual o problema dos demais que tentam ensinar?</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
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
""", unsafe_allow_html=True)

# ==================== SOLUÇÃO ====================
st.markdown("""
    <div class="section section-light">
        <h2>✅ Aprenda com quem é especialista no assunto</h2>
        <div class="quote-box">
            <p class="quote-text">
                Você não precisa ler mais de 7.000 páginas para dominar a mente humana. 
                <span class="quote-highlight">A Cortex já processou, filtrou e organizou o ouro de cada mestre da inteligência humana para você aplicar hoje mesmo.</span>
            </p>
        </div>
        <p style="text-align: center; color: #555555; font-size: 1.05rem; line-height: 1.8; margin-top: 30px;">
            A Cortex é um <strong>programa de 21 dias</strong> com atividades práticas que te ensinam os princípios fundamentais 
            do comportamento humano. Sem teoria chata. Sem PDFs gigantes. Apenas <strong>o essencial para você aplicar e transformar sua vida.</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# ==================== BENEFÍCIOS ====================
st.markdown("<h2 style='text-align: center; color: #1a1a2e; margin-bottom: 40px; position: relative; padding-bottom: 20px;'>🎯 Características principais<span style='position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background: linear-gradient(90deg, #e94560 0%, #f39c12 100%); border-radius: 2px;'></span></h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="benefit-card">
            <div class="benefit-icon">⚡</div>
            <h3>Aprenda no tempo perfeito</h3>
            <p>Não em 6 meses. Não em 1 ano. Em apenas 21 dias você terá os conhecimentos que levaria meses para ler em livros e cursos.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="benefit-card">
            <div class="benefit-icon">🎯</div>
            <h3>100% prático</h3>
            <p>Cada dia tem atividades que você faz. Sem teoria chata. Sem vídeos longos. Pura aplicação.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="benefit-card">
            <div class="benefit-icon">🧠</div>
            <h3>Baseado em ciência</h3>
            <p>Todos os conceitos vêm das melhores referências mundiais sobre comportamento humano. Você aprende só o que realmente funciona.</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="benefit-card">
            <div class="benefit-icon">💡</div>
            <h3>Aplique imediatamente</h3>
            <p>Aprenda uma técnica e use no mesmo dia. Com seus relacionamentos, no trabalho, em casa. Resultados reais.</p>
        </div>
    """, unsafe_allow_html=True)

# ==================== O QUE VOCÊ PERDE ====================
st.markdown("""
    <div class="section section-white" style="border-top: 4px solid #c0392b;">
        <h2 style="color: #1a1a2e;">⚠️ Quem não entende comportamento humano está à mercê de:</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
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
""", unsafe_allow_html=True)

# ==================== MICROLEARNING ====================
st.markdown("""
    <div class="section section-dark">
        <h2>🧬 Microlearning + Neurociência = Aprendizado Real</h2>
        <p style="text-align: center; color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; margin-bottom: 40px; line-height: 1.8;">
            Cada módulo é projetado com base em como o cérebro realmente aprende. Não é coincidência que você vai reter o conhecimento.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
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
        </div>
    </div>
""", unsafe_allow_html=True)

# ==================== CHECKOUT ====================
st.markdown("""
    <div class="checkout-section">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2>🎁 Escolha seu plano agora</h2>
            <p style="font-size: 1.1rem; color: #555555; max-width: 600px; margin: 0 auto;">Acesso vitalício a todo o conteúdo. Pagamento único. Sem mensalidades. Comece sua transformação hoje mesmo.</p>
        </div>
        
        <div class="urgency-banner">
            ⏰ OFERTA ESPECIAL DE CAMPANHA!
            <span class="timer">Expira em: 3 dias</span>
        </div>
""", unsafe_allow_html=True)

# Produtos
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
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
            <a href="https://seulink.eduzz.com/cortex-ia" target="_blank">
                <button class="btn-checkout">Quero acessar agora</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
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
            <a href="https://seulink.eduzz.com/cortex-ia-completo" target="_blank">
                <button class="btn-checkout">Garantir a experiência completa</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

# Order Bump
st.markdown("""
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
        <div style="color: #555555; margin: 20px 0; line-height: 1.8;">
            <p>✓ Análise de padrões comportamentais</p>
            <p>✓ Diagnóstico personalizado</p>
            <p>✓ Soluções para problemas específicos</p>
            <p>✓ Plano de ação customizado</p>
            <p>✓ Acesso vitalício</p>
        </div>
        <a href="https://seulink.eduzz.com/cortex-ia-chat" target="_blank">
            <button class="btn-checkout">Adicionar Chat IA Agora</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Bônus
st.markdown("""
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
""", unsafe_allow_html=True)

# ==================== DEPOIMENTOS ====================
st.markdown("<h2 style='text-align: center; color: #1a1a2e; margin-bottom: 40px; position: relative; padding-bottom: 20px;'>💬 O que dizem nossos clientes<span style='position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background: linear-gradient(90deg, #e94560 0%, #f39c12 100%); border-radius: 2px;'></span></h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                "Cortex mudou completamente minha forma de ver relacionamentos. Em 21 dias aprendi mais do que em anos tentando sozinho. Recomendo para todos!"
            </p>
            <p class="testimonial-author">Marina Silva</p>
            <p class="testimonial-role">Psicóloga</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                "Nunca pensei que seria tão prático. As atividades diárias são incríveis e realmente funcionam. Minha produtividade aumentou 300%."
            </p>
            <p class="testimonial-author">Carlos Mendes</p>
            <p class="testimonial-role">Empreendedor</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <p class="testimonial-text">
                "A IA do Cortex é absurda. Consegui resolver conflitos que tinha há anos. Melhor investimento que já fiz em desenvolvimento pessoal."
            </p>
            <p class="testimonial-author">Juliana Costa</p>
            <p class="testimonial-role">Gerente de Projetos</p>
        </div>
    """, unsafe_allow_html=True)

# ==================== FAQ ====================
st.markdown("<h2 style='text-align: center; color: #1a1a2e; margin-bottom: 40px; position: relative; padding-bottom: 20px;'>❓ Perguntas Frequentes<span style='position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background: linear-gradient(90deg, #e94560 0%, #f39c12 100%); border-radius: 2px;'></span></h2>", unsafe_allow_html=True)

faqs = [
    {
        "question": "Como funciona o acesso à plataforma?",
        "answer": "Após a compra, você recebe um email com suas credenciais de acesso. Você pode acessar a plataforma de qualquer dispositivo (computador, tablet, smartphone) a qualquer hora do dia. O acesso é vitalício, então você pode fazer o programa quantas vezes quiser."
    },
    {
        "question": "Posso acessar em múltiplos dispositivos?",
        "answer": "Sim! Você pode acessar sua conta de qualquer dispositivo. Recomendamos começar no computador para melhor experiência, mas você pode continuar no celular ou tablet quando estiver fora de casa."
    },
    {
        "question": "Quanto tempo preciso dedicar por dia?",
        "answer": "Apenas 15-20 minutos por dia. Cada módulo é projetado para ser concluído em uma única sessão. Você pode fazer no seu próprio ritmo, mas recomendamos seguir a sequência de 21 dias para melhores resultados."
    },
    {
        "question": "E se eu não gostar? Há garantia?",
        "answer": "Oferecemos garantia de satisfação de 30 dias. Se você não ficar satisfeito com o programa, devolvemos 100% do seu dinheiro, sem perguntas. Queremos que você tenha confiança total na sua compra."
    },
    {
        "question": "Como funciona o Chat IA?",
        "answer": "O Chat IA é um assistente especializado em comportamento humano. Você pode fazer perguntas sobre situações específicas, pedir análises de padrões comportamentais e receber planos de ação personalizados. Funciona 24/7 e está disponível sempre que você precisar."
    },
    {
        "question": "Preciso ter conhecimento prévio?",
        "answer": "Não! O programa é projetado para iniciantes. Começamos do zero e vamos construindo seu conhecimento passo a passo. Não importa seu background, você conseguirá acompanhar perfeitamente."
    },
    {
        "question": "Como é o suporte?",
        "answer": "Temos um time de especialistas disponível todos os dias para responder suas dúvidas. Você pode nos contatar por email em suporte@inteligenciacortex.com.br e responderemos em até 24 horas. Clientes do plano Cortex + IA têm suporte prioritário 24/7."
    }
]

for i, faq in enumerate(faqs):
    with st.expander(f"❓ {faq['question']}", expanded=False):
        st.write(faq['answer'])

# ==================== CTA FINAL ====================
st.markdown("""
    <div class="final-cta">
        <h2>Pronto para dominar o comportamento humano?</h2>
        <p>
            Não deixe essa oportunidade passar. Junte-se a mais de 15.000 pessoas que já transformaram suas vidas com Cortex.
        </p>
        <a href="#checkout" style="text-decoration: none;">
            <button class="btn-primary">⚡ Começar Agora</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Inteligência Cortex. Todos os direitos reservados.</p>
        <p>
            <a href="mailto:suporte@inteligenciacortex.com.br">Contato</a> • 
            <a href="#">Política de Privacidade</a> • 
            <a href="#">Termos de Uso</a>
        </p>
    </div>
""", unsafe_allow_html=True)
