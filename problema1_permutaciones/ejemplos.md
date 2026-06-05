# Ejemplos de uso - Problema 1: Permutaciones y k-Permutaciones

## Descripción

Este documento presenta ejemplos de ejecución del programa correspondiente al Problema 1 del bono de programación de Matemáticas Discretas I.

El programa permite:

* Consultar la descripción matemática.
* Revisar el algoritmo implementado.
* Ejecutar ejemplos predefinidos.
* Comparar implementaciones iterativas y recursivas.
* Ejecutar pruebas automáticas.
* Utilizar una calculadora interactiva de permutaciones.

---

# Menú principal

Al iniciar el programa se muestra:

```text
╔══════════════════════════════════════════════╗
║    PERMUTACIONES Y k-PERMUTACIONES           ║
╚══════════════════════════════════════════════╝

1. Ver descripción matemática
2. Ver algoritmo
3. Ver ejemplos
4. Comparar factorial iterativo y recursivo
5. Ejecutar pruebas
6. Usar calculadora
0. Salir
```

---

# Ejemplo 1: Permutación P(10,3)

### Entrada

```text
Seleccione una opción: 6

Ingrese n: 10
Ingrese r: 3
```

### Salida

```text
P(10, 3) = 10! / (10 - 3)!
         = 10! / 7!
         = 3628800 / 5040
         = 720

Resultado: 720
```

Interpretación:

Se cuentan todas las formas posibles de ordenar 3 elementos distintos tomados de un conjunto de 10 elementos distintos.

---

# Ejemplo 2: Permutación P(20,5)

### Entrada

```text
Seleccione una opción: 6

Ingrese n: 20
Ingrese r: 5
```

### Salida

```text
P(20, 5) = 20! / (20 - 5)!
         = 20! / 15!
         = 1860480

Resultado: 1860480
```

---

# Ejemplo 3: Permutación total

### Entrada

```text
Seleccione una opción: 6

Ingrese n: 7
Ingrese r: 7
```

### Salida

```text
P(7,7) = 5040
```

Interpretación:

Cuando r = n, la permutación coincide con n!.

---

# Ejemplo 4: Caso especial P(n,0)

### Entrada

```text
Seleccione una opción: 6

Ingrese n: 4
Ingrese r: 0
```

### Salida

```text
P(4,0) = 1
```

Interpretación:

Existe exactamente una forma de ordenar cero elementos.

---

# Validación de entradas

## Caso 1: r > n

### Entrada

```text
n = 3
r = 5
```

### Salida

```text
Error:
r no puede ser mayor que n (r=5 > n=3).
No se pueden ordenar 5 objetos de un conjunto de solo 3.
```

---

## Caso 2: n negativo

### Entrada

```text
n = -1
r = 2
```

### Salida

```text
Error:
n debe ser no negativo.
```

---

## Caso 3: r negativo

### Entrada

```text
n = 4
r = -1
```

### Salida

```text
Error:
r debe ser no negativo.
```

---

# Comparación entre factorial iterativo y recursivo

### Entrada

```text
Seleccione una opción: 4
```

### Salida

```text
Comparación de implementaciones para 10!

Iterativo : 10! = 3628800
Recursivo : 10! = 3628800
¿Son iguales? ✓ Sí

Nota: ambos dan el mismo resultado.
La versión iterativa usa O(1) de espacio adicional.
La recursiva usa O(10) de espacio en la pila de llamadas.
```

---

# Pruebas automáticas

### Entrada

```text
Seleccione una opción: 5
```

### Salida (fragmento)

```text
P(  5, 2) =         20 | ✓ PASS
P( 10, 3) =        720 | ✓ PASS
P( 20, 5) =    1860480 | ✓ PASS
P(  7, 7) =       5040 | ✓ PASS
P(  4, 0) =          1 | ✓ PASS
```

Resultado final:

```text
7/7 pruebas aprobadas.
```

---

# Navegación

Después de visualizar información o realizar cálculos, el usuario puede seleccionar:

```text
──────────────────────────────────────────
1. Volver al menú principal
0. Salir
──────────────────────────────────────────
```

En la calculadora interactiva también se ofrece:

```text
──────────────────────────────────────────
1. Realizar otro cálculo
2. Volver al menú principal
0. Salir
──────────────────────────────────────────
```

---

# Comentario final

El programa implementa una calculadora general de permutaciones y k-permutaciones utilizando validación de entradas, ejemplos de uso, pruebas automáticas y una interfaz interactiva basada en menús.

La implementación sigue el modelo matemático:

P(n,r) = n!/(n-r)!

y utiliza una estrategia eficiente basada en el producto directo:

P(n,r) = n × (n-1) × ... × (n-r+1)

lo que reduce el número de operaciones necesarias para calcular el resultado.
