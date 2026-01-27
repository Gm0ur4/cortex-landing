import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cortex | Protocolo de Inteligência Comportamental",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- ESTILO AVANÇADO (CSS PROFISSIONAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    /* Reset de Elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #0A0E14 !important; /* Fundo Escuro para Autoridade */
        color: #E2E8F0;
    }

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Container Principal */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    
    /* HERO SECTION */
    .hero {
        padding: 60px 0;
        text-align: center;
        background: radial-gradient(circle at center, #1A222E 0%, #0A0E14 100%);
        border-radius: 30px;
        border: 1px solid #2D3748;
        margin-bottom: 40px;
    }
    
    .badge {
        background: rgba(55, 208, 135, 0.1);
        color: #37D087;
        padding: 8px 16px;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 1px solid rgba(55, 208, 135, 0.3);
    }

    .hero h1 {
        color: #FFFFFF;
        font-size: 3.2rem;
        font-weight: 800;
        margin: 20px 0;
        letter-spacing: -1px;
        line-height: 1.1;
    }
    
    .hero h1 span {
        background: linear-gradient(90deg, #37D087, #39D7FE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.2rem;
        max-width: 700px;
        margin: 0 auto 40px;
        line-height: 1.6;
    }
    
    .cta-button {
        background: #37D087;
        color: #0A0E14 !important;
        padding: 20px 50px;
        border-radius: 12px;
        font-weight: 800;
        font-size: 1.2rem;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(55, 208, 135, 0.2);
        text-transform: uppercase;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(55, 208, 135, 0.4);
        background: #41E094;
    }

    /* GRID DE MÉTODO */
    .method-card {
        background: #161B22;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #30363D;
        height: 100%;
    }

    .method-card h3 {
        color: #37D087;
        margin-bottom: 15px;
        font-size: 1.3rem;
    }

    .method-card p {
        color: #8B949E;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* SECTION TITLES */
    .section-title {
        text-align: center;
        margin: 80px 0 40px;
    }
    
    .section-title h2 {
        font-size: 2.2rem;
        color: #FFFFFF;
    }

    /* PROVA SOCIAL CLEAN */
    .stat-box {
        text-align: center;
        padding: 20px;
        border-right: 1px solid #30363D;
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #FFFFFF;
        display: block;
    }

    .stat-label {
        color: #8B949E;
        font-size: 0.8rem;
    }

    /* FAQ */
    .faq-container {
        background: #161B22;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
        border: 1px solid #30363D;
    }

    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO DA PÁGINA ---

with st.container():
    # Hero Section
    st.markdown(f"""
        <div class="main-container">
            <div class="hero">
                <span class="badge">Protocolo Neurocientífico 2026</span>
                <h1>Assuma o Controle do <span>Código Humano</span></h1>
                <p class="hero-subtitle">
                    O Cortex não é um curso. É um sistema de ativação de 21 dias que instala as habilidades de persuasão, leitura fria e domínio emocional que levaram décadas para serem decifradas.
                </p>
                <a href="https://cortexcheckout.streamlit.app" target="_blank" class="cta-button">
                    Ativar meu Acesso
                </a>
                <p style="margin-top: 20px; font-size: 0.8rem; color: #4A5568;">
                    ⚡ Acesso Imediato • 22 Best-sellers Processados • IA de Suporte Inclusa
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stats Section (Social Proof sutil e elegante)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-box"><span class="stat-number">15k+</span><span class="stat-label">Operadores</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box"><span class="stat-number">4.9/5</span><span class="stat-label">Satisfação</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box"><span class="stat-number">92%</span><span class="stat-label">Retenção</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-box" style="border:none"><span class="stat-number">24/7</span><span class="stat-label">Suporte IA</span></div>', unsafe_allow_html=True)

    # Por que o Cortex?
    st.markdown('<div class="section-title"><h2>O fim da obesidade mental</h2><p style="color:#8B949E">Chega de ler 500 páginas para extrair 1 insight. Nós filtramos o ruído.</p></div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="method-card"><h3>⚡ Microlearning</h3><p>Sessões de 15 minutos desenhadas para a janela de atenção do cérebro moderno. Absorção máxima, fadiga zero.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="method-card"><h3>🧠 Neuro-ativação</h3><p>Não é teoria. São desafios práticos diários que forçam a criação de novas sinapses comportamentais.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="method-card"><h3>🤖 Cortex AI</h3><p>Uma inteligência treinada nos maiores bancos de dados de psicologia do mundo para resolver seus problemas em tempo real.</p></div>""", unsafe_allow_html=True)

    # Demonstração
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: linear-gradient(90deg, #1A222E, #0A0E14); padding: 40px; border-radius: 20px; border: 1px dashed #37D087; text-align: center;">
            <h3 style="color: white; margin-bottom: 20px;">Quer ver a engenharia por dentro?</h3>
            <a href="https://aprendizadocortexdemo.streamlit.app/" target="_blank" style="color: #37D087; text-decoration: none; font-weight: 700;">
                TESTAR DEMONSTRAÇÃO GRATUITA →
            </a>
        </div>
    """, unsafe_allow_html=True)

    # FAQ Reduzido e Direto
    st.markdown('<div class="section-title"><h2>Dúvidas de quem pensa</h2></div>', unsafe_allow_html=True)
    
    with st.expander("O acesso expira em 21 dias?"):
        st.write("Não. O protocolo de ativação dura 21 dias, mas o acesso à plataforma e a todas as futuras atualizações é vitalício.")
    
    with st.expander("Como a IA funciona na prática?"):
        st.write("Você descreve um conflito (ex: 'Tenho uma reunião difícil com um chefe autoritário') e a Cortex AI analisa os gatilhos e te dá o roteiro exato de comportamento baseado em ciência.")

    # CTA Final
    st.markdown(f"""
        <div style="text-align: center; padding: 100px 0;">
            <h2 style="color: white; font-size: 2.5rem; margin-bottom: 30px;">Pronto para sair do automático?</h2>
            <a href="https://cortexcheckout.streamlit.app" target="_blank" class="cta-button">
                Quero o Protocolo Completo
            </a>
            <p style="margin-top: 20px; color: #8B949E;">R$ 39,90 no Plano Start • R$ 79,90 no Plano Expert (IA Inclusa)</p>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown('<div style="text-align: center; color: #4A5568; padding: 40px; border-top: 1px solid #1A222E;">© 2026 Cortex Intelligence System</div>', unsafe_allow_html=True)
