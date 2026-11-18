from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Painel de Indicadores - PA ANA", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>header,footer,#MainMenu{visibility:hidden}.block-container{padding:0.5rem 0.5rem 0}</style>", unsafe_allow_html=True)
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=2200, scrolling=True)
