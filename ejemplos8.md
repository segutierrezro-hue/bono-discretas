# Ejemplos de Entrada y Salida — Problema 8
## Caminos Mínimos en una Grilla Rectangular

---

## Uso básico

```bash
python3 problema8_caminos.py
```

---

## Modo 1 — Caminos básicos (ejecutado automáticamente)

### De (0,0) a (3,2)
```
  Caminos de (0,0) a (3,2):
  Total de pasos : 3 + 2 = 5
  Fórmula        : C(5, 3) = 5! / (3! × 2!)
                 = 120 / (6 × 2)
                 = 10
  Verificación   : C(5,2) = 10 ✓
```

### De (0,0) a (4,6)
```
  Caminos de (0,0) a (4,6):
  Total de pasos : 4 + 6 = 10
  Fórmula        : C(10, 4) = 10! / (4! × 6!)
                 = 3628800 / (24 × 720)
                 = 210
  Verificación   : C(10,6) = 210 ✓
```

---

## Pruebas automáticas

```
PRUEBAS — Caminos mínimos C(a+b, a)
════════════════════════════════════════════════════════════
  C(4,2)   =      6  |  ✓ PASS  |  Grilla 2×2 clásica
  C(5,3)   =     10  |  ✓ PASS  |  Grilla 3×2
  C(8,4)   =     70  |  ✓ PASS  |  Grilla 4×4
  C(5,0)   =      1  |  ✓ PASS  |  Solo subir (a=0)
  C(5,5)   =      1  |  ✓ PASS  |  Solo derecha (b=0)
  C(2,1)   =      2  |  ✓ PASS  |  Grilla 1×1 (2 caminos)
  C(15,10) =   3003  |  ✓ PASS  |  Grilla 10×5

  Resultado: 7/7 pruebas aprobadas.
```

---

## Modo 2 — Puntos obligatorios

Caminos de (0,0) a (4,4) que **deben pasar por (2,2)**:

```
  Tramo (0,0) → (2,2) : C(4,2) = 6
  Tramo (2,2) → (4,4) : C(4,2) = 6
  Total : 6 × 6 = 36

  Caminos totales sin restricción = 70
  Los que pasan por (2,2) representan el 51.4% del total.
```

---

## Modo 3 — Puntos bloqueados (programación dinámica)

Caminos de (0,0) a (3,3) **bloqueando las celdas (1,2) y (2,1)**:

```
  Grilla de caminos (0,0)→(3,3):
  (Las celdas muestran cuántos caminos llegan a ese punto)

  y=3 |    1    1    1 [ 2]
  y=2 |    1  [X]    0    1
  y=1 |    1    2  [X]    1
  y=0 |  [S]    1    1    1
       ────────────────────
        x=0  x=1  x=2  x=3

  Caminos evitando (1,2) y (2,1) = 2
  Caminos sin bloqueos            = 20
  Caminos eliminados              = 18
```

---

## Modo interactivo

```
CALCULADORA DE CAMINOS MÍNIMOS — Modo interactivo
════════════════════════════════════════════════════
  Modos disponibles:
  [1] Caminos básicos de (0,0) a (a,b)
  [2] Caminos con puntos obligatorios
  [3] Caminos con puntos bloqueados
  [0] Salir

  Selecciona modo [0-3]: 1
  Ingresa a (pasos a la derecha): 5
  Ingresa b (pasos hacia arriba) : 3

  Caminos de (0,0) a (5,3):
  Total de pasos : 5 + 3 = 8
  Fórmula        : C(8, 5) = 8! / (5! × 3!)
                 = 40320 / (120 × 6)
                 = 56

  ✓ Caminos de (0,0) a (5,3) = 56
```

---

## Tabla de referencia

| a  | b  | C(a+b, a) | Interpretación                        |
|----|----|-----------|---------------------------------------|
| 1  | 1  | 2         | Grilla 1×1: solo 2 caminos posibles   |
| 2  | 2  | 6         | Grilla 2×2 clásica                    |
| 3  | 3  | 20        | Grilla 3×3                            |
| 4  | 4  | 70        | Grilla 4×4                            |
| 5  | 5  | 252       | Grilla 5×5                            |
| 10 | 5  | 3003      | Grilla rectangular 10×5               |
| 0  | n  | 1         | Solo subir: un único camino           |
