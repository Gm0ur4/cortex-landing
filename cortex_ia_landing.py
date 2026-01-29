import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cortex - Domine o Comportamento Humano",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================
# CSS GLOBAL (LANDING + CHECKOUT)
# ==============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

* { font-family: 'Inter', sans-serif; }

html, body, .stApp {
    background: linear-gradient(135deg, #020930 0%, #BE90E3 100%) !important;
}

/* ---------- CONTAINER ---------- */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ---------- HERO ---------- */
.hero {
    padding: 80px 20px;
    text-align: center;
}

.hero h1 {
    color: white;
    font-size: 3.5rem;
    font-weight: 800;
}

.hero-subtitle strong {
    color: white;
}

.hero-cta {
    background: linear-gradient(90deg,#FFB800,#EDAB00);
    color: white;
    padding: 18px 40px;
    border-radius: 8px;
    font-weight: 700;
    border: none;
    cursor: pointer;
}

/* ---------- CTA FINAL ---------- */
.final-cta {
    background: linear-gradient(90deg,#39D7FE,#39D7FE);
    padding: 80px 20px;
    text-align: center;
    border-radius: 16px;
    margin: 60px 0;
}

.final-cta h2 { color:white; }

/* ==============================
   CHECKOUT
============================== */

.checkout-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

.checkout-title {
    color:white;
    text-align:center;
    font-size:2.5rem;
    font-weight:800;
    margin:60px 0 10px;
}

.products-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
}

@media(max-width:768px){
    .products-grid{grid-template-columns:1fr;}
}

.product-card {
    background:white;
    border-radius:16px;
    padding:40px;
    box-shadow:0 10px 40px rgba(0,0,0,.08);
}

.product-card.featured {
    border:2px solid #37D087;
}

.product-title {
    color:#952791;
    font-size:1.5rem;
    font-weight:800;
}

.price {
    font-size:2.5rem;
    color:#952791;
    font-weight:800;
}

.features-list {
    list-style:none;
    padding:0;
}

.features-list li {
    padding:8px 0;
}

.btn-checkout {
    background:linear-gradient(90deg,#37D087,#39D7FE);
    color:white;
    border:none;
    padding:16px;
    border-radius:8px;
    width:100%;
    font-weight:700;
    cursor:pointer;
}

/* Order bump */

.order-bump {
    background:#FFF9E6;
    border:2px solid #FFD700;
    border-radius:16px;
    padding:30px;
    margin:40px 0;
}

.footer {
    text-align:center;
    color:#999;
    margin-top:60px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HERO
# ==============================
st.markdown("""
<div class="container">
<div class="hero">
<h1>🧬 A Cortex é a primeira plataforma para dominar comportamento humano em 21 dias</h1>

<p class="hero-subtitle">
<strong>Mais de 15.000 usuários já utilizam a plataforma.</strong>
</p>

<a href="#checkout">
<button class="hero-cta">⚡ Começar Agora</button>
</a>

</div>
</div>
""", unsafe_allow_html=True)

# ==============================
# CTA FINAL ANTES DO CHECKOUT
# ==============================
st.markdown("""
<div class="container">
<div class="final-cta">
<h2>🚀 Comece sua transformação hoje</h2>
<p>Você pode continuar como está. Ou mudar em 21 dias.</p>

<a href="#checkout">
<button class="hero-cta">⚡ Começar Agora</button>
</a>

</div>
</div>
""", unsafe_allow_html=True)

# ==============================
# CHECKOUT
# ==============================
st.markdown('<div id="checkout" class="checkout-container">', unsafe_allow_html=True)

st.markdown("""
<h2 class="checkout-title">Finalize seu acesso</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="product-card">
<h3 class="product-title">Plataforma Cortex</h3>

<p>21 dias de aprendizado prático.</p>

<div class="price">R$ 39,90</div>

<ul class="features-list">
<li>21 dias de conteúdo</li>
<li>Atividades práticas</li>
<li>Acesso vitalício</li>
<li>Atualizações incluídas</li>
</ul>

<button class="btn-checkout"
onclick="window.open('https://seulink.eduzz.com/cortex-ia','_blank')">
Quero acessar agora
</button>

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="product-card featured">
<h3 class="product-title">Cortex + Chat IA</h3>

<p>Aprendizado + análises personalizadas.</p>

<div class="price">R$ 79,90</div>

<ul class="features-list">
<li>Plataforma completa</li>
<li>Chat IA comportamental</li>
<li>Plano de ação personalizado</li>
<li>Acesso vitalício</li>
</ul>

<button class="btn-checkout"
onclick="window.open('https://seulink.eduzz.com/cortex-ia-completo','_blank')">
Garantir experiência completa
</button>

</div>
""", unsafe_allow_html=True)

# Order bump
st.markdown("""
<div class="order-bump">
<h3>🤖 Adicione somente a IA por R$ 59,90</h3>

<p>Receba análises e planos personalizados.</p>

<button class="btn-checkout"
onclick="window.open('https://seulink.eduzz.com/cortex-ia-chat','_blank')">
Adicionar IA
</button>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
© 2026 Cortex IA
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
