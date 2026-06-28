import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from streamlit_folium import st_folium

import streamlit as st
import pandas as pd
import numpy as np

# Configuração simples e robusta
st.set_page_config(page_title="CAR 360", layout="wide")

# Título da Plataforma
st.title("CAR 360 – Inteligência Territorial")
st.markdown("---")

# Abas para as jornadas
tab1, tab2, tab3 = st.tabs(["👨‍🌾 JORNADA DO PRODUTOR", "🧑‍💻 JORNADA DO ANALISTA", "🏛 JORNADA DO GESTOR"])

# --- JORNADA DO PRODUTOR ---
with tab1:
    st.subheader("Regularização Ambiental Simplificada")
    cpf = st.text_input("CPF do Produtor", key="cpf")
    if st.button("Consultar Imóvel", key="btn_produtor"):
        st.success("Dados carregados com sucesso.")
        col_a, col_b = st.columns(2)
        col_a.metric("Área do Imóvel", "120 ha")
        col_b.metric("Score Ambiental", "85/100")
        st.info("IA: O cadastro está apto para validação automática.")

# --- JORNADA DO ANALISTA ---
with tab2:
    st.subheader("Fila de Prioridades e Risco")
    st.write("Análise orientada por IA para maior eficiência.")
    df = pd.DataFrame({'Processo': ['CAR-101', 'CAR-102'], 'Risco': ['Alto', 'Médio']})
    st.table(df)
    if st.button("Gerar Parecer Automático", key="btn_analista"):
        st.warning("IA: Parecer preliminar gerado: Aprovação condicionada.")

# --- JORNADA DO GESTOR ---
with tab3:
    st.subheader("Dashboard Executivo Nacional")
    col1, col2, col3 = st.columns(3)
    col1.metric("Cobertura BR", "83%")
    col2.metric("Processos/mês", "45 mil")
    col3.metric("Estados Ativos", "22")
    
    st.write("### Onde estamos atuando:")
    st.bar_chart({'Estados': [80, 95, 60, 40], 'Cobertura': [10, 20, 30, 40]})

# Footer fixo com o conceito central
st.markdown("---")
st.caption("CAR 360 | Dados conectados, decisões inteligentes.")
