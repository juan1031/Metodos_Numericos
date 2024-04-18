import streamlit as st


def punto_cuatro():

    file1 = open('./data/punto_4/contexto_mco.md').read()
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    st.markdown(file1)
    # Añadir una imagen
    st.image('./data/punto_4/EDA_metodos.png', caption='EDA de la base de datos')

    
