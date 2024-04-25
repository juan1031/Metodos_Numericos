from components.markdown.markdown import Markdown
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

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
            Numéricos para resolver un conjunto de problemas planteados en el taller/parcial.''')
    st.divider()

    st.header("Taller")

    # Ruta o URL del documento
    file_path = './assets/Problem_Set_I_Numerical_Methods.pdf'

    feature_image1 = Image.open(r'./assets/images/vistapdf.png')
    with st.container():
        image_col, text_col = st.columns((1, 3))
        with image_col:
            st.image(feature_image1, caption='Fuente: Propia')
            with open(file_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            _, col, _ = st.columns([0.5, 1, 0.5])
            with col:
                st.download_button(label="Descargar Taller/Parcial", key='3',
                                   data=PDFbyte,
                                   file_name="Taller.pdf",
                                   mime='application/octet-stream')
        with text_col:
            st.header("Objetivo")
            st.markdown(
                text1,
                unsafe_allow_html=True,
            ),

    st.divider()
