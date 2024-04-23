import numpy as np
from scipy.sparse import csc_matrix
import math
import sympy as sp
import time
import plotly.graph_objects as go


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Tiempo de ejecución de {func.__name__}: {execution_time:.6f} segundos")
        return result
    return wrapper


def check_diagonal_dominance(func):
    def wrapper(*args, **kwargs):
        A = args[1]
        n = A.shape[0]
        for i in range(n):
            if np.abs(A[i, i]) < np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
                raise ValueError("La matriz A no es diagonalmente dominante.")
        return func(*args, **kwargs)
    return wrapper


class MetodosNumericos:

    def __init__(self, f=None, f_prima=None, cournot_duopolio=None, matriz_jacobiana=None):
        """
        Inicializa la clase con la función objetivo y su derivada (si es necesario).

        Parameteros:
        - f: Función la cual se calculará la raíz.
        - f_prima: Derivada de la función (opcional, solo necesario para el método de Newton).
        """
        self.f = f
        self.f_prima = f_prima
        self.cournot_duopolio = cournot_duopolio
        self.matriz_jacobiana = matriz_jacobiana

    def calcular_tiempo_ejecucion(self, metodo, *args, **kwargs):
        start_time = time.time()
        resultado = metodo(*args, **kwargs)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
        return resultado, tiempo_ejecucion

    def calcular_error_relativo(self, aproximacion, valor_exacto):
        if valor_exacto == 0 and aproximacion == 0:
            return 0
        elif valor_exacto <= 1e-10:
            return 0
        error_relativo = np.abs((aproximacion-valor_exacto)/valor_exacto)
        return error_relativo

    @staticmethod
    def derivada(f):
        x = sp.Symbol('x')
        derivada = sp.diff(f(x), x)
        return derivada

    @staticmethod
    def matriz_singular(matriz):
        return "La matriz es singular" if np.linalg.det(matriz) == 0 else "La matriz no es singular"

    def plot_function(self, intervalo_x=None):

        func = self.f
        if intervalo_x is None:
            x_values = np.linspace(-10, 10, 1000)
        else:
            x_values = np.linspace(intervalo_x[0], intervalo_x[1], 1000)
        y_values = func(x_values)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Función',
                                 line=dict(color='blue', width=2)))

        fig.update_layout(
            width=450,
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            xaxis_ticks='outside',
            yaxis_ticks='outside',
            xaxis_linecolor='black',
            yaxis_linecolor='black',
            xaxis_gridcolor='rgba(255, 255, 255, 0.1)',
            yaxis_gridcolor='rgba(255, 255, 255, 0.1)'
        )

        return fig

    def comparar_metodos(self, intervalo_biseccion, intervalo_secante, p0_newton, tolerancia, max_iter):
        """
        Compara los métodos de bisección, secante y Newton para encontrar la raíz de la función.

        Parameters:
        - intervalo_biseccion: Tupla que representa el intervalo inicial para el método de bisección.
        - intervalo_secante: Tupla que representa el intervalo inicial para el método de la secante.
        - p0_newton: Punto inicial para el método de Newton.
        - tolerancia: Tolerancia para el criterio de parada de los métodos.
        - max_iter: Número máximo de iteraciones permitidas.

        Returns:
        - resultado_biseccion: Raíz encontrada por el método de bisección.
        - tiempo_biseccion: Tiempo de ejecución del método de bisección.
        - resultado_secante: Raíz encontrada por el método de la secante.
        - tiempo_secante: Tiempo de ejecución del método de la secante.
        - resultado_newton: Raíz encontrada por el método de Newton.
        - tiempo_newton: Tiempo de ejecución del método de Newton.
        """
        # Método de bisección
        resultado_biseccion, tiempo_biseccion = self.calcular_tiempo_ejecucion(
            self.biseccion, intervalo_biseccion[0], intervalo_biseccion[1], tolerancia, max_iter)

        # Método de la secante
        resultado_secante, tiempo_secante = self.calcular_tiempo_ejecucion(
            self.secante, intervalo_secante[0], intervalo_secante[1], tolerancia, max_iter)

        # Método de Newton
        resultado_newton, tiempo_newton = self.calcular_tiempo_ejecucion(
            self.newton, p0_newton, tolerancia, max_iter)

        return resultado_biseccion, tiempo_biseccion, resultado_secante, tiempo_secante, resultado_newton, tiempo_newton

    def biseccion(self, a, b, tol=1e-6, max_iter=100):
        """
        Método de bisección para encontrar la raíz de la función en el intervalo [a, b].
        """
        aproximaciones = []
        fa = self.f(a)
        fb = self.f(b)

        iter_count = 0  # Contador de iteraciones

        while abs(a - b) > tol and iter_count < max_iter:
            x_med = (a + b) / 2
            aproximaciones.append(x_med)
            f_med = self.f(x_med)

            if f_med == 0:
                return x_med, 0 if iter_count == 0 else self.calcular_error_relativo(aproximaciones[-2], aproximaciones[-1])
            elif fa * f_med > 0:
                a, fa = x_med, f_med
            else:
                b = x_med
                fb = f_med

            iter_count += 1  # Incrementar el contador de iteraciones

        return (a + b) / 2, self.calcular_error_relativo(aproximaciones[-2], aproximaciones[-1])

    def secante(self, p0, p1, tol=1e-6, max_iter=100):
        """
        Método de la secante para encontrar la raíz de la función.
        """
        aproximaciones = [p0, p1]
        for i in range(max_iter):
            f0, f1 = self.f(p0), self.f(p1)
            if f0 == f1:
                raise ValueError(
                    'La función produce la misma salida para los dos puntos iniciales')
            p2 = (p0 * f1 - p1 * f0) / (f1 - f0)
            aproximaciones.append(p2)
            if abs(p2 - p1) < tol:
                return p2, self.calcular_error_relativo(aproximaciones[-2], aproximaciones[-1])
            p0, p1 = p1, p2
        raise ValueError(
            'El método no convergió después de {} iteraciones'.format(max_iter))

    def newton(self, p0, tol=1e-6, max_iter=100):
        """
        Método de Newton para encontrar la raíz de la función.
        """
        aproximaciones = [p0]
        for i in range(max_iter):
            p1 = p0 - self.f(p0) / self.f_prima(p0)
            aproximaciones.append(p1)
            if abs(p1 - p0) < tol:
                return p1, self.calcular_error_relativo(aproximaciones[-2], aproximaciones[-1])
            p0 = p1
        raise ValueError(
            'El método no convergió después de {} iteraciones'.format(max_iter))

    def newton_multivariable(self, p0, c1, c2, gamma, tol=1e-6, max_iter=100):
        """
        Método de Newton para encontrar las raíces de un sistema de ecuaciones.
        """
        aproximaciones = [p0]
        for i in range(max_iter):
            # Calculamos el valor del sistema de ecuaciones en el punto actual
            f_value = np.array(self.cournot_duopolio(*p0, c1, c2, gamma))

            # Si el valor es lo suficientemente cercano a cero, terminamos
            if np.all(np.abs(f_value) < tol):
                return p0, np.array(aproximaciones)

            # Calculamos la matriz jacobiana en el punto actual
            J_value = self.matriz_jacobiana(*p0, c1, c2, gamma)

            # Calculamos el siguiente paso utilizando la fórmula de Newton-Raphson para sistemas
            p1 = p0 - np.linalg.inv(J_value) @ f_value

            aproximaciones.append(p1)

            # Si la norma de la diferencia entre p1 y p0 es menor que la tolerancia, terminamos
            if np.linalg.norm(p1 - p0) < tol:
                return p1, np.array(aproximaciones)

            p0 = p1
        raise ValueError(
            'El método no convergió después de {} iteraciones'.format(max_iter))

    # def punto_fijo(self, p0, tol=1e-6, max_iter=100):
    #     """
    #     Método de punto fijo para encontrar la raíz de la función.

    #     Parameters:
    #     - p0: Punto inicial.
    #     - tol: Tolerancia, criterio de parada del algoritmo.
    #     - max_iter: Número máximo de iteraciones permitidas.

    #     Returns:
    #     - La raíz encontrada.
    #     """

    #     for i in range(max_iter):
    #         p1 = self.f(p0)
    #         if abs(p1 - p0) < tol:
    #             return p1
    #         p0 = p1
    #     raise ValueError(
    #         'El método no convergió después de {} iteraciones'.format(max_iter))

    def diagonal(self, A, b):
        if A.shape[0] == A.shape[1]:
            for i in range(A.shape[0]):
                if A[i, :].dot(A[i, :]).sum() != A[i, i]**2:
                    print('La matriz no es diagonal')
                    break
                elif A[i, i] == 0:
                    print('Es singular')
                    break
                else:
                    x = []
                    for j in range(A.shape[0]):
                        x.append(b[j]/A[j, j])
                    return x

    def forward_substi(self, L, b):
        'Recibe una matriz Low triangular y un vector b del sistema Ax=b'
        z = np.empty(L.shape[0])
        z[0] = b[0]/L[0, 0]
        for i in range(1, L.shape[0]):
            suma = 0
            for j in range(i):
                suma = suma + L[i, j]*z[j]  # esto se puede vectorizar
            z[i] = (b[i]-suma)/L[i, i]
        return z

    def Gauss(self, A, b):
        for colum in range(A.shape[0]+1):
            for fila in range(colum+1, A.shape[0]):
                multip = A[fila, colum]/A[colum, colum]
                A[fila, :] = A[fila, :] - A[colum, :]*multip
                b[fila] = b[fila]-b[colum]*multip
        return [A, b]

    def backward_substi(self, U, z):
        'Recibe una matriz Upper triangular y un vector z'
        v = np.empty(U.shape[0])
        v[-1] = z[-1]/U[-1, -1]
        for i in range(U.shape[0]-2, -1, -1):
            suma = 0
            for j in range(U.shape[0]-1, i, -1):
                suma = suma + U[i, j]*v[j]
            v[i] = (z[i]-suma)/U[i, i]
        return v

    def Cholesky(self, A):
        'Return matrix L (lower triangular) decomposition of A'
        Q = csc_matrix(A.shape)
        Q[0, 0] = np.sqrt(A[0, 0])
        for i in range(A.shape[0]):
            for j in range(A.shape[0]):
                if i < j:
                    if i == 0:
                        Q[j, i] = A[i, j]/Q[i, i]
                    else:
                        suma = 0
                        for r in range(i):
                            suma = suma + Q[i, r]*Q[j, r]
                        Q[j, i] = (A[i, j]-suma)/Q[i, i]
                elif i == j:
                    suma = 0
                    for r in range(i):
                        suma = suma + Q[i, r]**2
                    Q[i, j] = np.sqrt(A[i, j]-suma)
        return Q

    def Doolittle(self, A):
        U = csc_matrix(A.shape)
        L = csc_matrix(A.shape)
        L[0, 0] = 1
        for i in range(A.shape[0]):
            for j in range(A.shape[0]):
                if i == 0:
                    U[i, j] = A[i, j]
                elif i > j:
                    suma = 0
                    for r in range(j):
                        suma = suma + L[i, r]*U[r, j]
                    L[i, j] = (A[i, j] - suma)/U[j, j]
                elif i == j:
                    L[i, j] = 1
                    suma = 0
                    for r in range(i):
                        suma = suma + L[i, r]*U[r, j]
                    U[i, j] = A[i, j] - suma
                else:
                    suma = 0
                    for r in range(i):
                        suma = suma + L[i, r]*U[r, j]
                    U[i, j] = A[i, j] - suma
        return (U, L)

    def sumaGramm(self, A, m, x):
        suma = 0.0
        for k in range(m):
            suma = suma + A[k][x]*A[k][x]
        return suma

    def productoGramm(self, A, m, x, y):
        producto = 0.0
        for k in range(m):
            producto = producto + (A[k][x]*A[k][y])
        return producto

    def metodoGramm(self, A, b, n):
        # La matriz A es mxn por tanto la matriz E sera de orden mxn y U nxn

        # Creamos matriz E
        E = []
        for i in range(n):
            E.append([0]*n)
        # Creamos matriz U
        U = []
        for i in range(n):
            U.append([0]*n)

        # Algoritmo
        for j in range(n):
            for k in range(n):
                E[k][j] = A[k][j]
            for i in range(j):
                producto = 0.0
                U[i][j] = self.productoGramm(E, n, i, j)
                for k in range(n):
                    E[k][j] = E[k][j] - U[i][j]*E[k][i]
            U[j][j] = math.sqrt(self.sumaGramm(E, n, j))
            for k in range(n):
                E[k][j] = E[k][j]/U[j][j]

        y = np.linalg.solve(E, b)
        x = np.linalg.solve(U, y)

        Q = np.array(E, float)
        R = np.array(U, float)

        print("Al finalizar el algoritmo tendremos:\n")
        print('Matriz Q:\n', Q.round(7))
        print('\nMatriz R:\n', R.round(7))

        return Q, R

    # Ayuda: https://en.wikipedia.org/wiki/Jacobi_method
    # @check_diagonal_dominance
    @calculate_time
    def jacobi(self, A, b, x=None, max_iter=1000, tolerance=1e-10):
        n = A.shape[0]
        if x is None:
            x = np.zeros(n)
        for _ in range(max_iter):
            x_new = np.zeros(n)
            for i in range(n):
                s1 = np.dot(A[i, :i], x[:i])
                s2 = np.dot(A[i, i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]
            if np.allclose(x, x_new, atol=tolerance, rtol=0.):
                break
            x = x_new
        error = np.dot(A, x) - b
        return x, np.dot(A, x), error

    # Ayuda: http://blog.espol.edu.ec/analisisnumerico/gauss-seidel-ejemplo01/
    # @check_diagonal_dominance
    @calculate_time
    def gauss_seidel(self, A, b, x=None, max_iter=1000, tolerance=1e-10):
        n = A.shape[0]
        if x is None:
            x = np.zeros(n)
        for _ in range(max_iter):
            for i in range(n):
                suma = np.dot(A[i, :i], x[:i]) + \
                    np.dot(A[i, i + 1:], x[i + 1:])
                x[i] = (b[i] - suma) / A[i, i]
            if np.allclose(A @ x, b, atol=tolerance, rtol=0.):
                break
        error = np.dot(A, x) - b
        return x, np.dot(A, x), error

    def gradient_descent(self, x0, learning_rate, tol=1e-5, max_iter=1000):
        """
        Gradient descent optimization algorithm.

        Parameters:
        - f: Function to minimize.
        - f_prime: Derivative of the function.
        - x0: Initial guess for the minimum.
        - learning_rate: Step size for the gradient descent.
        - tol: Tolerance for convergence.
        - max_iter: Maximum number of iterations.

        Returns:
        - x_min: Minimum of the function.
        - f_min: Minimum value of the function.
        - iterations: Number of iterations performed.
        """
        x = x0
        iterations = 0
        while True:
            grad = self.f_prima(x)
            x_new = x - learning_rate * grad
            if np.abs(x_new - x) < tol or iterations >= max_iter:
                break
            x = x_new
            iterations += 1
        return x, self.f(x), iterations
