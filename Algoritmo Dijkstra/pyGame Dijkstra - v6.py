from os import lstat
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
LISTA_MEMORIA = list() # Lista de posiciones visitadas
CHECKPOINT = pygame.image.load("assets/checkPoint.jpg")
THIEF = pygame.image.load("assets/ladron.png")
OBSTACULO = pygame.image.load("assets/obtaculo.jpg")
# Posición inicial de avatar
X_1, Y_1 = 80, 40

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
                MATRIZ_MEMORIA[x][y] = 0
                MATRIZ_OBSTACULOS[i][j] = 0
            elif (i,j) == (x, y): # 25, 88, -1
                # LIBRE
                if MATRIZ_OBSTACULOS[x][y] == 0 and MATRIZ_OBSTACULOS[x][y] != 25 and MATRIZ_OBSTACULOS[x][y] != 88: # 0
                    MATRIZ_OBSTACULOS[x][y] = 25
                    MATRIZ_MEMORIA[x][y] = 25
                    algoritmo(0)
                # OCUPADO
                else:
                    MATRIZ_MEMORIA[x][y] = MATRIZ_MEMORIA[x][y]
                    MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
            else:
                MATRIZ_OBSTACULOS[x][y] = MATRIZ_OBSTACULOS[x][y]
                MATRIZ_MEMORIA[x][y] = MATRIZ_MEMORIA[x][y]

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
                
def mover(opc):
    print("mover")
    for i in range(0, 20):
        for j in range(0, 20):
            if MATRIZ_OBSTACULOS[i][j] == 88:
                avatar_x = i
                avatar_y = j
                LISTA_MEMORIA.append([i, j])

    if opc == 1: # Arriba
        # Obstaculo y borde
        if MATRIZ_OBSTACULOS[avatar_x][avatar_y-1] == -1 or avatar_y == 0:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        # Meta
        # elif MATRIZ_OBSTACULOS[avatar_x][avatar_y-1] == 25:
        #     run = False
            # print("You win!")
        else:
            # Movimiento normal
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = 0
            MATRIZ_OBSTACULOS[avatar_x][int(avatar_y-1)] = 88
    
    if opc == 2: # Abajo
        if avatar_y == 19:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        elif MATRIZ_OBSTACULOS[avatar_x][avatar_y+1] == -1:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        else:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = 0
            MATRIZ_OBSTACULOS[avatar_x][int(avatar_y+1)] = 88

    if opc == 3: # Izquierda
        if avatar_x == 0:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        elif MATRIZ_OBSTACULOS[avatar_x-1][avatar_y] == -1:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        else:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = 0
            MATRIZ_OBSTACULOS[int(avatar_x-1)][avatar_y] = 88
        
    if opc == 4: # Derecha
        if avatar_x == 19:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        elif MATRIZ_OBSTACULOS[avatar_x+1][avatar_y] == -1:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = MATRIZ_OBSTACULOS[avatar_x][avatar_y]   
        else:
            MATRIZ_OBSTACULOS[avatar_x][avatar_y] = 0
            MATRIZ_OBSTACULOS[int(avatar_x+1)][avatar_y] = 88
    
    # Imprimir
    # for i in range(0, 20): # Y
    #     for j in range(0, 20): # X
    #         print("[",MATRIZ_OBSTACULOS[j][i], "]", end="")
    #     print("\n")
    # print("\n\n")
    
    
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

def algoritmo(opc):
    # MAPA DE CALOR
    if opc == 0:
        # Posición de la meta
        for i in range(0,20):
            for j in range(0, 20):
                if MATRIZ_OBSTACULOS[i][j] == 25:
                    MATRIZ_MEMORIA[i][j] = 25
                    x_2 = i
                    y_2 = j
        # Crear mapa a partir de la posición de la meta
        for i in range(0,20):
            for j in range(0, 20):
                if MATRIZ_MEMORIA[i][j] == 25:
                    MATRIZ_MEMORIA[i][j] = 0
                elif MATRIZ_OBSTACULOS[i][j] == -1:
                    MATRIZ_MEMORIA[i][j] = -1
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

    # Saber hacia dónde moverse
    if opc == 1:
        for i in range(0, 20): 
            for j in range(0, 20): 
                if MATRIZ_OBSTACULOS[i][j] == 88:
                    lista = list()
                    lista.append({'costo':MATRIZ_MEMORIA[i][j-1], 'x':i, 'y':j-1})
                    lista.append({'costo':MATRIZ_MEMORIA[i-1][j-1], 'x':i-1, 'y':j-1})
                    lista.append({'costo':MATRIZ_MEMORIA[i-1][j], 'x':i-1, 'y':j})
                    lista.append({'costo':MATRIZ_MEMORIA[i-1][j+1], 'x':i-1, 'y':j+1})
                    lista.append({'costo':MATRIZ_MEMORIA[i][j+1], 'x':i, 'y':j+1})
                    lista.append({'costo':MATRIZ_MEMORIA[i+1][j+1], 'x':i+1, 'y':j+1})
                    lista.append({'costo':MATRIZ_MEMORIA[i+1][j], 'x':i+1, 'y':j})
                    lista.append({'costo':MATRIZ_MEMORIA[i+1][j-1], 'x':i+1, 'y':j-1})
                    # print("Lista: ", lista)
                    for r in range(0, len(lista)):
                        print(lista[r],"\n")
                        # if -1 in lista[r]: 
                    for l in lista:
                        if l['costo'] == -1:
                            lista.remove(l)
                        # Eliminar si es un obstáculo y no comparar 
                    # for l in range(0, lista.length()):
                        # print("Lista: ", l['costo'])
                    # print(lista)
                        # else: print("No removido: ", l['costo'])

                        # return lista
                    # print(lista)
                    # El primero de la lista para compararlo
                    menor_costo = lista[0]['costo']
                    menor = lista[0]
                    # Por cada objeto guardado
                    for k in lista:
                        # comparar costos
                        if k['costo'] < menor_costo:
                            menor_costo = k['costo'] # Costo menor actual va cambiando
                            menor = k # Objeto completo menor costo
                        # regresar el menor
                    if menor['costo'] > 0:
                        MATRIZ_OBSTACULOS[i][j] = 0
                        MATRIZ_OBSTACULOS[menor['x']][menor['y']] = 88
                        return menor


                    

def main():
    # Inicializar pygame
    pygame.init()
    # Ventanas
    screen = pygame.display.set_mode(SIZE)
    screen2 = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Juego 1")
    clock = pygame.time.Clock()
    # Crear objetos 
    MATRIZ_OBSTACULOS[int(X_1/40)][int(Y_1/40)] = 88
    llenarFondo(screen, screen2)
    run = True
    pause = False

    while run:
        # start_key = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# Eventos
        clicks = pygame.mouse.get_pressed()
        if clicks:
            algoritmo(1)
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


