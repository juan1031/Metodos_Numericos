import numpy as np
from src.MetodosNumericos import MetodosNumericos
import streamlit as st


class RegressionMetrics:
    def __init__(self, data, var_objetivo):
        self.data = data.copy()
        self.var_objetivo = var_objetivo

    def fit(self):
        # intersección
        intercept = np.ones((len(self.data), 1))
        self.data['intercept'] = intercept

        # Separar las variables independientes (X) de la variable dependiente (y)
        X = self.data.drop(self.var_objetivo, axis=1)
        y = self.data[self.var_objetivo]

        # Calcular la matriz de diseño
        A = X.T.dot(X)
        b = X.T.dot(y)

        # Aplicar el método de Gauss
        mn = MetodosNumericos()
        self.coefs = mn.backward_substi(mn.Gauss(A.to_numpy(), b.to_numpy())[
                                        0], mn.Gauss(A.to_numpy(), b.to_numpy())[1])

        # Calcular los nombres de las variables
        self.variable_names = X.columns.tolist()

        # Calcular las predicciones
        self.predicted_y = X.dot(self.coefs)

        # Calcular los residuos
        self.residuals = y - self.predicted_y

        # Calcular el Total Sum of Squares (TSS)
        self.TSS = np.sum((y - np.mean(y)) ** 2)

        # Calcular el Residual Sum of Squares (RSS)
        self.RSS = np.sum(self.residuals ** 2)

        # Calcular R-squared
        self.R_squared = 1 - (self.RSS / self.TSS)

        # Calcular los errores estándar
        n = len(self.data)
        p = len(self.coefs)
        X_matrix = X.to_numpy()
        sigma_squared = self.RSS / (n - p)
        var_cov_matrix = np.linalg.inv(A) * sigma_squared
        self.standard_errors = np.sqrt(np.diag(var_cov_matrix))

    def display_metrics(self):
        # Display the results using Streamlit
        st.text("=" * 54)
        st.text("{:<12} {:>20} {:>20}".format(
            "Variable", "Coef", "Standard Error"))
        st.text("-" * 54)

        for name, coef, error in zip(self.variable_names, self.coefs, self.standard_errors):
            st.text("{:<12} {:>20.15f} {:>20.15f}".format(name, coef, error))

        st.text("=" * 54)
        st.text("R-squared: {}".format(self.R_squared))
