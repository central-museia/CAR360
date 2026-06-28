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
    st.subheader("Regularização Ambiental em 3 Passos")
    
    # Passo 1: Identificação
    cpf = st.text_input("1. Informe o CPF do Titular")
    
    if cpf:
        # Simulação de Login e Consulta
        st.write("🔄 *Consultando base Gov.br e SICAR...*")
        
        # Passo 2: Validação Automática
        st.markdown("### Dados Identificados")
        col_c, col_d = st.columns(2)
        col_c.write("**Proprietário:** João Silva")
        col_d.write("**Área do Imóvel:** 120,5 ha")
        
        st.markdown("---")
        
        # Onde a IA atua (Explicação simples)
        st.write("🔍 **IA CAR 360:** Analisando georreferenciamento...")
        st.progress(75) # Barra de progresso visual
        
        # Cards de IA (Explicabilidade)
        with st.expander("✅ Por que o score é 85?"):
            st.write("A IA validou sua **Área de Preservação Permanente (APP)** com base em imagens do MapBiomas. Não foram encontradas sobreposições recentes.")
        
        with st.expander("⚠️ O que é a Reserva Legal?"):
            st.write("A Reserva Legal é uma área do seu imóvel que garante o uso sustentável dos recursos naturais. O sistema identificou que a sua área está 100% preservada.")
            
        st.metric("Score de Confiabilidade", "85/100")
        
        # Passo 3: Finalização
        st.info("O sistema detectou que seu CAR está apto para validação automática.")
        if st.button("Finalizar e Enviar para Análise", key="final_prod"):
            st.success("Enviado! Sua regularização está em análise prioritária pelo analista.")

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
