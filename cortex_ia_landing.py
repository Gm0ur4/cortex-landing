import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Cortex - High Performance Mind", page_icon="🧠", layout="wide")

# --- ESTILO PREMIUM 2.0 (CSS AVANÇADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* Variáveis de Cor */
    :root {
        --primary: #952791;
        --secondary: #37D087;
        --accent: #39D7FE;
        --bg-dark: #0f172a;
    }

    * { font-family: 'Inter', sans-serif; }

    /* Fundo com movimento sutil */
    .stApp {
        background: radial-gradient(circle at top right, #fdf4ff, #e0f2fe);
        background-attachment: fixed;
    }

    /* Animação de Entrada */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .reveal { animation: fadeInUp 0.8s ease-out forwards; }

    /* Efeito Glassmorphism nos Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 30px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .glass-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        background: rgba(255, 255, 255, 0.9);
    }

    /* Título Hero com Gradiente */
    .hero-title {
        background: linear-gradient(90deg, #952791, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem !important;
        font-weight: 800;
        line-height: 1.1;
    }

    /* Botão Neon */
    .btn-neon {
        background: linear-gradient(90deg, #37D087, #39D7FE);
        color: white !important;
        padding: 20px 50px;
        border-radius: 50px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: none;
        box-shadow: 0 0 20px rgba(55, 208, 135, 0.4);
        transition: 0.3s;
        text-decoration: none;
        display: inline-block;
    }

    .btn-neon:hover {
        box-shadow: 0 0 35px rgba(55, 208, 135, 0.6);
        transform: scale(1.05);
    }
    
    /* Grid Adjustments */
    .custom-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(f"""
    <div style="text-align: center; padding: 100px 20px;" class="reveal">
        <p style="color: #952791; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;">A Revolução do Comportamento</p>
        <h1 class="hero-title">Domine a mente humana<br>em 21 dias.</h1>
        <p style="color: #64748b; font-size: 1.2rem; max-width: 800px; margin: 30px auto;">
            A Cortex filtra o conhecimento dos 22 maiores best-sellers do mundo e entrega 
            em pílulas práticas de 15 minutos. Ciência aplicada, sem enrolação.
        </p>
        <br>
        <a href="https://cortexcheckout.streamlit.app" class="btn-neon">Começar Jornada Agora</a>
    </div>
""", unsafe_allow_html=True)

# --- FEATURE SECTION (GLASSMORTHISM) ---
st.markdown("""
    <div class="custom-grid">
        <div class="glass-card">
            <h3 style="color: #952791;">⚡ Microlearning</h3>
            <p>Sessões rápidas de 15 minutos que se encaixam na sua rotina, focadas em retenção máxima.</p>
        </div>
        <div class="glass-card">
            <h3 style="color: #952791;">🧠 Neurociência</h3>
            <p>Todo o conteúdo é baseado em como o cérebro processa novas informações e cria hábitos.</p>
        </div>
        <div class="glass-card">
            <h3 style="color: #952791;">🎯 Prática Real</h3>
            <p>Chega de PDF. Você recebe missões diárias para aplicar o que aprendeu no mundo real.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Continuação do seu FAQ e Depoimentos...
