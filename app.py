import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CAR 360", layout="wide")

# CSS para o padrão governamental
st.markdown("""
    <style>
    .stButton>button {background-color: #003399; color: white; width: 100%;}
    </style>
""", unsafe_allow_html=True)

# Sidebar de Navegação
st.sidebar.image("logo.png", width=150)
st.sidebar.title("CAR 360")
menu = st.sidebar.radio("Escolha o seu perfil:", ["Início", "Produtor", "Analista", "Gestor"])

# --- WIREFRAME 1: Tela Inicial ---
if menu == "Início":
    st.title("Plataforma Nacional de Inteligência Territorial")
    st.subheader("🌎 Um único ambiente para todo o ecossistema CAR")
    if st.button("Entrar com Gov.br"):
        st.info("Autenticação realizada com sucesso!")
    
    st.markdown("---")
    st.write("### Bases Integradas")
    bases = ["SICAR", "Consulta Pública", "SNIF", "RER", "Gov.br", "Painéis CAR", "Bases Geoespaciais"]
    for b in bases: st.write(f"✓ {b}")

# --- WIREFRAME 2, 3 e 4: Jornada do Produtor ---
elif menu == "Produtor":
    st.header("👨‍🌾 Regularização Ambiental")
    tab1, tab2 = st.tabs(["Identificação", "Validação Inteligente"])
    
    with tab1:
        st.write("### Dados do Proprietário")
        st.text_input("CPF")
        if st.button("Confirmar Dados"):
            st.success("Proprietário, Área e Reserva Legal identificados.")
            
    with tab2:
        st.metric("Score de Confiabilidade", "92%")
        st.progress(92)
        st.warning("⚠ Existe uma pequena sobreposição. Clique no chat ao lado.")
        if st.button("💬 Assistente CAR 360"):
            st.write("**IA:** A legislação determina que áreas de APP devem ser preservadas. Encontramos uma divergência na sua delimitação.")

# --- WIREFRAME 5: Analista ---
elif menu == "Analista":
    st.header("🧑‍💻 Fila Inteligente")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔴 Alto risco", 182)
    c2.metric("🟡 Médio risco", 652)
    c3.metric("🟢 Baixo risco", 3.542)
    
    st.write("### CAR 345781 - Selecionado")
    st.error("IA detectou: Sobreposição, Divergência documental, APP incompatível")
    st.info("Parecer: A propriedade apresenta inconsistência na delimitação da APP.")
    col_a, col_b, col_c = st.columns(3)
    col_a.button("Aprovar"); col_b.button("Solicitar Correção"); col_c.button("Encaminhar")

# --- WIREFRAME 6 e 7: Gestor ---
elif menu == "Gestor":
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
