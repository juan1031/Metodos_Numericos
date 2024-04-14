import streamlit as st
import numpy as np
import sympy as sp

file1 = open('./data/punto_5/contexto_cournot.md').read()
file2 = open('./data/punto_5/pasos_cournot.md').read()

def cournot_duopolio(q1, q2, c1, c2, gamma):
    f1 = ((q1 + q2)**(-1/gamma)) - (1/gamma)*((q1 + q2)**((-1/gamma)-1))*q1 - (1/2)*c1
    f2 = ((q1 + q2)**(-1/gamma)) - (1/gamma)*((q1 + q2)**((-1/gamma)-1))*q2 - (1/2)*c2
    return f1, f2

def matriz_jacobiana(q1, q2, c1, c2, gamma):
    # Calcular las derivadas parciales de f1 y f2 con respecto a q1 y q2
    f1_q1 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[0], q1)
    f1_q2 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[0], q2)
    f2_q1 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[1], q1)
    f2_q2 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[1], q2)

    # Construir y retornar la matriz jacobiana
    return np.array([[f1_q1, f1_q2], [f2_q1, f2_q2]])



# Función para encontrar los óptimos
def encontrar_optimos(c1, c2, gamma):
    q1, q2 = sp.symbols('q1 q2')
   

def punto_cinco():
    # Interfaz de usuario
    st.title("Punto 5")
    st.markdown(file1)

    col1, col2, col3 = st.columns(3)
    with col1:
        c1 = st.number_input("Costo marginal de la empresa 1:", min_value=0.0, max_value=1.0, value=0.6, step=0.01)
    with col2:
        c2 = st.number_input("Costo marginal de la empresa 2:", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
    with col3:
        gamma = st.number_input("Parámetro γ:", min_value=0.1, max_value=2.0, value=0.6, step=0.1)

    if st.button("Calcular"):
        q1_optimo, q2_optimo = encontrar_optimos(c1, c2, gamma)
        if q1_optimo is not None and q2_optimo is not None:
            st.write("q1 óptimo:", q1_optimo)
            st.write("q2 óptimo:", q2_optimo)
        else:
            st.error("No se pudieron calcular los valores óptimos.")

    if st.button("Ver pasos"):
                st.markdown(file2)




