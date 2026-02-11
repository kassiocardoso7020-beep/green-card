import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO GREEN CARD SOVEREIGN (VERDE ESMERALDA & OURO) ---
st.set_page_config(page_title="Green Card Sovereign", page_icon="🌳", layout="wide")

st.markdown("""
    <style>
    /* Fundo Verde Floresta Profundo */
    .main { background-color: #001a0a; color: #2ecc71; } 
    
    /* Botões em Verde Esmeralda com texto preto para contraste */
    .stButton>button { 
        background-color: #2ecc71; 
        color: #000000; 
        border: 2px solid #D4AF37; 
        border-radius: 10px; 
        width: 100%;
        font-weight: bold;
    }
    
    /* Sidebar Verde Escuro com borda Dourada */
    .stSidebar { background-color: #000d05; border-right: 2px solid #D4AF37; }
    
    /* Títulos em Dourado (Luxo Dubai) */
    h1, h2, h3 { color: #D4AF37 !important; text-shadow: 1px 1px 2px #000; }
    
    /* Barra de progresso Verde Esmeralda */
    .stProgress > div > div > div > div { background-color: #2ecc71; }
    
    /* Métricas em Ouro */
    [data-testid="stMetricValue"] { color: #D4AF37 !important; }
    
    /* Abas customizadas */
    .stTabs [data-baseweb="tab"] { color: #2ecc71; }
    .stTabs [aria-selected="true"] { color: #D4AF37; border-bottom-color: #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DO SISTEMA (SIMULANDO BANCO DE DADOS) ---
if 'total_trees' not in st.session_state:
    st.session_state.total_trees = 1 
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 99.9 

# --- SIDEBAR: IDENTIDADE E COMPLIANCE ---
st.sidebar.image("https://img.icons8.com/ios-filled/100/D4AF37/tree-planting.png")
st.sidebar.title("Green Card")
st.sidebar.markdown("---")
st.sidebar.info("🔱 **Kassio - FOUNDER ELITE**")
st.sidebar.write("📍 Localização: Solo Validado")
st.sidebar.write("⚖️ Status: Global Compliance OK")

# --- NOVO: SISTEMA DE COMPARTILHAMENTO ---
st.sidebar.markdown("---")
st.sidebar.subheader("📢 Expandir a Rede")
link_convite = "https://green-card.streamlit.app" 
mensagem_zap = f"Venha minerar ativos no solo com a Green Card! Acesse: {link_convite}"

if st.sidebar.button("Compartilhar via WhatsApp"):
    # Gera o link que abre o WhatsApp com a mensagem pronta
    link_final = f"https://wa.me/?text={mensagem_zap.replace(' ', '%20')}"
    st.sidebar.markdown(f"[Clica aqui para enviar]({link_final})")


# --- DASHBOARD PRINCIPAL (CONTADOR MAINNET) ---
st.title("🏛️ Green Card Sovereign")
col_count, col_status = st.columns([2, 1])

with col_count:
    progress = st.session_state.total_trees / 1000000
    st.write(f"### {st.session_state.total_trees} / 1.000.000 árvores para a abertura da Mainnet")
    st.progress(progress)

with col_status:
    if st.session_state.total_trees < 1000000:
        st.warning("⚠️ Mainnet: LOCKED")
    else:
        st.success("✅ Mainnet: UNLOCKED")

# --- NAVEGAÇÃO ---
tab1, tab2, tab3, tab4 = st.tabs(["[Plantio]", "[Evolução]", "[Wallet]", "[Área do Fundador]"])

# --- TAB 1: SCANNER IA (RIGOR DE SOLO) ---
with tab1:
    st.header("📸 Planting Scanner - IA Gemini 1.5 Flash")
    
    modo = st.radio("Modo de Validação:", ["Individual", "Larga Escala (3x3m)"])
    foto = st.camera_input("Capturar Plantio Direto no Solo")

    if foto:
        with st.spinner("Auditando Rigor de Solo e Espécie..."):
            time.sleep(2) 
            
            st.success("✅ Solo Natural Detectado. Proibição de Vasos: OK.")
            st.write("**Relatório Gemini:**")
            st.write("- Ambiente: Campo Aberto / Solo Direto")
            st.write("- Espécie: Mogno Africano (Extinção Crítica)")
            st.write("- Espaçamento (Modo Larga Escala): 3x3m Confirmado")
            
            st.metric(label="Recompensa Estimada", value="300 $GCARD", delta="Liberado: 99.9 $GCARD (33.3%)")
            
            if st.button("Confirmar Validação e Gerar NFT"):
                st.session_state.total_trees += 1
                st.session_state.wallet_balance += 99.9
                st.balloons()
                st.write("🎫 **Certificado Sovereign Gerado:** `#GC-" + str(st.session_state.total_trees).zfill(6) + "`")

# --- TAB 3: WALLET E ECONOMIA ---
with tab3:
    st.header("💰 Sovereign Wallet")
    c1, c2, c3 = st.columns(3)
    c1.metric("Saldo Total", f"{st.session_state.wallet_balance:.2f} $GCARD")
    c2.metric("Status do Cartão", "Bloqueado (Até 1M)")
    c3.metric("Taxa de Saque", "2% (Fundo Estabilidade)")

    st.write("---")
    st.subheader("🛡️ Regras de Liquidez")
    st.write("- **Trava de Baleias:** Ativa para saldos > 5.000 $GCARD.")
    st.write("- **Fundo de Estabilidade:** 1% de cada taxa reservado para garantir preço de R$ 1,00.")
    
    with st.expander("👤 Painel de Herança"):
        st.text_input("Endereço da Carteira do Sucessor")
        st.button("Cadastrar Herdeiro")

# --- TAB 4: ÁREA DO FUNDADOR (PROTEGIDA) ---
with tab4:
    senha = st.text_input("Insira a senha de acesso Dubai:", type="password")
    if senha == "DUBAI2026":
        st.header("👑 Painel de Controle - Kassio")
        st.write("### Métricas Internas da Holding")
        st.write(f"- Árvores Ativas: {st.session_state.total_trees}")
        st.write(f"- Tokens Queimados por Abandono: 0 $GCARD")
        st.write(f"- Fundo de Estabilidade Acumulado: {st.session_state.wallet_balance * 0.01:.2f} $GCARD")
    elif senha != "":
        st.error("❌ Acesso Negado. Sanções de Segurança Ativadas.")

# --- FOOTER ---
st.markdown("---")
st.caption("Green Card Sovereign © 2026 - Operação Dubai Compliance.")
