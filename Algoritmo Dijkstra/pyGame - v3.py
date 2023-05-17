from typing import Tuple
import pygame
import random

# Variables
SIZE = [800, 800]
CUADRADO_ALTO = 40
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FONDO = (24, 25, 30)
MATRIZ_OBSTACULOS = list()
LISTA_MEMORIA = list()

# crear matriz de memoria
for i in range(0, 20):
    MATRIZ_OBSTACULOS2 = list()
    for j in range(0, 20):
        MATRIZ_OBSTACULOS2.append(0)
    MATRIZ_OBSTACULOS.append(MATRIZ_OBSTACULOS2)

# matriz_facil = [ [0]*5 for n in range(5) ]

def llenarFondo(screen:pygame.Surface):
    screen.fill(FONDO)
    color = 0
    for i in range(0, SIZE[0], CUADRADO_ALTO):
        for j in range(0, SIZE[1], CUADRADO_ALTO):
            if color%2 == 0:
                pygame.draw.rect(screen, NEGRO, [i, j, CUADRADO_ALTO, CUADRADO_ALTO], 0, 2)
            else:
                pygame.draw.rect(screen, BLANCO, [i, j, CUADRADO_ALTO, CUADRADO_ALTO], 0, 2)
            color += 1
        color += 1
    return screen
    
def crearObjetos(thief:pygame.Surface, checkPoint:pygame.Surface, obstaculo:pygame.Surface):
    # Objeto imagen ladrón
    thiefrect = thief.get_rect()
    thiefrect.move_ip(80, 40)
    # Objeto imagen checkPoint
    checkPointrect = checkPoint.get_rect()
    checkPointrect.move_ip(760, 0)
    # Objeto imagen obstáculo1
    obstCord1 = random.randrange(0,SIZE[0],40)
    obstCord2 = random.randrange(0,SIZE[1],40)
    obstaculorect = obstaculo.get_rect()
    obstaculorect.move_ip(obstCord1, obstCord2)
    return [thiefrect, checkPointrect, obstaculorect]

def guardarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)

    for i in range(0, 20):
        for j in range(0, 20):
            if [i, j] == [x, y]:
                MATRIZ_OBSTACULOS[j][i] = 1
    # Imprimir matriz
    for i in range(0, 20):
        for j in range(0, 20):
            print("[",MATRIZ_OBSTACULOS[i][j], "]", end="")
        print("\n")
    print("\n\n")

def eliminarObstaculo(x, y):
    x = int(x/40)
    y = int(y/40)
                
    for i in range(0, 20): # Y
        for j in range(0, 20): # X
            if [i, j] == [x, y] and MATRIZ_OBSTACULOS[j][i] == 1:
                MATRIZ_OBSTACULOS[j][i] = 0
    # Imprimir matriz
    for i in range(0, 20):
        for j in range(0, 20):
            print("[",MATRIZ_OBSTACULOS[i][j], "]", end="")
        print("\n")
    print("\n\n")
    
def movimiento(thief, keys:int, clicks:Tuple, obstaculo:pygame.Surface, thiefrect:pygame.Rect, obstaculorect:pygame.Rect, screen:pygame.Surface):
    if keys:
        if (keys == 1):
            # Si choca con un obstáculo
            if thiefrect.top == obstaculorect.bottom and thiefrect.right == obstaculorect.right:
                thiefrect.top = obstaculorect.bottom
            else:
            # Movimiento normal
                # Borrar imagen para actualizar
                screen.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(0, -40)
            # Si llega al borde
            if thiefrect.top < 0:
                thiefrect.top = 0
        if (keys == 2):
            if thiefrect.bottom == obstaculorect.top and thiefrect.right == obstaculorect.right:
                thiefrect.bottom = obstaculorect.top
            else:
                screen.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(0, 40)
            if thiefrect.bottom > SIZE[1]:
                thiefrect.bottom = SIZE[1]
        if (keys == 3):
            if thiefrect.left == obstaculorect.right and thiefrect.top == obstaculorect.top:
                thiefrect.left = obstaculorect.right
            else:
                screen.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(-40, 0)
            if thiefrect.left < 0:
                thiefrect.left = 0
        if (keys == 4):
            if thiefrect.right == obstaculorect.left and thiefrect.top == obstaculorect.top:
                thiefrect.right = obstaculorect.left
            else:
                screen.blit(llenarFondo(screen), thiefrect, thiefrect)
                thiefrect = thiefrect.move(40, 0)
            if thiefrect.right > SIZE[0]:
                thiefrect.right = SIZE[0]
        # Guardar movimientos en una lista
        if keys == 1 or keys == 2 or keys == 3 or keys == 4:
            LISTA_MEMORIA.append([thiefrect.left, thiefrect.top])
            # print(LISTA_MEMORIA)
        # Actualizar imagen en lugar nuevo
        screen.blit(thief, thiefrect)
        
    if clicks:
        if clicks[0]:
            mouse = pygame.mouse.get_pos()
            x = (mouse[0]//40)*40
            y = (mouse[1]//40)*40
            # recta = pygame.draw.rect(screen, (250,156,28),(x,y,40,40))
            # pygame.display.update(recta)
            # screen.blit(recta)
            obstaculorect = obstaculo.get_rect()
            obstaculorect.move_ip(x, y)

            guardarObstaculo(x, y)
            # screen.blit(obstaculo, obstaculorect)
            
            # pygame.display.update(obstaculorect)

            # print ("LEFT")
        if clicks[2]:
            mouse = pygame.mouse.get_pos()
            x = (mouse[0]//40)*40
            y = (mouse[1]//40)*40
            eliminarObstaculo(x, y)

            # print ("RIGHT")
    return thiefrect, obstaculorect, obstaculo

def main():
    # Inicializar pygame
    pygame.init()
    # Ventana
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Juego 1")

    clock = pygame.time.Clock()
    # Crear objetos y posicionarlos
    checkPoint = pygame.image.load("assets/checkPoint.jpg")
    obstaculo = pygame.image.load("assets/obtaculo.jpg")
    thief = pygame.image.load("assets/ladron.png")
    llenarFondo(screen)
    thiefrect, checkPointrect, obstaculorect = crearObjetos(thief, checkPoint, obstaculo)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# Eventos
        keys = random.randrange(0,5)
        clicks = pygame.mouse.get_pressed()
        # Avanzar aleatoriamente
        if keys or clicks:
            thiefrect, obstaculorect, obstaculo = movimiento(thief, keys, clicks, obstaculo, thiefrect, obstaculorect, screen)
# Eventos
        
        # GANAR
        if thiefrect.top == checkPointrect.top and thiefrect.right == checkPointrect.right:
            run = False
            print("You win!")

        # pygame.time.delay(50)
        # clock.tick(10) # Reducir para avanzar más lento
        pygame.time.delay(80)
        clock.tick(5)
        screen.blit(checkPoint, checkPointrect) 
        screen.blit(obstaculo, obstaculorect)
        pygame.display.update()
        # pygame.display.flip()
    # Salir de pygame
    print(LISTA_MEMORIA)
    print(LISTA_MEMORIA.__len__()," movimientos")
    pygame.quit()
    
if __name__ == '__main__': main()