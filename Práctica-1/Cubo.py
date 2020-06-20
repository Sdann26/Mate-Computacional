import pygame
from pygame.locals import *

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

# Creación de los puntos del cubo 
verticies = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

# Función para dibujar los ejes

def draw_axis():
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, np.array([10, 0, 0, 0, 0, 0,
                                                  0, 10, 0, 0, 0, 0,
                                                  0, 0, 10, 0, 0, 0,
                                                  ]))
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0,  np.array([1, 0, 0, 1, 1, 1,
                                                  0, 1, 0, 1, 1, 1,
                                                  0, 0, 1, 1, 1, 1,
                                                  ]))
        glDrawArrays(GL_LINES, 0, 6)


# Función para dibujar el Cubo

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

# Función para dibujar el Cubo Transformado

def Cube2():
    glBegin(GL_LINES)

    n_verticies = np.ones((4,2))

    verticies = (
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 0, 0),
        (1, 0, 1),
        (1, 1, 1),
        (0, 0, 1),
        (0, 1, 1)
        )

    verticies = list(verticies)

    # Matriz de Transformación

    P = [[0.91068360, -0.24401693 ,  0.33333333],
    [0.33333333 ,  0.91068360,  -0.24401693],
    [-0.24401693 ,  0.33333333 ,  0.91068360]]

    matriz_v = np.zeros((8, 3))
    i = 0

    for v in verticies:
        nuevo = np.dot(P,v)
        matriz_v[i] = nuevo
        i = 1 + i

    # Nueva matriz con los puntos actualizados

    matriz_v = tuple(matriz_v)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(matriz_v[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Perspectiva de la cámara inicial
    glTranslatef(-0.5,-0.5, -6)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Sirve para mover la cámara de enfoque

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)

        # Gráfica el cubo 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        draw_axis()
        pygame.time.wait(600)
        pygame.display.flip()

        # Gráfica el cubo transformado
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube2()
        draw_axis()
        pygame.time.wait(600)
        pygame.display.flip()

main()
