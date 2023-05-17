import pygame
# import random
from typing import List, Tuple

# Globales
SIZE = [800, 800]
CUADRADO_ALTO = 40
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (102, 204, 0)
FONDO = (24, 25, 30)
MATRIZ_OBSTACULOS = list()
MATRIZ_MEMORIA = list()
LISTA_MEMORIA = list() # Lista de posiciones visitadas
CHECKPOINT = pygame.image.load("assets/checkPoint.jpg")
THIEF = pygame.image.load("assets/ladron.png")
THIEF_RED = pygame.image.load("assets/ladron_closed.png")
THIEF_GREEN = pygame.image.load("assets/ladron_open.png")
OBSTACULO = pygame.image.load("assets/obtaculo.jpg")
VISITADO_X, VISITADO_Y = 0,0
VISITADOS_RUTA = list()
# Posición inicial de avatar
X_1, Y_1 = 0,0

# crear matriz de obstáculos
for i in range(0, 20):
    MATRIZ_OBSTACULOS2 = list()
    for j in range(0, 20):
        MATRIZ_OBSTACULOS2.append(0)
    MATRIZ_OBSTACULOS.append(MATRIZ_OBSTACULOS2)

def buscarVecinos(x_1, y_1):
    vecinos = list()
    # 8 POSICIONES
    for i in range(-1, 2):
        if i == -1 or i == 1: # izq, der, diagonal
            for j in range(-1, 2):
                # BORDE
                if x_1+i < 0 or y_1+j < 0  or x_1+i > 19 or y_1+j > 19: 
                    vecinos = vecinos
                # OBSTÁCULO
                elif MATRIZ_OBSTACULOS[x_1+i][y_1+j] == -1:
                    vecinos = vecinos
                # No regresar a la posición pasada
                # elif X_1+i == VISITADO_X and Y_1+j == VISITADO_Y: 
                #     vecinos = vecinos
                # MOVIMIENTO NORMAL
                else:                   
                    vecinos.append({'g':0, 'f':0, 'h':0, 'x':x_1+i, 'y':y_1+j, 'padre': [x_1, y_1]})
                    # lista_abierta.append({'costo':distancia_meta, 'x':X_1+i, 'y':Y_1+j, 'padre_X': X_1, 'padre_y':Y_1})
                    # lista.append({'costo':MATRIZ_MEMORIA[X_1+i][Y_1+j], 'x':X_1+i, 'y':Y_1+j, 'visitado':0})

        if i == 0:
            for j in range(-1, 2, 2): # arriba, abajo
                if y_1+j < 0 or y_1+j > 19:
                    vecinos = vecinos
                elif MATRIZ_OBSTACULOS[x_1+i][y_1+j] == -1:
                    vecinos = vecinos
                # elif X_1+i == VISITADO_X and Y_1+j == VISITADO_Y:
                #     vecinos = vecinos
                else:
                    vecinos.append({'g':0, 'f':0, 'h':0, 'x':x_1+i, 'y':y_1+j, 'padre': [x_1, y_1]})
        # 8 POSICIONES
    return vecinos

def casilla(x_1, y_1):
    f=0
    g=0
    h=0
    padre = [None]
    vecinos = buscarVecinos(x_1, y_1)

    casilla = {'g':g, 'f':f, 'h':h, 'x':x_1, 'y':y_1, 'padre': padre}

    return [casilla, vecinos]

# crear matriz de algoritmo para Dijksra
for i in range(0, 20):
    MATRIZ_MEMORIA2 = list()
    for j in range(0, 20):
        MATRIZ_MEMORIA2.append(0)
    MATRIZ_MEMORIA.append(MATRIZ_MEMORIA2)

# for i in range(0, 20):
#     for j in range(0, 20):
#         MATRIZ_MEMORIA[i][j] = casilla(i,j)[0]

def llenarFondo(screen:pygame.Surface, screen2:pygame.Surface):
    screen.fill(FONDO)
    color = 0
    k = 0
    m = 0

    for i in range(0, SIZE[0], CUADRADO_ALTO):
        k = int(i/40)
        for j in range(0, SIZE[1], CUADRADO_ALTO):
            m = int(j/40)
            # Avatar
            if MATRIZ_OBSTACULOS[k][m] == 88:
                thiefrect = THIEF_RED.get_rect()
                thiefrect.move_ip(i, j)
                screen2.blit(THIEF_RED, thiefrect)
            elif MATRIZ_OBSTACULOS[k][m] == 89:
                thiefrect = THIEF_GREEN.get_rect()
                thiefrect.move_ip(i, j)
                screen2.blit(THIEF_GREEN, thiefrect)
            elif MATRIZ_OBSTACULOS[k][m] == 90:
                thiefrect = THIEF.get_rect()
                thiefrect.move_ip(i, j)
                screen2.blit(THIEF, thiefrect)
            # Obstaculo
            elif MATRIZ_OBSTACULOS[k][m] == -1:
                obstaculorect = OBSTACULO.get_rect()
                obstaculorect.move_ip(i, j)
                screen.blit(OBSTACULO, obstaculorect)
            # checkPoint
            elif MATRIZ_OBSTACULOS[k][m] == 25:
                pygame.draw.rect(screen, VERDE, [i, j, CUADRADO_ALTO, CUADRADO_ALTO], 0, 2)
            else:
            # Fondo blanco y negro
                if color%2 == 0 and MATRIZ_OBSTACULOS[k][m] == 0:
                    pygame.draw.rect(screen, NEGRO, [i, j, CUADRADO_ALTO, CUADRADO_ALTO], 0, 2)
                else:
                    pygame.draw.rect(screen, BLANCO, [i, j, CUADRADO_ALTO, CUADRADO_ALTO], 0, 2)
            color += 1
        color += 1

    pygame.display.update()
    return screen

def guardarCheckPoint(x, y, screen, screen2):
    x = int(x/40)
    y = int(y/40)
    for i in range(0, 20):
        for j in range(0, 20):
            # BORRAR SI YA EXISTE
            if MATRIZ_OBSTACULOS[i][j] == 25:
                MATRIZ_OBSTACULOS[i][j] = 0
            elif [i, j] == [x, y]:
            # LIBRE
                if MATRIZ_OBSTACULOS[x][y] == 0 and MATRIZ_OBSTACULOS[x][y] != 25 and MATRIZ_OBSTACULOS[x][y] != 88:
                    MATRIZ_OBSTACULOS[x][y] = 25
                    buscar_ruta_2(x,y, screen, screen2)
                    # buscar_ruta(0,x,y)
            # OCUPADO
                else:
                    MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
            else:
                MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]

def guardarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)

    for i in range(0, 20):
        for j in range(0, 20):
            if [i, j] == [x, y]:
                # Si se coloca encima del avatar
                if MATRIZ_OBSTACULOS[x][y] == 88 or MATRIZ_OBSTACULOS[i][j] == 25:
                    MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
                else:
                    MATRIZ_OBSTACULOS[x][y] = -1

def eliminarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)
    # print(x, y)
    for i in range(0, 20):
        for j in range(0, 20):
            if [i, j] == [x, y] and MATRIZ_OBSTACULOS[x][y] == -1:
                MATRIZ_OBSTACULOS[x][y] = 0
    
def nuevo_objeto(clicks:Tuple, screen, screen2):
    if clicks[0]:
        mouse = pygame.mouse.get_pos()
        key_checkPoint = pygame.key.get_pressed()
        x = (mouse[0]//40)*40
        y = (mouse[1]//40)*40
        
        if key_checkPoint[pygame.K_LSHIFT]:
            guardarCheckPoint(x, y, screen, screen2)
        else:
            guardarObstaculo(x, y)

    if clicks[2]:
        mouse = pygame.mouse.get_pos()
        x = (mouse[0]//40)*40
        y = (mouse[1]//40)*40
        eliminarObstaculo(x, y)

    llenarFondo(screen, screen2)

def dijkstra(x_2, y_2, x_1, y_1):
    distancia_x = int(((x_1)-x_2))
    distancia_y = int(((y_1)-y_2))
    distancia_meta = int(pow(distancia_x,2)+pow(distancia_y,2))
    distancia_meta = int(distancia_meta**(.5))
    
    return distancia_meta

def dibujar_camino_final():
    global VISITADOS_RUTA
    print("final")

    for i in range(len(VISITADOS_RUTA)):
        x = VISITADOS_RUTA[i]['x']
        y = VISITADOS_RUTA[i]['y']
        MATRIZ_OBSTACULOS[x][y] = 90

def buscar_ruta_2(x_2, y_2, screen, screen2):
    global X_1
    global Y_1
    global VISITADO_X
    global VISITADO_Y
    global VISITADOS_RUTA
    lista_abierta = list()
    lista_cerrada = list()
    terminado = False
    
    padre = casilla(X_1, Y_1)[0]
    lista_abierta.append(padre)
    
    while terminado != True:

        # Usar siempre el menor de la lista
        if len(lista_abierta) > 0:
            menor = 0
            for i in range(len(lista_abierta)):
                # Si el menor costo se repite, tomar el primero
                if lista_abierta[i]['f'] < lista_abierta[menor]['f']:
                    menor = i
            actual = lista_abierta[menor]
            
            # Si llegamos a la meta
            if (actual['x'], actual['y']) == (x_2, y_2):
                lista_cerrada.append(actual)
                print("You Win!")
                temp_hijo = actual
                print("Meta: ", actual)
                VISITADOS_RUTA.append(temp_hijo)
                # Recorrer cada padre
                while (temp_hijo['padre'] != [None]): # 3,3
                    x_padre = temp_hijo['padre'][0] # 2,2
                    y_padre = temp_hijo['padre'][1]
                    print("temp_hijo: ",temp_hijo)
                    for i in range(len(lista_cerrada)):
                        # Padre de variable temp en lista_cerrada
                        if (lista_cerrada[i]['x'], lista_cerrada[i]['y']) == (x_padre, y_padre):
                            print("padre: ",lista_cerrada[i])
                            print("abuelo: ",lista_cerrada[i]['padre'])
                            # El padre ahora es hijo
                            temp_hijo = lista_cerrada[i]
                            print("Nuevo temp_hijo: ", temp_hijo)
                            VISITADOS_RUTA.append(temp_hijo)
                
                dibujar_camino_final()
                terminado = True
                
            else:
                lista_abierta.remove(actual)
                lista_cerrada.append(actual)
                x_1 = actual['x']
                y_1 = actual['y']
                # Vecinos de la casilla de menor costo en lista_abierta
                vecinos:List = casilla(x_1, y_1)[1]

                for i in range(len(vecinos)):
                    vecino = vecinos[i]
                    cerrado = False
                    # if vecino not in lista_cerrada:
                    for j in range(len(lista_cerrada)):
                        if (vecino['x'], vecino['y']) == (lista_cerrada[j]['x'], lista_cerrada[j]['y']):
                            cerrado = True
                            # print("\nVecino en lista cerrada", vecino)

                    if cerrado == False:
                        # print("\nNo cerrado...", vecino)
                        temp = actual['g']+1
                        abierto = False

                        for k in range(len(lista_abierta)):
                            if (vecino['x'], vecino['y']) == (lista_abierta[k]['x'], lista_abierta[k]['y']):
                                abierto = True
                            
                        # Si el vecino está en la lista y su peso es mayor
                        if abierto:
                            # print("Lista abierta...",vecino)
                            if temp < vecino['g']:
                                # Camino más corto a vecino encontrado
                                vecino['g'] = temp
                        else:
                            # print("Libre...")
                            vecino['g'] = temp
                            lista_abierta.append(vecino)

                        vecino['h'] = dijkstra(x_2, y_2, vecino['x'], vecino['y'])
                        vecino['f'] = vecino['g']+vecino['h']
                        vecino['padre'] = [x_1, y_1]
                # vecinos.clear()
                
                # Guardar en matriz para dibujar
                for i in range(len(lista_abierta)):
                    x = lista_abierta[i]['x']
                    y = lista_abierta[i]['y']
                    MATRIZ_OBSTACULOS[x][y] = 89
                    
                for i in range(len(lista_cerrada)):
                    x = lista_cerrada[i]['x']
                    y = lista_cerrada[i]['y']
                    MATRIZ_OBSTACULOS[x][y] = 88

                llenarFondo(screen, screen2)
                    
        else:
            terminado = True
        

def main():
    # Inicializar pygame
    pygame.init()
    # Ventanas
    screen = pygame.display.set_mode(SIZE)
    screen2 = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Juego 1")
    clock = pygame.time.Clock()
    # Crear objetos 
    MATRIZ_OBSTACULOS[int(X_1)][int(Y_1)] = 89
    llenarFondo(screen, screen2)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# Eventos
        clicks = pygame.mouse.get_pressed()
        if clicks:
            nuevo_objeto(clicks, screen, screen2)
# Eventos
        # pygame.time.delay(50) # Aumentar para avanzar más rápido
        # clock.tick(10) # Reducir para avanzar más lento
        pygame.time.delay(80)
        clock.tick(5)
        pygame.display.update()
    # Salir de pygame
    # print(LISTA_MEMORIA)
    # print("Total movimientos:",len(LISTA_MEMORIA))
    pygame.quit()
    
if __name__ == '__main__': main()


