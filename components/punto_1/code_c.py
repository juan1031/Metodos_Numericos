import streamlit as st


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

st.write("El valor de los dos pagos iguales que Pablo debe realizar es:", valor_pagos_iguales)