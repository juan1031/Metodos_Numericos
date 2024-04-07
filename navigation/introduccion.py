import streamlit as st
from src.funciones import displayPDF
from components.markdown import Markdown


def intro_page():

    # -------------------------------------------------------------
    st.title("Taller 1")
    st.write("Contenido de la Página 1")
    # -------------------------------------------------------------

    st.markdown(
        f'{open("./data/Introduccion.html").read()}',
        unsafe_allow_html=True)

    st.markdown(
        Markdown(open("./data/.Introduccion").read()).show(),
        unsafe_allow_html=True,
    )

    displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
