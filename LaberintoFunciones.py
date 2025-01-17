import random

FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def inicializar_laberinto():
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    return laberinto

def imprimir_laberinto(laberinto, fila_jugador, columna_jugador):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end='')  # Jugador
            elif laberinto[i][j]:
                print("O ", end='')  # Meta
            else:
                print(". ", end='')  # Espacio vacío
        print()

def verificar_meta(fila_jugador, columna_jugador):
    return fila_jugador == META_FILA and columna_jugador == META_COLUMNA

def obtener_movimiento():
    return input("\nIngrese su siguiente movimiento (w: arriba, s: abajo, a: izquierda, d: derecha): ")

def mover_jugador(fila_jugador, columna_jugador, movimiento):
    if movimiento == 'p' and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == 's' and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == 'a' and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == 'd' and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    else:
        print("Movimiento no válido.")
    return fila_jugador, columna_jugador
#12_03-24