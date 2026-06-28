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
menu = st.sidebar.radio("Navegação", ["Início", "Portal do Produtor", "Painel do Analista", "Gestão Nacional", "Mapa de Risco"])

# Lógica das Abas
# Dados simulados de pontos de risco ou car para o mapa
def get_map_data(level):
    # Cria pontos aleatórios para simular a distribuição no mapa
    return pd.DataFrame(
        np.random.randn(100, 2) / ([20, 20] if level == "Brasil" else [2, 2]) + [-15.78, -47.92],
        columns=['lat', 'lon']
    )

st.title("CAR 360 – Inteligência Territorial")

# Navegação de Níveis
nivel = st.radio("Selecione a camada de visão:", ["Brasil", "Estado", "Município"], horizontal=True)

# Indicadores que mudam conforme o nível
c1, c2, c3 = st.columns(3)
if nivel == "Brasil":
    c1.metric("Estados Ativos", "22/27")
    c2.metric("Cobertura", "87%")
    c3.metric("Potencial", "1,4M")
elif nivel == "Estado":
    c1.metric("Municípios Ativos", "45/144")
    c2.metric("Cobertura", "62%")
    c3.metric("Risco Médio", "45k")
else:
    c1.metric("Imóveis Sem CAR", "1.200")
    c2.metric("Área Degradada", "300ha")
    c3.metric("Prioridade", "Alta")

# Exibição do Mapa Interativo
st.subheader(f"Visualização: {nivel}")
st.map(get_map_data(nivel))

# IA Contextual abaixo do mapa
if nivel == "Brasil":
    st.info("💡 A IA recomenda priorizar expansão nos estados da região Norte.")
elif nivel == "Estado":
    st.warning("⚠️ Atenção: Concentração de pendências detectada no quadrante sul do estado.")
    
    st.markdown("### Acesso")
    a,b,c=st.columns(3)
    a.button("👨‍🌾 Produtor")
    b.button("🧑‍💻 Analista")
    c.button("🏛 Gestor")
    st.markdown("### Bases Integradas")
    st.success("SICAR • Gov.br • SNCR • RER • SIGEF • MapBiomas • INPE • Bases Estaduais")
elif menu=="Produtor":
    st.header("👨‍🌾 Jornada do Produtor")
    with st.expander("Dados encontrados",True):
        st.write("✔ CPF validado")
        st.write("✔ Imóvel Rural")
        st.write("✔ APP")
        st.write("✔ Reserva Legal")
    if st.button("Executar Validação Inteligente"):
        st.progress(92)
        st.metric("Score","92%")
        st.warning("Pequena sobreposição detectada.")
        with st.chat_message("assistant"):
            st.write("A IA identificou divergência de 0,8 ha em APP. Recomenda-se ajustar o polígono antes do envio.")
elif menu=="Analista":
    st.header("🧑‍💻 Central do Analista")
    x,y,z=st.columns(3)
    x.metric("🔴 Alto risco","182","-15")
    y.metric("🟡 Médio","652","+21")
    z.metric("🟢 Baixo","3542","+108")
    st.text_area("Parecer IA","A propriedade apresenta divergência em APP e possível sobreposição com imóvel vizinho.",height=140)
    a,b,c=st.columns(3)
    a.button("Aprovar")
    b.button("Solicitar Correção")
    c.button("Encaminhar")
st.title("🏛 Painel Executivo de Governança Territorial")

# Simulação de dados em níveis
data = {
    'Brasil': {'Imoveis': 12000000, 'CAR': 8000000, 'Analisados': 3000000, 'Pendentes': 5000000, 'Risco_Alta': 182000},
    'Estado': {'Imoveis': 2000000, 'CAR': 1500000, 'Analisados': 600000, 'Pendentes': 900000, 'Risco_Alta': 45000},
    'Municipio': {'Imoveis': 5000, 'CAR': 4200, 'Analisados': 1200, 'Pendentes': 3000, 'Risco_Alta': 120}
}

# Navegação em Níveis
nivel = st.radio("Nível de Governança", ["Brasil", "Estado", "Municipio"], horizontal=True)
d = data[nivel]

# Indicadores Estratégicos
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Imóveis", f"{d['Imoveis']:,}")
col2.metric("Com CAR", f"{d['CAR']:,}")
col3.metric("Analisados", f"{d['Analisados']:,}")
col4.metric("Pendentes", f"{d['Pendentes']:,}")

st.write("---")

# Mapa de Risco e Fila Inteligente
c1, c2 = st.columns([2, 1])
with c1:
    st.subheader(f"Mapa de Risco - {nivel}")
    map_data = pd.DataFrame(np.random.randn(50, 2)/50 + [-15.78, -47.92], columns=['lat', 'lon'])
    st.map(map_data)

with c2:
    st.subheader("Fila por Prioridade")
    st.error(f"🔴 Alta Prioridade: {d['Risco_Alta']:,}")
    st.warning("🟡 Média Prioridade: 250.000")
    st.success("🟢 Baixa Prioridade: 400.000")
    st.write("---")
    st.info("**IA Generativa:** Aumentar equipe de análise na região Norte devido ao desmatamento recente.")

# Arquitetura do Motor de Governança
with st.expander("⚙️ Ver Arquitetura do Motor de Governança"):
    st.markdown("""
    **Fluxo de Inteligência:**
    1. **Bases Públicas** (SICAR, SNIF, SIGEF) 
    2. ➔ **Integração e Padronização** 3. ➔ **Motor Analítico (IA)** 4. ➔ **Governança Territorial** 5. ➔ **Tomada de Decisão**
    """)

# Footer informativo
st.write("---")
st.caption("CAR 360 - Dados conectados, decisões inteligentes. | Versão 2026")
