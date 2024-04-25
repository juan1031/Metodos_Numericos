from src.funciones import displayPDF
from components.markdown.markdown import Markdown
from PIL import Image
from src.funciones import slideshow_swipeable
import streamlit as st

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

    st.header("Objetivo")
    st.markdown(
        text1,
        unsafe_allow_html=True,
    ),

    st.header("Taller")

    IMAGES = [
        "../assets/images/sc1.png",
        "../assets/images/sc2.png",
        "../assets/images/sc3.png",
        "../assets/images/sc4.png",
        "../assets/images/sc51.png",
        "../assets/images/sc52.png",
    ]

    slideshow_swipeable(IMAGES)

    #     Ruta o URL del documento
    # file_path = 'assets/Problem_Set_I_Numerical_Methods.pdf'

    # feature_image1 = Image.open(r'img/min_manual.png')
    # with st.container():
    #     image_col, text_col = st.columns((1,3))
    #     with image_col:
    #         st.image(feature_image1, caption='Fuente: Propia')
    #     with text_col:
    #         st.markdown(""" <style> .font {
    #             font-size:22px ; font-family: 'Black'; color: #FFFFF;}
    #             </style> """, unsafe_allow_html=True)
    #         st.markdown('<p class="font">Manual Obtención y Procesamiento de Datos</p>', unsafe_allow_html=True)
    # displayPDF("assets/Problem_Set_I_Numerical_Methods.pdf")
