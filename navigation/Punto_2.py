import streamlit as st
import hydralit_components as hc
from components.punto_2.punto2_a import punto2_a


def punto_dos():

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
        {'icon': "", 'label': a},
        {'icon': "", 'label': b},
        {'icon': "", 'label': c}
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

    # a) La solución numérica a la ecuación ex = 2(1 − x)

    if chosen_tab == a:
        punto2_a()
    if chosen_tab == b:
        pass
    if chosen_tab == c:
        pass
