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
    st.subheader("Ecuaciones de Valor")
    st.write("### ¿Qué son las Ecuaciones de Valor?")
    st.write("Las ecuaciones de valor son herramientas fundamentales en el campo de las finanzas que nos permiten analizar y comparar flujos de efectivo en diferentes momentos del tiempo. En esta aplicación, nos centraremos en comprender su significado y cómo podemos resolverlas utilizando Python.")

    st.write("### ¿Para qué sirven las Ecuaciones de Valor?")
    st.write("Las ecuaciones de valor son útiles para una variedad de propósitos en el mundo financiero, desde la valoración de inversiones hasta la toma de decisiones de financiamiento. Aquí exploraremos algunos de los casos de uso más comunes.")

    st.write("### Objetivo")
    st.write("Construir una clase en Python que permita solucionar numéricamente las ecuaciones de valor.")

    st.write("### Problema")
    st.write("Ecuación de valor. Cuando se quiere hallar un flujo de caja equivalente se utiliza una ecuación de valor y así se construye una condición (ecuación) que permite hallar el flujo equivalente. En algunos casos, hallar la solución a dicha condición no es una tarea sencilla. Tenga en cuenta que en algunos casos la variable de interés no es necesariamente el flujo de caja. Otras variables de interés pueden ser la periodicidad o una tasa de interés.")
    st.write("Reto: Construir una clase que reciba un argumento, (tasa, flujo o n). Si recibe")
    st.markdown("- **tasa**: entonces halle la tasa que cumple la ecuación de valor.")
    st.markdown("- **flujo**: entonces halle el flujo que cumple la ecuación de valor.")
    st.markdown("- **n**: entonces halle el valor n que cumple la ecuación de valor.")

    st.markdown("Por ende la clase construida es:")


    #clase 

    st.markdown('##')
    st.divider()

    st.markdown("Con ayuda de la clase construida, responder a los siguientes problemas: ")

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
