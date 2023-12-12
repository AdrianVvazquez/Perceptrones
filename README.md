
# Introducción a la Inteligencia Artificial con pygame
Todos los archivos son creados desde cero con excepción de las imágenes descargadas de internet. Respecto a la arquitectura, es preferible cambiar a un patrón orientado a objetos. Todo es muy básico y no se usó ninguna librería de IA o para procesamiento de datos. 
Se creó un juego con pygame en python para aplicar algoritmos para encontrar la ruta más corta. Estos algoritmos son usados diariamente por nuestros dispositivos de navegación o en los videojuegos.

## Carpetas
## 1. [Algoritmo Dijkstra]
Tiene las iteraciones que llevaron al juego final, que es la versión que está en la carpeta "Juego Final 1".
A partir de la versión 5 el juego es estable. Se dejaron para seguir experimentando con matrices.
En unas versiones el jugador se mueve aleatoriamente por el tablero, en otras se experimentó con el algoritmo estrella, finalmente se usó el algoritmo Dijkstra para mover al jugador sobre un mapa de calor.

## 2. Buscador [Juego Final 1]
Versión final del buscador con el algoritmo Dijkstra, el Agente elige al vecino de menor costo. Se cambia el color de los vecinos visitados para mostrar el funcionamiento del algoritmo.

## 3. 3 en línea o gato [Juego Final 2]
Windows vs Apple.  Por ahora es 

## 4. Escenarios [Juego Final 3]
Scripts para juego con Unity en C#. Agente y Nodo. No está la interfaz del escenario. 
Se resuelven 3 posibles escenarios en donde el algoritmo de Dijkstra no llega al objetivo. Se itera un número de épocas grande y se exploran todos los caminos posibles al objetivo.

### Fuentes de consulta
https://www.pygame.org/wiki/GettingStarted
