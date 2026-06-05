import math

# ─────────────────────────────────────────────
# 1. DESCRIPCIÓN Y DOCUMENTACIÓN
# ─────────────────────────────────────────────

def mostrar_descripcion():
    print(
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
""")
    
# ─────────────────────────────────────────────
# 2. FUNCIONES MATEMÁTICAS
# ─────────────────────────────────────────────

# 2.1 FACTORIAL ITERATIVO

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

# 2.2 FACTORIAL RECURSIVO 

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

# 2.3 CÁLCULO DE P(n, r)

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
# 3. VALIDACIÓN
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
# 4. PRESENTACIÓN
# ─────────────────────────────────────────────

# 4.1 COMPARACIÓN ITERATIVO vs RECURSIVO

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

# 4.2 MOSTRAR ALGORITMO

def mostrar_algoritmo():
    print("""
════════════════════════════════════════════════════

ALGORITMO

1. Validar entradas.
2. Verificar que r <= n.
3. Calcular:

   P(n,r)=n!/(n-r)!

4. Mostrar resultado.

Complejidad:
- O(r) usando producto directo.

════════════════════════════════════════════════════
""")
    
# 4.3 MOSTRAR EJEMPLOS

def mostrar_ejemplos():

    print("\nEjemplo 1")
    permutacion(10, 3)

    print("\nEjemplo 2")
    permutacion(20, 5)

# 4.4 MOSTRAR OPCIONES

def volver_o_salir():
    """
    Permite regresar al menú principal o salir del programa.
    """
    while True:

        print("\n" + "─" * 50)
        print("1. Volver al menú principal")
        print("0. Salir")
        print("─" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            return True

        elif opcion == "0":
            print("\nFin del programa.")
            return False

        print("\nOpción inválida.")

# ─────────────────────────────────────────────
# 5. PRUEBAS
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

    # Casos especiales o errores esperados
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
# 6. CALCULADORA
# ─────────────────────────────────────────────

def menu_calculadora():

    while True:

        print("\n" + "═"*60)
        print("CALCULADORA DE PERMUTACIONES")
        print("═"*60)
        print("1. Calcular P(n,r)")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            return

        elif opcion == "1":

            try:

                n = int(input("Ingrese n: "))
                r = int(input("Ingrese r: "))

                resultado = permutacion(
                    n,
                    r,
                    mostrar_procedimiento=True
                )

                print(f"\nResultado: {resultado}")

                while True:

                    print("\n" + "─"*50)
                    print("1. Realizar otro cálculo")
                    print("2. Volver al menú principal")
                    print("0. Salir")
                    print("─"*50)

                    accion = input("Seleccione una opción: ")

                    if accion == "1":
                        break

                    elif accion == "2":
                        return

                    elif accion == "0":
                        exit()

                    print("Opción inválida.")

            except Exception as e:

                print(f"\nError: {e}")

        else:

            print("\nOpción inválida.")

# ─────────────────────────────────────────────
# 7. MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():

    while True:

        print("\n")
        print("╔══════════════════════════════════════════════╗")
        print("║    PERMUTACIONES Y k-PERMUTACIONES           ║")
        print("╚══════════════════════════════════════════════╝")

        print("1. Ver descripción matemática")
        print("2. Ver algoritmo")
        print("3. Ver ejemplos")
        print("4. Comparar factorial iterativo y recursivo")
        print("5. Ejecutar pruebas")
        print("6. Usar calculadora")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            mostrar_descripcion()

            if not volver_o_salir():
                break

        elif opcion == "2":

            mostrar_algoritmo()

            if not volver_o_salir():
                break

        elif opcion == "3":

            mostrar_ejemplos()

            if not volver_o_salir():
                break

        elif opcion == "4":

            comparar_implementaciones(10)
            comparar_implementaciones(15)

            if not volver_o_salir():
                break

        elif opcion == "5":

            ejecutar_pruebas()

            if not volver_o_salir():
                break

        elif opcion == "6":

            menu_calculadora()

        elif opcion == "0":

            print("\nFin del programa.")
            break

        else:

            print("\nOpción inválida.")

# ─────────────────────────────────────────────
# 8. MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()