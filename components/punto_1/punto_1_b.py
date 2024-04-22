import streamlit as st
import numpy as np
import math

def punto_1_b():
    codeb = '''
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

st.write("El número de meses en que se debe realizar el pago es:", n_aproximado) 
st.write("Exactamente es en", dias_exactos, "días.") 
    '''

    with st.echo():
        exec(codeb)


