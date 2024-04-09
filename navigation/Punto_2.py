import streamlit as st

from src.MetodosNumericos import MetodosNumericos
from src.funciones import tiempo_vs_precision
from src.funciones import ecuacion_a, ecuacion_b, ecuacion_c, ecuacion_d
from src.funciones import graficar


file1 = open('./data/punto_2/pregunta.md').read()


def punto_dos():

    # -------------------------------------------------------------
    st.title("Punto 2 ")
    # -------------------------------------------------------------

    # Importamos la clase MetodosNumericos que proporcionaste

    # a) La solución numérica a la ecuación ex = 2(1 − x)
    precision_vs_tiempo_a = tiempo_vs_precision(
        ecuacion_a, MetodosNumericos.biseccion, 1e-8, 1e-15, 1e-8)
    st.pyplot(graficar(precision_vs_tiempo_a,
              'Tiempo vs Precisión para ex = 2(1 − x)'))

    # b) Una aproximación numérica a la raíz de f(x) = x^3 + x − 7
    precision_vs_tiempo_b = tiempo_vs_precision(
        ecuacion_b, MetodosNumericos.newton, 1e-8, 1e-15, 1e-8)
    st.pyplot(graficar(precision_vs_tiempo_b,
              'Tiempo vs Precisión para x^3 + x − 7'))

    # c) Halle la raíz positiva de la ecuación x = 5(1 − e^−x ) con cinco decimales de aproximación
    precision_vs_tiempo_c = tiempo_vs_precision(
        ecuacion_c, MetodosNumericos.newton, 1e-8, 1e-15, 1e-8)
    st.pyplot(graficar(precision_vs_tiempo_c,
              'Tiempo vs Precisión para x = 5(1 − e^−x )'))

    # d) Halle la raíz de la función f(x) = x − 3e^−x con 6 decimales de aproximación
    precision_vs_tiempo_d = tiempo_vs_precision(
        ecuacion_d, MetodosNumericos.newton, 1e-8, 1e-15, 1e-8)
    st.pyplot(graficar(precision_vs_tiempo_d,
              'Tiempo vs Precisión para x − 3e^−x'))

    st.markdown(file1)
