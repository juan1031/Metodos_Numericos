import streamlit as st
import hydralit_components as hc
from components.footer import footer_style

file1 = open('./data/punto_5/contexto_cournot.md').read()

def punto_cinco():

    # -------------------------------------------------------------
    st.title("Punto 5")
    # -------------------------------------------------------------
    st.markdown(file1)

    st.markdown(
        '''
        ''')
