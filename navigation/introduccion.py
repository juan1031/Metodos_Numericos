import streamlit as st
from src.funciones import displayPDF


def intro_page():

    # -------------------------------------------------------------
    st.title("Taller 1")
    st.write("Contenido de la Página 1")
    # -------------------------------------------------------------

    st.markdown(
        '''
        ''')

    displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
