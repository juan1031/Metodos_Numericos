## ¿Que es el MCO? 

El Método de los Mínimos Cuadrados Ordinarios (MCO) es una técnica fundamental en estadística y econometría empleada para estimar los parámetros de un modelo de regresión lineal. Su objetivo principal es encontrar la línea que mejor se ajuste a un conjunto de datos observados, minimizando la suma de los cuadrados de las diferencias entre los valores observados y los valores predichos por el modelo. Esto implica que el MCO otorga más peso a los errores grandes que a los errores pequeños, lo que puede ser ventajoso en diversos casos prácticos. 

Es esencial tener en cuenta que los estimadores obtenidos mediante el MCO deben cumplir con ciertas condiciones para garantizar su validez: 

 
- **Insesgados**: Estos estimadores tienden a centrarse alrededor del valor verdadero del parámetro cuando el tamaño de la muestra es grande.  

- **Consistentes**: A medida que el tamaño de la muestra aumenta, la probabilidad de que los estimadores se acerquen al valor verdadero del parámetro también debe aumenta. 

- **Eficientes**: Entre todos los estimadores lineales insesgados, los estimadores MCO deben tener la menor varianza.  
 

Para entenderlo de mejor manera es necesario recordar la fórmula de regresión lineal  


$y_i = \beta_0 + \beta_1X_i$ 


Sin embargo, dado que la distribución de valores nunca se ajustará perfectamente a una recta, se introduce un componente estocástico para representar esta diferencia, conocido como residuo: 

$\epsilon_i = y_i - ŷ_i$ 



De esta manera, la ecuación de regresión se convierte en: 

 
 

$y_i = \beta_0 + \beta_1X_i+\epsilon_i$ 

 
 

Se buscan aquellos coeficientes que minimicen la suma de los residuos, es decir, minimizan la diferencia entre el valor real y el predicho. Pero dado que estas distancias pueden ser positivas o negativas en la sumatoria, podrían cancelarse, por lo tanto, es necesario elevar al cuadrado, donde quedaría: 

 
 

$\sum_{i=1}^{n}\epsilon_{i}^2=\sum_{i=1}^{n}(y_i-\^y_i)^2$ 

 
 

¡Listo! Ahora entendemos de dónde viene el método de mínimos cuadrados para estimar los betas. Pero ahora necesitamos construir la recta que nos proporcione el valor más bajo posible de la suma de los cuadrados de los residuos. Para ello, sustituimos el valor estimado de y por los términos de la ecuación de la recta: 

 
 

$\sum_{i=1}^{n}\epsilon_{i}^2=\sum_{i=1}^{n}(y_i-b_0-b_1x_i)^2$ 

 
 

Donde: 

 
 

$b_1=\frac{s_xy}{{s_x}^2}$ 

 
 

y  

 
 

$b_o = \={y}-b_1\={x}$ 

 
 

Así, podemos construir la recta que minimiza la suma de los cuadrados. 


Fuente: Molina (17 de Junio de 2020) La distancia más corta. El método de los mínimos cuadrados. Recuperado de https://anestesiar.org/2020/la-distancia-mas-corta-el-metodo-de-los-minimos-cuadrados/ 


## Problema planteado

Calcular los betas de MCO, el error estándar y el R2, para la base de datos que cuenta con estas variables:

- **faminc**: Ingreso familiar anual.
- **cigtax**: Impuesto al consumo de cigarrillos.
- **cigprice**: Precio del cigarillo.
- **bwght**: Peso del bebé al nacer en onzas.
- **lbwght**: Peso del bebé al nacer en libras.
- **packs**: Paquetes de 10 cigarrillos.
- **male**: 1 para femenino, 0 para masculino.
- **motheduc**: Años de escolaridad de la madre.
- **fatheduc**: Años de escolaridad del padre.
- **cigs**: Número de cigarrillos promedio que la madre fumó por día durante el embarazo.

Para este ejercicio, se busca estimar cuáles de estas variables tiene mayor influencia en el peso del bebé en onzas (**bwght**).

