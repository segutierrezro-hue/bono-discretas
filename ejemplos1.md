# Ejemplos de Entrada y Salida — Problema 1
## Permutaciones y k-Permutaciones

---

## Uso básico

```bash
python3 problema1_permutaciones.py
```

---

## Ejemplos del enunciado (ejecutados automáticamente)

### P(10, 3)
```
P(10, 3) = 10! / (10 - 3)!
         = 10! / 7!
         = 3628800 / 5040
         = 720
```

### P(20, 5)
```
P(20, 5) = 20! / (20 - 5)!
         = 20! / 15!
         = 2432902008176640000 / 1307674368000
         = 1860480
```

---

## Comparación iterativo vs recursivo

```
Comparación de implementaciones para 10!
──────────────────────────────────────────
  Iterativo : 10! = 3628800
  Recursivo : 10! = 3628800
  ¿Son iguales? ✓ Sí

  La versión iterativa usa O(1) de espacio adicional.
  La recursiva usa O(10) de espacio en la pila de llamadas.
```

---

## Pruebas automáticas

```
PRUEBAS DE PERMUTACIONES P(n, r)
════════════════════════════════════════════════════════════
  P(  5, 2) =         20  |  ✓ PASS  |  Ordenar 2 letras de {A,B,C,D,E}
  P( 10, 3) =        720  |  ✓ PASS  |  Ejemplo del enunciado P(10,3)
  P( 20, 5) =    1860480  |  ✓ PASS  |  Ejemplo del enunciado P(20,5)
  P(  7, 7) =       5040  |  ✓ PASS  |  Permutación total de 7 elementos (7!)
  P(  6, 1) =          6  |  ✓ PASS  |  Elegir 1 elemento de 6 (trivial)
  P(  4, 0) =          1  |  ✓ PASS  |  Ordenar 0 elementos → siempre 1 forma
  P(100, 2) =       9900  |  ✓ PASS  |  n grande, r pequeño

  Resultado: 7/7 pruebas aprobadas.
```

---

## Validación de errores

```
VALIDACIÓN DE CASOS ESPECIALES (errores esperados)
────────────────────────────────────────────────────
  P(3, 5) → ✓ Error capturado: r no puede ser mayor que n (r=5 > n=3).
  P(-1,2) → ✓ Error capturado: n debe ser no negativo. Se recibió n=-1.
  P(4,-1) → ✓ Error capturado: r debe ser no negativo. Se recibió r=-1.
```

---

## Modo interactivo

```
CALCULADORA DE PERMUTACIONES — Modo interactivo
════════════════════════════════════════════════
  Ingresa n (tamaño del conjunto): 8
  Ingresa r (objetos a ordenar)  : 3

  P(8, 3) = 8! / (8 - 3)!
           = 8! / 5!
           = 40320 / 120
           = 336

  ✓ P(8, 3) = 336
```

---

## Tabla de referencia

| n  | r | P(n,r)    | Interpretación                        |
|----|---|-----------|---------------------------------------|
| 5  | 2 | 20        | Podios de 2 en una carrera de 5       |
| 10 | 3 | 720       | Primer, segundo, tercer puesto de 10  |
| 7  | 7 | 5040      | Permutaciones totales de 7 elementos  |
| 4  | 0 | 1         | No ordenar nada: 1 sola forma         |
| 20 | 5 | 1.860.480 | Caso del enunciado                    |
