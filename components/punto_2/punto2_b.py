import streamlit as st
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards

from components.PlotlyChart import PlotlyChart
from components.markdown.markdown import Markdown

from src.MetodosNumericos import MetodosNumericos


def punto2_b():

    st.subheader(
        '''
        b) Una aproximación numérica de la raiz de $f(x) = x^{3}+x-7$. Luego con 1.7 (raiz de f) halle el error relativo de su aproximación
        '''
    )

    st.write('Configuración de los Parámetros')

    col1, _, col2 = st.columns([1, 0.05, 1.5])
    # Pedir al usuario el intervalo para el método de bisección
    with col1:
        mn = MetodosNumericos(f=lambda x: x**3+x-7,
                              f_prima=lambda x: 3*x**2+1)

        intervalo_biseccion = st.slider(
            "Intervalo para Bisección", -3.0, 3.0, (0.0, 3.0), 0.1)

        # Pedir al usuario el intervalo para el método de la secante
        intervalo_secante = st.slider(
            "Intervalo para Secante", -3.0, 3.0, (0.0, 3.0), 0.1)
    with col2:

        # Pedir al usuario el punto inicial para el método de Newton
        p0_newton = st.number_input(
            "Punto inicial para Newton", value=0.0, step=0.1)

        # Pedir al usuario la tolerancia
        tolerancia = st.number_input(
            "Tolerancia", value=1e-6, format="%e", step=1e-7)

        # Pedir al usuario el número máximo de iteraciones
        max_iter = st.number_input(
            "Número máximo de iteraciones", value=100, step=10)

        # Ejecuta los métodos y almacena los resultados y tiempos
        resultado_biseccion, tiempo_biseccion, resultado_secante, tiempo_secante, resultado_newton, tiempo_newton = mn.comparar_metodos(
            intervalo_biseccion, intervalo_secante, p0_newton, tolerancia, max_iter)

        error_relativo_biseccion = abs(resultado_biseccion[0]-1.7)/1.7
        error_relativo_secante = abs(resultado_secante[0]-1.7)/1.7
        error_relativo_newton = abs(resultado_newton[0]-1.7)/1.7

        chart = PlotlyChart(error_relativo_biseccion, error_relativo_secante, error_relativo_newton,
                            tiempo_biseccion, tiempo_secante, tiempo_newton)

    col1, _, col2 = st.columns([1, 0.05, 1.5])

    with col1:
        st.write('Resultado de las aproximaciones según los metodos:')
        st.metric(
            'Bisección:', value=resultado_biseccion[0])
        st.metric('Secante:', value=resultado_secante[0])
        st.metric('Newton R:', value=resultado_newton[0])
        style_metric_cards(background_color='rgba(0,0,0,0)',
                           border_left_color="#003C6F", border_color="#003C6F", box_shadow="blue")

    with col2:
        chart.show()

    col1, _, col2 = st.columns([1, 0.05, 1.5])

    with col1:
        st.plotly_chart(mn.plot_function())

    with col2:
        st.markdown(
            f'''
            <p style="font-family: Arial; font-size: 20px; font-weight: bold; text-align: left;">
            <b>Análisis</b>
            ''',
            unsafe_allow_html=True
        )
        st.markdown(
            f'''
            En esta ocasión, contábamos con el valor real de la raíz de la función, lo que nos permitió 
            calcular el error relativo de manera precisa. Resulta interesante observar que, a pesar de 
            esta simulación con un valor real predeterminado, los errores relativos obtenidos para cada 
            método fueron bastante similares. Sin embargo, al analizar el tiempo de ejecución, queda 
            claro que el método de Newton-Raphson sigue siendo más rápido que el resto..
            ''',
        )

    st.divider()
