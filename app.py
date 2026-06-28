
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CAR 360", page_icon="🌎", layout="wide")

st.markdown("""
<style>

/* ===========================
   FUNDO
=========================== */

.stApp{
    background:#F7F9FC;
}

/* ===========================
   SIDEBAR
=========================== */

section[data-testid="stSidebar"]{
    background:#0B2343;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* ===========================
   TITULOS
=========================== */

h1{
    color:#1351B4;
    font-weight:700;
}

h2{
    color:#1351B4;
}

h3{
    color:#1F2937;
}

p, label, div{
    color:#1F2937;
}

/* ===========================
   CONTAINER
=========================== */

.main .block-container{

    padding-top:2rem;
    padding-bottom:2rem;

    max-width:1400px;

}

/* ===========================
   BOTÕES
=========================== */

.stButton button{

    width:100%;
    background:#1351B4;
    color:white;
    border-radius:10px;
    border:none;
    padding:12px;

    font-weight:600;

}

.stButton button:hover{

    background:#2670E8;

}

/* ===========================
   INPUTS
=========================== */

input{

    background:white !important;
    color:black !important;

}

/* ===========================
   METRICS
=========================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:20px;

    box-shadow:0px 2px 8px rgba(0,0,0,.08);

    border-left:6px solid #1351B4;

}

/* ===========================
   EXPANDER
=========================== */

details{

    background:white;

    border-radius:10px;

    padding:10px;

    border:1px solid #E5E7EB;

}

/* ===========================
   ALERTAS
=========================== */

.stAlert{

    border-radius:10px;

}

/* ===========================
   DATAFRAME
=========================== */

[data-testid="stDataFrame"]{

    border-radius:12px;

    overflow:hidden;

}

/* ===========================
   CHAT
=========================== */

[data-testid="stChatMessage"]{

    background:white;

    border-radius:12px;

    padding:15px;

    border-left:5px solid #1351B4;

}

/* ===========================
   RADIO
=========================== */

.stRadio label{

    font-size:16px;

}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌎 CAR 360")
menu=st.sidebar.radio("Menu",["Início","Produtor","Analista","Gestor","Arquitetura"])

if menu=="Início":
    st.title("CAR 360 – Plataforma Inteligência Territorial")
    st.info("Protótipo para apresentação do Hackathon")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Cadastros","8,1 M","+2,4%")
    c2.metric("Municípios","5.570")
    c3.metric("Análises IA","3,2 M","+12%")
    c4.metric("Cobertura","87%")
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
elif menu=="Gestor":
    st.header("🏛 Painel Executivo")
    m1,m2,m3,m4=st.columns(4)
    m1.metric("Cobertura","87%")
    m2.metric("Pendências","842 mil")
    m3.metric("Municípios críticos","314")
    m4.metric("Alertas IA","18.245")
    df=pd.DataFrame(np.random.randn(100,2)/30+[-15,-50],columns=["lat","lon"])
    st.map(df)
    st.bar_chart(pd.DataFrame({"Cadastros":[72,18,10]},index=["Analisados","Pendentes","Validação"]))
    st.success("Recomendação da IA: priorizar reforço operacional na Região Norte.")
else:
    st.header("Arquitetura CAR 360")
    st.code("""BASES OFICIAIS
SICAR
Gov.br
SNCR
SIGEF
MapBiomas
INPE

        ↓

Motor de IA Generativa
Validação
Score
Monitoramento
Recomendações

        ↓

Produtor | Analista | Gestor
""")
