# Variables globales
global tamañoTablero
tamañoTablero = 8

#funcion para llenar el tablero por primera vez
def llenarTablero(tamañoTablero):
    lista = []
    for i in range(tamañoTablero):
        lista.append(0)
    return lista

def analizandolados(tablero,fila,columna):
    N = len(tablero)
    #izquierda
    for i in range(columna):
        if(tablero[fila][i] == "R"):
            return False

    #derecha
    for i in range(columna,N,1):
        if(tablero[fila][i] == "R"):
            return False

    #diagonal superior izquierda
    for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False
        
    #diagonal superior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,N,1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior izquierda
    for f,c in zip(range(fila,N,1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,N,1)):
        if(tablero[f][c] == "R"):
            return False

    return True

def columnaLlena(tablero,columna):
    N = len(tablero)
    for i in range(N):
        if(tablero[i][columna] == "R"):
            return False
    return True


def acomodandoReinas(tablero,columna):
    N = len(tablero)
    if columna >= N:
        return False

    for i in range(N):
        if(columnaLlena(tablero,columna) == True):
            if(analizandolados(tablero,i,columna) == True):
                tablero[i][columna] = "R"
                acomodandoReinas(tablero,columna + 1)
            else:
                tablero[i][columna] = 0
        else:
            acomodandoReinas(tablero,columna + 1)
        

def solucion(tablero): 
	for i in range(tamañoTablero): 
		for j in range(tamañoTablero): 
			print (tablero[i][j], end = " ") 
		print()

#funcion principal donde se va a ejecutar todo
def principal():
    tablero = []
    for i in range(tamañoTablero):
        tablero.append(llenarTablero(tamañoTablero))

    #Colocando a la primera reina
    #nomre   fila columna = "R"
    #tablero [1]    [0]   = "R"
    tablero[7][0] = "R"
    #Acomodando las demas reinas
    acomodandoReinas(tablero,1)
    # print(tablero)
    solucion(tablero)

principal()