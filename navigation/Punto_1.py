import streamlit as st
import hydralit_components as hc
from components.footer import footer_style
from components.punto_1.punto_1_a import punto_1_a
from components.punto_1.punto_1_b import punto_1_b
from components.punto_1.punto_1_c import punto_1_c

file1 = open('./data/punto_1/que_es.md').read()
file3 = open('./data/punto_1/objetivo.md').read()
file4 = open('./data/punto_1/problema.md').read()
filea = open('./data/punto_1/a.md').read()
fileb = open('./data/punto_1/b.md').read()
filec = open('./data/punto_1/c.md').read()
fileformulas = open('./data/punto_1/formulas.md').read()
image = './assets/images/image.png'


def punto_uno():

    a = 'A)'
    b = 'B)'
    c = 'C)'

    tabs = [
        a,
        b,
        c,
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
    # -------------------------------------------------------------

    st.markdown(file1)
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.image(image, caption='Fuente: Bresani Tamayo, C., Burns OHara, A. R., Escalante Gavancho, P., & Medroa Delgado, G. (2018). Matemática financiera: teoría y ejercicios.', width=700)

    st.markdown(file3)

    st.markdown(file4)

    st.markdown(fileformulas)

    # clase

    st.divider()

    st.header(
        "Con ayuda de la clase construida, responder a los siguientes problemas: ")

    chosen_tab = hc.option_bar(
        option_definition=option_data,
        title='',
        key='PrimaryOptionx2',
        override_theme=theme,
        horizontal_orientation=True)

    if chosen_tab == a:
        st.markdown(filea)
        st.divider()
        punto_1_a()

        st.write("Para garantizar la capacidad de retirar `$75,000` dentro de seis meses, `$45,000` dentro de ocho meses, la mitad del depósito dentro de diez meses y mantener un saldo de `$300,000` dentro de 12 meses, se debe depositar hoy un total de aproximadamente `$579,074.10` en una cuenta de ahorros que ofrece un interés del 2% mensual.")

        st.divider()
        with st.expander("Ver script del primer punto"):
            with open("./components/punto_1/code_a.py", "r") as file:
                script_content = file.read()
            st.code(script_content, language="python")
        st.divider()

    elif chosen_tab == b:
        st.markdown(fileb)
        st.divider()

        punto_1_b()
        st.write("Para cumplir con el pago de los tres documentos por cobrar, que en total suman `$900.000`, a una tasa de interés mensual del 4%, el pago debe realizarse en aproximadamente `1.56 meses`. Esto se traduce en `47 días`.")
        st.divider()

        with st.expander("Ver script del segundo punto"):
            with open("./components/punto_1/code_b.py", "r") as file:
                script_content = file.read()
            st.code(script_content, language="python")

        st.divider()

    elif chosen_tab == c:
        st.markdown(filec)
        st.divider()
        punto_1_c()

        st.write("Pablo cancelará la deuda con dos pagos iguales en el mes 6 y 12, cada uno por un monto aproximado de `$324.145` a una tasa de interés del 3% mensual")

        st.divider()

        with st.expander("Ver script del tercer punto"):
            with open("./components/punto_1/code_c.py", "r") as file:
                script_content = file.read()
            st.code(script_content, language="python")

        st.divider()
