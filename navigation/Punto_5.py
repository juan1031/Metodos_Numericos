import streamlit as st
import numpy as np
import sympy as sp
from src.newton import NewtonMethod
from scipy.optimize import newton

file1 = open('./data/punto_5/contexto_cournot.md').read()
file2 = open('./data/punto_5/pasos_cournot.md').read()


def punto_cinco():

    st.markdown(file1)

    col1, col2, col3 = st.columns(3)
    with col1:
        c1 = st.number_input("Costo marginal de la empresa 1:",
                             min_value=0.0, max_value=1.0, value=0.6, step=0.01)
    with col2:
        c2 = st.number_input("Costo marginal de la empresa 2:",
                             min_value=0.0, max_value=1.0, value=0.8, step=0.01)
    with col3:
        gamma = st.number_input(
            "Parámetro γ:", min_value=0.1, max_value=2.0, value=0.6, step=0.1)

    col1, col2 = st.columns(2)
    with col1:
        q1_0 = st.number_input("Cantidad inicial de la empresa 1:",
                               min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    with col2:
        q2_0 = st.number_input("Cantidad inicial de la empresa 2:",
                               min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Calcular"):
        newton_solver = NewtonMethod(gamma, c1, c2)
        # Valores iniciales de q1 y q2
        q1, q2 = newton_solver.solve(q1_0, q2_0)
        st.write("Cantidad óptima de producción para la empresa 1:", q1)
        st.write("Cantidad óptima de producción para la empresa 2:", q2)

    st.divider()

    with st.expander("Ver pasos"):
        st.markdown(file2)

    with st.expander("Ver script de la clase NewtonMethod"):
        with open("./src/newton.py", "r") as file:
            script_content = file.read()
        st.code(script_content, language="python")

    st.divider() 