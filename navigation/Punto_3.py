import numpy as np
import streamlit as st
import plotly.graph_objects as go

from src.MetodosNumericos import MetodosNumericos
from components.PlotlyChart import PlotlyChartPuntoC


def punto_tres():

    file1 = open('./data/punto_3/condicion_1orden.md').read()
    st.markdown(
        '''
        ## Hallar puntos criticos de forma numérica para las siguientes funciones:
        ''')

    col1, _, col2 = st.columns([1, 0.2, 1])

    with col1:

        def f(x): return np.exp(-x)-x
        def f_prima(x): return -np.exp(-x)-1
        mn = MetodosNumericos(f=f, f_prima=f_prima)
        x = mn.newton(0)[0]

        st.markdown(
            '#### Gráfico y punto critico de la función $f(x) = e^{-x}-x$')
        chart = PlotlyChartPuntoC(
            f, [-5, 5], x)
        chart.show()

        st.markdown(f'''El punto critico para ésta función se encontro mediante el metodo de newton otorgando el valor de **{x}**,
                    con un error relativo de **{mn.newton(0)[1]}**, el detalle de la evaluación en el punto se da en la gráfica
                    sin embargo tambien se lo describiremos a continuación: **f({x}) = {f(x)}**''')

    with col2:
        def f2(x): return np.log(x)-(5*x**2)
        def f2_prima(x): return (1/x)-10*x
        mn = MetodosNumericos(f=f2, f_prima=f2_prima)

        st.markdown(
            '#### Gráfico y punto critico de la función $f(x)=log(x)-5x^2$')
        st.plotly_chart(mn.plot_function([-2, 3]))

        st.markdown(file1)
    st.divider()
