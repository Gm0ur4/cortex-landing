import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cortex - Domine o Comportamento Humano",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- ESTILO PREMIUM (CSS OTIMIZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Reset Streamlit */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%);
    }
    
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    * { font-family: 'Inter', sans-serif; }
    
    .container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    
    /* HERO SECTION */
    .hero {
        padding: 100px 20px;
        text-align: center;
    }
    
    .hero h1 {
        color: #952791;
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 25px;
    }
    
    .hero-subtitle {
        color: #666;
        font-size: 1.3rem;
        margin-bottom: 40px;
    }

    /* GRIDS & CARDS */
    .grid-layout {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        margin-top: 30px;
    }

    .card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: 0.3s ease;
    }
    
    .card:hover { transform: translateY(-5px); }

    /* SEÇÕES ESPECÍFICAS */
    .problem-item { border-left: 5px solid #FF6B6B; background: #FFF5F5; }
    .benefit-card { border-top: 4px solid #37D087; text-align: center; }
    .lose-item { border-left: 5px solid #FF6B6B; }
    
    .solution-section {
        background: white;
        padding: 60px 40px;
        border-radius: 20px;
        border: 2px solid #37D087;
        text-align: center;
    }

    .quote-highlight { color: #37D087; font-weight: 800; }

    /* BOTÕES */
    .btn-main {
        display: inline-block;
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: white !important;
        padding: 18px 45px;
        border-radius: 50px;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 10px 20px rgba(55, 208, 135, 0.3);
        border: none;
    }

    /* FAQ */
    .faq-item {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .faq-question { color: #952791; font-weight: 700; margin-bottom: 5px; }

    @media (max-width: 768px) {
        .hero h1 { font-size: 2.2rem; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. HERO ---
st.markdown("""
    <div class="hero">
        <div class="container">
            <h1>🧠 A Cortex é a primeira plataforma desenvolvida para te ensinar comportamento em 21 dias</h1>
            <p class="hero-subtitle">
                Fim dos cursos chatos e PDFs intermináveis. Mais de 15.000 alunos dominando o conhecimento dos 22 maiores best-sellers do mundo.
            </p>
            <a href="#cta" class="btn-main">⚡ Começar Agora</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 2. PROBLEMAS ---
st.markdown("""
    <div class="container">
        <h2 style="text-align:center; color:#952791;">❌ Qual o problema dos demais que tentam ensinar?</h2>
        <div class="grid-layout">
            <div class="card problem-item">
                <h3>📚 Sobrecarga</h3>
                <p>Milhares de livros. Qual ler? Você fica perdido entre teorias contraditórias.</p>
            </div>
            <div class="card problem-item">
                <h3>⏰ Tempo Perdido</h3>
                <p>Ler 7.000 páginas leva meses. Você quer resultados AGORA, não no ano que vem.</p>
            </div>
            <div class="card problem-item">
                <h3>🤔 Sem Prática</h3>
                <p>A teoria é linda, mas na hora do conflito real, você trava por não saber aplicar.</p>
            </div>
            <div class="card problem-item">
                <h3>💰 Custo Elevado</h3>
                <p>Cursos caros, genéricos e que não se adaptam à sua realidade específica.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 3. SOLUÇÃO ---
st.markdown("""
    <div class="container">
        <div class="solution-section">
            <h2 style="color:#952791;">✅ Aprenda com especialistas</h2>
            <p style="font-size:1.3rem; line-height:1.6;">
                "Você não precisa ler 7.000 páginas. <span class="quote-highlight">A Cortex filtrou o ouro de cada mestre para você aplicar hoje mesmo.</span>"
            </p>
            <p style="color:#666; margin-top:20px;">Um programa de 21 dias prático e sem enrolação.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 4. BENEFÍCIOS ---
st.markdown("""
    <div class="container">
        <h2 style="text-align:center; color:#952791;">🎯 Características principais</h2>
        <div class="grid-layout">
            <div class="card benefit-card"><h3>⚡ Tempo Perfeito</h3><p>Resultados sólidos em 21 dias.</p></div>
            <div class="card benefit-card"><h3>🎯 100% Prático</h3><p>Atividades diárias de aplicação real.</p></div>
            <div class="card benefit-card"><h3>🧠 Científico</h3><p>Baseado em Psicologia e Neurociência.</p></div>
            <div class="card benefit-card"><h3>🚀 Relacionamentos</h3><p>Entenda as pessoas e mude conexões.</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. MICROLEARNING ---
st.markdown("""
    <div style="background: #F3E5F5; padding: 60px 0;">
        <div class="container">
            <h2 style="text-align:center; color:#952791;">🧬 Microlearning = Aprendizado Real</h2>
            <div class="grid-layout">
                <div class="card"><h3>🔗 Links Cerebrais</h3><p>Conexão com exemplos reais para memória duradoura.</p></div>
                <div class="card"><h3>⏱️ Sessões Curtas</h3><p>15-20 minutos por dia. O tempo ideal para o cérebro.</p></div>
                <div class="card"><h3>🔄 Repetição</h3><p>Conceitos revisitados para você nunca mais esquecer.</p></div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. O QUE VOCÊ PERDE ---
st.markdown("""
    <div class="container">
        <h2 style="text-align:center; color:#FF6B6B;">⚠️ O risco de não entender a mente humana:</h2>
        <div class="grid-layout">
            <div class="card lose-item"><h3>😔 Relações Vazias</h3><p>Preso em conflitos desnecessários.</p></div>
            <div class="card lose-item"><h3>📉 Procrastinação</h3><p>Sem entender seus motivos, você não avança.</p></div>
            <div class="card lose-item"><h3>💔 Insegurança</h3><p>Dúvida constante por falta de autoconhecimento.</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 7. FAQ ---
st.markdown("""
    <div class="container">
        <h2 style="text-align:center; color:#952791;">❓ Perguntas Frequentes</h2>
        <div class="faq-item">
            <div class="faq-question">Quanto tempo leva para ver resultados?</div>
            <div class="faq-answer">Muitos notam mudanças já na primeira semana de atividades.</div>
        </div>
        <div class="faq-item">
            <div class="faq-question">Preciso de experiência?</div>
            <div class="faq-answer">Não, a jornada é desenhada do zero ao avançado.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 8. CTA FINAL ---
st.markdown("""
    <div id="cta" style="text-align:center; padding: 80px 20px; background: linear-gradient(90deg, #37D087, #39D7FE); color:white; border-radius:30px; margin: 40px 20px;">
        <h2>🚀 Transforme sua vida hoje</h2>
        <p>Acesso vitalício | 21 dias de jornada | Resultados reais</p>
        <a href="https://seu-checkout.com" class="btn-main" style="background: white; color: #37D087 !important; margin-top:20px;">QUERO COMEÇAR AGORA</a>
    </div>
""", unsafe_allow_html=True)

# --- 9. FOOTER ---
st.markdown("""
    <div class="container" style="text-align:center; color:#999; font-size:0.8rem;">
        <p>© 2026 Inteligência Cortex. Todos os direitos reservados.</p>
    </div>
""", unsafe_allow_html=True)
