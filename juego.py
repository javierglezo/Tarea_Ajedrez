# Dimensión del tablero
filas = 8
columnas = 8

# Crear el tablero con espacios vacios
tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Colocar fichas blancas  
tablero[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
tablero[1] = ['♟'] * 8

# Colocar fichas negras
tablero[6] = ['♙'] * 8
tablero[7] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']


def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))


def guardar_tablero_en_fichero(nombre_fichero, tablero):
    with open(nombre_fichero, 'a') as fichero:
        for fila in tablero:
            fichero.write('\t'.join(fila) + '\n')
        fichero.write('\n')  

# Pedir nombre del fichero
nombre_fichero = input("Introduce el nombre del fichero para guardar la partida: ")

# Guardar el tablero inicial en el fichero
guardar_tablero_en_fichero(nombre_fichero, tablero)



# Función para mover fichas indefinidamente
def jugar():
    while True:
        jugar_fichas = input("¿Desea hacer un movimiento? (s/n): \nAyuda mover fichas (a): \nTu respuesta: ").lower()

        if jugar_fichas == 's':
            imprimir_tablero(tablero)

        # Mover fichas
            try:
                fila_origen = int(input("Fila de la pieza que desea mover: "))
                col_origen = int(input("Columna de la pieza que desea mover: "))
                fila_destino = int(input("Fila a la que desea mover la pieza: "))
                col_destino = int(input("Columna a la que desea mover la pieza: "))
            except ValueError:
                print("Entrada no válida. Introduzca valores numéricos.")
                continue

            # Hacer movimiento y guardar tablero en el fichero
            tablero[fila_destino][col_destino] = tablero[fila_origen][col_origen]
            tablero[fila_origen][col_origen] = ' '
            guardar_tablero_en_fichero(nombre_fichero, tablero)

        if jugar_fichas == 'n':
            print("Partida finalizada. Tablero final:")
            imprimir_tablero(tablero)
            quit()

        if jugar_fichas == 'a':
            print("Peones -(Mueven 1fila), \nAlfiles -(Avanzan en diagonal), \nCaballos -(Mueven 1columna 2filas), \nTorres -(Mueven por su columna o fila), \nReina -(Mueve línea recta por las filas, columnas y diagonales en el tablero)")



