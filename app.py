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
        
        # Simulador de Banco de Dados CAR
        exemplo = st.selectbox("Selecione um CPF/Imóvel para teste:", 
                               ["Selecione...", "001 - Regular", "002 - Sobreposição APP", "003 - Déficit de Reserva Legal"])
        
        if exemplo != "Selecione...":
            if st.button("Consultar Bases Oficiais (SICAR/SNIF)"):
                with st.spinner('Cruzando dados geoespaciais...'):
                    time.sleep(1.5)
                
                # LÓGICA DE DADOS FICTÍCIOS
                if exemplo == "001 - Regular":
                    st.success("✅ Cadastro Validado - 100% Conforme")
                    st.metric("Score de Confiabilidade", "98/100")
                    st.write("IA: Nenhuma inconsistência detectada em relação ao Código Florestal.")
                    
                elif exemplo == "002 - Sobreposição APP":
                    st.error("⚠️ Inconsistência Detectada: Sobreposição em APP")
                    st.write("🔍 **IA CAR 360:** Identificamos que a área de produção agrícola intercepta Área de Preservação Permanente (Lei 12.651/12, Art. 4º).")
                    st.info("💡 **Ação Sugerida:** Ajustar polígono de cultivo para respeitar a faixa marginal do curso d'água.")
                    if st.button("Aplicar Ajuste Automático"):
                        st.success("Polígono reajustado. Novo score: 92/100.")
                        
                elif exemplo == "003 - Déficit de Reserva Legal":
                    st.warning("⚠️ Inconsistência Detectada: Déficit de Reserva Legal")
                    st.write("🔍 **IA CAR 360:** O imóvel apresenta 15% de Reserva Legal, mas o Bioma Cerrado exige 20% (Decreto 7.830/2012).")
                    st.info("💡 **Ação Sugerida:** Iniciar adesão ao PRA (Programa de Regularização Ambiental) ou compensação via Cota de Reserva Ambiental.")
                    if st.button("Simular Adesão ao PRA"):
                        st.success("Termo de compromisso gerado para assinatura.")

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
