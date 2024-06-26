import streamlit as st
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards

from components.PlotlyChart import PlotlyChart
from components.markdown.markdown import Markdown

from src.MetodosNumericos import MetodosNumericos


def punto2_c():

    st.subheader(
        '''
        c) Hallar la raíz positiva de la ecuación $x=5(1-e^{-x})$ con cinco decimales de aproximación.
        '''
    )

    st.write('Configuración de los Parámetros')

    col1, _, col2 = st.columns([1, 0.05, 1.5])
    # Pedir al usuario el intervalo para el método de bisección
    with col1:
        mn = MetodosNumericos(f=lambda x: 5*(1-np.exp(-x)),
                              f_prima=lambda x: 5*np.exp(-x))

        intervalo_biseccion = st.slider(
            "Intervalo para Bisección", -1.0, 2.0, (-1.0, 2.0), 0.1)

        # Pedir al usuario el intervalo para el método de la secante
        intervalo_secante = st.slider(
            "Intervalo para Secante", -1.0, 2.0, (-1.0, 2.0), 0.1)
    with col2:

        # Pedir al usuario el punto inicial para el método de Newton
        p0_newton = st.number_input(
            "Punto inicial para Newton", value=0.0, step=0.1)

        # Pedir al usuario la tolerancia
        tolerancia = st.number_input(
            "Tolerancia", value=1e-5, format="%e", step=1e-7)

        # Pedir al usuario el número máximo de iteraciones
        max_iter = st.number_input(
            "Número máximo de iteraciones", value=100, step=10)

        # Ejecuta los métodos y almacena los resultados y tiempos
        resultado_biseccion, tiempo_biseccion, resultado_secante, tiempo_secante, resultado_newton, tiempo_newton = mn.comparar_metodos(
            intervalo_biseccion, intervalo_secante, p0_newton, tolerancia, max_iter)

        error_relativo_biseccion = resultado_biseccion[1]
        error_relativo_secante = resultado_secante[1]
        error_relativo_newton = resultado_newton[1]

        chart = PlotlyChart(error_relativo_biseccion, error_relativo_secante, error_relativo_newton,
                            tiempo_biseccion, tiempo_secante, tiempo_newton)

    col1, _, col2 = st.columns([1, 0.05, 1.5])

    with col1:
        st.write('Resultado de las aproximaciones según los metodos:')
        st.metric(
            'Bisección:', value=round(resultado_biseccion[0], 5))
        st.metric('Secante:', value=round(resultado_secante[0], 5))
        st.metric('Newton R:', value=round(resultado_newton[0], 5))
        style_metric_cards(background_color='rgba(0,0,0,0)',
                           border_left_color="#003C6F", border_color="#003C6F", box_shadow="blue")

    with col2:
        chart.show()

    col1, _, col2 = st.columns([1, 0.05, 1.5])

    with col1:
        st.plotly_chart(mn.plot_function([-1, 2]))

    with col2:
        st.markdown(
            '''
            <p style="font-family: Arial; font-size: 20px; font-weight: bold; text-align: left;">
            <b>Análisis</b>
            ''',
            unsafe_allow_html=True
        )
        st.markdown(
            f'''
            Los resultados obtenidos de las aproximaciones utilizando los métodos de bisección, 
            secante y Newton-Raphson con un máximo de **{max_iter}** iteraciones para cada metodo con esta función
            una aproximación exacta en cero. El método de bisección, secante y newton tiene un 
            error relativo de aproximadamente **{error_relativo_biseccion}**, **{error_relativo_newton}**, **{error_relativo_secante}**
            respectivamente, donde indica una bastante precisión con el intervalo definido por defecto. 
            Por otro lado, el metodo de bisección se demora mucho más que los demás, y el intervalo definido para secante y newton juegan
            un papel muy importante en esta métrica.
            ''',
        )

    st.divider()
