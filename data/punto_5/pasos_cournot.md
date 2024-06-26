###  Así fue como se calcularon los $q_1$ y $q_2$ óptimos:

#### Paso 1:
Definir la ecuación que representa la condición de estacionaridad para cada empresa

$f_1(q) = (q_1 + q_2)^{-1/γ} - \frac{1}{γ}(q_1 + q_2)^{-(1+1/γ)} q_1- \frac{1}{2}c_1 = 0$

$f_2(q) = (q_1 + q_2)^{-1/γ} - \frac{1}{γ}(q_1 + q_2)^{-(1+1/γ)} q_2- \frac{1}{2}c_2 = 0$

#### Paso 2:

Luego se debe calcular las derivadas parciales de $f_1$ y $f_2$ con respecto a $q_1$ y $q_2$

$\frac{\partial f_1}{\partial q_1}= -q_1\left(-1 - \frac{1}{γ}\right)\left((q_1 + q_2)^{-1 - \frac{1}{γ}}\right)\left(\frac{1}{γ(q_1 + q_2)}\right) - \frac{(q_1 + q_2)^{-1 - \frac{1}{γ}}}{γ} - \frac{1}{γ(q_1 + q_2)(q_1 + q_2)^{\frac{1}{γ}}}$

$\frac{\partial f_1}{\partial q_2}= -q_1\left(-1 - \frac{1}{γ}\right)\left((q_1 + q_2)^{-1 - \frac{1}{γ}}\right)\left(\frac{1}{γ(q_1 + q_2)}\right) - \frac{1}{γ(q_1 + q_2)(q_1 + q_2)^{\frac{1}{γ}}}$

$\frac{\partial f_2}{\partial q_1}= -q_2\left(-1 - \frac{1}{γ}\right)\left((q_1 + q_2)^{-1 - \frac{1}{γ}}\right)\left(\frac{1}{γ(q_1 + q_2)}\right) - \frac{1}{γ(q_1 + q_2)(q_1 + q_2)^{\frac{1}{γ}}}$

$\frac{\partial f_2}{\partial q_2}= -q_2\left(-1 - \frac{1}{γ}\right)\left((q_1 + q_2)^{-1 - \frac{1}{γ}}\right)\left(\frac{1}{γ(q_1 + q_2)}\right) - \frac{(q_1 + q_2)^{-1 - \frac{1}{γ}}}{γ} - \frac{1}{γ(q_1 + q_2)(q_1 + q_2)^{\frac{1}{γ}}}$

#### Paso 3:

Para encontrar los puntos óptimos, necesitamos calcular las raíces de las funciones $f_1$ y $f_2$. Para esto, empleamos el método de Newton bivariado. En cada paso de este método, evaluamos las funciones y sus derivadas en los valores actuales de q1 y q2 (inicialmente asignados como supuestos). Luego, ajustamos estos valores en el método y así, hasta que alcancemos una convergencia dentro de una tolerancia predefinida o lleguemos al número máximo de iteraciones permitidas.


