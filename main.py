import random

def generar_tablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    resolver_tablero(tablero)
    vaciar_casillas(tablero)
    return tablero

def resolver_tablero(tablero):
    if not encontrar_vacia(tablero):
        return True

    fila, columna = encontrar_vacia(tablero)
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numeros)

    for num in numeros:
        if es_valido(tablero, fila, columna, num):
            tablero[fila][columna] = num

            if resolver_tablero(tablero):
                return True

            tablero[fila][columna] = 0

    return False

def encontrar_vacia(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return None

def es_valido(tablero, fila, columna, num):
    for i in range(9):
        if tablero[fila][i] == num or tablero[i][columna] == num:
            return False

    fila_inicio = (fila // 3) * 3
    columna_inicio = (columna // 3) * 3

    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if tablero[i][j] == num:
                return False

    return True

def vaciar_casillas(tablero):
    casillas_vacias = random.randint(50, 60)
    contador = 0

    while contador < casillas_vacias:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)

        if tablero[fila][columna] != 0:
            tablero[fila][columna] = 0
            contador += 1

def imprimir_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == 0:
                print("_", end=" ")
            else:
                print(elemento, end=" ")
        print()

def main():
    
    # Generar un tablero de Sudoku
    tablero = generar_tablero()

    # Imprimir el tablero generado
    print("Tablero generado:")
    imprimir_tablero(tablero)

    while True:
        # Preguntar al usuario si desea resolver el Sudoku
        respuesta = input("¿Deseas resolver este Sudoku? (si/no): ")

        if respuesta.lower() == "si":
            resolver_tablero(tablero)
            print("\nSudoku resuelto:")
            imprimir_tablero(tablero)
            print("¡Hasta luego!")
        
        else:
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")

if __name__ == "__main__":
    main()