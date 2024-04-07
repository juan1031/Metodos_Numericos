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
        if np.linalg.det(matriz) == 0:
            return "La matriz es singular"
        return "La matriz no es singular"

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
        x_med = (a+b)/2
        fa = self.f(a)
        fb = self.f(b)
        f_med = self.f(x_med)

        while abs(a - b) > tol:

            if f_med == 0:
                return x_med
            elif fa * f_med > 0:
                a, fa = x_med, f_med
            else:
                b, fb = x_med, f_med

            x_med = (a + b) / 2
            f_med = self.f(x_med)

        return x_med

    def secante(self, p0, p1, tol=1e-6):
        """
        Método de la secante para encontrar la raíz de la función.

        Parameters:
        - p0: Primer punto inicial.
        - p1: Segundo punto inicial.
        - tol: Tolerancia, criterio de parada del algoritmo.

        Returns:
        - La raíz encontrada.
        """
        f0 = self.f(p0)
        f1 = self.f(p1)
        i = 0

        while True:
            i += 1

            if f0 == f1:
                print('Divide por 0')
                break

            p2 = (p0 * f1 - p1 * f0) / (f1 - f0)
            f2 = self.f(p2)

            if abs(f2) < tol:
                print(f'La raíz está en: {p2}')
                break
            else:
                p0, p1, f0, f1 = p1, p2, f1, f2

        print(f'Iteraciones: {i}')

    def newton(self, p0, tol=1e-6):
        """
        Método de Newton para encontrar la raíz de la función.

        Parameteros:
        - p0: Punto inicial.
        - tol: Tolerancia, criterio de parada del algoritmo.

        Returnos:
        - La raíz encontrada.
        """
        while True:
            p1 = p0 - self.f(p0) / self.f_prima(p0)
            f1 = self.f(p1)

            if abs(f1) < tol:
                print(f'La raíz está en: {p1}')
                break
            p0 = p1

    def diagonal(A, b):
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

    def forward_substi(L, b):
        'Recibe una matriz Low triangular y un vector b del sistema Ax=b'
        z = np.empty(L.shape[0])
        z[0] = b[0]/L[0, 0]
        for i in range(1, L.shape[0]):
            suma = 0
            for j in range(i):
                suma = suma + L[i, j]*z[j]  # esto se puede vectorizar
            z[i] = (b[i]-suma)/L[i, i]
        return z

    def Gauss(A, b):
        for colum in range(A.shape[0]):
            for fila in range(colum+1, A.shape[0]):
                multip = A[fila, colum]/A[colum, colum]
                A[fila, :] = A[fila, :] - A[colum, :]*multip
                b[fila] = b[fila]-b[colum]*multip
        return A, b

    def backward_substi(U, z):
        'Recibe una matriz Upper triangular y un vector z'
        v = np.empty(U.shape[0])
        v[-1] = z[-1]/U[-1, -1]
        for i in range(U.shape[0]-2, -1, -1):
            suma = 0
            for j in range(U.shape[0]-1, i, -1):
                suma = suma + U[i, j]*v[j]
            v[i] = (z[i]-suma)/U[i, i]
        return v

    def Cholesky(A):
        'Return matrix L (lower triangular) decomposition of A'
        n = A.shape[0]
        L = np.zeros_like(A)
        for i in range(n):
            for j in range(i+1):
                suma = 0
                for k in range(j):
                    suma += L[i, k] * L[j, k]
                if i == j:
                    L[i, j] = np.sqrt(A[i, i] - suma)
                else:
                    L[i, j] = (A[i, j] - suma) / L[j, j]
        return L

    def Doolittle(A):
        n = A.shape[0]
        L = np.eye(n)
        U = np.zeros_like(A)
        for i in range(n):
            for j in range(i, n):
                suma = 0
                for k in range(i):
                    suma += (L[i, k] * U[k, j])
                U[i, j] = A[i, j] - suma
            for j in range(i+1, n):
                suma = 0
                for k in range(i):
                    suma += (L[j, k] * U[k, i])
                L[j, i] = (A[j, i] - suma) / U[i, i]
        return U, L

    def sumaGramm(A, m, x):
        suma = 0.0
        for k in range(m):
            suma = suma + A[k][x]*A[k][x]
        return suma

    def productoGramm(A, m, x, y):
        producto = 0.0
        for k in range(m):
            producto = producto + (A[k][x]*A[k][y])
        return producto

    def metodoGramm(A, b, n):
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
                U[i][j] = productoGramm(E, n, i, j)
                for k in range(n):
                    E[k][j] = E[k][j] - U[i][j]*E[k][i]
            U[j][j] = math.sqrt(sumaGramm(E, n, j))
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


class MetodosNumericos_v2:

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

    def diagonal(A, b):
        if A.shape[0] == A.shape[1]:
            diag = np.diag(A)
            if 0 in diag:
                return "La matriz es singular"
            else:
                return np.divide(b, diag)

    def forward_substi(L, b):
        z = np.empty(L.shape[0])
        z[0] = b[0] / L[0, 0]
        for i in range(1, L.shape[0]):
            z[i] = (b[i] - np.dot(L[i, :i], z[:i])) / L[i, i]
        return z

    def backward_substi(U, z):
        v = np.empty(U.shape[0])
        v[-1] = z[-1] / U[-1, -1]
        for i in range(U.shape[0] - 2, -1, -1):
            v[i] = (z[i] - np.dot(U[i, i:], v[i:])) / U[i, i]
        return v

    def Gauss(A, b):
        for colum in range(A.shape[0]):
            for fila in range(colum + 1, A.shape[0]):
                multip = A[fila, colum] / A[colum, colum]
                A[fila, :] -= A[colum, :] * multip
                b[fila] -= b[colum] * multip
        return A, b

    def Cholesky(A):
        n = A.shape[0]
        L = np.zeros_like(A)
        for i in range(n):
            for j in range(i+1):
                suma = np.dot(L[i, :j], L[j, :j])
                if i == j:
                    L[i, j] = np.sqrt(A[i, i] - suma)
                else:
                    L[i, j] = (A[i, j] - suma) / L[j, j]
        return L

    def Doolittle(A):
        n = A.shape[0]
        L = np.eye(n)
        U = np.zeros_like(A)
        for i in range(n):
            for j in range(i, n):
                suma = np.dot(L[i, :i], U[:i, j])
                U[i, j] = A[i, j] - suma
            for j in range(i+1, n):
                suma = np.dot(L[j, :i], U[:i, i])
                L[j, i] = (A[j, i] - suma) / U[i, i]
        return U, L

    def sumaGramm(A, m, x):
        suma = 0.0
        for k in range(m):
            suma = suma + A[k][x]*A[k][x]
        return suma

    def productoGramm(A, m, x, y):
        producto = 0.0
        for k in range(m):
            producto = producto + (A[k][x]*A[k][y])
        return producto

    def metodoGramm(A, b, n):
        E = np.array([A[i] for i in range(n)])
        U = np.zeros((n, n))

        for j in range(n):
            for k in range(n):
                E[k][j] = A[k][j]
            for i in range(j):
                producto = MetodosNumericos.productoGramm(E, n, i, j)
                U[i][j] = producto
                for k in range(n):
                    E[k][j] = E[k][j] - U[i][j]*E[k][i]
            U[j][j] = math.sqrt(MetodosNumericos.sumaGramm(E, n, j))
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
