import streamlit as st
import numpy as np
import plotly.graph_objects as go

from components.PlotlyChart import PlotlyChart
from src.MetodosNumericos import MetodosNumericos
from src.funciones import tiempo_vs_precision
from src.funciones import ecuacion_a, ecuacion_b, ecuacion_c, ecuacion_d
from src.funciones import graficar


file1 = open('./data/punto_2/pregunta.md').read()

# -------------------------- Seccion A --------------------------------------
mn = MetodosNumericos(f=lambda x: np.exp(x) - 2*(1 - x),
                      f_prima=lambda x: np.exp(x) + 2)

intervalo_biseccion = [0, 3]
intervalo_secante = [0, 3]
p0_newton = 0
tolerancia = 1e-6
max_iter = 100

# Ejecuta los métodos y almacena los resultados y tiempos
resultado_biseccion, tiempo_biseccion, resultado_secante, tiempo_secante, resultado_newton, tiempo_newton = mn.comparar_metodos(
    intervalo_biseccion, intervalo_secante, p0_newton, tolerancia, max_iter)

error_relativo_biseccion = resultado_biseccion[1]
error_relativo_secante = resultado_secante[1]
error_relativo_newton = resultado_newton[1]

chart = PlotlyChart(error_relativo_biseccion, error_relativo_secante, error_relativo_newton,
                    tiempo_biseccion, tiempo_secante, tiempo_newton)

# ----------------------------------------------------------------------------


def punto_dos():

    # -------------------------------------------------------------
    st.title("Punto 2 ")
    # -------------------------------------------------------------

    # a) La solución numérica a la ecuación ex = 2(1 − x)

    # Mostrar el gráfico en Streamlit
    # Agregar un espacio entre las columnas
    col1, _, col2 = st.columns([1, 0.05, 1])

    with col1:
        st.write("")  # Espacio vacío para centrar la columna
        chart.show()

    with col2:
        st.write("")  # Espacio vacío para centrar la columna
        st.plotly_chart(mn.plot_function())

    # b) Una aproximación numérica a la raíz de f(x) = x^3 + x − 7

    # c) Halle la raíz positiva de la ecuación x = 5(1 − e^−x ) con cinco decimales de aproximación

    # d) Halle la raíz de la función f(x) = x − 3e^−x con 6 decimales de aproximación

    st.markdown(file1)
