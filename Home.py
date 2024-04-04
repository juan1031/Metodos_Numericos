import streamlit as st
from src.funciones import displayPDF

# Configuración de la página
st.set_page_config(layout="wide", page_title="Métodos Numéricos", page_icon="")

displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
