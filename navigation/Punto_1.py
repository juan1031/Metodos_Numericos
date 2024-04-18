import streamlit as st
import hydralit_components as hc
from components.footer import footer_style

file1 = open('./data/punto_1/que_es.md').read()
file2 = open('./data/punto_1/para_que_sirve.md').read()
file3 = open('./data/punto_1/objetivo.md').read()
file4 = open('./data/punto_1/problema.md').read()
filea = open('./data/punto_1/a.md').read()
fileb = open('./data/punto_1/b.md').read()
filec = open('./data/punto_1/c.md').read()

# NavBar

a = 'A)'
b = 'B)'
c = 'C)'

tabs = [
    a,
    b,
    c
]

option_data = [
    {'icon': "🏆", 'label': a},
    {'icon': "🏆", 'label': b},
    {'icon': "🏆", 'label': c}
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#81c3d7',
              'txc_active': 'white', 'option_active': '#16425b'}
font_fmt = {'font-class': 'h3', 'font-size': '40%'}


def punto_uno():

    # -------------------------------------------------------------
    st.title("Punto 1")
    # -------------------------------------------------------------
    st.markdown(file1)

    st.markdown(file2)
    
    st.markdown(file3)

    st.markdown(file4)

    # clase

    st.markdown('##')
    st.divider()

    st.markdown(
        "Con ayuda de la clase construida, responder a los siguientes problemas: ")

    page = hc.option_bar(
        option_definition=option_data,
        title='Subsecciones',
        key='PrimaryOptionx2',
        override_theme=over_theme,
        horizontal_orientation=True)
    

    codea = '''
class ValorPresente:
    def __init__(self, tasa_mensual, retiros, saldo_final_deseado):
        self.tasa_mensual = tasa_mensual
        self.retiros = retiros
        self.saldo_final_deseado = saldo_final_deseado

    def calcular_valor_presente(self, P):
        return sum(retiro / ((1 + self.tasa_mensual) ** mes) for mes, retiro in self.retiros.items()) + \
               (0.5 * P / ((1 + self.tasa_mensual) ** 10)) + \
               (self.saldo_final_deseado / ((1 + self.tasa_mensual) ** 12)) - P

    def newton_raphson(self, P0, tol=1e-6, max_iter=100):
        """
        Método de Newton-Raphson para encontrar la raíz de la ecuación.
        """
        P = P0
        for _ in range(max_iter):
            f_P = self.calcular_valor_presente(P)
            f_prime_P = -1 - 0.5 / ((1 + self.tasa_mensual) ** 10)
            P_next = P - f_P / f_prime_P
            if abs(P_next - P) < tol:
                return P_next
            P = P_next
        raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones".format(max_iter))

tasa_mensual = 0.02
retiros = {6: 75000, 8: 45000}
saldo_final_deseado = 300000

vp_calculator = ValorPresente(tasa_mensual, retiros, saldo_final_deseado)

P0 = 100000
depositado dentro de diez meses y aún se tenga un saldo de `$ 300.000 ` dentro de 12 meses?
valor_presente = vp_calculator.newton_raphson(P0)

print("Valor presente (P):", valor_presente)'''

    codeb = '''
import math

class Punto2FechaPago:
    def __init__(self, documentos, pago_total, tasa_interes):
        self.documentos = documentos
        self.pago_total = pago_total
        self.tasa_interes = tasa_interes

    def calcular_fecha_pago(self):
        lado_izquierdo = sum(monto / ((1 + self.tasa_interes) ** meses) for monto, meses in self.documentos.items())

        lado_derecho = self.pago_total / lado_izquierdo

        log_lado_derecho = math.log(lado_derecho)

        exponente = log_lado_derecho / math.log(1 + self.tasa_interes)

        n = exponente

        return n

    def calcular_dias_exactos(self, meses):
        dias_exactos = meses * 30  # Estimación de 30 días por mes
        return round(dias_exactos)

    def newton_raphson(self, x0, tol=1e-6, max_iter=100):
        """
        Método de Newton-Raphson para encontrar la raíz de la ecuación.
        """
        x = x0
        for _ in range(max_iter):
            f_x = (1.04) ** (x - 5) - 900000 / 1029859.345
            f_prime_x = math.log(1.04) * (1.04) ** (x - 5)
            x_next = x - f_x / f_prime_x
            if abs(x_next - x) < tol:
                return x_next
            x = x_next
        raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones".format(max_iter))

documentos = {200000: 4, 300000: 6, 600000: 8}
pago_total = 900000
tasa_interes = 0.04

fecha_pago_calculator = Punto2FechaPago(documentos, pago_total, tasa_interes)

n_aproximado = fecha_pago_calculator.newton_raphson(10)

dias_exactos = fecha_pago_calculator.calcular_dias_exactos(n_aproximado)

print("El número de meses en que se debe realizar el pago es:", n_aproximado)
print("Exactamente es en", dias_exactos, "días.")
'''

    codec = '''
class Punto3DeudaPablo:
    def __init__(self, tasa_interes):
        self.tasa_interes = tasa_interes

    def calcular_valor_presente(self):
        VP = 50000  + \
             200000 / ((1 + self.tasa_interes) ** 5) + \
             350000 / ((1 + self.tasa_interes) ** 8)
        return VP

    def newton_raphson(self, x0, tol=1e-6, max_iter=100):
        """
        Método de Newton-Raphson para encontrar la raíz de la ecuación.
        """
        x = x0
        for _ in range(max_iter):
            f_x = self.calcular_valor_presente() - x * (
                1 / ((1 + self.tasa_interes) ** 6) + 1 / ((1 + self.tasa_interes) ** 12))
            f_prime_x = - (1 / ((1 + self.tasa_interes) ** 6) + 1 / ((1 + self.tasa_interes) ** 12))
            x_next = x - f_x / f_prime_x
            if abs(x_next - x) < tol:
                return x_next
            x = x_next
        raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones".format(max_iter))

tasa_interes_mensual = 0.03
deuda_pablo = Punto3DeudaPablo(tasa_interes=tasa_interes_mensual)

VP = deuda_pablo.calcular_valor_presente()

x0 = VP / 2
valor_pagos_iguales = deuda_pablo.newton_raphson(x0)

print("El valor de los dos pagos iguales que Pablo debe realizar es:", valor_pagos_iguales)
'''

    if page == a:
        st.markdown(filea)
        st.code(codea, language='python')

    elif page == b:
        st.markdown(fileb)
        st.code(codeb, language='python')

    elif page == c:
        st.markdown(filec)
        st.code(codec, language='python')