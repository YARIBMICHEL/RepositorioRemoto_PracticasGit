from LaberintoFunciones import *
def main():
    laberinto = inicializar_laberinto()
    fila_jugador, columna_jugador = 0, 0

    while True:
        imprimir_laberinto(laberinto, fila_jugador, columna_jugador)

        if verificar_meta(fila_jugador, columna_jugador):
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break
        movimiento = obtener_movimiento()
        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador, movimiento)

if __name__ == "__main__":
    main()
    #12_03-24