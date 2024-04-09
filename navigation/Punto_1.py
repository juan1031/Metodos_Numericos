import streamlit as st
import hydralit_components as hc
from components.footer import footer_style

file1 = open('./data/punto_1/que_es.md').read()
file2 = open('./data/punto_1/para_que_sirve.md').read()
file3 = open('./data/punto_1/objetivo.md').read()
file4 = open('./data/punto_1/problema.md').read()


# NavBar

a = 'A)'
b = 'B)'
c = 'C)'

tabs = [
    a,
    b,
    c
]

option_data = [
    {'icon': "📜", 'label': a},
    {'icon': "1️⃣", 'label': b},
    {'icon': "🏆", 'label': c}
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#81c3d7',
              'txc_active': 'white', 'option_active': '#16425b'}
font_fmt = {'font-class': 'h3', 'font-size': '40%'}


def punto_uno():

    # -------------------------------------------------------------
    st.title("Punto 1")
    # -------------------------------------------------------------
    st.markdown(file1)

    st.markdown(file2)
    
    st.markdown(file3)

    st.markdown(file4)

    # clase

    st.markdown('##')
    st.divider()

    st.markdown(
        "Con ayuda de la clase construida, responder a los siguientes problemas: ")

    page = hc.option_bar(
        option_definition=option_data,
        title='Subsecciones',
        key='PrimaryOptionx2',
        override_theme=over_theme,
        horizontal_orientation=True)

    if page == a:
        st.markdown('##')

    elif page == b:
        st.markdown('##')

    elif page == c:
        st.markdown('##')
