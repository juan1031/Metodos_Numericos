## Conceptos y Fórmulas 

Es de gran importancia comprender el concepto de `valor futuro (VF)`, el cual segpun GBM Academy (s.f.) hace referencia a las entradas de dinero que pudiera generar una inversión en una fecha futura.  Es decir, es la cantidad final de dinero que se obtendrá de una inversión a determinada cantidad de tiempo y con la aplicación de una tasa de interés simple o compuesta

**También se debe comprender el concepto de VF pero en este caso la fecha focal será 0 (o sea sólo se usará VP), por ende no hay necesidad de implementarlo. No enfocaremos únicamente en VP**

según GBM Academy (s.f.), el `valor presente (VP)` representa cuánto vale actualmente una suma de dinero que se recibirá en el futuro. Este cálculo es esencial debido a la fluctuación del valor del dinero con el tiempo; lo que vale hoy no será equivalente a su valor real cuando se reciba en el futuro. El cálculo del VP puede ser crucial para evaluar la conveniencia de realizar una inversión.

Las variables que intervienen en el cálculo del valor presente son:

- $F$: flujo de dinero
- $n$: años en el futuro
- $i$: interés

Dónde su fórmula es la siguiente:

$VP= \frac{Fn}{(1+i)n}$

Fuente: GBM Academy. (s.f.). ¿Cuál es la diferencia entre valor presente y futuro? Recuperado el 22 de abril de 2024, de https://gbm.com/academy/cual-es-la-diferencia-entre-valor-presente-y-futuro/ 


Ahora debemos hacer los despejes para encontrar los debidos valores de tasa, flujo o tiempo.

- Para encontrar la tasa ($r$):

$r = \left( \frac{\sum_{n=0}^{n} F_n}{VP} \right)^{\frac{1}{n}} - 1$

- Para encontrar el flujo ($F_n$):

$F_n = VP \times (1 + r)^n$

- Para encontrar el tiempo ($n$):

$n = \frac{\log \left( \frac{\sum_{n=0}^{n} F_n}{VP} \right)}{\log(1 + r)}$

Por ende, teniendo en cuenta todo lo anterior la clase construida es:


