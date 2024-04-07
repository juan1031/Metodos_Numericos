from navigation.Punto_5 import punto_cinco
from navigation.Punto_4 import punto_cuatro
from navigation.Punto_3 import punto_tres
from navigation.Punto_2 import punto_dos
from navigation.Punto_1 import punto_uno
from navigation.introduccion import intro_page

from components.footer import footer_style

import streamlit as st
import hydralit_components as hc

# Configuración de la página
st.set_page_config(
    page_title='Métodos Numéricos',
    page_icon="assets/images/JML-sin-fondo.png",
    initial_sidebar_state="collapsed"
)


max_width_str = f"max-width: {90}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)

# Footer

st.markdown(footer_style, unsafe_allow_html=True)

# NavBar

introduccion = 'Introducción'
punto_1 = 'Punto'
punto_2 = 'Punto 2'
punto_3 = 'Punto 3'
punto_4 = 'Punto 4'
punto_5 = 'Punto 5'


tabs = [
    introduccion,
    punto_1,
    punto_2,
    punto_3,
    punto_4,
    punto_5
]

option_data = [
    {'icon': "📜", 'label': introduccion},
    {'icon': "1️⃣", 'label': punto_1},
    {'icon': "🏆", 'label': punto_2},
    {'icon': "🏆", 'label': punto_3},
    {'icon': "🏆", 'label': punto_4},
    {'icon': "🏆", 'label': punto_5}

]

over_theme = {'txc_inactive': 'black', 'menu_background': '#81c3d7',
              'txc_active': 'white', 'option_active': '#16425b'}
font_fmt = {'font-class': 'h3', 'font-size': '60%'}

chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

if chosen_tab == introduccion:
    intro_page()

if chosen_tab == punto_1:
    punto_uno()

if chosen_tab == punto_2:
    punto_dos()

if chosen_tab == punto_3:
    punto_tres()

if chosen_tab == punto_4:
    punto_cuatro()

if chosen_tab == punto_5:
    punto_cinco()
