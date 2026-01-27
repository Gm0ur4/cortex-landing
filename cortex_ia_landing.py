import streamlit as st

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Cortex | Inteligência Comportamental", page_icon="🧠", layout="wide")

# --- CSS DE ALTA CONVERSÃO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    :root {
        --primary: #952791;
        --secondary: #37D087;
        --dark: #0f172a;
    }

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background: #0f172a; /* Fundo Escuro para passar sofisticação */
        color: white;
    }

    /* Animações */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .reveal { animation: fadeInUp 0.8s ease-out; }

    /* Hero Section */
    .hero-container {
        padding: 120px 20px;
        text-align: center;
        background: radial-gradient(circle at center, rgba(149, 39, 145, 0.15) 0%, rgba(15, 23, 42, 1) 70%);
    }

    .badge {
        background: rgba(55, 208, 135, 0.1);
        border: 1px solid var(--secondary);
        color: var(--secondary);
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 20px;
        display: inline-block;
    }

    .main-title {
        font-size: 4.5rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #FFF 60%, #952791 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* Glass Cards */
    .card-vendas {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 24px;
        transition: 0.3s;
    }

    .card-vendas:hover {
        border: 1px solid var(--primary);
        transform: translateY(-5px);
    }

    /* Botão Irresistível */
    .cta-button {
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: #000 !important;
        padding: 22px 60px;
        border-radius: 12px;
        font-size: 1.3rem;
        font-weight: 800;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 10px 40px rgba(55, 208, 135, 0.3);
        transition: 0.3s;
        border: none;
        cursor: pointer;
    }

    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 50px rgba(55, 208, 135, 0.5);
    }

    .sub-cta {
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 15px;
    }

    /* Seção de Dor (The Gap) */
    .pain-section {
        background: #000;
        padding: 80px 20px;
        border-radius: 30px;
        margin: 40px 0;
    }

    h2 { font-size: 2.5rem !important; font-weight: 700 !important; text-align: center; }
    .highlight-green { color: var(--secondary); }
    .highlight-purple { color: var(--primary); }

    </style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
    <div class="hero-container reveal">
        <span class="badge">🔥 15.000+ Alunos Ativos</span>
        <h1 class="main-title">Instale o "Software" do Comportamento Humano no seu Cérebro.</h1>
        <p style="font-size: 1.4rem; color: #cbd5e1; max-width: 900px; margin: 0 auto 40px auto;">
            A Cortex não é um curso. É um <b>upgrade mental</b> de 21 dias. <br>
            Aprenda a ler pessoas, negociar como um mestre e dominar suas emoções usando as mesmas técnicas da elite global.
        </p>
        <a href="https://cortexcheckout.streamlit.app" class="cta-button">QUERO ACESSO IMEDIATO ⚡</a>
        <p class="sub-cta">Pagamento seguro via Eduzz • Acesso Vitalício</p>
    </div>
""", unsafe_allow_html=True)

# --- THE PROBLEM (A DOR) ---
st.markdown("""
    <div class="pain-section">
        <h2>Você está perdendo dinheiro e oportunidades por ser <span style="color: #ff4b4b;">"Cego Comportamental"</span>?</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 50px;">
            <div class="card-vendas">
                <h3 style="color: #ff4b4b;">O Problema</h3>
                <p style="color: #94a3b8;">90% das pessoas fracassam não por falta de técnica, mas por não entenderem de <b>GENTE</b>. Elas perdem vendas, destroem relacionamentos e são manipuladas sem perceber.</p>
            </div>
            <div class="card-vendas">
                <h3 class="highlight-green">A Solução Cortex</h3>
                <p style="color: #94a3b8;">Nós decodificamos 22 best-sellers mundiais (7.000+ páginas) em um método prático. Você aprende o que realmente importa em 15 minutos por dia.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- MÉTODOS (OS DIFERENCIAIS) ---
st.markdown("""
    <div style="padding: 60px 0;">
        <h2 style="margin-bottom: 50px;">Por que a Cortex <span class="highlight-purple">Vende e Entrega</span>?</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
            <div class="card-vendas" style="text-align: center;">
                <div style="font-size: 3rem;">🛰️</div>
                <h4>Micro-Doses de Poder</h4>
                <p style="font-size: 0.9rem;">Nada de aulas de 1 hora. Pílulas de conhecimento direto na veia para execução imediata.</p>
            </div>
            <div class="card-vendas" style="text-align: center;">
                <div style="font-size: 3rem;">🤖</div>
                <h4>IA Comportamental 24/7</h4>
                <p style="font-size: 0.9rem;">Um consultor de psicologia treinado nas maiores obras do mundo para tirar suas dúvidas em tempo real.</p>
            </div>
            <div class="card-vendas" style="text-align: center;">
                <div style="font-size: 3rem;">💸</div>
                <h4>ROI Imediato</h4>
                <p style="font-size: 0.9rem;">Use o que aprendeu na reunião da manhã para fechar o contrato à tarde.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- CTA FINAL DE IMPACTO ---
st.divider()
st.markdown("""
    <div style="text-align: center; padding: 100px 20px; background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%); border-radius: 40px;">
        <h2 style="margin-bottom: 20px;">Pare de tentar adivinhar o que as pessoas pensam.</h2>
        <p style="font-size: 1.2rem; margin-bottom: 40px; color: #94a3b8;">O conhecimento que separa os líderes dos seguidores agora está ao seu alcance.</p>
        <div style="background: rgba(255,255,255,0.05); display: inline-block; padding: 20px 40px; border-radius: 20px; border: 1px dashed #37D087; margin-bottom: 30px;">
            <span style="font-size: 1.5rem; font-weight: 800; color: #37D087;">Oferta Especial: Acesso Vitalício Liberado</span>
        </div><br>
        <a href="https://cortexcheckout.streamlit.app" class="cta-button">GARANTIR MINHA VAGA AGORA 🚀</a>
        <div style="margin-top: 30px;">
            <img src="https://img.icons8.com/color/48/000000/visa.png" width="35"/>
            <img src="https://img.icons8.com/color/48/000000/mastercard.png" width="35"/>
            <img src="https://img.icons8.com/color/48/000000/pix.png" width="35"/>
        </div>
    </div>
""", unsafe_allow_html=True)
