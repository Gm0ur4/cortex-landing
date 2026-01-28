# STREAMLIT – LANDING PAGE + CHECKOUT ONE PAGE
# Versão otimizada para conversão, clareza e credibilidade

import streamlit as st
from datetime import datetime

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Cortex | Domine o Comportamento Humano em 21 Dias",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# ESTILO GLOBAL – PREMIUM, CONFIANÇA, NEUROCIÊNCIA
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

html, body, .stApp {
    background: linear-gradient(135deg, #F4FFFE 0%, #EEF9FF 100%) !important;
}

.container {
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 24px;
}

h1, h2, h3 { letter-spacing: -0.02em; }

/* ================= HERO ================= */
.hero {
    padding: 90px 0 70px;
    text-align: center;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 800;
    color: #7B1E77;
    margin-bottom: 24px;
}

.hero p {
    font-size: 1.3rem;
    color: #555;
    max-width: 780px;
    margin: 0 auto 40px;
    line-height: 1.6;
}

.cta-primary {
    background: linear-gradient(90deg, #37D087, #39D7FE);
    color: #fff;
    padding: 18px 44px;
    border-radius: 10px;
    font-size: 1.1rem;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: 0.3s;
    box-shadow: 0 12px 30px rgba(55,208,135,.35);
}

.cta-primary:hover {
    transform: translateY(-3px);
}

.hero-proof {
    margin-top: 22px;
    font-size: .95rem;
    color: #777;
}

/* ================= SECTIONS ================= */
.section {
    margin: 80px 0;
}

.section-box {
    background: #fff;
    border-radius: 18px;
    padding: 60px;
    box-shadow: 0 14px 45px rgba(0,0,0,.08);
}

.section h2 {
    font-size: 2.3rem;
    color: #7B1E77;
    font-weight: 800;
    text-align: center;
    margin-bottom: 50px;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 36px;
}

.card {
    background: #F9FBFC;
    border-radius: 14px;
    padding: 32px;
    border-left: 5px solid #37D087;
}

.card h3 {
    color: #7B1E77;
    margin-bottom: 10px;
}

.card p {
    color: #666;
    line-height: 1.6;
}

/* ================= CHECKOUT ================= */
.checkout {
    background: linear-gradient(135deg, #FFFFFF 0%, #F0FFFE 100%);
    border-radius: 20px;
    padding: 70px 50px;
    box-shadow: 0 20px 60px rgba(0,0,0,.12);
}

.price {
    font-size: 3rem;
    font-weight: 800;
    color: #7B1E77;
    margin: 20px 0;
}

.features li {
    list-style: none;
    margin: 12px 0;
    color: #555;
}

.features li::before {
    content: "✓";
    color: #37D087;
    font-weight: 800;
    margin-right: 10px;
}

.security {
    margin-top: 25px;
    font-size: .9rem;
    color: #777;
}

/* ================= FAQ ================= */
.faq-item {
    background: #fff;
    padding: 28px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,.06);
}

.faq-item h4 { color: #7B1E77; }
.faq-item p { color: #666; line-height: 1.6; }

/* ================= RESPONSIVO ================= */
@media(max-width: 768px) {
    .hero h1 { font-size: 2.2rem; }
    .hero p { font-size: 1.05rem; }
    .section-box, .checkout { padding: 40px 24px; }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="container hero">
    <h1>Domine o comportamento humano em apenas 21 dias</h1>
    <p>
        A Cortex transforma os maiores livros de comportamento humano do mundo
        em um sistema prático, simples e aplicável no seu dia a dia.
    </p>
    <button class="cta-primary" onclick="document.getElementById('checkout').scrollIntoView({behavior:'smooth'})">
        Começar agora
    </button>
    <div class="hero-proof">15.000+ alunos • Avaliação média 4.9 ★ • Acesso vitalício</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PROBLEMA
# =========================================================
st.markdown("""
<div class="container section">
    <div class="section-box">
        <h2>Por que a maioria nunca entende comportamento humano?</h2>
        <div class="grid-2">
            <div class="card"><h3>Excesso de teoria</h3><p>Livros longos, cursos extensos e conteúdos que não se conectam com a vida real.</p></div>
            <div class="card"><h3>Sem aplicação prática</h3><p>Você até aprende, mas não sabe como usar em relações, trabalho ou decisões.</p></div>
            <div class="card"><h3>Tempo desperdiçado</h3><p>Meses consumindo conteúdo para resultados mínimos ou inexistentes.</p></div>
            <div class="card"><h3>Falta de direção</h3><p>Ninguém te mostra o caminho essencial, só jogam informação.</p></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SOLUÇÃO
# =========================================================
st.markdown("""
<div class="container section">
    <div class="section-box">
        <h2>A solução Cortex</h2>
        <p style="text-align:center; font-size:1.1rem; color:#555; max-width:800px; margin:0 auto;">
            Um programa de 21 dias baseado em neurociência, microlearning e prática real.
            Tudo que você precisa — sem excesso, sem enrolação.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# CHECKOUT INTEGRADO
# =========================================================
st.markdown("""
<div id="checkout" class="container section">
    <div class="checkout">
        <h2 style="text-align:center">Acesso completo à Cortex</h2>
        <p style="text-align:center; color:#666">Programa completo • IA comportamental • Atualizações vitalícias</p>
        <div style="text-align:center" class="price">R$ 297</div>
        <ul class="features">
            <li>21 dias de atividades práticas</li>
            <li>IA especialista em comportamento humano 24/7</li>
            <li>Persuasão, leitura de pessoas, controle emocional</li>
            <li>Acesso vitalício e atualizações futuras</li>
            <li>Garantia incondicional de 7 dias</li>
        </ul>
        <button class="cta-primary" style="width:100%; margin-top:25px">Ir para pagamento seguro</button>
        <div class="security">Pagamento 100% seguro via Eduzz • SSL • Antifraude</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FAQ
# =========================================================
st.markdown("""
<div class="container section">
    <h2>Perguntas frequentes</h2>
    <div class="faq-item"><h4>Funciona para qualquer pessoa?</h4><p>Sim. A Cortex se adapta à sua realidade, ritmo e objetivos.</p></div>
    <div class="faq-item"><h4>Quanto tempo por dia?</h4><p>Entre 15 e 20 minutos por dia.</p></div>
    <div class="faq-item"><h4>O acesso é vitalício?</h4><p>Sim. Inclui todas as atualizações futuras.</p></div>
    <div class="faq-item"><h4>E se eu não gostar?</h4><p>Você tem 7 dias de garantia incondicional.</p></div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="container" style="text-align:center; color:#999; margin:60px 0">
© 2026 Cortex • Todos os direitos reservados
</div>
""", unsafe_allow_html=True)
