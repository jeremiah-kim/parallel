import streamlit as st
import altair as alt
st.set_page_config(
    page_title="Parallel Dashboard",
    page_icon="👋",
    layout="wide"
)

with open('pages/style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

st.markdown('<p class="dashboard_title">Welcome to our directory!</p>', unsafe_allow_html=True)

st.sidebar.success("Select a research project above.")

st.markdown(
    """
    This will have more stuff soon.
    """
)

alt.themes.enable("dark")