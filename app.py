import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="CAR 360", layout="wide")

# Inicializa o estado da página
if 'persona' not in st.session_state:
    st.session_state.persona = None

# --- TELA DE SELEÇÃO (CARDS) ---
if st.session_state.persona is None:
    st.title("CAR 360 - Selecione seu Perfil")
    st.write("Escolha sua jornada para iniciar a operação:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👨‍🌾 PRODUTOR", use_container_width=True, type="primary"):
            st.session_state.persona = "Produtor"
            st.rerun()
    with col2:
        if st.button("🧑‍💻 ANALISTA", use_container_width=True, type="primary"):
            st.session_state.persona = "Analista"
            st.rerun()
    with col3:
        if st.button("🏛 GESTOR", use_container_width=True, type="primary"):
            st.session_state.persona = "Gestor"
            st.rerun()

# --- JORNADAS (APÓS SELEÇÃO) ---
else:
    # Botão de voltar global
    if st.button("⬅ Voltar ao Início"):
        st.session_state.persona = None
        st.rerun()
        
    st.divider()

    # JORNADA PRODUTOR
    if st.session_state.persona == "Produtor":
        st.title("👨‍🌾 Jornada do Produtor")
        simular_erro = st.toggle("Simular Cadastro com Inconsistência")
        
        # Fluxo simplificado para demonstração
        cpf = st.text_input("CPF do Proprietário:")
        if st.button("Consultar Gov.br"):
            with st.spinner('Validando com bases oficiais...'):
                time.sleep(1.5)
            if simular_erro:
                st.error("⚠️ Pendência: Reserva Legal abaixo do limite.")
                st.button("Corrigir Automaticamente")
            else:
                st.success("✅ Cadastro validado! Score: 95/100")

    # JORNADA ANALISTA
    elif st.session_state.persona == "Analista":
        st.title("🧑‍💻 Fila de Análise Inteligente")
        df = pd.DataFrame({'Processo': ['CAR-101', 'CAR-102'], 'Risco': ['Alto', 'Médio']})
        st.dataframe(df, use_container_width=True)
        if st.button("Gerar Parecer IA"):
            st.info("IA: Sugiro aprovação condicionada.")

    # JORNADA GESTOR
    elif st.session_state.persona == "Gestor":
        st.title("🏛 Painel Executivo Nacional")
        col1, col2, col3 = st.columns(3)
        col1.metric("Cobertura BR", "83%")
        col2.metric("Pendentes", "12.400")
        col3.metric("Estados", "22")
        st.map(pd.DataFrame({'lat': [-15.78], 'lon': [-47.92]}))
