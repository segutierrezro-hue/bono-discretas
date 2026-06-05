# Bono de Programación — Matemáticas Discretas I

**Universidad Nacional de Colombia**
**Docente:** Jhoan Sebastian Tenjo García

---

## Descripción

Este repositorio contiene la solución de dos problemas de conteo combinatorio correspondientes al bono de programación de Matemáticas Discretas I.

Cada problema fue implementado en Python como una herramienta general que:

* Acepta parámetros variables.
* Valida entradas y casos de error.
* Explica el procedimiento matemático utilizado.
* Incluye pruebas automáticas.
* Permite la interacción mediante menús de consola.

---

## Problemas resueltos

| # | Problema                        | Fórmula principal         |
| - | ------------------------------- | ------------------------- |
| 1 | Permutaciones y k-Permutaciones | `P(n,r)=n!/(n-r)!`        |
| 8 | Caminos Mínimos en una Grilla   | `C(a+b,a)=(a+b)!/(a!·b!)` |

---

## Requisitos

* Python 3.8 o superior.
* No requiere dependencias externas.
* Utiliza únicamente la librería estándar de Python.

Para verificar la versión instalada ingresa a la terminal y escribe:

```bash
python3 --version
```
y si no la tienes instalada puedes ingresar a:
https://www.python.org/downloads/ 

---

## Instalación

### Clonar el repositorio

Para traer el repositorio abre la terminal y escribe lo siguiente:
```bash
git clone https://github.com/TU_USUARIO/bono-discretas.git
```
y luego 
```bash
cd bono-discretas
```
Como puedes observar debes ingresar el usuario de tu github en la parte TU_USUARIO, ejemplo el mio es segutierrezro-hue y quedaría

```bash
git clone https://github.com/segutierrezro-hue/bono-discretas.git
```
---

## Ejecución

### Problema 1 — Permutaciones y k-Permutaciones

Para ejecutar el programa del problema 1, ve dentro de la terminal, copia este comando y pegalo en la terminal

```bash
python3 problema1_permutaciones/problema1_permutaciones.py
```

### Problema 8 — Caminos Mínimos en una Grilla

Lo mismo ocurre con el problema 8

```bash
python3 problema8_caminos/problema8_caminos.py
```

---

## Interfaz de los programas

Ambos programas presentan un menú interactivo que permite acceder a las diferentes funcionalidades sin necesidad de modificar el código.
Necesitas ingresar el número al que deseas ingresar y dar enter
### Problema 1

```text
1. Ver descripción matemática
2. Ver algoritmo
3. Ver ejemplos
4. Comparar factorial iterativo y recursivo
5. Ejecutar pruebas
6. Usar calculadora
0. Salir
```

### Problema 8

```text
1. Ver descripción matemática
2. Ver algoritmo
3. Ver ejemplos
4. Ejecutar pruebas
5. Usar calculadora
0. Salir
```
También observarás un menú que muestra:

```text
──────────────────────────────────────────────────
1. Volver al menú principal
0. Salir
──────────────────────────────────────────────────
Seleccione una opción:
```
En donde dice seleccone una opción tiene la posibilidad de regrasar al menú principal con 1, o ingresar 0 para salir del programa y probar otro problema
---

## Estructura del repositorio

```text
bono-discretas/
│
├── README.md
├── requirements.txt
│
├── problema1_permutaciones/
│   ├── problema1_permutaciones.py
│   └── ejemplos.md
│
└── problema8_caminos/
    ├── problema8_caminos.py
    └── ejemplos.md
```

---

# Problema 1 — Permutaciones y k-Permutaciones

## Objetivo

Calcular el número de formas de ordenar `r` elementos distintos tomados de un conjunto de `n` elementos distintos.

### Fórmula

```text
P(n,r)=n!/(n-r)!
```

### Funcionalidades

* Factorial iterativo.
* Factorial recursivo.
* Comparación de eficiencia entre implementaciones.
* Cálculo de permutaciones con procedimiento paso a paso.
* Validación de entradas.
* Casos especiales.
* Pruebas automáticas.
* Calculadora interactiva.

### Ejemplos

```text
P(10,3)=720
P(20,5)=1860480
P(7,7)=5040
```

---

# Problema 8 — Caminos Mínimos en una Grilla

## Objetivo

Calcular la cantidad de caminos mínimos entre dos puntos de una grilla rectangular utilizando técnicas de conteo combinatorio.

Se permiten únicamente movimientos:

```text
→ Derecha
↑ Arriba
```

### Fórmula básica

```text
C(a+b,a)=(a+b)!/(a!·b!)
```

### Funcionalidades

* Conteo básico de caminos mínimos.
* Explicación paso a paso del procedimiento.
* Caminos con puntos obligatorios.
* Caminos con puntos bloqueados.
* Programación dinámica para restricciones.
* Visualización de grillas.
* Validación de entradas.
* Pruebas automáticas.
* Calculadora interactiva.

### Ejemplos

```text
(0,0) → (3,2) = 10 caminos

(0,0) → (4,4)
pasando por (2,2)
= 36 caminos

(0,0) → (3,3)
evitando obstáculos
= 2 caminos
```

---

## Documentación adicional

Cada carpeta contiene un archivo `ejemplos.md` con:

* Casos de prueba.
* Ejemplos de entrada y salida.
* Validaciones.
* Explicaciones de uso.
* Navegación de los menús.

---

## Autor

Sebastian Fernando Gutiérrez Rojas — Matemáticas Discretas I
Universidad Nacional de Colombia
2026
