import sympy as sp

class NewtonMethod:
    def __init__(self, gamma, c1, c2, tol=1e-6, max_iter=100):
        self.gamma = gamma
        self.c1 = c1
        self.c2 = c2
        self.tol = tol
        self.max_iter = max_iter
        
        # Definir los símbolos q1 y q2
        self.q1, self.q2 = sp.symbols('q1 q2')
        
        # Definir las funciones f1 y f2
        self.f1 = ((self.q1 + self.q2)**(-1/self.gamma)) - (1/self.gamma)*((self.q1 + self.q2)**((-1/self.gamma)-1))*self.q1 - (1/2)*self.c1
        self.f2 = ((self.q1 + self.q2)**(-1/self.gamma)) - (1/self.gamma)*((self.q1 + self.q2)**((-1/self.gamma)-1))*self.q2 - (1/2)*self.c2
        
        # Calcular las derivadas parciales de f1 y f2
        self.df1_q1 = sp.diff(self.f1, self.q1)
        self.df1_q2 = sp.diff(self.f1, self.q2)
        self.df2_q1 = sp.diff(self.f2, self.q1)
        self.df2_q2 = sp.diff(self.f2, self.q2)
        
    def solve(self, q1_initial, q2_initial):
        q1 = q1_initial
        q2 = q2_initial
        iter_count = 0
        
        while True:
            f1_val = self.f1.subs({self.q1: q1, self.q2: q2})
            f2_val = self.f2.subs({self.q1: q1, self.q2: q2})
            
            # Verificar la condición de convergencia
            if abs(f1_val) < self.tol and abs(f2_val) < self.tol:
                return max(q1, 0), max(q2, 0)
            
            # Calcular el paso de Newton
            J = sp.Matrix([[self.df1_q1.subs({self.q1: q1, self.q2: q2}), self.df1_q2.subs({self.q1: q1, self.q2: q2})],
                           [self.df2_q1.subs({self.q1: q1, self.q2: q2}), self.df2_q2.subs({self.q1: q1, self.q2: q2})]])
            
            delta_q = J.inv() * sp.Matrix([[-f1_val], [-f2_val]])
            
            # Actualizar las variables q1 y q2
            q1 += delta_q[0]
            q2 += delta_q[1]
            
            # Proyectar a no negatividad
            q1 = max(q1, 0)
            q2 = max(q2, 0)
            
            iter_count += 1
            
            if iter_count >= self.max_iter:
                raise RuntimeError(f"El método de Newton no converge después de {self.max_iter} iteraciones.")

