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
                    st.error("⚠️ Identificamos uma área que precisa de correção")
                    st.write("🔍 **O que acontece:**")
                    st.write("Uma parte do seu terreno que está sendo usada para plantio ou construção não pode ser usada, porque fica muito perto do rio. A lei protege essa área perto da água.")
                    st.info("💡 **Como resolver:**")
                    st.write("O sistema pode corrigir o desenho para você agora mesmo. Assim, seu cadastro fica dentro da regra e você não precisa se preocupar.")
                    if st.button("Corrigir o desenho do terreno"):
                        st.success("Pronto! O desenho foi corrigido. Seu cadastro já está em conformidade.")
                        
                elif exemplo == "003 - Déficit de Reserva Legal":
                    st.warning("⚠️ Identificamos que falta um pouco de mata preservada")
                    st.write("🔍 **O que acontece:**")
                    st.write("Pelo tamanho da sua terra aqui no Cerrado, a lei pede que uma parte maior do terreno fique com mata preservada (a reserva).")
                    st.info("💡 **Como resolver:**")
                    st.write("Nós te ajudamos a resolver isso de um jeito simples. Você pode fazer um plano de plantio ou compensar essa área depois. Quer que a gente organize isso para você?")
                    if st.button("Quero organizar a área de mata"):
                        st.success("Tudo certo! Enviamos um guia passo a passo para o seu celular. É simples e nós vamos te acompanhar.")

    # JORNADA ANALISTA
    # --- JORNADA DO ANALISTA ---
    # --- JORNADA DO ANALISTA ---
    if st.session_state.persona == "Analista":
        st.title("🧑‍💻 Fila de Análise Inteligente")
    
        # 1. Filtro por Estado
        estado = st.selectbox("Selecione o Estado para iniciar a análise:", 
                          ["Selecione...", "MT - Mato Grosso", "PA - Pará", "BA - Bahia"])
    
        if estado != "Selecione...":
            st.write(f"### Processos em: {estado}")
        
            # 2. Tabela de Prioridades (Fila Automática)
            # Em um sistema real, aqui entraria a integração com o banco de dados
            df_fila = pd.DataFrame({
                'Processo': ['CAR-8823', 'CAR-9912', 'CAR-1022'],
                'Risco': ['Alto', 'Médio', 'Baixo'],
                'Solicitante': ['João da Silva', 'Maria Souza', 'Fazenda Rio Verde']
            })
            st.dataframe(df_fila, use_container_width=True)
        
            processo_sel = st.selectbox("Selecione o processo para analisar:", df_fila['Processo'])
        
            if st.button("Abrir Processo Completo"):
            st.divider()
            st.subheader(f"Análise Detalhada: {processo_sel}")
            
            # --- LÓGICA DE DADOS POR PROCESSO ---
            # Aqui simulamos a carga automática de dados de diferentes sistemas
            if processo_sel == "CAR-8823": # EXEMPLO: TUDO OK
                status = "Conforme"
                msg_ia = "✅ Todos os cruzamentos (SICAR, SIGEF, INCRA) validaram o imóvel."
            elif processo_sel == "CAR-9912": # EXEMPLO: DIVERGÊNCIA SIGEF
                status = "Inconsistente"
                msg_ia = "⚠️ Divergência detectada com o sistema SIGEF: O perímetro do imóvel não coincide com a base fundiária."
            else: # EXEMPLO: DIVERGÊNCIA MAPBIOMAS
                status = "Problema"
                msg_ia = "❌ Alerta: Imagem de satélite mostra supressão de vegetação nativa pós-2008 (Base: MapBiomas)."

            # --- PAINEL DE DADOS ---
            col1, col2 = st.columns(2)
            with col1:
                st.write("📊 **Integração de Sistemas:**")
                st.write(f"- Status: **{status}**")
                st.write(msg_ia)
            
            with col2:
                st.write("💡 **Orientação da IA para o Analista:**")
                if status == "Conforme":
                    st.success("O processo está pronto para validação final.")
                elif status == "Inconsistente":
                    st.warning("Verificar documento de propriedade no SIGEF. Solicitar retificação se necessário.")
                else:
                    st.error("Protocolar auto de infração ou solicitar embargos. Evidência mapeada anexada abaixo.")

            # --- EVIDÊNCIAS ---
            st.write("📷 **Evidências Automatizadas:**")
            st.image("https://via.placeholder.com/600x200?text=Evidencias+Tecnicas+do+Processo", caption="Documentos e Imagens Consolidados")
    # JORNADA GESTOR
    elif st.session_state.persona == "Gestor":
        st.title("🏛 Painel Executivo Nacional")
        col1, col2, col3 = st.columns(3)
        col1.metric("Cobertura BR", "83%")
        col2.metric("Pendentes", "12.400")
        col3.metric("Estados", "22")
        st.map(pd.DataFrame({'lat': [-15.78], 'lon': [-47.92]}))
