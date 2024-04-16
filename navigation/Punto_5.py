import streamlit as st
import numpy as np
import sympy as sp
from  src.MetodosNumericos import MetodosNumericos
from scipy.optimize import newton

file1 = open('./data/punto_5/contexto_cournot.md').read()
file2 = open('./data/punto_5/pasos_cournot.md').read()

def cournot_duopolio(q1, q2, c1, c2, gamma):
    f1 = ((q1 + q2)**(-1/gamma)) - (1/gamma)*((q1 + q2)**((-1/gamma)-1))*q1 - (1/2)*c1
    f2 = ((q1 + q2)**(-1/gamma)) - (1/gamma)*((q1 + q2)**((-1/gamma)-1))*q2 - (1/2)*c2
    return f1, f2

def matriz_jacobiana2(q1, q2, c1, c2, gamma):
    # Calcular las derivadas parciales de f1 y f2 con respecto a q1 y q2
    f1_q1 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[0], q1)
    f1_q2 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[0], q2)
    f2_q1 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[1], q1)
    f2_q2 = sp.diff(cournot_duopolio(q1, q2, c1, c2, gamma)[1], q2)

    # Construir y retornar la matriz jacobiana
    return np.array([[f1_q1, f1_q2], [f2_q1, f2_q2]])

def matriz_jacobiana3(q1, q2, c1, c2, gamma):
    q1_sym = sp.Symbol('q1')
    q2_sym = sp.Symbol('q2')
    f1 = cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[0]
    f2 = cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[1]
    
    # Calcular las derivadas parciales de f1 y f2 con respecto a q1 y q2
    f1_q1 = sp.diff(f1, q1_sym).subs({q1_sym: q1, q2_sym: q2})
    f1_q2 = sp.diff(f1, q2_sym).subs({q1_sym: q1, q2_sym: q2})
    f2_q1 = sp.diff(f2, q1_sym).subs({q1_sym: q1, q2_sym: q2})
    f2_q2 = sp.diff(f2, q2_sym).subs({q1_sym: q1, q2_sym: q2})

    # Construir y retornar la matriz jacobiana
    return np.array([[f1_q1, f1_q2], [f2_q1, f2_q2]])

def matriz_jacobiana(q1, q2, c1, c2, gamma):
    # Define las variables simbólicas
    q1_sym, q2_sym = sp.symbols('q1 q2')

    # Calcula las derivadas parciales simbólicas
    f1_q1 = sp.diff(cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[0], q1_sym)
    f1_q2 = sp.diff(cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[0], q2_sym)
    f2_q1 = sp.diff(cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[1], q1_sym)
    f2_q2 = sp.diff(cournot_duopolio(q1_sym, q2_sym, c1, c2, gamma)[1], q2_sym)

    # Construye y retorna la matriz jacobiana
    J_value = np.array([[f1_q1.subs({q1_sym: q1, q2_sym: q2}).evalf(), f1_q2.subs({q1_sym: q1, q2_sym: q2}).evalf()],
                        [f2_q1.subs({q1_sym: q1, q2_sym: q2}).evalf(), f2_q2.subs({q1_sym: q1, q2_sym: q2}).evalf()]])

    return J_value

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
        # Inicializar la clase MetodosNumericos
        metodos_numericos = MetodosNumericos(cournot_duopolio=cournot_duopolio, matriz_jacobiana=matriz_jacobiana)
        
        # Definir un punto inicial
        p0 = np.array([0.1, 0.1])  # Punto inicial para q1 y q2
        
        try:
            # Calcular los óptimos usando el método de Newton multivariable
            optimos, historial_aproximaciones = metodos_numericos.newton_multivariable(p0, c1, c2, gamma)
            q1_optimo, q2_optimo = optimos
            
            # Mostrar los resultados
            st.write("q1 óptimo:", q1_optimo)
            st.write("q2 óptimo:", q2_optimo)
            
        except ValueError as e:
            st.error(str(e))

    if st.button("Ver pasos"):
        st.markdown(file2)