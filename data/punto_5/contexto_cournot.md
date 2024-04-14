
## **¿Qué es la Competencia de Cournot?**

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

Se busca encontrar la cantidad de producción óptima para dos firmas, de manera que ninguna tenga incentivos para cambiar su producción. Cada empresa enfrenta el dilema de que aumentar su producción puede incrementar sus ingresos al vender más, pero también puede reducir los precios debido a una mayor oferta en el mercado. Por lo tanto, el objetivo es determinar las cantidades de producción que maximicen el beneficio neto, considerando la relación entre producción, precio y costos.

- ### **Funciones de Costos:**

Cada empresa tiene una función de costos, representada por $ C_i(q_i) = \frac{1}{2} c_i q_i $, donde $ c_i $ representa el costo marginal de la empresa $ i $.

- ### **Función de Demanda Inversa:**

$ P(q) = q^{-1/γ} $, esta función produce el precio de mercado, dada la oferta conjunta $q = q_1 +q_2$, donde $ γ $ es un parámetro que indica como reacciona la demanda del mercado a cambios en la cantidad total producida por ambas empresas. 

- ### **Función de Beneficio:**

La ecuación de beneficio para una empresa en particular se deriva de la función de ingresos totales y la función de costos totales. 

$\pi_i =  P(q)*q_i - C_i(q_i) $

es decir 

$\pi_i = (q_1 +q_2)^{-1/γ} - \frac{1}{2}c_i q_i $

- ### **Condición de Estacionariedad**

Se refiere a un equilibrio en el cual ninguna de las empresas tiene incentivos para cambiar su nivel de producción, dado el nivel de producción de las demás empresas en el mercado. Este equilibrio se alcanza cuando las empresas están maximizando sus beneficios con respecto a la cantidad producida. En términos matemáticos, la condición de estacionaridad se puede expresar como el punto en el cual la derivada del beneficio de cada empresa con respecto a su nivel de producción es igual a cero, es decir, donde la función de beneficio alcanza un máximo o un mínimo. Y esta representada como:

$f_i(q) = (q_1 + q_2)^{-1/γ} - \frac{1}{γ}(q_1 + q_2)^{-(1/γ+1)} q_i-\frac{1}{2}c_i  = 0$

Para resolver el problema, se crea una función que recibe como parámetros la funcion de costos de cada una de las empresas ($c_1$ y $c_2$), además de recibir el valor de $ γ $. A continuación un ejemplo: 


#### **Parámetros dados para el ejemplo:**

$c_1 = 0.6 $ y $c_2 = 0.8 $, $γ = 0.6 $.




