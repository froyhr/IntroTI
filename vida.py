#!/usr/bin/env python3
import os
import random
import time

FILAS, COLS = 25, 60
tablero = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(FILAS)]

def contar_vecinos(r, c):
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % FILAS, (c + dc) % COLS
            total += tablero[nr][nc]
    return total

os.system("clear")
print("\033[?25l", end="")  # Oculta el cursor de la terminal

try:
    generacion = 0
    while True:
        print("\033[H", end="")  # Reposiciona el cursor arriba sin limpiar toda la pantalla
        salida = [f"Juego de la Vida de Conway | Generación: {generacion} | Presiona Ctrl+C para salir\n"]
        for r in range(FILAS):
            linea = "".join("█" if tablero[r][c] else " " for c in range(COLS))
            salida.append(linea)
        print("\n".join(salida))

        nuevo_tablero = [[0] * COLS for _ in range(FILAS)]
        for r in range(FILAS):
            for c in range(COLS):
                v = contar_vecinos(r, c)
                if tablero[r][c] == 1 and v in (2, 3):
                    nuevo_tablero[r][c] = 1
                elif tablero[r][c] == 0 and v == 3:
                    nuevo_tablero[r][c] = 1
        tablero = nuevo_tablero
        generacion += 1
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\033[?25h\nSimulación detenida por el usuario.")
