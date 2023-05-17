import pygame
# import random
from typing import Tuple

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
OBSTACULO = pygame.image.load("assets/obtaculo.jpg")
VISITADO_X, VISITADO_Y = 0,0
# Posición inicial de avatar
X_1, Y_1 = 0,0

# crear matriz de obstáculos
for i in range(0, 20):
    MATRIZ_OBSTACULOS2 = list()
    for j in range(0, 20):
        MATRIZ_OBSTACULOS2.append(0)
    MATRIZ_OBSTACULOS.append(MATRIZ_OBSTACULOS2)

# crear matriz de algoritmo para Dijksra
for i in range(0, 20):
    MATRIZ_MEMORIA2 = list()
    for j in range(0, 20):
        MATRIZ_MEMORIA2.append(0)
    MATRIZ_MEMORIA.append(MATRIZ_MEMORIA2)
    

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

def guardarCheckPoint(x, y):
    x = int(x/40)
    y = int(y/40)
    for i in range(0, 20):
        for j in range(0, 20):
            # Borrar checkPoint si ya existe
            if MATRIZ_OBSTACULOS[i][j] == 25:
                # MATRIZ_MEMORIA[x][y] = 0
                MATRIZ_OBSTACULOS[i][j] = 0
            elif (i,j) == (x, y): # 25, 88, -1
                # LIBRE
                if MATRIZ_OBSTACULOS[x][y] == 0 and MATRIZ_OBSTACULOS[x][y] != 25 and MATRIZ_OBSTACULOS[x][y] != 88: # 0
                    MATRIZ_OBSTACULOS[x][y] = 25
                    # MATRIZ_MEMORIA[x][y] = 25
                    algoritmo(0,x,y,True)
                # OCUPADO
                else:
                    # MATRIZ_MEMORIA[x][y] = MATRIZ_MEMORIA[x][y]
                    MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
            else:
                MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
                # MATRIZ_MEMORIA[x][y] = MATRIZ_MEMORIA[x][y]

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
    
def nuevo_objeto(clicks:Tuple):
    if clicks[0]:
        mouse = pygame.mouse.get_pos()
        key_checkPoint = pygame.key.get_pressed()
        x = (mouse[0]//40)*40
        y = (mouse[1]//40)*40
        
        if key_checkPoint[pygame.K_LSHIFT]:
            guardarCheckPoint(x, y)
        else:
            guardarObstaculo(x, y)

    if clicks[2]:
        mouse = pygame.mouse.get_pos()
        x = (mouse[0]//40)*40
        y = (mouse[1]//40)*40
        eliminarObstaculo(x, y)

def algoritmo(opc, x_2, y_2, run):
    # MAPA DE CALOR
    if opc == 0:
        # Crear mapa a partir de la posición de la meta
        for i in range(0,20):
            for j in range(0, 20):
                if MATRIZ_OBSTACULOS[i][j] == 25:
                    MATRIZ_MEMORIA[i][j] = 0
                else:
                    distancia_x = int(abs((i-x_2)))
                    distancia_y = int(abs((j-y_2)))
                    distancia_meta = int(pow(distancia_x,2)+pow(distancia_y,2))
                    distancia_meta = int(distancia_meta**(.5))
                    MATRIZ_MEMORIA[i][j] = distancia_meta
        # Imprimir mapa
        for i in range(0, 20):
            for j in range(0, 20):
                print("[",MATRIZ_MEMORIA[j][i], "]", end="")
            print("\n")
        print("\n\n")

    # MOVIMIENTO
    if opc == 1:
        global X_1
        global Y_1
        global VISITADO_X
        global VISITADO_Y
        lista = list() # Lista con posibles movimientos

        for i in range(-1, 2):
            if i == -1 or i == 1: # izq, der, diagonal
                for j in range(-1, 2): # -1,0,1
                    if j == 0:
                        MATRIZ_OBSTACULOS[X_1+i][Y_1+j] = 89
                        if X_1+i < 0 or X_1+i > 19:
                            lista = lista
                        elif MATRIZ_OBSTACULOS[X_1+i][Y_1+j] == -1:
                            lista = lista
                        else:
                            lista.append({'costo':MATRIZ_MEMORIA[X_1+i][Y_1+j], 'x':X_1+i, 'y':Y_1+j})
                            # lista.append({'costo':MATRIZ_MEMORIA[X_1+i][Y_1+j], 'x':X_1+i, 'y':Y_1+j, 'visitado':0})
            if i == 0:
                for j in range(-1, 2, 2): # arriba, abajo
                    # print(X_1, Y_1+j)
                    if Y_1+j < 0 or Y_1+j > 19:
                        lista = lista
                    elif MATRIZ_OBSTACULOS[X_1+i][Y_1+j] == -1:
                        lista = lista
                    else:
                        lista.append({'costo':MATRIZ_MEMORIA[X_1+i][Y_1+j], 'x':X_1+i, 'y':Y_1+j})
                        # MATRIZ_OBSTACULOS[X_1+i][Y_1+j] = 88
        # print(lista)

        costo_menor = lista[0]
        # Posición de menor costo
        for i in lista:
            # if [i['x'], i['y']] is not 
            if i['x'] != VISITADO_X and i['y'] != VISITADO_Y:
                if i['costo'] < costo_menor['costo']:
                    costo_menor = i
                if MATRIZ_MEMORIA[i['x']][i['y']] == 0:
                    run = False
                    print("Win")

        if costo_menor['costo'] != 0:
            MATRIZ_OBSTACULOS[costo_menor['x']][costo_menor['y']] = 88
            MATRIZ_OBSTACULOS[X_1][Y_1] = 0
            # print(VISITADO_X, VISITADO_Y)
            VISITADO_X = X_1
            VISITADO_Y = Y_1
            # print(VISITADO_X, VISITADO_Y)
            X_1 = costo_menor['x']
            Y_1 = costo_menor['y']
    return run

def main():
    # Inicializar pygame
    pygame.init()
    # Ventanas
    screen = pygame.display.set_mode(SIZE)
    screen2 = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Juego 1")
    clock = pygame.time.Clock()
    # Crear objetos 
    MATRIZ_OBSTACULOS[int(X_1)][int(Y_1)] = 88
    llenarFondo(screen, screen2)
    run = True
    while run:
        # start_key = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# Eventos
        clicks = pygame.mouse.get_pressed()
        if clicks:
            run = algoritmo(1,0,0, run) # Se mandas dos ceros pero no los usa.
            nuevo_objeto(clicks)
            llenarFondo(screen, screen2)
# Eventos
        # pygame.time.delay(50) # Aumentar para avanzar más rápido
        # clock.tick(10) # Reducir para avanzar más lento
        pygame.time.delay(80)
        clock.tick(5)
        pygame.display.update()
    # Salir de pygame
    print(LISTA_MEMORIA)
    print("Total movimientos: ",LISTA_MEMORIA.__len__())
    pygame.quit()
    
if __name__ == '__main__': main()


