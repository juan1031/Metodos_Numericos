import streamlit as st
import hydralit_components as hc
from components.footer import footer_style


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

    st.markdown('##')
    st.divider()
    page = hc.option_bar(
        option_definition=option_data,
        title='Subsecciones',
        key='PrimaryOptionx2',
        override_theme=over_theme,
        horizontal_orientation=True)

    if page == a:
        st.write('hola')
        # la gracia es que aqui en cada seccion solo se llame la funcion que sea el script independiente

    elif page == b:
        st.write('hola')

    elif page == c:
        st.write('hola')
