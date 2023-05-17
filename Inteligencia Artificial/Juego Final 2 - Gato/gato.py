# '''
# Adrian Vázquez

# Python - pygame
# Juego de tres en línea contra la PC con aprendizaje e inteligencia artificial

# '''

import pygame
import time
import random
pygame.font.init()
# Medidas
SIZE = [750, 800]
SIZE_BODY = [750, 750]
ANCHO = 250
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FONDO = (24, 25, 30)
# Imagenes
APPLE_IMG = pygame.image.load("assets/apple_200px.png")
WINDOWS_IMG = pygame.image.load("assets/windows_200px.png")
# Ventana
SCREEN = pygame.display.set_mode(SIZE)
# Otros
WIN = False
FRASE_INICIAL = "¿Listo? Tú empiezas."
FRASES = ["Mmm... Buena esa.", "¡Bien...! Pero no tanto jaja", "Sí... Lo veía venir.", "¡Bien! Guardaré esa para después.", "Bien... Pero, ¿Y si hago esto?"]
FONT = pygame.font.Font(pygame.font.get_default_font(), 24)
MATRIZ_TABLERO = list()
# LISTA_CASILLAS = [1,2,3,4,5,6,7,8,9]
LISTA_CASILLAS = [
    {'index':1,'pos':[0,0]},{'index':2,'pos':[1,0]},{'index':3,'pos':[2,0]},
    {'index':4,'pos':[0,1]},{'index':5,'pos':[1,1]},{'index':6,'pos':[2,1]},
    {'index':7,'pos':[0,2]},{'index':8,'pos':[1,2]},{'index':9,'pos':[2,2]}]

LISTA_CASILLAS_2 = [
    {'index':1,'pos':[0,0]},{'index':2,'pos':[1,0]},{'index':3,'pos':[2,0]},
    {'index':4,'pos':[0,1]},{'index':5,'pos':[1,1]},{'index':6,'pos':[2,1]},
    {'index':7,'pos':[0,2]},{'index':8,'pos':[1,2]},{'index':9,'pos':[2,2]}]

LINEAS_GANAR = [
    [1,5,9], [3,5,7],
    [1,2,3], [4,5,6], [7,8,9],
    [1,4,7], [2,5,8], [3,6,9]
]

for i in range(0, 3):
    MATRIZ_TABLERO2 = list()
    for j in range(0, 3):
        MATRIZ_TABLERO2.append(0)
    MATRIZ_TABLERO.append(MATRIZ_TABLERO2)
    
c = 0
for i in range(0, 3):
    for j in range(0, 3):
        c+=1
        MATRIZ_TABLERO[j][i]={'index':c, 'jugador':" "}


def llenarFondo():
    global SCREEN
    SCREEN.fill(NEGRO)
    # Fondo para frases
    pygame.draw.rect(SCREEN, NEGRO, [0, 750, 750, 50],0,2)
    # Tablero de juego
    for i in range(0, SIZE_BODY[0], ANCHO):
        for j in range(0, SIZE_BODY[1], ANCHO):
            pygame.draw.rect(SCREEN, BLANCO, [i, j, 249, 249],0,2)
    
    return SCREEN


def guardar_y_dibujar(x, y, img:pygame.Surface, player_name):

    MATRIZ_TABLERO[x][y]['jugador'] = player_name

    imgRect = img.get_rect()
    imgRect.move_ip(int((x*250)+20),int((y*250)+20))
    SCREEN.blit(img, imgRect)
    pygame.display.update()
        
    for i in range(0, 3):
        for j in range(0, 3):
            print("[",MATRIZ_TABLERO[j][i], "]", end="")
        print("\n")
    print("\n\n")


def mostrar_frase(frase):
    frase_movimiento = pygame.font.Font.render(FONT, frase, True, BLANCO, NEGRO)
    SCREEN.blit(frase_movimiento, dest=(200, 750))
    pygame.display.update()
    
def ocultar_frase():
    pygame.draw.rect(SCREEN, NEGRO, [0, 750, 750, 50],0,2)

def buscar_casillas(jugador):
    movimientos_jugador = list()
    for i in range(0, 3):
        for j in range(0, 3):
            if MATRIZ_TABLERO[i][j]['jugador'] == jugador:
                movimientos_jugador.append(MATRIZ_TABLERO[i][j])
    
    return movimientos_jugador

def validar_casilla(casilla):

    if (MATRIZ_TABLERO[casilla['pos'][0]][casilla['pos'][1]]['jugador'] == ' '):
        print("casilla: ",casilla)
        guardar_y_dibujar(casilla['pos'][0], casilla['pos'][1], APPLE_IMG, "PC")
    
        movimientos_pc = buscar_casillas("PC")
        if verificar_ganar(movimientos_pc) == True:
            print("¡Te gané!")
            
    return WIN
            

def verificar_ganar(movimientos):
    global WIN

    for linea in LINEAS_GANAR:
        c=0
        for index in linea:
            # '''Si movimientos de PLAYER1 == index'''
            for i in range(len(movimientos)):
                if movimientos[i]['index'] == index:
                    c+=1
                    if c == 3:
                        WIN = True
    return WIN

def verificar_empate(movimientos):
    global LISTA_CASILLAS_2

    # '''Movimientos disponibles'''
    for i in range(len(LISTA_CASILLAS)): # [0-9]: {index, pos}
        # print("1... ", LISTA_CASILLAS[i])
        for casilla in range(len(movimientos)):
            # print("2... Index: ",movimientos_player1[casilla]['index'])
            if movimientos[casilla]['index'] == LISTA_CASILLAS[i]['index']:
                if LISTA_CASILLAS[i] in LISTA_CASILLAS_2: 
                    LISTA_CASILLAS_2.remove(LISTA_CASILLAS[i])
    
    # '''PC movimiento'''
    if len(LISTA_CASILLAS_2) < 1:
        return True
    
def procesar_movimiento():
    global LISTA_CASILLAS # {index:int, posición:[]}
    global LISTA_CASILLAS_2
    print("\nProcesando...")
    
    # '''Guardar movimientos de Player1(contrincante)'''
    movimientos_player = buscar_casillas("PLAYER1")
    
    # '''Recorrer lista ganar_posibles'''
    if verificar_ganar(movimientos_player) == True:
        print("¡Ganaste!")
    else:

        if verificar_empate(movimientos_player) == True:
            print("¡Empate!")
        else:
            num_random_frase = random.randrange(0,5)
            frase = FRASES[num_random_frase]

            # '''Frase'''
            mostrar_frase(frase)
            time.sleep(1)

            
            # else:
            mov_casilla = random.choice(LISTA_CASILLAS_2)
            print("Ir a: ",mov_casilla)
            LISTA_CASILLAS_2.remove(mov_casilla)
            validar_casilla(mov_casilla)
        return WIN 
        
    return WIN 

        
def main():
    # Inicializar pygame
    pygame.init()
    pygame.display.set_caption("Juego del gato")
    
    clock = pygame.time.Clock()
    run = True

    llenarFondo()
    mostrar_frase(FRASE_INICIAL)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        while WIN is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Click izquierdo
            if pygame.mouse.get_pressed()[0]:
                # Ocultar frase
                ocultar_frase()
                mouse_pos = pygame.mouse.get_pos()
                x = (mouse_pos[0]//ANCHO)
                y = (mouse_pos[1]//ANCHO)

                # Player1: movimiento
                guardar_y_dibujar(x, y, WINDOWS_IMG, "PLAYER1")

                # Procesar movimiento
                time.sleep(1)
                procesar_movimiento()
        print("Saliendo...")

        pygame.time.delay(80)
        clock.tick(5)

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__': main()
