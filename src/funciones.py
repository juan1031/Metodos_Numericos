import streamlit as st
import base64
from src.MetodosNumericos import MetodosNumericos
import numpy as np
import matplotlib.pyplot as plt
import time


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'

        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

# --------- Segundo punto -------------


def tiempo_vs_precision(funcion, metodo, precision_inicial, precision_final, paso):
    tiempos = []
    precisiones = np.arange(precision_inicial, precision_final, paso)
    for precision in precisiones:
        start_time = time.time()
        metodo(funcion, precision)
        end_time = time.time()
        tiempo = end_time - start_time
        tiempos.append(tiempo)
    return precisiones, tiempos


def ecuacion_a(x, precision):
    def f(x):
        return np.exp(x) - 2*(1 - x)
    metodos = MetodosNumericos(f=f)
    return metodos.biseccion(0, 3, tol=precision)


def ecuacion_b(x, precision):
    def f(x):
        return x**3 + x - 7
    metodos = MetodosNumericos(f=f)
    return metodos.newton(x, tol=precision)


def ecuacion_c(x, precision):
    def f(x):
        return x - 5*(1 - np.exp(-x))
    metodos = MetodosNumericos(f=f)
    return metodos.newton(x, tol=precision)


def ecuacion_d(x, precision):
    def f(x):
        return x - 3*np.exp(-x)
    metodos = MetodosNumericos(f=f)
    return metodos.newton(x, tol=precision)


def graficar(tiempo_vs_precision, titulo):
    precisiones, tiempos = tiempo_vs_precision
    plt.plot(precisiones, tiempos, marker='o')
    plt.title(titulo)
    plt.xlabel('Precisión')
    plt.ylabel('Tiempo (s)')
    plt.grid(True)
    return plt.gcf()

# -------------------------------------
