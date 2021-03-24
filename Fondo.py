from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Fondo():
    def dibujar(self):
        glPushMatrix()
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0) 
        glVertex(-1.0, 1.00, 0.0)
        glVertex(1.00, 1.0, 0.0)
        glVertex(1.00, -1.00, 0.0)
        glVertex(-1.03, -1.05, 0.0)
        glEnd()
        glPopMatrix()