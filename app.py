import streamlit as st
import pandas as pd
import numpy as np

# Configuração de Layout
st.set_page_config(page_title="CAR 360", layout="wide")

# CSS customizado para garantir o visual "Governo Moderno"
st.markdown("""
    <style>
    /* Força o fundo da página principal para um cinza bem claro */
    .stApp {
        background-color: #f0f2f6;
    }
    /* Força a cor de todos os textos para preto escuro */
    h1, h2, h3, p, div, span {
        color: #000000 !important;
    }
    /* Ajuste dos botões para ficarem visíveis */
    .stButton>button {
        background-color: #003399 !important;
        color: white !important;
        border: none;
        font-weight: bold;
    }
    /* Deixa o conteúdo do container bem visível */
    .main .block-container {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Navegação
st.sidebar.image("logo.png", width=150)
menu = st.sidebar.radio("Navegação", ["Início", "Produtor", "Analista", "Gestor", "Arquitetura"])

# --- WIREFRAME 1 ---
if menu == "Início":
    st.title("CAR 360")
    st.subheader("Plataforma Nacional de Inteligência Territorial")
    st.info("🌎 Um único ambiente para todo o ecossistema CAR")
    st.button("Entrar com Gov.br")
    st.write("---")
    st.write("### Como deseja acessar?")
    col1, col2, col3 = st.columns(3)
    col1.button("👨‍🌾 Produtor Rural"); col2.button("🧑‍💻 Analista Ambiental"); col3.button("🏛 Gestor Público")
    st.write("### Bases Integradas")
    for base in ["SICAR", "Consulta Pública", "SNIF", "RER", "Gov.br", "Painéis CAR", "Bases Geoespaciais"]:
        st.write(f"✓ {base}")

# --- WIREFRAMES 2, 3, 4 ---
elif menu == "Produtor":
    st.header("👨‍🌾 Regularização Ambiental")
    with st.expander("Identificação", expanded=True):
        st.write("✔ CPF | ✔ Gov.br | ✔ Localização")
    with st.expander("Informações Encontradas"):
        for item in ["Proprietário", "Área", "Município", "APP", "Reserva Legal", "Hidrografia"]:
            st.write(f"✔ {item}")
    if st.button("Confirmar"):
        st.subheader("Validação Inteligente")
        st.progress(0.92)
        st.metric("Score de Confiabilidade", "92%")
        st.warning("⚠ Existe uma pequena sobreposição. Clique para visualizar.")
        with st.chat_message("assistant"):
            st.write("**Assistente CAR 360:** A legislação exige preservação de cursos d'água. Identificamos sobreposição na sua área.")
            st.button("Mostrar no mapa")

# --- WIREFRAME 5 ---
elif menu == "Analista":
    st.header("🧑‍💻 Fila Inteligente")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔴 Alto risco", 182); c2.metric("🟡 Médio risco", 652); c3.metric("🟢 Baixo risco", 3542)
    st.write("---")
    st.subheader("Análise: CAR 345781")
    st.write("IA encontrou: ✔ Sobreposição, ✔ Divergência, ✔ APP incompatível")
    st.text_area("Parecer preliminar:", "A propriedade apresenta inconsistência na delimitação da APP.")
    col_a, col_b, col_c = st.columns(3)
    col_a.button("Aprovar"); col_b.button("Solicitar Correção"); col_c.button("Encaminhar")

# --- WIREFRAMES 6 e 7 ---
elif menu == "Gestor":
    st.header("🏛 Painel Nacional de Governança Territorial")
    st.map(pd.DataFrame(np.random.randn(20, 2)/50 + [-15, -50], columns=['lat', 'lon']))
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Cobertura CAR", "87%")
        st.bar_chart(pd.DataFrame({'Valores': [72, 18, 10]}, index=['Analisados', 'Pendentes', 'Em Validação']))
    with col2:
        st.subheader("Monitoramento Nacional")
        st.write("Prioridades: ✔ Municípios sem cadastro, ✔ Sobreposição elevada, ✔ APP crítica")
        st.success("Recomendação: Aumentar equipe de análise na região Norte.")

# --- WIREFRAME 8 ---
elif menu == "Arquitetura":
    st.header("Arquitetura CAR 360")
    st.code("BASES OFICIAIS: SICAR, SNIF, Consulta Pública, Gov.br, RER, SIGEF")
    st.markdown("### ↓")
    st.success("CAR 360 - Inteligência, Governança, Validação, Score, Monitoramento")
    st.markdown("### ↓")
    st.write("👨‍🌾 Produtor | 🧑‍💻 Analista | 🏛 Gestor")
