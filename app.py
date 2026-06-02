import streamlit as st

# ============ CONFIGURAÇÃO DA PÁGINA ============
st.set_page_config(
    page_title="Sports Prediction — 2026 World Cup",
    page_icon="assets/bola_previsao.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ LOGO NA SIDEBAR ============
st.logo(
    "assets/logo fundo preto.png",
    icon_image="assets/bola_previsao.png",
    size="large",
)

# ============ DEFINIÇÃO DAS PÁGINAS ============
datasets = st.Page("pages/Explorador_de_Dados.py", title="Dataset", icon="🗄️", default=True)
ao_vivo = st.Page("pages/Simulacao_Ao_Vivo.py", title="Live World Cup Simulation", icon="⚽")
explorador_forca = st.Page("pages/Explorador_de_Forca.py", title="2026 World Cup Simulation", icon="🏆")

# ============ NAVEGAÇÃO ============
pg = st.navigation(
    {
        "Sports Forecast": [datasets, explorador_forca, ao_vivo],
    }
)

# ============ EXECUTAR PÁGINA SELECIONADA ============
pg.run()
