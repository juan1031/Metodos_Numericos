
# **¿Qué es la Competencia de Cournot?**

La competencia de Cournot es un modelo de mercado de oligopolio donde dos o más empresas producen el mismo producto y compiten por su cuota de mercado. En este modelo, las empresas deciden simultánea e independientemente la cantidad del producto que generarán, lo que determina el precio de mercado total.

## **Contexto Teórico:**

- **Ley de la Demanda:** Existe una relación inversa entre la cantidad y el precio en el mercado. A medida que aumenta la producción, los precios tienden a ser más bajos, y viceversa.
- **Supuestos Principales:**
  - Un número fijo de empresas en el mercado, todas con poder de mercado.
  - Todos los bienes producidos son homogéneos, es decir, son idénticos desde la perspectiva del consumidor.
  - Competencia basada en la cantidad producida, no en los precios.
  - Cada empresa toma decisiones estratégicas considerando las acciones de su competencia.
  - Las decisiones de producción se toman simultáneamente, sin cooperación entre empresas.

## **Problema Propuesto:**

El problema es calcular un equilibrio de Cournot para un duopolio, donde dos empresas compiten por maximizar sus beneficios. Cada empresa debe encontrar la cantidad óptima de producción que maximice su beneficio neto, considerando la relación entre producción, precio y costos.

### **Funciones de Costos:**

Cada empresa tiene una función de costos, representada por $ C_i(q_i) = \frac{1}{2} c_i q_i $, donde $ c_i $ representa el costo marginal de la empresa $ i $.


### **Función de Demanda Inversa:**

La función de demanda inversa para el mercado total está representada por $ P(q) = q^{-1/γ} $, donde $ γ $ es un parámetro que indica la elasticidad de la demanda.

### **Ecuaciones de Equilibrio:**

Para encontrar el equilibrio de Cournot, se deben satisfacer las siguientes ecuaciones de optimización de beneficios para cada empresa:

\[
\begin{align*}
f_1(q) &= (q_1 + q_2)^{-1/γ} - \frac{1}{γ}(q_1 + q_2)^{-(1+1/γ)} - c_1q_1 = 0 \\
f_2(q) &= (q_1 + q_2)^{-1/γ} - \frac{1}{γ}(q_1 + q_2)^{-(1+1/γ)} - c_2q_2 = 0
\end{align*}
\]

Para resolver este problema mediante el método de Newton, se requiere una función que calcule tanto la función misma como el jacobiano.

### **Parámetros dados para el ejemplo:**

$γ = 0.6 $, $c_1 = 0.6 $ y $c_2 = 0.8 $.
