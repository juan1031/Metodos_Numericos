import streamlit as st
import hydralit_components as hc
from components.punto_2.punto2_a import punto2_a
from components.punto_2.punto2_b import punto2_b
from components.punto_2.punto2_c import punto2_c
from components.punto_2.punto2_d import punto2_d
from components.markdown.markdown import Markdown


def punto_dos():
    file1 = open('./data/punto_2/intro.md').read()
    text1 = Markdown(file1).show(tab=True)

    st.markdown(
        text1,
        unsafe_allow_html=True
    )

    # NavBar

    a = 'A)'
    b = 'B)'
    c = 'C)'
    d = 'D)'

    tabs = [
        a,
        b,
        c,
        d
    ]

    option_data = [
        {'icon': "", 'label': a},
        {'icon': "", 'label': b},
        {'icon': "", 'label': c},
        {'icon': "", 'label': d}
    ]

    # Define el tema para el NavBar
    theme = {
        'menu_background': '#1a1a1a',  # Color de fondo del menú
        'txc_inactive': '#999999',  # Color del texto de las pestañas inactivas
        'txc_active': 'white',  # Color del texto de la pestaña activa
        'option_active': '#007bff'  # Color de la pestaña activa
    }

    # Crea el NavBar con los datos y el tema especificados
    chosen_tab = hc.option_bar(
        option_definition=option_data,
        title='',
        key='PrimaryOptionx2',
        override_theme=theme,
        horizontal_orientation=True)

    if chosen_tab == a:
        punto2_a()
    if chosen_tab == b:
        punto2_b()
    if chosen_tab == c:
        punto2_c()
    if chosen_tab == d:
        punto2_d()
