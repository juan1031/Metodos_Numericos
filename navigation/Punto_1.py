import streamlit as st
import hydralit_components as hc
from components.footer import footer_style
from components.punto_1.punto_1_a import punto_1_a
from components.punto_1.punto_1_b import punto_1_b
from components.punto_1.punto_1_c import punto_1_c

file1 = open('./data/punto_1/que_es.md').read()
file2 = open('./data/punto_1/para_que_sirve.md').read()
file3 = open('./data/punto_1/objetivo.md').read()
file4 = open('./data/punto_1/problema.md').read()
filea = open('./data/punto_1/a.md').read()
fileb = open('./data/punto_1/b.md').read()
filec = open('./data/punto_1/c.md').read()


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
    {'icon': "🏆", 'label': a},
    {'icon': "🏆", 'label': b},
    {'icon': "🏆", 'label': c}
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#81c3d7',
              'txc_active': 'white', 'option_active': '#16425b'}
font_fmt = {'font-class': 'h3', 'font-size': '40%'}


def punto_uno():
    # -------------------------------------------------------------

    st.markdown(file1)

    st.markdown(file2)

    st.markdown(file3)

    st.markdown(file4)

    # clase

    st.divider()


    page = hc.option_bar(
        option_definition=option_data,
        title='Con ayuda de la clase construida, responder a los siguientes problemas: ',
        key='PrimaryOptionx2',
        override_theme=over_theme,
        horizontal_orientation=True)

    if page == a:
        st.markdown(filea)
        punto_1_a()
        with st.expander("Ver script del primer punto"):
            with open("./components/punto_1/code_a.py", "r") as file:
                script_content = file.read()
            st.code(script_content, language="python")

    elif page == b:
        st.markdown(fileb)
        punto_1_b()
        with st.expander("Ver script del segundo punto"):
            with open("./components/punto_1/code_b.py", "r") as file:
                script_content = file.read()
            st.code(script_content, language="python")

    else:
        st.markdown(filec)
        punto_1_c()
    with st.expander("Ver script del tercer punto"):
        with open("./components/punto_1/code_c.py", "r") as file:
            script_content = file.read()
        st.code(script_content, language="python")