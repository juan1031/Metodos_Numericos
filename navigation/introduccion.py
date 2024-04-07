import streamlit as st
from src.funciones import displayPDF
from components.markdown.markdown import Markdown

file1 = f'{open("./data/.Ejemplo").read()}'
text1 = Markdown(file1).show(tab=True)

file2 = f'{open("./data/Ejemplo.md").read()}'


def intro_page():

    # -------------------------------------------------------------
    st.title("Trabajo 1")
    # -------------------------------------------------------------

    st.success(
        'Este trabajo fue realizado por: María José Castillo, Luisa Fernanda Guevara y Juan David Bocanegra')

    st.markdown(
        text1,
        unsafe_allow_html=True,
    )
    for i in range(2):
        st.markdown('#')

    st.markdown(file2)
    displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
