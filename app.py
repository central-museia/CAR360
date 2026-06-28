import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="CAR 360", layout="wide")

# Estilização CSS para o padrão Governo Moderno
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #003399;}
    .stButton>button {background-color: #003399; color: white;}
    </style>
""", unsafe_allow_html=True)

# Logo e Sidebar
st.sidebar.image("ChatGPT Image 28 de jun. de 2026, 11_44_52.png", width=200)
menu = st.sidebar.radio("Navegação", ["Início", "Portal do Produtor", "Painel do Analista", "Gestão Nacional", "Mapa de Risco"])

# Lógica das Abas
if menu == "Início":
    st.title("CAR 360 - Plataforma de Inteligência Territorial")
    st.image("ChatGPT Image 28 de jun. de 2026, 11_44_52.png", width=300)
    st.write("Dados conectados, decisões inteligentes.")

elif menu == "Portal do Produtor":
    st.header("👨‍🌾 Regularização Ambiental")
    cpf = st.text_input("Insira seu CPF")
    if st.button("Confirmar"):
        st.success("Dados validados!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score de Confiabilidade", "92%")
        with col2:
            st.write("⚠ Sobreposição detectada na área de Reserva Legal.")

elif menu == "Painel do Analista":
    st.header("🧑‍💻 Fila Inteligente")
    col1, col2, col3 = st.columns(3)
    col1.metric("Alto Risco", 182)
    col2.metric("Médio Risco", 652)
    col3.metric("Baixo Risco", 3542)
    st.table(pd.DataFrame({'ID': [345781], 'Status': ['Sobreposição'], 'Prioridade': ['Alta']}))

elif menu == "Gestão Nacional":
    st.header("🏛 Painel do Gestor")
    col1, col2 = st.columns(2)
    col1.metric("Cobertura CAR", "87%")
    col2.metric("Pendentes", "18%")
    st.bar_chart(pd.DataFrame({'Pendências': [18, 10, 72]}, index=['Pendentes', 'Em Validação', 'Analisados']))

elif menu == "Mapa de Risco":
    st.header("🌍 Mapa de Inteligência Territorial")
    # Gerando dados fictícios para o mapa
    map_data = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [-15.78, -47.92], columns=['lat', 'lon'])
    st.map(map_data)
