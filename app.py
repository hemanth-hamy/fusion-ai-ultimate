import streamlit as st
from utils.core import render_tab

st.set_page_config(page_title="Fusion AI Ultimate", layout="wide")

TABS = ["Overview", "Diagnose", "Analytics", "Security", "Optimize", "Integrations", "Voice Mode", "YouTube AI"]
st.sidebar.title("🔭 Fusion AI Navigation")
selection = st.sidebar.radio("Go to", TABS)

st.title("🚀 Fusion AI Ultimate")
st.markdown(f"## {selection}")
render_tab(selection)