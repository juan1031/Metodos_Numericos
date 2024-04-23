import numpy as np
import streamlit as st
import plotly.graph_objects as go

from src.MetodosNumericos import MetodosNumericos
from components.PlotlyChart import PlotlyChartPuntoC


def punto_tres():

    file1 = open('./data/punto_3/acondicion.md').read()
    file2 = open('./data/punto_3/bcondicion.md').read()
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
        st.plotly_chart(mn.plot_function([-5, 5]))

        st.markdown(file1)

    with col2:
        def f2(x): return np.log(x)-(5*x**2)
        def f2_prima(x): return (1/x)-10*x
        mn = MetodosNumericos(f=f2, f_prima=f2_prima)
        x = mn.gss_max(0, 0.5)
        st.markdown(
            '#### Gráfico y punto critico de la función $f(x)=log(x)-5x^2$')
        chart = PlotlyChartPuntoC(
            f2, [-5, 5], x)
        chart.show()

        st.markdown(file2)

        st.markdown('''Se pudo demostrar un punto critico en el dominio el cual es con la condición de primer orden el cual es
                    $\sqrt{1/10}$. ''' + f'''El punto critico para ésta función se encontro mediante el metodo numérico GSS (Golden-section search)
                    otorgando el valor de **{x}**, el detalle de la evaluación en el punto se da en la gráfica sin embargo tambien 
                    se lo describiremos más sencillo a continuación: **f({x}) = {f(x)}**''')
    st.divider()
