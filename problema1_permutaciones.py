"""
=============================================================
PROBLEMA 1: Calculadora General de Permutaciones y k-Permutaciones
=============================================================
Matemáticas Discretas I — Universidad Nacional de Colombia
Docente: Jhoan Sebastian Tenjo García

DESCRIPCIÓN MATEMÁTICA:
    Una permutación de r objetos tomados de n objetos distintos
    cuenta el número de formas de ORDENAR r elementos de un conjunto
    de n elementos (el orden importa, sin repetición).

FÓRMULA:
    P(n, r) = n! / (n - r)!

    Casos especiales:
        - P(n, 0) = 1          (hay exactamente 1 forma de ordenar 0 elementos)
        - P(n, n) = n!         (permutación total)
        - P(n, r) inválido si r > n

ALGORITMO:
    1. Validar que n y r sean enteros no negativos y que r <= n.
    2. Calcular n! y (n-r)! usando factorial (iterativo o recursivo).
    3. Retornar n! // (n-r)!

EFICIENCIA:
    - Factorial iterativo: O(n) en tiempo, O(1) en espacio.
    - Factorial recursivo: O(n) en tiempo, O(n) en espacio (pila de llamadas).
    - Para n grandes se puede usar math.factorial que está optimizado en C.
    - Calcular P(n,r) directamente como n*(n-1)*...*(n-r+1) evita
      calcular (n-r)! innecesariamente → O(r) multiplicaciones.
=============================================================
"""

import math


# ─────────────────────────────────────────────
# 1. FACTORIAL ITERATIVO
# ─────────────────────────────────────────────

def factorial_iterativo(n: int) -> int:
    """
    Calcula n! de forma iterativa.
    Complejidad: O(n) tiempo, O(1) espacio.
    """
    if n < 0:
        raise ValueError(f"El factorial no está definido para n={n} (debe ser >= 0).")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# ─────────────────────────────────────────────
# 2. FACTORIAL RECURSIVO (extensión opcional)
# ─────────────────────────────────────────────

def factorial_recursivo(n: int) -> int:
    """
    Calcula n! de forma recursiva.
    Complejidad: O(n) tiempo, O(n) espacio (pila de llamadas).
    """
    if n < 0:
        raise ValueError(f"El factorial no está definido para n={n} (debe ser >= 0).")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)


# ─────────────────────────────────────────────
# 3. VALIDACIÓN DE ENTRADAS
# ─────────────────────────────────────────────

def validar_entradas(n, r) -> None:
    """
    Verifica que n y r sean enteros no negativos y que r <= n.
    Lanza ValueError con mensaje descriptivo si algo falla.
    """
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError(f"n y r deben ser enteros. Se recibió n={type(n).__name__}, r={type(r).__name__}.")
    if n < 0:
        raise ValueError(f"n debe ser no negativo. Se recibió n={n}.")
    if r < 0:
        raise ValueError(f"r debe ser no negativo. Se recibió r={r}.")
    if r > n:
        raise ValueError(
            f"r no puede ser mayor que n (r={r} > n={n}). "
            f"No se pueden ordenar {r} objetos de un conjunto de solo {n}."
        )


# ─────────────────────────────────────────────
# 4. CÁLCULO DE P(n, r)
# ─────────────────────────────────────────────

def permutacion(n: int, r: int, mostrar_procedimiento: bool = True) -> int:
    """
    Calcula P(n, r) = n! / (n - r)!

    Parámetros:
        n (int): Tamaño total del conjunto (>= 0).
        r (int): Número de objetos a ordenar (0 <= r <= n).
        mostrar_procedimiento (bool): Si True, imprime el paso a paso.

    Retorna:
        int: El número de k-permutaciones P(n, r).
    """
    validar_entradas(n, r)

    # Calculo eficiente: producto n * (n-1) * ... * (n-r+1)
    resultado = 1
    for i in range(n, n - r, -1):
        resultado *= i

    if mostrar_procedimiento:
        fact_n = factorial_iterativo(n)
        fact_nr = factorial_iterativo(n - r)
        print(f"\n  P({n}, {r}) = {n}! / ({n} - {r})!")
        print(f"           = {n}! / {n - r}!")
        print(f"           = {fact_n} / {fact_nr}")
        print(f"           = {resultado}")

    return resultado


# ─────────────────────────────────────────────
# 5. COMPARACIÓN ITERATIVO vs RECURSIVO
# ─────────────────────────────────────────────

def comparar_implementaciones(n: int) -> None:
    """
    Compara las implementaciones iterativa y recursiva del factorial para un n dado.
    """
    print(f"\n{'─'*50}")
    print(f"  Comparación de implementaciones para {n}!")
    print(f"{'─'*50}")

    res_iter = factorial_iterativo(n)
    res_rec  = factorial_recursivo(n)

    print(f"  Iterativo : {n}! = {res_iter}")
    print(f"  Recursivo : {n}! = {res_rec}")
    print(f"  ¿Son iguales? {'✓ Sí' if res_iter == res_rec else '✗ No'}")
    print(f"\n  Nota: ambos dan el mismo resultado.")
    print(f"  La versión iterativa usa O(1) de espacio adicional.")
    print(f"  La recursiva usa O({n}) de espacio en la pila de llamadas.")


# ─────────────────────────────────────────────
# 6. PRUEBAS
# ─────────────────────────────────────────────

def ejecutar_pruebas() -> None:
    """
    Ejecuta al menos 5 pruebas con distintos valores y valida casos especiales.
    """
    print("\n" + "═"*60)
    print("  PRUEBAS DE PERMUTACIONES P(n, r)")
    print("═"*60)

    # Casos normales
    casos = [
        (5,  2,  20,    "Ordenar 2 letras de {A,B,C,D,E}"),
        (10, 3,  720,   "Ejemplo del enunciado P(10,3)"),
        (20, 5,  1860480, "Ejemplo del enunciado P(20,5)"),
        (7,  7,  5040,  "Permutación total de 7 elementos (7!)"),
        (6,  1,  6,     "Elegir 1 elemento de 6 (trivial)"),
        (4,  0,  1,     "Ordenar 0 elementos → siempre 1 forma"),
        (100,2,  9900,  "n grande, r pequeño"),
    ]

    aprobadas = 0
    for n, r, esperado, descripcion in casos:
        try:
            resultado = permutacion(n, r, mostrar_procedimiento=False)
            estado = "✓ PASS" if resultado == esperado else f"✗ FAIL (esperado {esperado})"
            if resultado == esperado:
                aprobadas += 1
        except Exception as e:
            resultado = None
            estado = f"✗ ERROR: {e}"

        print(f"  P({n:>3}, {r}) = {str(resultado):>10}  |  {estado}  |  {descripcion}")

    print(f"\n  Resultado: {aprobadas}/{len(casos)} pruebas aprobadas.")

    # Casos especiales / errores esperados
    print("\n" + "─"*60)
    print("  VALIDACIÓN DE CASOS ESPECIALES (errores esperados)")
    print("─"*60)

    casos_invalidos = [
        (3,  5,  "r > n"),
        (-1, 2,  "n negativo"),
        (4,  -1, "r negativo"),
    ]

    for n, r, descripcion in casos_invalidos:
        try:
            permutacion(n, r, mostrar_procedimiento=False)
            print(f"  P({n}, {r}) → ✗ Debería haber lanzado error ({descripcion})")
        except (ValueError, TypeError) as e:
            print(f"  P({n}, {r}) → ✓ Error capturado correctamente ({descripcion}): {e}")


# ─────────────────────────────────────────────
# 7. PROGRAMA PRINCIPAL (interfaz de usuario)
# ─────────────────────────────────────────────

def menu_interactivo() -> None:
    """
    Permite al usuario calcular P(n, r) de forma interactiva.
    """
    print("\n" + "═"*60)
    print("  CALCULADORA DE PERMUTACIONES — Modo interactivo")
    print("═"*60)
    print("  Calcula P(n, r) = n! / (n-r)!")
    print("  Escribe 'salir' para terminar.\n")

    while True:
        entrada_n = input("  Ingresa n (tamaño del conjunto): ").strip()
        if entrada_n.lower() == "salir":
            break
        entrada_r = input("  Ingresa r (objetos a ordenar): ").strip()
        if entrada_r.lower() == "salir":
            break

        try:
            n = int(entrada_n)
            r = int(entrada_r)
            resultado = permutacion(n, r, mostrar_procedimiento=True)
            print(f"\n  ✓ P({n}, {r}) = {resultado}\n")
        except (ValueError, TypeError) as e:
            print(f"\n  ✗ Entrada inválida: {e}\n")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   PROBLEMA 1: Permutaciones y k-Permutaciones            ║")
    print("║   Matemáticas Discretas I — UNAL                         ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # Mostrar ejemplos del enunciado con procedimiento
    print("\n── Ejemplos del enunciado (con procedimiento) ──")
    permutacion(10, 3, mostrar_procedimiento=True)
    permutacion(20, 5, mostrar_procedimiento=True)

    # Comparar factorial iterativo vs recursivo
    comparar_implementaciones(10)
    comparar_implementaciones(15)

    # Suite de pruebas automáticas
    ejecutar_pruebas()

    # Modo interactivo
    print("\n" + "═"*60)
    respuesta = input("  ¿Deseas usar el modo interactivo? (s/n): ").strip().lower()
    if respuesta == "s":
        menu_interactivo()

    print("\n  Fin del programa.")
