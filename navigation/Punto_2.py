import streamlit as st

file1 = open('./data/punto_2/pregunta.md').read()


def punto_dos():

    # -------------------------------------------------------------
    st.title("Punto 2 ")
    # -------------------------------------------------------------

    st.markdown(file1)
