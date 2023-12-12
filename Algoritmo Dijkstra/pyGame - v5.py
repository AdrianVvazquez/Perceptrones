import pygame
import random
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
LISTA_MEMORIA = list()
CHECKPOINT = pygame.image.load("assets/checkPoint.jpg")
THIEF = pygame.image.load("assets/ladron.png")
OBSTACULO = pygame.image.load("assets/obtaculo.jpg")
X_I, Y_I = 80, 40

# crear matriz de obstáculos y algoritmo Dijksra
for i in range(0, 20):
    MATRIZ_OBSTACULOS2 = list()
    for j in range(0, 20):
        MATRIZ_OBSTACULOS2.append(0)
    MATRIZ_OBSTACULOS.append(MATRIZ_OBSTACULOS2)
    MATRIZ_MEMORIA.append(MATRIZ_OBSTACULOS2)
# matriz_facil = [ [0]*5 for n in range(5) ]
    

def llenarFondo(screen:pygame.Surface):
    screen.fill(FONDO)
    color = 0
    k = 0
    m = 0
    # obstaculorect = OBSTACULO.get_rect()

    for i in range(0, SIZE[0], CUADRADO_ALTO):
        k = int(i/40)
        for j in range(0, SIZE[1], CUADRADO_ALTO):
            m = int(j/40)     
            # Obstaculos
            if MATRIZ_OBSTACULOS[k][m] == -1:
                obstaculorect = OBSTACULO.get_rect()
                obstaculorect.move_ip(i, j)
                screen.blit(OBSTACULO, obstaculorect)
                algoritmo(0)
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

    return screen
    
def crearObjetos(screen2:pygame.Surface):
    # Objeto imagen ladrón
    thiefrect = THIEF.get_rect()
    thiefrect.move_ip(X_I, Y_I)
    screen2.blit(THIEF, thiefrect)
    pygame.display.update()
    LISTA_MEMORIA.append([int(X_I/40),int(Y_I/40)])

    return thiefrect

def guardarCheckPoint(x, y):
    x = int(x/40)
    y = int(y/40)
    for i in range(0, 20):
        for j in range(0, 20):
            # Si no hay obstaculo y está libre = 25
            if MATRIZ_OBSTACULOS[i][j] == 0 and MATRIZ_OBSTACULOS[i][j] != -1:
                MATRIZ_OBSTACULOS[x][y] = 25
            else:
                if MATRIZ_OBSTACULOS[i][j] != 25:
                    MATRIZ_OBSTACULOS[i][j] = MATRIZ_OBSTACULOS[i][j]
                # Borrar checkPoint si ya existe
                else:
                    MATRIZ_OBSTACULOS[i][j] = 0
    
    # for i in range(0, 20):
    #     for j in range(0, 20):
    #         print("[",MATRIZ_OBSTACULOS[j][i], "]", end="")
    #     print("\n")
    # print("\n\n")

def guardarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)

    for i in range(0, 20):
        for j in range(0, 20):
            if [i, j] == [x, y]:
                MATRIZ_OBSTACULOS[x][y] = -1
    # Imprimir matriz
    # for i in range(0, 20):
    #     for j in range(0, 20):
    #         print("[",MATRIZ_OBSTACULOS[j][i], "]", end="")
    #     print("\n")
    # print("\n\n")

def eliminarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)
    # print(x, y)
    for i in range(0, 20): # Y
        for j in range(0, 20): # X
            if [i, j] == [x, y] and MATRIZ_OBSTACULOS[x][y] == -1:
                MATRIZ_OBSTACULOS[x][y] = 0
    # Imprimir matriz
    # for i in range(0, 20):
    #     for j in range(0, 20):
    #         print("[",MATRIZ_OBSTACULOS[j][i], "]", end="")
    #     print("\n")
    # print("\n\n")
    
def movimiento(keys:int, clicks:Tuple, thiefrect:pygame.Rect, screen:pygame.Surface, screen2:pygame.Surface):

    if keys:
        if (keys == 1):
            x = int((thiefrect.center[0]-20)/40)
            y = int((thiefrect.top-20)/40)
            # Si choca con un obstáculo
            if MATRIZ_OBSTACULOS[x][y] == -1:
                thiefrect.top = thiefrect.top
            # Movimiento normal
            else:
                screen2.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(0, -40)
            # Si llega al borde
            if thiefrect.top < 0:
                thiefrect.top = 0
        if (keys == 2):
            x = int((thiefrect.center[0]-20)/40)
            y = int(thiefrect.bottom/40)
            if y < 20:
                # Obstáculo
                if MATRIZ_OBSTACULOS[x][y] == -1:
                    thiefrect.bottom = thiefrect.bottom
                else:
                # Movimiento normal
                    screen2.blit(llenarFondo(screen), thiefrect, thiefrect)
                    thiefrect = thiefrect.move(0, 40)
            # Borde
            if thiefrect.bottom > SIZE[1]:
                thiefrect.bottom = SIZE[1]
        if (keys == 3):
            x = int((thiefrect.left-20)/40)
            y = int(thiefrect.top/40)
            if MATRIZ_OBSTACULOS[x][y] == -1:
                thiefrect.left = thiefrect.left
            else:
                screen2.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(-40, 0)
            if thiefrect.left < 0:
                thiefrect.left = 0
        if (keys == 4):
            x = int((thiefrect.right+20)/40)
            y = int(thiefrect.top/40)
            # print(x,y)
            if x < 20:
                if MATRIZ_OBSTACULOS[x][y] == -1:
                    thiefrect.right = thiefrect.right
                else:
                    screen2.blit(llenarFondo(screen),thiefrect,thiefrect)
                    thiefrect = thiefrect.move(40, 0)
            if thiefrect.right > SIZE[0]:
                thiefrect.right = SIZE[0]
        # Guardar movimientos en una lista
        if keys == 1 or keys == 2 or keys == 3 or keys == 4:
            LISTA_MEMORIA.append([int(thiefrect.left/40), int(thiefrect.top/40)])
            # print(LISTA_MEMORIA)
        # Actualizar imagen en posición nueva
        screen2.blit(THIEF, thiefrect)
    
    if clicks:
        if clicks[0]:
            mouse = pygame.mouse.get_pos()
            x = (mouse[0]//40)*40
            y = (mouse[1]//40)*40
            key_checkPoint = pygame.key.get_pressed()
            
            if key_checkPoint[pygame.K_LSHIFT]:
                guardarCheckPoint(x, y)
                algoritmo(0)
            else:
                guardarObstaculo(x, y)
            # print ("LEFT")

            
            
        if clicks[2]:
            mouse = pygame.mouse.get_pos()
            x = (mouse[0]//40)*40
            y = (mouse[1]//40)*40
            eliminarObstaculo(x, y)
            # print ("RIGHT")
            # llenarFondo(screen)

    return thiefrect

def algoritmo(opc):
    X_F = 0
    Y_F = 0
    if opc == 0:
        # Crear mapa de calor a partir de la posición de la meta
        for i in range(0,20):
            for j in range(0, 20):
                if MATRIZ_OBSTACULOS[i][j] == 25:
                    X_F = i
                    Y_F = j

        distancia = int(X_F-Y_F)

        print(X_F,Y_F)

    



def main():
    # Inicializar pygame
    pygame.init()
    # Ventanas
    screen = pygame.display.set_mode(SIZE)
    screen2 = pygame.display.set_mode(SIZE) # Matriz con algortimo Dijkstra implementada aquí
    pygame.display.set_caption("Juego 1")
    clock = pygame.time.Clock()
    # Crear objetos y posicionarlos
    llenarFondo(screen)
    thiefrect = crearObjetos(screen2)
    run = True
    pause = False

    while run:
        # start_key = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Tecla para PAUSE
            # if event.type == pygame.K_p and pause == False:
            #     pause = True
            # key = pygame.key.get_pressed()
# Eventos
        # Para mover avatar con el teclado
        # if key[pygame.K_UP]:
        #     keys = 1 
        # elif key[pygame.K_DOWN]:
        #     keys = 2 
        # elif key[pygame.K_LEFT]:
        #     keys = 3 
        # elif key[pygame.K_RIGHT]:
        #     keys = 4
        # else: keys = NULL
        keys = random.randrange(0,5)
        # Para forzar un movimiento
        # keys = 4
        clicks = pygame.mouse.get_pressed()
        # Avanzar aleatoriamente
        if keys or clicks:
            thiefrect = movimiento(keys, clicks, thiefrect, screen, screen2)
# Eventos

        # GANAR
        if MATRIZ_OBSTACULOS[int((thiefrect.center[0]-20)/40)][int((thiefrect.center[1]-20)/40)] == 25:
            run = False
            print("You win!")
        # pygame.time.delay(50) # Aumentar para avanzar más rápido
        # clock.tick(10) # Reducir para avanzar más lento
        pygame.time.delay(80)
        clock.tick(5)
        pygame.display.update()
        # Puede ser 
        # pygame.display.flip()
    # Salir de pygame
    print(LISTA_MEMORIA)
    print("Total movimientos: ",LISTA_MEMORIA.__len__())
    pygame.quit()
    
if __name__ == '__main__': main()


