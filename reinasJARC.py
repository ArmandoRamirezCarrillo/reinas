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
    #izquierda
    for i in range(columna):
        if(tablero[fila][i] == "R"):
            return False

    #derecha
    for i in range(columna,tamañoTablero,1):
        if(tablero[fila][i] == "R"):
            return False

    #diagonal superior izquierda
    for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False
        
    #diagonal superior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamañoTablero,1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior izquierda
    for f,c in zip(range(fila,tamañoTablero,1), range(columna,-1,-1)):
        if(tablero[f][c] == "R"):
            return False

    #diagonal inferior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamañoTablero,1)):
        if(tablero[f][c] == "R"):
            return False

    return True

#Verifica si la columna ya tiene o no una Reina
def columnaLlena(tablero,columna):
    for i in range(tamañoTablero):
        if(tablero[i][columna] == "R"):
            return True
    return False

def acomodandoReinas(tablero, columna):
    if(columna >= tamañoTablero):
        return True
    
    if(columnaLlena(tablero,columna) == True):
        if(acomodandoReinas(tablero, columna + 1) == True):
            return True
        
    for i in range(tamañoTablero):
        if(analizandolados(tablero,i,columna)):
            tablero[i][columna] = "R"
            if(acomodandoReinas(tablero,columna + 1) == True):
                return True
            tablero[i][columna] = 0
        tablero[i][columna] = 0
    return False

#Imprime el tablero de ajedrez, con la solucion
def tableroAjedrez(tablero): 
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
    tablero[0][0] = "R"

    #Acomodando las demas reinas
    if(acomodandoReinas(tablero,0) == True):
        tableroAjedrez(tablero)
        print("\nPrograma Finalizado")
        print("\nJose Armando Ramirez Carrillo")
        return True

principal()