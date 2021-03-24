from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Bala import *

class Carrito():
    posicionX = 0.0
    posicionY = -0.0
    angulo = 0
    rotacion = 0
    desfase = 90
    velocidad = 4.5 
    velocidad_angular = 345
    colisionando = False
    disparando = False

    def checar_colisiones(self, obstaculo, obstaculo2, obstaculo3, obstaculo4, obstaculo5, obstaculo6, obstaculo7, obstaculo8, obstaculo9, obstaculo11, obstaculo12, obstaculo13, obstaculo14, obstaculo15, obstaculo16, obstaculo17, obstaculo18, obstaculo19, obstaculo20):
        # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
        # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
        # Y extremoSuperiorCarrito > extremoInferiorObstaculo
        # Y extremoInferiorCarrito < extremoSuperiorObstaculo
        if self.posicionX + 0.05 > obstaculo.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo.posicionY + 0.05:
            self.colisionando = True
        
        elif self.posicionX + 0.05 > obstaculo2.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo2.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo2.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo2.posicionY + 0.05:
            self.colisionando = True
        
        elif self.posicionX + 0.05 > obstaculo3.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo3.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo3.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo3.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo4.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo4.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo4.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo4.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo5.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo5.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo5.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo5.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo6.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo6.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo6.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo6.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo7.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo7.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo7.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo7.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo8.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo8.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo8.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo8.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo9.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo9.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo9.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo9.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo11.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo11.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo11.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo11.posicionY + 0.05:
            self.colisionando = True
                
        elif self.posicionX + 0.05 > obstaculo12.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo12.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo12.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo12.posicionY + 0.05:
            self.colisionando = True

        elif self.posicionX + 0.05 > obstaculo13.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo13.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo13.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo13.posicionY + 0.05:
            self.colisionando = True
        
        elif self.posicionX + 0.05 > obstaculo14.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo14.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo14.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo14.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo15.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo15.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo15.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo15.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo16.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo16.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo16.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo16.posicionY + 0.05:
            self.colisionando = True
                
        elif self.posicionX + 0.05 > obstaculo17.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo17.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo17.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo17.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo18.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo18.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo18.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo18.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo19.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo19.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo19.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo19.posicionY + 0.05:
            self.colisionando = True
            
        elif self.posicionX + 0.05 > obstaculo20.posicionX - 0.05 and self.posicionX - 0.05 < obstaculo20.posicionX + 0.05 and self.posicionY + 0.05 > obstaculo20.posicionY - 0.05 and self.posicionY - 0.05 < obstaculo20.posicionY + 0.05:
            self.colisionando = True
                
        else:
            self.colisionando = False

        if  obstaculo.vivo == False and obstaculo2.vivo == False and obstaculo3.vivo == False and obstaculo4.vivo == False and obstaculo5.vivo == False and obstaculo6.vivo == False and obstaculo7.vivo == False and obstaculo8.vivo == False and obstaculo9.vivo == False and obstaculo11.vivo == False and obstaculo12.vivo == False and obstaculo13.vivo == False and obstaculo14.vivo == False and obstaculo15.vivo == False and obstaculo16.vivo == False and obstaculo17.vivo == False and obstaculo18.vivo == False and obstaculo19.vivo == False and obstaculo20.vivo == False :
            self.disparando
            exit()


    def actualizar(self, window, tiempo_delta):
        estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)


        if estadoIzquierda == glfw.PRESS:
            self.angulo = self.angulo + (self.velocidad_angular * tiempo_delta)
            if self.angulo > 360:
                self.angulo = 0
        if estadoDerecha == glfw.PRESS:
            self.angulo = self.angulo - (self.velocidad_angular * tiempo_delta)
            if self.angulo < 0:
                self.angulo = 360

        #if estadoArriba == glfw.PRESS:
        #   yCarrito = yCarrito + \
        #     (sin((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        #  xCarrito = xCarrito + \
            #    (cos((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)

        #Cierre del juego
        if self.colisionando == True: 
            sys.exit()
    
    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        if self.colisionando == True:
            glColor3f(1.0, 1.0, 1.0)
        else:
            glColor3f(0.745, 0.749, 0.749)
        glVertex3f(0.0, 0.05, 0.0)
        glVertex3f(-0.05, -0.05, 0.0)
        glVertex3f(0.05, -0.05, 0.0)
        glEnd()
        glPopMatrix()
  
        