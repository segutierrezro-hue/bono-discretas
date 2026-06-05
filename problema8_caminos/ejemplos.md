# Ejemplos de uso - Problema 8: Caminos Mínimos en una Grilla

## Descripción

Este documento presenta ejemplos de ejecución del programa correspondiente al Problema 8 del bono de programación de Matemáticas Discretas I.

El programa permite:

* Consultar la descripción matemática.
* Revisar el algoritmo implementado.
* Ejecutar ejemplos predefinidos.
* Ejecutar pruebas automáticas.
* Utilizar una calculadora interactiva para resolver distintos tipos de problemas de caminos mínimos.

---

# Menú principal

Al iniciar el programa se muestra:

```text
╔══════════════════════════════════════════════╗
║     CAMINOS MÍNIMOS EN UNA GRILLA           ║
╚══════════════════════════════════════════════╝

1. Ver descripción matemática
2. Ver algoritmo
3. Ver ejemplos
4. Ejecutar pruebas
5. Usar calculadora
0. Salir
```

---

# Ejemplo 1: Caminos mínimos básicos

### Entrada

```text
Seleccione una opción: 5

Seleccione una opción: 1

Ingrese a: 3
Ingrese b: 2
```

### Salida

```text
Caminos de (0,0) a (3,2):

Total de pasos : 3 + 2 = 5

Fórmula:
C(5,3) = 5! / (3! × 2!)

        = 120 / (6 × 2)

        = 10

Resultado: 10
```

Interpretación:

Existen 10 caminos mínimos distintos para ir desde (0,0) hasta (3,2), moviéndose únicamente hacia la derecha o hacia arriba.

---

# Ejemplo 2: Caminos mínimos en una grilla 4×6

### Entrada

```text
Seleccione una opción: 5

Seleccione una opción: 1

Ingrese a: 4
Ingrese b: 6
```

### Salida

```text
Caminos de (0,0) a (4,6):

Total de pasos : 10

C(10,4) = 210

Resultado: 210
```

---

# Ejemplo 3: Punto obligatorio

### Entrada

```text
Seleccione una opción: 5

Seleccione una opción: 2

Ingrese a: 4
Ingrese b: 4

Puntos obligatorios:
2,2
```

### Salida

```text
Tramo (0,0) → (2,2)

C(4,2) = 6

Tramo (2,2) → (4,4)

C(4,2) = 6

Total:

6 × 6 = 36

Resultado: 36
```

Interpretación:

Todo camino válido debe pasar por el punto (2,2), por lo que el recorrido se divide en dos segmentos independientes.

---

# Ejemplo 4: Puntos bloqueados

### Entrada

```text
Seleccione una opción: 5

Seleccione una opción: 3

Ingrese a: 3
Ingrese b: 3

Bloqueados:
1,2 2,1
```

### Salida

```text
Grilla de caminos (0,0)→(3,3)

y=3 |    1    1    1 [ 2]
y=2 |    1  [X]    0    1
y=1 |    1    2  [X]    1
y=0 |  [S]    1    1    1
     ────────────────────
      x=0  x=1  x=2  x=3

Caminos evitando bloqueos = 2

Resultado: 2
```

Interpretación:

Las celdas marcadas con [X] no pueden ser utilizadas durante el recorrido.

---

# Validación de entradas

## Caso 1: Coordenadas negativas

### Entrada

```text
a = -1
b = 3
```

### Salida

```text
Error:
Las coordenadas deben ser enteros no negativos.
```

---

## Caso 2: Punto obligatorio fuera de la grilla

### Entrada

```text
a = 4
b = 4

Punto obligatorio:
(5,2)
```

### Salida

```text
Error:
El punto obligatorio está fuera de la grilla.
```

---

## Caso 3: Punto bloqueado inválido

### Entrada

```text
a = 3
b = 3

Bloqueado:
(-1,1)
```

### Salida

```text
Error:
Las coordenadas bloqueadas deben pertenecer a la grilla.
```

---

# Pruebas automáticas

### Entrada

```text
Seleccione una opción: 4
```

### Salida (fragmento)

```text
PRUEBAS — Caminos mínimos C(a+b,a)

════════════════════════════════════════════════════

C(4,2)   =      6 | ✓ PASS
C(5,3)   =     10 | ✓ PASS
C(8,4)   =     70 | ✓ PASS
C(5,0)   =      1 | ✓ PASS
C(5,5)   =      1 | ✓ PASS
C(2,1)   =      2 | ✓ PASS
C(15,10) =   3003 | ✓ PASS
```

Resultado final:

```text
7/7 pruebas aprobadas.
```

---

# Navegación

Después de visualizar información o ejecutar pruebas, el usuario puede seleccionar:

```text
──────────────────────────────────────────
1. Volver al menú principal
0. Salir
──────────────────────────────────────────
```

Después de realizar un cálculo:

```text
──────────────────────────────────────────
1. Realizar otro cálculo
2. Volver al menú principal
0. Salir
──────────────────────────────────────────
```

---

# Tabla de referencia

| a  | b | Caminos |
| -- | - | ------- |
| 1  | 1 | 2       |
| 2  | 2 | 6       |
| 3  | 3 | 20      |
| 4  | 4 | 70      |
| 5  | 5 | 252     |
| 10 | 5 | 3003    |

---

# Comentario final

El programa implementa una calculadora general para problemas de caminos mínimos en grillas rectangulares utilizando técnicas combinatorias y programación dinámica.

Se incluyen tres modalidades:

* Conteo básico de caminos mínimos.
* Caminos con puntos obligatorios.
* Caminos con puntos bloqueados.

La solución básica utiliza el coeficiente binomial:

C(a+b,a) = (a+b)! / (a! × b!)

mientras que la variante con obstáculos utiliza programación dinámica para contabilizar únicamente los caminos válidos.
