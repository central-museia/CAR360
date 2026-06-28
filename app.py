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
# --- JORNADA DO PRODUTOR (INTERATIVA) ---
# --- JORNADA DO PRODUTOR (COMPLETA E TESTÁVEL) ---
with tab1:
    st.subheader("👨‍🌾 Regularização em tempo real")
    
    # Variável de controle para testar:
    # Mude para True para ver o erro, False para ver o sucesso
    simular_erro = st.toggle("Simular Cadastro com Inconsistência", value=False)
    
    if 'step' not in st.session_state: st.session_state.step = 1

    # PASSO 1: Identificação
    if st.session_state.step == 1:
        st.write("### Identificação")
        cpf = st.text_input("CPF do Proprietário:")
        if st.button("Consultar Gov.br"):
            st.session_state.step = 2
            st.rerun()

    # PASSO 2: Diagnóstico IA
    elif st.session_state.step == 2:
        st.write("### Diagnóstico IA")
        with st.spinner('Analisando bases oficiais...'):
            import time; time.sleep(1.5)
        
        if simular_erro:
            st.error("⚠️ Identificamos uma pendência na sua Reserva Legal.")
            st.write("🔍 **IA CAR 360:** A área de Reserva Legal está abaixo do limite legal para este bioma.")
            st.info("💡 **O que fazer:** Clique abaixo para ajustar o polígono automaticamente.")
            if st.button("Corrigir Polígono"):
                st.success("Polígono ajustado conforme legislação vigente!")
        else:
            st.success("✅ Cadastro validado! Nenhuma inconsistência encontrada.")
            st.metric("Score de Confiabilidade", "95/100")
        
        col_voltar, col_prox = st.columns([1, 4])
        if col_voltar.button("Voltar"): st.session_state.step = 1; st.rerun()
        if not simular_erro and col_prox.button("Prosseguir"): st.session_state.step = 3; st.rerun()

    # PASSO 3: Confirmação
    elif st.session_state.step == 3:
        st.write("### Finalização")
        st.balloons()
        st.success("Cadastro enviado com sucesso!")
        if st.button("Novo Consulta"): st.session_state.step = 1; st.rerun()
# --- JORNADA DO ANALISTA ---
# --- JORNADA DO ANALISTA ---
with tab2:
    st.subheader("Fila de Análise Inteligente")
    st.write("A IA prioriza casos com maior risco ambiental para otimizar sua decisão.")
    
    # 1. Fila de Priorização (Simulação de dados)
    df_analista = pd.DataFrame({
        'Processo': ['CAR-101', 'CAR-102', 'CAR-103'],
        'Risco': ['Alto', 'Médio', 'Baixo'],
        'Score': [35, 65, 88]
    })
    
    # Exibe tabela com destaque de cor nas linhas
    st.dataframe(df_analista, use_container_width=True)
    
    # 2. Abrir processo selecionado
    processo = st.selectbox("Selecione o processo para análise detalhada:", df_analista['Processo'])
    
    if st.button("Carregar Evidências e Mapa"):
        st.markdown("---")
        col_e1, col_e2 = st.columns([1, 1])
        
        with col_e1:
            st.write("📍 **Localização e Geometria:**")
            # Simulando o mapa com pontos
            st.map(pd.DataFrame({'lat': [-15.78], 'lon': [-47.92]}))
            
        with col_e2:
            st.write("🔍 **Pendências Identificadas pela IA:**")
            st.error("Sobreposição em APP detectada via satélite.")
            st.warning("Falta de comprovação de Reserva Legal no SIGEF.")
            
        # 3. Parecer Preliminar da IA
        st.markdown("### 🤖 Sugestão do Assistente CAR 360")
        st.info("O sistema sugere: **Solicitar ajuste de limites e anexar nova RL.**")
        
        # 4. Decisão Humana
        st.markdown("### Decisão Final")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        col_btn1.button("✅ Aprovar", type="primary")
        col_btn2.button("📝 Solicitar Ajuste")
        col_btn3.button("❌ Rejeitar")

# --- JORNADA DO GESTOR ---
with tab3:
    st.subheader("Painel Estratégico de Governança")
    
    # KPIs Executivos
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Cobertura CAR", "83%", "+2.5%")
    kpi2.metric("Backlog", "12.400", "-15%")
    kpi3.metric("Tempo Médio", "45 dias", "-10 dias")
    kpi4.metric("Estados Ativos", "22/27")
    
    st.markdown("---")
    
    # Mapa e Insights
    col_mapa, col_insights = st.columns([2, 1])
    
    with col_mapa:
        st.write("### Mapa Nacional de Atuação")
        # Simulação de mapa de calor de atuação
        mapa_data = pd.DataFrame(np.random.randn(20, 2)/5 + [-15.78, -47.92], columns=['lat', 'lon'])
        st.map(mapa_data)
        
    with col_insights:
        st.write("### Insights do Gestor")
        st.warning("⚠️ **Atenção:** Mato Grosso apresenta maior tempo médio de processamento.")
        st.success("✅ **Sucesso:** Região Sul atingiu 95% de regularização.")
        
        st.write("---")
        st.write("### Eficiência Operacional")
        # Gráfico simples de evolução mensal
        st.line_chart(pd.DataFrame([10, 25, 45, 60, 83], columns=["% de Regularização"]))

    if st.button("Exportar Relatório Executivo"):
        st.toast("Relatório gerado com sucesso!")

# Footer fixo com o conceito central
st.markdown("---")
st.caption("CAR 360 | Dados conectados, decisões inteligentes.")
