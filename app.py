import streamlit as st
import pandas as pd
import numpy as np

# Configuração de Layout
st.set_page_config(page_title="CAR 360", layout="wide")

# CSS customizado para garantir o visual "Governo Moderno"
st.markdown("""
    <style>
    /* Paleta de Cores CAR 360 */
    :root {
        --cor-azul: #003366;
        --cor-verde: #228B22;
        --fundo: #f4f7f6;
    }
    
    .stApp { background-color: var(--fundo); }
    
    h1, h2, h3 { color: var(--cor-azul) !important; font-weight: 700; }
    
    /* Botões seguindo a marca */
    div.stButton > button {
        background-color: var(--cor-azul) !important;
        color: white !important;
        border-radius: 8px;
        border: none;
    }
    
    /* Cards de Persona e Indicadores */
    .metric-card {
        background: white;
        border: 2px solid var(--cor-azul);
        border-radius: 12px;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Navegação
st.sidebar.image("logo.png", width=150)
menu = st.sidebar.radio("Navegação", ["Início", "Produtor", "Analista", "Gestor", "Arquitetura"])

# --- WIREFRAME 1: Login e Acesso ---
if menu == "Início":
    st.image("logo.png", width=150)
    st.title("CAR 360")
    st.subheader("Plataforma Nacional de Inteligência Territorial")
    st.markdown("### 🌎 Um único ambiente para todo o ecossistema CAR")
    st.button("Entrar com Gov.br")
    
    st.write("---")
    st.write("#### Como deseja acessar?")
    cols = st.columns(3)
    cols[0].button("👨‍🌾 Produtor Rural")
    cols[1].button("🧑‍💻 Analista Ambiental")
    cols[2].button("🏛 Gestor Público")
    
    st.write("#### Bases Integradas")
    st.write("✓ SICAR | ✓ Consulta Pública | ✓ SNIF | ✓ RER | ✓ Gov.br | ✓ Painéis CAR")

# --- WIREFRAME 2, 3, 4: Produtor ---
elif menu == "Produtor":
    st.header("👨‍🌾 Regularização Ambiental")
    with st.container():
        st.write("### Identificação")
        st.checkbox("CPF")
        st.checkbox("Gov.br")
        st.checkbox("Localização")
    
    st.success("Informações confirmadas: Proprietário, Área, Município, APP, Reserva Legal, Hidrografia")
    
    if st.button("Confirmar Cadastro"):
        st.metric("Score de Confiabilidade", "92%", delta_color="normal")
        st.progress(0.92)
        st.warning("⚠ Sobreposição detectada. Clique para entender.")
        if st.button("💬 Assistente CAR 360"):
            st.info("A legislação determina que áreas de APP devem ser preservadas. Clique aqui para ver no mapa.")

# --- WIREFRAME 5: Analista ---
elif menu == "Analista":
    st.header("🧑‍💻 Fila do Analista")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔴 Alto Risco", 182)
    c2.metric("🟡 Médio Risco", 652)
    c3.metric("🟢 Baixo Risco", 3542)
    
    st.write("---")
    st.subheader("Workspace: CAR 345781")
    st.error("Parecer da IA: Propriedade apresenta inconsistência na delimitação da APP.")
    
    b1, b2, b3 = st.columns(3)
    b1.button("Aprovar"); b2.button("Solicitar Correção"); b3.button("Encaminhar")

# --- WIREFRAME 6, 7: Gestão ---
elif menu == "Gestor":
    st.header("🏛 Painel Nacional")
    st.map(pd.DataFrame(np.random.randn(20, 2)/50 + [-15, -50], columns=['lat', 'lon']))
    
    m1, m2 = st.columns(2)
    m1.metric("Cobertura CAR", "87%")
    m2.metric("Pendentes", "18%")
    
    st.success("IA Recomendação: Aumentar equipe de análise na região Norte.")

# --- WIREFRAME 8: Arquitetura ---
elif menu == "Arquitetura":
    st.header("Arquitetura do Sistema")
    st.info("BASES: SICAR | SNIF | Gov.br | RER | SIGEF")
    st.markdown("---")
    st.write("### [ CAR 360 ]")
    st.write("IA Generativa • Motor de Score • Governança")
    st.markdown("---")
    st.write("Produtor ➡️ Analista ➡️ Gestor")
