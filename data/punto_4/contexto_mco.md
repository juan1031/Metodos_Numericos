## ¿Que es el MCO?

El Método de los Mínimos Cuadrados Ordinarios (MCO) es una técnica fundamental en estadística y econometría empleada para estimar los parámetros de un modelo de regresión lineal. Su objetivo principal es encontrar la línea que mejor se ajuste a un conjunto de datos observados, minimizando la suma de los cuadrados de las diferencias entre los valores observados y los valores predichos por el modelo. Esto implica que el MCO otorga más peso a los errores grandes que a los errores pequeños, lo que puede ser ventajoso en diversos casos prácticos.

Es esencial tener en cuenta que los estimadores obtenidos mediante el MCO deben cumplir con ciertas condiciones para garantizar su validez:

- **Insesgados**: Estos estimadores tienden a centrarse alrededor del valor verdadero del parámetro cuando el tamaño de la muestra es grande. 

- **Consistentes**: A medida que el tamaño de la muestra aumenta, la probabilidad de que los estimadores se acerquen al valor verdadero del parámetro también debe aumenta.
- **Eficientes**: Entre todos los estimadores lineales insesgados, los estimadores MCO deben tener la menor varianza. 


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

