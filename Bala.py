from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

    
class Bala():
    posicionX = 0
    posicionY = 0
    anguloBala = 0

    def actualizar(self, tiempo_delta, carrito, obstaculo, obstaculo2, obstaculo3, obstaculo4, obstaculo5, obstaculo6, obstaculo7, obstaculo8, obstaculo9, obstaculo11, obstaculo12, obstaculo13, obstaculo14, obstaculo15, obstaculo16, obstaculo17, obstaculo18, obstaculo19, obstaculo20):
        self.anguloBala = carrito.angulo
        if carrito.disparando:
            if self.posicionX >= 1:
                carrito.disparando = False
            elif self.posicionX <= -1:
                carrito.disparando = False
            elif self.posicionY >= 1:
                carrito.disparando = False
            elif self.posicionY <= -1:
                carrito.disparando = False
            
            self.posicionY = self.posicionY + \
                (sin((self.anguloBala + carrito.desfase) * 3.14159 / 180) * carrito.velocidad * tiempo_delta)
            self.posicionX = self.posicionX + \
                (cos((self.anguloBala + carrito.desfase) * 3.14159 / 180) * carrito.velocidad * tiempo_delta)
            # checar colision con obstaculo si sigue "vivo"
            if obstaculo.vivo and self.posicionX + 0.01 > obstaculo.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo.posicionY + 0.05:
                
                obstaculo.vivo = False
                carrito.disparando = False

            if obstaculo2.vivo and self.posicionX + 0.01 > obstaculo2.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo2.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo2.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo2.posicionY + 0.05:
                obstaculo2.vivo = False
                carrito.disparando = False
            
            if obstaculo3.vivo and self.posicionX + 0.01 > obstaculo3.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo3.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo3.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo3.posicionY + 0.05:
                obstaculo3.vivo = False
                carrito.disparando = False
            
            if obstaculo4.vivo and self.posicionX + 0.01 > obstaculo4.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo4.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo4.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo4.posicionY + 0.05:
                obstaculo4.vivo = False
                carrito.disparando = False
            
            if obstaculo5.vivo and self.posicionX + 0.01 > obstaculo5.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo5.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo5.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo5.posicionY + 0.05:
                obstaculo5.vivo = False
                carrito.disparando = False
            
            if obstaculo6.vivo and self.posicionX + 0.01 > obstaculo6.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo6.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo6.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo6.posicionY + 0.05:
                obstaculo6.vivo = False
                carrito.disparando = False
            
            if obstaculo7.vivo and self.posicionX + 0.01 > obstaculo7.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo7.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo7.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo7.posicionY + 0.05:
                obstaculo7.vivo = False
                carrito.disparando = False
            
            if obstaculo8.vivo and self.posicionX + 0.01 > obstaculo8.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo8.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo8.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo8.posicionY + 0.05:
                obstaculo8.vivo= False
                carrito.disparando = False
            
            if obstaculo9.vivo and self.posicionX + 0.01 > obstaculo9.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo9.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo9.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo9.posicionY + 0.05:
                obstaculo9.vivo = False
                carrito.disparando = False
            
            if obstaculo11.vivo and self.posicionX + 0.01 > obstaculo11.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo11.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo11.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo11.posicionY + 0.05:
                obstaculo11.vivo = False
                carrito.disparando = False

            if obstaculo12.vivo and self.posicionX + 0.01 > obstaculo12.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo12.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo12.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo12.posicionY + 0.05:
                obstaculo12.vivo = False
                carrito.disparando = False
            
            if obstaculo13.vivo and self.posicionX + 0.01 > obstaculo13.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo13.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo13.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo13.posicionY + 0.05:
                obstaculo13.vivo = False
                carrito.disparando = False
            
            if obstaculo14.vivo and self.posicionX + 0.01 > obstaculo14.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo14.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo14.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo14.posicionY + 0.05:
                obstaculo14.vivo = False
                carrito.disparando = False
            
            if obstaculo15.vivo and self.posicionX + 0.01 > obstaculo15.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo15.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo15.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo15.posicionY + 0.05:
                obstaculo15.vivo = False
                carrito.disparando = False
            
            if obstaculo16.vivo and self.posicionX + 0.01 > obstaculo16.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo16.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo16.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo16.posicionY + 0.05:
                obstaculo16.vivo = False
                carrito.disparando = False
            
            if obstaculo17.vivo and self.posicionX + 0.01 > obstaculo17.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo17.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo17.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo17.posicionY + 0.05:
                obstaculo17.vivo = False
                carrito.disparando = False
            
            if obstaculo18.vivo and self.posicionX + 0.01 > obstaculo18.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo18.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo18.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo18.posicionY + 0.05:
                obstaculo18.vivo= False
                carrito.disparando = False
            
            if obstaculo19.vivo and self.posicionX + 0.01 > obstaculo19.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo19.posicionX + 0.05 and self.posicionY + 0.01 > obstaculo19.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo19.posicionY + 0.05:
                obstaculo19.vivo = False
                carrito.disparando = False
            
            if obstaculo20.vivo and self.posicionX + 0.01 > obstaculo20.posicionX - 0.05 and self.posicionX - 0.01 < obstaculo20.posicionX  + 0.05 and self.posicionY + 0.01 > obstaculo20.posicionY - 0.05 and self.posicionY - 0.01 < obstaculo20.posicionY + 0.05:
                
                obstaculo20.vivo = False
                carrito.disparando = False

    def dibujar(self, carrito):
        self.anguloBala = carrito.angulo

        if carrito.disparando == True:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(self.anguloBala, 0.0, 0.0, 1.0)
            glBegin(GL_QUADS)
            glColor3f(1.0, 1.0, 1.0)
            glVertex3f(-0.01, 0.01, 0.0)
            glVertex3f(0.01, 0.01, 0.0)
            glVertex3f(0.01, -0.01, 0.0)
            glVertex3f(-0.01, -0.01, 0.0)
            glEnd()
            glPopMatrix()