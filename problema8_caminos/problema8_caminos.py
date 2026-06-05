import math

# ─────────────────────────────────────────────
# 1. DESCRIPCIÓN Y DOCUMENTACIÓN
# ─────────────────────────────────────────────
def mostrar_descripcion():
    print(
"""
=============================================================
PROBLEMA 8: Caminos Mínimos en una Grilla Rectangular
=============================================================
Matemáticas Discretas I — Universidad Nacional de Colombia
Docente: Jhoan Sebastian Tenjo García

DESCRIPCIÓN MATEMÁTICA:
    Se quiere ir desde la esquina (0, 0) hasta la esquina (a, b)
    de una grilla rectangular, moviéndose SOLO hacia la derecha (→)
    o hacia arriba (↑).

    Un camino mínimo tiene exactamente (a + b) pasos:
        - 'a' pasos hacia la derecha
        - 'b' pasos hacia arriba

    El problema se reduce a: ¿de cuántas formas se pueden elegir
    las posiciones de los 'a' pasos a la derecha (o equivalentemente
    los 'b' pasos hacia arriba) dentro de los (a+b) pasos totales?

FÓRMULA:
    C(a+b, a) = (a+b)! / (a! * b!)

    Lo cual es simplemente el coeficiente binomial C(a+b, a) = C(a+b, b).

ALGORITMO PRINCIPAL:
    1. Validar que a y b sean enteros no negativos.
    2. Calcular C(a+b, a) usando la fórmula del coeficiente binomial.

ALGORITMO CON PUNTOS OBLIGATORIOS:
    Si el camino debe pasar por puntos intermedios (x1,y1), (x2,y2)...,
    se multiplican los caminos entre segmentos consecutivos:
        caminos = C(x1+y1, x1) * C((x2-x1)+(y2-y1), x2-x1) * ...

ALGORITMO CON PUNTOS BLOQUEADOS (programación dinámica):
    Se construye una tabla dp[i][j] = número de caminos hasta (i,j)
    marcando como 0 las celdas bloqueadas.
        dp[i][j] = dp[i-1][j] + dp[i][j-1]   si (i,j) no está bloqueado
        dp[i][j] = 0                            si (i,j) está bloqueado

EFICIENCIA:
    - Fórmula directa C(a+b, a): O(min(a,b)) multiplicaciones.
    - Programación dinámica para puntos bloqueados: O(a*b) tiempo y espacio.
    - Para grillas muy grandes con puntos bloqueados, la DP es la única opción.
=============================================================
""")

# ─────────────────────────────────────────────
# 2. VALIDACIÓN DE ENTRADAS
# ─────────────────────────────────────────────

def validar_coordenadas(a, b, nombre_a="a", nombre_b="b") -> None:
    """Verifica que a y b sean enteros no negativos."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"{nombre_a} y {nombre_b} deben ser enteros.")
    if a < 0 or b < 0:
        raise ValueError(f"{nombre_a} y {nombre_b} deben ser no negativos. "
                         f"Se recibió {nombre_a}={a}, {nombre_b}={b}.")

# ─────────────────────────────────────────────
# 3. COEFICIENTE BINOMIAL 
# ─────────────────────────────────────────────

def binomial(n: int, k: int) -> int:
    """
    Calcula C(n, k) = n! / (k! * (n-k)!) de forma eficiente.
    Usa la librería estándar math.comb (Python >= 3.8).
    Complejidad: O(min(k, n-k)) multiplicaciones.
    """
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

# ─────────────────────────────────────────────
# 4. CAMINOS 
# ─────────────────────────────────────────────

# 4.1 CAMINOS MÍNIMOS 

def caminos_minimos(a: int, b: int, mostrar_procedimiento: bool = True) -> int:
    """
    Cuenta los caminos mínimos de (0,0) a (a,b) moviéndose → o ↑.

    Fórmula: C(a+b, a) = (a+b)! / (a! * b!)

    Parámetros:
        a (int): Número de pasos a la derecha (>= 0).
        b (int): Número de pasos hacia arriba (>= 0).
        mostrar_procedimiento (bool): Imprime el desarrollo.

    Retorna:
        int: Número de caminos mínimos.
    """
    validar_coordenadas(a, b)
    total_pasos = a + b
    resultado = binomial(total_pasos, a)

    if mostrar_procedimiento:
        print(f"\n  Caminos de (0,0) a ({a},{b}):")
        print(f"  Total de pasos : {a} + {b} = {total_pasos}")
        print(f"  Fórmula        : C({total_pasos}, {a}) = {total_pasos}! / ({a}! × {b}!)")
        print(f"                 = {math.factorial(total_pasos)} / "
              f"({math.factorial(a)} × {math.factorial(b)})")
        print(f"                 = {resultado}")
        print(f"  Verificación   : C({total_pasos},{b}) = {binomial(total_pasos, b)} "
              f"{'✓' if binomial(total_pasos, b) == resultado else '✗'}")

    return resultado

# 4.2 CAMINOS CON PUNTOS OBLIGATORIOS

def caminos_con_puntos_obligatorios(
    a: int, b: int, puntos: list, mostrar_procedimiento: bool = True
) -> int:
    """
    Cuenta caminos de (0,0) a (a,b) que pasan por una lista de puntos intermedios.

    Los puntos deben estar en orden de recorrido (de menor a mayor coordenada).
    Se valida que cada punto sea alcanzable desde el anterior.

    Parámetros:
        a, b   : Destino.
        puntos : Lista de tuplas (x, y) intermedias, en orden.

    Retorna:
        int: Producto de caminos entre segmentos consecutivos.
    """
    validar_coordenadas(a, b)

    # Construir la ruta completa: origen → puntos → destino
    ruta = [(0, 0)] + puntos + [(a, b)]

    if mostrar_procedimiento:
        print(f"\n  Caminos de (0,0) a ({a},{b}) pasando por {puntos}:")

    resultado = 1
    for idx in range(len(ruta) - 1):
        x1, y1 = ruta[idx]
        x2, y2 = ruta[idx + 1]
        dx = x2 - x1
        dy = y2 - y1

        if dx < 0 or dy < 0:
            raise ValueError(
                f"El punto {ruta[idx+1]} no es alcanzable desde {ruta[idx]} "
                f"moviéndose solo → o ↑."
            )

        tramo = binomial(dx + dy, dx)
        resultado *= tramo

        if mostrar_procedimiento:
            print(f"  Tramo {ruta[idx]} → {ruta[idx+1]} : C({dx+dy},{dx}) = {tramo}")

    if mostrar_procedimiento:
        print(f"  Total : {' × '.join(str(binomial(ruta[i+1][0]-ruta[i][0]+ruta[i+1][1]-ruta[i][1], ruta[i+1][0]-ruta[i][0])) for i in range(len(ruta)-1))} = {resultado}")

    return resultado

# 4.3 CAMINOS CON PUNTOS BLOQUEADOS (DP)

def caminos_con_bloqueados(
    a: int, b: int, bloqueados: list, mostrar_grilla: bool = True
) -> int:
    """
    Cuenta caminos de (0,0) a (a,b) evitando celdas bloqueadas.
    Usa programación dinámica: dp[i][j] = número de caminos hasta (i,j).

    Parámetros:
        a, b       : Destino.
        bloqueados : Lista de tuplas (x, y) que no pueden visitarse.

    Retorna:
        int: Número de caminos válidos.
    """
    validar_coordenadas(a, b)
    bloqueados_set = set(bloqueados)

    if (0, 0) in bloqueados_set:
        raise ValueError("El origen (0,0) está bloqueado.")
    if (a, b) in bloqueados_set:
        raise ValueError(f"El destino ({a},{b}) está bloqueado.")

    # Tabla dp indexada como dp[columna][fila] → dp[x][y]
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[0][0] = 1

    for x in range(a + 1):
        for y in range(b + 1):
            if (x, y) in bloqueados_set:
                dp[x][y] = 0
                continue
            if x == 0 and y == 0:
                continue
            desde_izq  = dp[x - 1][y] if x > 0 else 0
            desde_abajo = dp[x][y - 1] if y > 0 else 0
            dp[x][y] = desde_izq + desde_abajo

    if mostrar_grilla and a <= 10 and b <= 10:
        print(f"\n  Grilla de caminos (0,0)→({a},{b}) con bloqueados {bloqueados}:")
        print(f"  (Las celdas muestran cuántos caminos llegan a ese punto)")
        print()
        for y in range(b, -1, -1):
            fila = ""
            for x in range(a + 1):
                if (x, y) in bloqueados_set:
                    fila += "  [X]"
                elif x == 0 and y == 0:
                    fila += "  [S]"
                elif x == a and y == b:
                    fila += f" [{dp[x][y]:2d}]"
                else:
                    fila += f"  {dp[x][y]:3d}"
            print(f"  y={y} |{fila}")
        print(f"       " + "─" * (5 * (a + 1)))
        print(f"        " + "  ".join(f"x={x}" for x in range(a + 1)))

    return dp[a][b]

# ─────────────────────────────────────────────
# 5. PRESENTACIÓN
# ─────────────────────────────────────────────

# 5.1 MOSTRAR ALGORITMO

def mostrar_algoritmo():

    print("""
════════════════════════════════════════════════════

ALGORITMO

CASO BÁSICO

1. Validar entradas.
2. Calcular:

   C(a+b,a)

3. Mostrar resultado.

PUNTOS OBLIGATORIOS

1. Dividir el recorrido en segmentos.
2. Calcular los caminos de cada segmento.
3. Multiplicar resultados.

PUNTOS BLOQUEADOS

1. Construir tabla DP.
2. Marcar bloqueos.
3. Aplicar:

   dp[i][j] =
   dp[i-1][j] + dp[i][j-1]

════════════════════════════════════════════════════
""")
    
# 5.2 MOSTRAR EJEMPLOS
    
def mostrar_ejemplos():

    print("\nEJEMPLO 1")
    caminos_minimos(3, 2)

    print("\nEJEMPLO 2")
    caminos_minimos(4, 6)

    print("\nEJEMPLO 3")
    caminos_con_puntos_obligatorios(
        4,
        4,
        [(2,2)]
    )

# 5.3 MOSTRAR OPCIONES

def volver_o_salir():

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
# 6. PRUEBAS
# ─────────────────────────────────────────────

def ejecutar_pruebas() -> None:
    """Ejecuta al menos 5 pruebas con distintos valores de entrada."""

    print("\n" + "═"*60)
    print("  PRUEBAS — Caminos mínimos C(a+b, a)")
    print("═"*60)

    # Casos normales
    casos = [
        (2,  2,  6,      "Grilla 2×2 clásica"),
        (3,  2,  10,     "Grilla 3×2"),
        (4,  4,  70,     "Grilla 4×4"),
        (0,  5,  1,      "Solo subir (a=0)"),
        (5,  0,  1,      "Solo derecha (b=0)"),
        (1,  1,  2,      "Grilla 1×1 (2 caminos)"),
        (10, 5,  3003,   "Grilla 10×5"),
    ]

    aprobadas = 0
    for a, b, esperado, descripcion in casos:
        try:
            resultado = caminos_minimos(a, b, mostrar_procedimiento=False)
            estado = "✓ PASS" if resultado == esperado else f"✗ FAIL (esperado {esperado})"
            if resultado == esperado:
                aprobadas += 1
        except Exception as e:
            resultado = None
            estado = f"✗ ERROR: {e}"
        print(f"  C({a+b},{a}) = {str(resultado):>6}  |  {estado}  |  {descripcion}")

    print(f"\n  Resultado: {aprobadas}/{len(casos)} pruebas aprobadas.")

    # Casos especiales
    print("\n" + "─"*60)
    print("  VALIDACIÓN DE CASOS ESPECIALES")
    print("─"*60)

    casos_invalidos = [
        (-1, 2, "a negativo"),
        (3, -1, "b negativo"),
    ]
    for a, b, desc in casos_invalidos:
        try:
            caminos_minimos(a, b, mostrar_procedimiento=False)
            print(f"  ({a},{b}) → ✗ Debería haber lanzado error ({desc})")
        except (ValueError, TypeError) as e:
            print(f"  ({a},{b}) → ✓ Error capturado ({desc}): {e}")

    # Prueba con puntos obligatorios
    print("\n" + "─"*60)
    print("  PRUEBA — Puntos obligatorios")
    print("─"*60)
    resultado = caminos_con_puntos_obligatorios(4, 4, [(2, 2)], mostrar_procedimiento=True)
    print(f"  Caminos de (0,0) a (4,4) pasando por (2,2) = {resultado}")
    sin_restriccion = caminos_minimos(4, 4, mostrar_procedimiento=False)
    print(f"  Caminos totales sin restricción = {sin_restriccion}")
    print(f"  Los que pasan por (2,2) representan el {100*resultado/sin_restriccion:.1f}% del total.")

    # Prueba con puntos bloqueados
    print("\n" + "─"*60)
    print("  PRUEBA — Puntos bloqueados (DP)")
    print("─"*60)
    resultado_bloq = caminos_con_bloqueados(3, 3, [(1, 2), (2, 1)], mostrar_grilla=True)
    resultado_libre = caminos_minimos(3, 3, mostrar_procedimiento=False)
    print(f"\n  Caminos de (0,0) a (3,3) bloqueando (1,2) y (2,1): {resultado_bloq}")
    print(f"  Caminos sin bloqueos: {resultado_libre}")
    print(f"  Caminos eliminados por los bloqueos: {resultado_libre - resultado_bloq}")

# ─────────────────────────────────────────────
# 7. CALCULADORA
# ─────────────────────────────────────────────

def menu_calculadora():

    while True:

        print("\n" + "═"*60)
        print("CALCULADORA DE CAMINOS MÍNIMOS")
        print("═"*60)

        print("1. Caminos básicos")
        print("2. Caminos con puntos obligatorios")
        print("3. Caminos con puntos bloqueados")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "0":
            return

        try:

            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))

        except ValueError:

            print("Entrada inválida.")
            continue

        try:

            if opcion == "1":

                resultado = caminos_minimos(
                    a,
                    b,
                    mostrar_procedimiento=True
                )

            elif opcion == "2":

                raw = input(
                    "Puntos obligatorios "
                    "(x1,y1 x2,y2 ...): "
                ).strip()

                puntos = (
                    [tuple(map(int, p.split(",")))
                     for p in raw.split()]
                    if raw else []
                )

                resultado = caminos_con_puntos_obligatorios(
                    a,
                    b,
                    puntos,
                    mostrar_procedimiento=True
                )

            elif opcion == "3":

                raw = input(
                    "Bloqueados "
                    "(x1,y1 x2,y2 ...): "
                ).strip()

                bloqueados = (
                    [tuple(map(int, p.split(",")))
                     for p in raw.split()]
                    if raw else []
                )

                resultado = caminos_con_bloqueados(
                    a,
                    b,
                    bloqueados,
                    mostrar_grilla=True
                )

            else:

                print("Opción inválida.")
                continue

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

# ─────────────────────────────────────────────
# 8. MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():

    while True:

        print("\n")
        print("╔══════════════════════════════════════════════╗")
        print("║     CAMINOS MÍNIMOS EN UNA GRILLA           ║")
        print("╚══════════════════════════════════════════════╝")

        print("1. Ver descripción matemática")
        print("2. Ver algoritmo")
        print("3. Ver ejemplos")
        print("4. Ejecutar pruebas")
        print("5. Usar calculadora")
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

            ejecutar_pruebas()

            if not volver_o_salir():
                break

        elif opcion == "5":

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