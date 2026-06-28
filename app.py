import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from streamlit_folium import st_folium


st.set_page_config(
    page_title="CAR 360", 
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    /* Forçar fundo branco absoluto */
    .stApp { background-color: #ffffff !important; }
    
    /* Garantir que todos os textos sejam legíveis (Preto) */
    div, p, h1, h2, h3, label, span { color: #000000 !important; }
    </style>
""", unsafe_allow_html=True)
# --- 8. DADOS MOCK ---
def gerar_dados():
    np.random.seed(42)
    imoveis = []
    for i in range(50):
        score = np.random.randint(20, 100)
        imoveis.append({
            'ID': f'CAR-{1000+i}',
            'Produtor': f'Produtor {i}',
            'Area': np.random.randint(50, 5000),
            'Score': score,
            'Status': 'Regularizado' if score > 70 else ('Atenção' if score > 40 else 'Crítico'),
            'lat': -15.78 + np.random.uniform(-5, 5),
            'lon': -47.92 + np.random.uniform(-5, 5),
            'Sobreposicao': np.random.choice([True, False], p=[0.3, 0.7])
        })
    return pd.DataFrame(imoveis)

df = gerar_dados()

# --- 7. SCORE DE CONFIABILIDADE (Lógica) ---
def calcular_score(dados):
    score = 40  # Base
    if dados['sobreposicao']: score -= 30
    if dados['falta_rl']: score -= 20
    score += 20 # Localização validada
    return max(0, min(100, score))

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="CAR 360", layout="wide")
st.markdown("""<style>.stApp {background-color: #f8f9fa;}</style>""", unsafe_allow_html=True)

menu = st.sidebar.radio("Navegação", ["Início", "Produtor", "Analista", "Gestor"])

# --- 3. JORNADA DO PRODUTOR ---
if menu == "Produtor":
    st.title("👨‍🌾 Regularização Ambiental")
    step = st.radio("Etapa", ["Identificação", "Validação", "Finalização"], horizontal=True)
    
    if step == "Identificação":
        cpf = st.text_input("CPF do Proprietário")
        if st.button("Consultar Base"):
            st.success("Dados encontrados! Área: 150ha | Bioma: Cerrado")
    
    elif step == "Validação":
        score = 92
        st.metric("Score de Confiabilidade", f"{score}%")
        st.progress(score/100)
        st.warning("IA: Sobreposição detectada na área de Reserva Legal.")
        if st.button("💬 O que é APP?"):
            st.info("APP (Área de Preservação Permanente) é uma área protegida, coberta ou não por vegetação nativa, com a função ambiental de preservar os recursos hídricos.")

# --- 4. JORNADA DO ANALISTA ---
elif menu == "Analista":
    st.title("🧑‍💻 Fila Inteligente")
    col1, col2, col3 = st.columns(3)
    col1.metric("Pendentes", len(df[df['Status']=='Crítico']))
    
    # Mapa
    m = folium.Map(location=[-15.78, -47.92], zoom_start=4)
    for _, row in df.iterrows():
        folium.Marker([row['lat'], row['lon']], popup=row['ID']).add_to(m)
    st_folium(m, width=800, height=300)
    
    st.table(df.head(5))
    if st.button("Gerar Parecer com IA"):
        st.success("IA: Sugiro solicitar ajuste de georreferenciamento na área de sobreposição.")

# --- 5. JORNADA DO GESTOR ---
elif menu == "Gestor":
    st.title("🏛 Painel Nacional")
    col1, col2 = st.columns(2)
    fig = px.pie(df, names='Status', title="Distribuição Nacional de Regularidade")
    col1.plotly_chart(fig)
    col2.metric("Cobertura CAR", "83%")
    st.bar_chart(df.groupby('Status')['Area'].sum())

# --- 2. CONCEITO CENTRAL ---
else:
    st.title("CAR 360")
    st.subheader("Plataforma Nacional de Inteligência Territorial")
    st.write("---")
    st.write("O CAR360 simplifica a regularização através de automação e transparência.")
    
    with st.expander("Ver Arquitetura do Sistema"):
        st.markdown("""
        **Camadas:**
        1. **Bases Oficiais** (SICAR, SNIF)
        2. **Core CAR360** (IA, Validação, Score)
        3. **Interface** (Produtor, Analista, Gestor)
        """)
