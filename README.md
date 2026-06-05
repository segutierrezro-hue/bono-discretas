# Bono de Programación — Matemáticas Discretas I
**Universidad Nacional de Colombia**  
Docente: Jhoan Sebastian Tenjo García — Segundo corte

---

## Descripción

Este repositorio contiene la solución a dos problemas de conteo combinatorio como parte del bono de programación del segundo corte de Matemáticas Discretas I. Cada problema está implementado como un programa general en Python que acepta parámetros variables, valida entradas y calcula resultados para distintos casos.

---

## Problemas resueltos

| # | Problema | Fórmula principal |
|---|----------|-------------------|
| 1 | Permutaciones y k-Permutaciones | `P(n,r) = n! / (n-r)!` |
| 8 | Caminos Mínimos en una Grilla | `C(a+b, a) = (a+b)! / (a! × b!)` |

---

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas (solo librería estándar)

Puedes verificar tu versión con:
```bash
python3 --version
```

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/bono-discretas.git
cd bono-discretas
```

### 2. Ejecutar Problema 1 — Permutaciones

```bash
python3 problema1_permutaciones/problema1_permutaciones.py
```

### 3. Ejecutar Problema 8 — Caminos Mínimos

```bash
python3 problema8_caminos/problema8_caminos.py
```

Cada programa ejecuta automáticamente los ejemplos, las pruebas y al final pregunta si deseas usar el **modo interactivo** para ingresar tus propios valores.

---

## Estructura del repositorio

```
bono-discretas/
│
├── README.md                          ← Este archivo
├── requirements.txt                   ← Dependencias (vacío, solo stdlib)
│
├── problema1_permutaciones/
│   ├── problema1_permutaciones.py     ← Código principal
│   └── ejemplos.md                    ← Ejemplos de entrada y salida
│
└── problema8_caminos/
    ├── problema8_caminos.py           ← Código principal
    └── ejemplos.md                    ← Ejemplos de entrada y salida
```

---

## Resumen de cada problema

### Problema 1 — Permutaciones y k-Permutaciones

**¿Qué cuenta?**  
El número de formas de **ordenar** `r` objetos distintos tomados de un conjunto de `n` objetos distintos. El orden importa y no hay repetición.

**Fórmula:**
```
P(n, r) = n! / (n - r)!
```

**Funcionalidades implementadas:**
- Cálculo de `n!` con versión iterativa y recursiva (comparación de eficiencia)
- Cálculo de `P(n, r)` con procedimiento paso a paso
- Validación de entradas (`r > n`, negativos, tipos inválidos)
- 7 pruebas automáticas + 3 casos de error validados
- Modo interactivo

---

### Problema 8 — Caminos Mínimos en una Grilla

**¿Qué cuenta?**  
El número de caminos de longitud mínima desde `(0,0)` hasta `(a,b)` en una grilla rectangular, moviéndose solo hacia la derecha (→) o hacia arriba (↑).

**Fórmula:**
```
C(a+b, a) = (a+b)! / (a! × b!)
```

**Funcionalidades implementadas:**
- Conteo básico de caminos con procedimiento paso a paso
- Caminos con **puntos obligatorios** intermedios
- Caminos con **puntos bloqueados** usando programación dinámica + visualización de grilla
- 7 pruebas automáticas + validación de errores
- Modo interactivo con 3 modos de uso

---

## Ejemplos rápidos

```python
# Problema 1
P(10, 3) = 720
P(20, 5) = 1860480

# Problema 8
Caminos de (0,0) a (3,2) = 10
Caminos de (0,0) a (4,4) pasando por (2,2) = 36
```

---

## Autor

Estudiante — Matemáticas Discretas I  
Universidad Nacional de Colombia  
2025
