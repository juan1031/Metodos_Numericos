import numpy as np
from scipy.sparse import csc_matrix
import math


class MetodosNumericos:

    def __init__(self, f=None, f_prima=None):
        """
        Inicializa la clase con la función objetivo y su derivada (si es necesario).

        Parameteros:
        - f: Función la cual se calculará la raíz.
        - f_prima: Derivada de la función (opcional, solo necesario para el método de Newton).
        """
        self.f = f
        self.f_prima = f_prima

    @staticmethod
    def matriz_singular(matriz):
        return "La matriz es singular" if np.linalg.det(matriz) == 0 else "La matriz no es singular"

    def biseccion(self, a, b, tol=1e-6):
        """
        Método de bisección para encontrar la raíz de la función en el intervalo [a, b].

        Parameters:
        - a: Extremo izquierdo del intervalo.
        - b: Extremo derecho del intervalo.
        - tol: Tolerancia, criterio de parada del algoritmo.

        Returns:
        - La raíz encontrada.
        """
        fa, fb = self.f(a), self.f(b)

        while abs(a - b) > tol:
            x_med = (a + b) / 2
            f_med = self.f(x_med)

            if f_med == 0:
                return x_med
            elif fa * f_med > 0:
                a, fa = x_med, f_med
            else:
                b, fb = x_med, f_med

        return (a + b) / 2

    def secante(self, p0, p1, tol=1e-6, max_iter=100):
        """
        Método de la secante para encontrar la raíz de la función.

        Parameters:
        - p0: Primer punto inicial.
        - p1: Segundo punto inicial.
        - tol: Tolerancia, criterio de parada del algoritmo.
        - max_iter: Número máximo de iteraciones permitidas.

        Returns:
        - La raíz encontrada.
        """
        for i in range(max_iter):
            f0, f1 = self.f(p0), self.f(p1)
            if f0 == f1:
                raise ValueError(
                    'La función produce la misma salida para los dos puntos iniciales')
            p2 = (p0 * f1 - p1 * f0) / (f1 - f0)
            if abs(p2 - p1) < tol:
                return p2
            p0, p1 = p1, p2
        raise ValueError(
            'El método no convergió después de {} iteraciones'.format(max_iter))

    def newton(self, p0, tol=1e-6, max_iter=100):
        """
        Método de Newton para encontrar la raíz de la función.

        Parameters:
        - p0: Punto inicial.
        - tol: Tolerancia, criterio de parada del algoritmo.
        - max_iter: Número máximo de iteraciones permitidas.

        Returns:
        - La raíz encontrada.
        """
        for i in range(max_iter):
            p1 = p0 - self.f(p0) / self.f_prima(p0)
            if abs(p1 - p0) < tol:
                return p1
            p0 = p1
        raise ValueError(
            'El método no convergió después de {} iteraciones'.format(max_iter))

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
