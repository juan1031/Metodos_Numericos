import streamlit as st
import numpy as np


def punto_1_a():

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
    valor_presente = vp_calculator.newton_raphson(P0)

    print("Valor presente (P):", valor_presente)
        '''

    with st.echo():
            exec(codea)
