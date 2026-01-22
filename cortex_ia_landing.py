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
        background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%) !important;
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
        color: #952791;
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
    
    .hero-cta {
        display: inline-block;
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
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
        background: #FFF5F5;
        border-radius: 12px;
        border-left: 5px solid #FF6B6B;
    }
    
    .problem-item h3 {
        color: #FF6B6B;
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
        background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%);
        border-radius: 12px;
        border: 2px solid #37D087;
    }
    
    .stat-number {
        color: #37D087;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
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
    }
    
    .faq-section h2 {
        color: #952791;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 800;
    }
    
    .faq-item {
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .faq-question {
        color: #952791;
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 10px;
    }
    
    .faq-answer {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* CTA FINAL */
    .final-cta {
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
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
        background: white;
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
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
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
            <h1>🧠 A Cortex é a primeira plataforma desenvolvida para te ensinar comportamento em 21 dias</h1>
            <p class="hero-subtitle">
                Somos pioneiros a dar o fim em cursos chatos e PDFs intermináveis.<br>
                <strong>São mais de 15.000 alunos absorvendo o conhecimento dos 22 maiores best-sellers do mundo</strong>
            </p>
            <button class="hero-cta" onclick="document.querySelector('.final-cta').scrollIntoView({behavior: 'smooth'})">
                ⚡ Começar Agora
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROBLEMA ---
st.markdown("""
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
                <div class="problem-item">
                    <h3>🤔 Sem aplicação prática</h3>
                    <p>Você lê, aprende a teoria, mas não sabe como aplicar na vida real. Relacionamentos, trabalho, pessoal... tudo continua igual.</p>
                </div>
                <div class="problem-item">
                    <h3>💰 Cursos caros e genéricos</h3>
                    <p>Cursos de comportamento custam caro, duram meses e não são personalizados para sua realidade específica.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SOLUÇÃO ---
st.markdown("""
    <div class="container">
        <div class="solution-section">
            <h2>✅ Aprenda com quem é especialista no assunto</h2>
            <div class="quote-box">
                <p class="quote-text">
                    Você não precisa ler mais de 7.000 páginas para dominar a mente humana. 
                    <span class="quote-highlight">A Cortex já processou, filtrou e organizou o ouro de cada mestre da inteligência humana para você aplicar hoje mesmo.</span>
                </p>
            </div>
            <p style="color: #666; font-size: 1.05rem; line-height: 1.8; text-align: center; margin-top: 30px;">
                A Cortex é um <strong>programa de 21 dias</strong> com atividades práticas que te ensinam os princípios fundamentais 
                do comportamento humano. Sem teoria chata. Sem PDFs gigantes. Apenas <strong>o essencial para você aplicar e transformar sua vida.</strong>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BENEFÍCIOS ---
st.markdown("""
    <div class="container">
        <div class="benefits-section">
            <h2>🎯 Características principais</h2>
            <div class="benefits-grid">
                <div class="benefit-card">
                    <div class="benefit-icon">⚡</div>
                    <h3>Aprenda no tempo perfeito</h3>
                    <p>Não em 6 meses. Não em 1 ano. Em apenas 21 dias você terá os conhecimentos que levaria meses para ler em livros e cursos.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🎯</div>
                    <h3>100% prático</h3>
                    <p>Cada dia tem atividades que você faz. Sem teoria chata. Sem vídeos longos. Pura aplicação.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🧠</div>
                    <h3>Baseado em ciência</h3>
                    <p>Todos os conceitos vêm das melhores referências mundiais sobre comportamento humano. Você aprende só o que realmente funciona.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">💡</div>
                    <h3>Aplique imediatamente</h3>
                    <p>Aprenda uma técnica e use no mesmo dia. Com seus relacionamentos, no trabalho, em casa. Resultados reais.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🚀</div>
                    <h3>Transforme relacionamentos</h3>
                    <p>Entenda por que as pessoas agem como agem. Mude conflitos em conexões. Construa relacionamentos mais fortes.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">💪</div>
                    <h3>Domine sua mente</h3>
                    <p>Entenda seus próprios padrões. Vença a procrastinação, ansiedade e insegurança. Tome controle da sua vida.</p>
                </div>
            </div>
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
                    <p>Tudo segue as melhores práticas de neurociência e psicologia cognitiva. Todo conteúdo sempre estará citando de onde vem a base. Aprendizado que funciona.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- O QUE VOCÊ PERDE ---
st.markdown("""
    <div class="container">
        <div class="loses-section">
            <h2>⚠️ Quem não entende comportamento humano está à mercê de:</h2>
            <div class="loses-grid">
                <div class="lose-item">
                    <h3>😔 Relações superficiais </h3>
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
                <div class="lose-item">
                    <h3>🔄 Ciclos repetidos</h3>
                    <p>Infelizmente, sem entender seus padrões, você repete os mesmos erros. Relacionamentos que fracassam. Oportunidades perdidas.</p>
                </div>
                <div class="lose-item">
                    <h3>⏳ Tempo desperdiçado</h3>
                    <p>Cada dia que passa sem esse conhecimento é um dia que você poderia estar transformando sua vida.</p>
                </div>
                <div class="lose-item">
                    <h3>💰 Potencial não realizado</h3>
                    <p>Você tem potencial. Mas sem entender comportamento, você fica preso. Nunca alcança o que poderia ser.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROVA SOCIAL ---
st.markdown("""
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
        <div style="background: white; padding: 60px 20px; margin: 40px 0; border-radius: 16px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08); text-align: center;">
            <h2 style="color: #952791; font-size: 2.2rem; margin-bottom: 50px; font-weight: 800;">📊 Confie nos nossos números</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; margin-bottom: 50px;">
                <div style="padding: 30px; background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%); border-radius: 12px; border: 2px solid #37D087;">
                    <p style="color: #37D087; font-size: 2.5rem; font-weight: 800; margin: 0;">15.000+</p>
                    <p style="color: #666; font-size: 0.95rem; margin: 10px 0 0 0;">Usuários ativos</p>
                </div>
                <div style="padding: 30px; background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%); border-radius: 12px; border: 2px solid #37D087;">
                    <p style="color: #37D087; font-size: 2.5rem; font-weight: 800; margin: 0;">4.9★</p>
                    <p style="color: #666; font-size: 0.95rem; margin: 10px 0 0 0;">Avaliação média</p>
                </div>
                <div style="padding: 30px; background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%); border-radius: 12px; border: 2px solid #37D087;">
                    <p style="color: #37D087; font-size: 2.5rem; font-weight: 800; margin: 0;">92%</p>
                    <p style="color: #666; font-size: 0.95rem; margin: 10px 0 0 0;">Taxa de conclusão</p>
                </div>
                <div style="padding: 30px; background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%); border-radius: 12px; border: 2px solid #37D087;">
                    <p style="color: #37D087; font-size: 2.5rem; font-weight: 800; margin: 0;">+40K</p>
                    <p style="color: #666; font-size: 0.95rem; margin: 10px 0 0 0;">Vidas transformadas</p>
                </div>
            </div>
            
            <h3 style="color: #952791; font-size: 1.8rem; margin-top: 50px; margin-bottom: 30px; font-weight: 800;">
                O Que Dizem Nossos Clientes
            </h3>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
                <div style="background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%); padding: 30px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08); border-left: 5px solid #37D087;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 15px;">⭐⭐⭐⭐⭐</div>
                    <p style="color: #666; font-size: 0.95rem; line-height: 1.6; margin-bottom: 15px; font-style: italic;">
                        "Cortex IA mudou minha vida. Em 21 dias aprendi mais sobre comportamento humano do que em 5 anos lendo livros. Agora entendo por que as pessoas agem como agem e consigo lidar melhor com tudo."
                    </p>
                    <div style="color: #952791; font-weight: 700; font-size: 0.9rem;">Maria Silva</div>
                </div>
                
                <div style="background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%); padding: 30px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08); border-left: 5px solid #37D087;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 15px;">⭐⭐⭐⭐⭐</div>
                    <p style="color: #666; font-size: 0.95rem; line-height: 1.6; margin-bottom: 15px; font-style: italic;">
                        "As atividades práticas são incríveis. Não é teoria chata. É algo que você faz e já vê resultado. Meus relacionamentos melhoraram muito."
                    </p>
                    <div style="color: #952791; font-weight: 700; font-size: 0.9rem;">João Santos</div>
                </div>
                
                <div style="background: linear-gradient(135deg, #FFFFFF 0%, #F9F9F9 100%); padding: 30px; border-radius: 12px; box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08); border-left: 5px solid #37D087;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 15px;">⭐⭐⭐⭐⭐</div>
                    <p style="color: #666; font-size: 0.95rem; line-height: 1.6; margin-bottom: 15px; font-style: italic;">
                        "Finalmente entendi meus próprios padrões de comportamento. Isso me libertou de inseguranças que carregava há anos. Recomendo para todos."
                    </p>
                    <div style="color: #952791; font-weight: 700; font-size: 0.9rem;">Ana Costa</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- DEMO ---
st.markdown("""
    <div class="container">
        <div class="demo-section">
            <h2>🎬 Veja como funciona</h2>
            <p style="color: #666; font-size: 1.05rem; margin-bottom: 30px; line-height: 1.8;">
                Quer ver um exemplo de como é uma atividade prática? Clique abaixo para acessar uma demonstração gratuita.
            </p>
            <button class="demo-btn" onclick="window.open('https://cortex-ia-demo.streamlit.app', '_blank')">
                🎥 Ver Demonstração Gratuita
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FAQ ---
st.markdown("""
    <div class="container">
        <div class="faq-section">
            <h2>❓ Perguntas frequentes</h2>
            
            <div class="faq-item">
                <div class="faq-question">Quanto tempo leva para ver resultados?</div>
                <div class="faq-answer">
                    Muitos clientes começam a notar mudanças na primeira semana. Os 21 dias são estruturados para uma transformação progressiva. Você vai perceber que entende melhor as pessoas, consegue lidar melhor com conflitos e se conhece mais.
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Preciso ter experiência anterior?</div>
                <div class="faq-answer">
                    Não! Cortex IA é para todos. Desde iniciantes até pessoas que já estudam comportamento. Cada um aprende no seu ritmo e aproveita conforme seu nível.
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Quanto tempo por dia preciso dedicar?</div>
                <div class="faq-answer">
                    Apenas 15-20 minutos por dia. É microlearning. Você faz a atividade do dia e pronto. Sem necessidade de longas sessões de estudo.
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Posso acessar para sempre?</div>
                <div class="faq-answer">
                    Sim! Você tem acesso vitalício à plataforma. Pode revisar o conteúdo quantas vezes quiser e receberá todas as atualizações futuras.
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">E se não gostar?</div>
                <div class="faq-answer">
                    Você tem 7 dias para explorar. Se não achar valor, é fácil resolver. Mas a maioria das pessoas adora desde o primeiro dia.
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Posso fazer o curso com outras pessoas?</div>
                <div class="faq-answer">
                    Sim! Muitas pessoas fazem juntas e compartilham experiências. Você pode fazer sozinho ou com amigos. Ambas as formas funcionam.
                </div>
            </div>
            
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CTA FINAL ---
st.markdown("""
    <div class="container">
        <div class="final-cta">
            <h2>🚀 Comece sua transformação hoje</h2>
            <p>
                Você pode continuar como está. Ou pode dar 21 dias para transformar sua vida.<br>
                <strong>A escolha é sua.</strong>
            </p>
            <button class="final-cta-btn" onclick="window.location.href='https://seu-checkout.streamlit.app'">
                ⚡ Começar Agora
            </button>
            <p style="margin-top: 30px; font-size: 0.9rem; opacity: 0.9;">
                Acesso vitalício • Sem contratos • Comece hoje
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="container">
        <div class="footer">
            <p>© 2026 Inteligência Cortex. Todos os direitos reservados.</p>
            <p>
                <a href="#">Política de Privacidade</a> | 
                <a href="#">Termos de Uso</a> | 
                <a href="#">Contato</a>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
