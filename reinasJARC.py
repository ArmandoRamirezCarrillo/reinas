# Variables globales
# global numReinas
# numReinas = 0

#funcion para llenar el tablero por primera vez
def llenarTablero(tamaño):
    lista = []

    for i in range(tamaño):
        lista.append(0)
    return lista

def analizandolados(tablero,fila,columna):
    tamaño = len(tablero)

    #izquierda
    for i in range(columna):
        if(tablero[fila][i] == "R"):
            return False

    #derecha
    for i in range(columna,tamaño,1):
        if(tablero[fila][i] == "R"):
            return False

    #diagonal superior izquierda
    for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False
        
    #diagonal superior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamaño,1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior izquierda
    for f,c in zip(range(fila,tamaño,1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamaño,1)):
        if(tablero[f][c] == "R"):
            return False

    return True

#Verifica si la columna ya tiene o no una Reina
def columnaLlena(tablero,columna):
    tamaño = len(tablero)
    for i in range(tamaño):
        if(tablero[i][columna] == "R"):
            return True
    return False

def acomodandoReinas(tablero, columna):
    tamaño = len(tablero)
    if(columna >= tamaño):
        return True
    
    if(columnaLlena(tablero,columna) == True):
        if(acomodandoReinas(tablero, columna + 1) == True):
            return True
        
    for i in range(tamaño):
        if(analizandolados(tablero,i,columna)):
            tablero[i][columna] = "R"
            if(acomodandoReinas(tablero,columna + 1) == True):
                return True
            tablero[i][columna] = 0
        tablero[i][columna] = 0
    return False

#Imprime el tablero de ajedrez, con la solucion
def tableroAjedrez(tablero,tamaño):
    for i in range(tamaño):
        for j in range(tamaño):
            print(tablero[i][j], end = " ")
        print()

#funcion principal donde se va a ejecutar todo
def principal():
    tamaño = int(input("Escribe el tamaño del tablero: "))

    tablero = []

    for i in range(tamaño):
        tablero.append(llenarTablero(tamaño))

    #Colocando a la primera reina
    tablero[0][0] = "R"

    #Acomodando las demas reinas
    if(acomodandoReinas(tablero,0) == True):
        tableroAjedrez(tablero,tamaño)
        print("\nPrograma Finalizado")
        print("\nJose Armando Ramirez Carrillo")
        return True
    else:
        print("\nSe hizo todo lo posible, pero no hay solucion")
        return False

principal()