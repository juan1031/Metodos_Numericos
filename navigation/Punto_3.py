import numpy as np
import streamlit as st
import plotly.graph_objects as go

from src.MetodosNumericos import MetodosNumericos
from components.PlotlyChart import PlotlyChartPuntoC


def punto_tres():

    st.markdown(
        '''
        Hallar puntos criticos de forma numérica para las siguientes funciones:
        ''')

    col1, _, col2 = st.columns([1, 0.1, 1])

    with col1:

        def f(x): return np.exp(-x)-x
        def f_prima(x): return -np.exp(-x)-1
        mn = MetodosNumericos(f=f, f_prima=f_prima)
        x = mn.newton(0)[0]
        chart = PlotlyChartPuntoC(
            f, [-10, 10], x, r'Punto Critico de la Función $f(x)=e^{-x}-x$')
        chart.show()

    with col2:
        def f(x): return np.log(x)-(5*x**2)
        def f_prima(x): return (1/x)-10*x
        mn = MetodosNumericos(f=f, f_prima=f_prima)
        st.plotly_chart(mn.plot_function([0, 10]))

        x = mn.gradient_descent(0.2, 0.0001, max_iter=1000)[0]
        chart = PlotlyChartPuntoC(
            f, [-10, 10], x, r'Punto Critico de la Función $f(x)=log(x)-5x^2$')
        chart.show()
