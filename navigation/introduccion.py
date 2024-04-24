import streamlit as st
from src.funciones import displayPDF
from components.markdown.markdown import Markdown
# from components.Custom_Components import CenteredColumns

# -------------------------------------------------------------

file1 = open("./data/objetivo.md").read()
text1 = Markdown(file1).show(tab=True)


def intro_page():

    st.success(
        '''El presente trabajo ha sido desarrollado por María José Castillo, 
        Luisa Fernanda Guevara y Juan David Bocanegra, como parte del curso de 
        Métodos Numéricos por el profesor Camilo Castillo de la Universidad Externado de Colombia. 
        En este proyecto, hemos creado un aplicativo utilizando
          técnicas de programación en Python y la implementación de la clase de Métodos
            Numéricos para resolver un conjunto de problemas planteados en el taller.''')
    st.divider()

    st.header("Objetivo")
    st.markdown(
        text1,
        unsafe_allow_html=True,
    ),

    st.header("Taller")
    displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
