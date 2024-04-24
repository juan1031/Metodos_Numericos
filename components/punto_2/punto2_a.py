
import streamlit as st
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards

from components.PlotlyChart import PlotlyChart
from components.markdown.markdown import Markdown

from src.MetodosNumericos import MetodosNumericos


def punto2_a():

    st.subheader(
        '''
        a) La solución numérica a la ecuación $e^x = 2(1 − x)$. Ayuda: está en el intervalo [0, 3].
        '''
    )

    st.write('Configuración de los Parámetros')

    col1, _, col2 = st.columns([1, 0.05, 1.5])
    # Pedir al usuario el intervalo para el método de bisección
    with col1:
        mn = MetodosNumericos(f=lambda x: np.exp(x) - 2*(1 - x),
                              f_prima=lambda x: np.exp(x) + 2)

        intervalo_biseccion = st.slider(
            "Intervalo para Bisección", 0.0, 3.0, (0.0, 3.0), 0.1)

        # Pedir al usuario el intervalo para el método de la secante
        intervalo_secante = st.slider(
            "Intervalo para Secante", 0.0, 3.0, (0.0, 3.0), 0.1)
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

        error_relativo_biseccion = resultado_biseccion[1]
        error_relativo_secante = resultado_secante[1]
        error_relativo_newton = resultado_newton[1]

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
            '''
            <p style="font-family: Arial; font-size: 20px; font-weight: bold; text-align: left;">
            <b>Análisis</b>
            ''',
            unsafe_allow_html=True
        )
        st.markdown(
            f'''
            Los resultados obtenidos de las aproximaciones utilizando los métodos de bisección, 
            secante y Newton-Raphson con un máximo de **{max_iter}** iteraciones para cada metodo muestran que cada método produce una estimación de la raíz, siendo
            todas bastante cercanas entre sí. Sin embargo, al observar los errores relativos asociados 
            a cada método, podemos notar diferencias significativas en su precisión. El método de bisección tiene un 
            error relativo de aproximadamente **{error_relativo_biseccion}**, 
            lo que indica una precisión moderada pero segura. Por otro lado, tanto el método de secante 
            como el de Newton-Raphson muestran errores relativos mucho más bajos, de alrededor de **{error_relativo_secante}**
            y **{error_relativo_newton}** unidades respectivamente. Esto sugiere que, aunque todos los métodos ofrecen una aproximación
            cercana, los métodos de secante y sobre todo Newton-Raphson son notablemente más precisos en este caso.
            ''',
        )

    st.divider()
