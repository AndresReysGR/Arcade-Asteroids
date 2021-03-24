from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Obstaculo():
    posicionX = 0.0
    posicionY = -0.9
    vivo = True

    def dibujar(self): #PENTAGONO
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0 )
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(0.490, 0.117, 0.980) 
            glVertex(0.0, 0.05, 0.0)
            glVertex(-0.05, 0.0, 0.0)
            glVertex(-0.03, -0.05, 0.0)
            glVertex(0.03, -0.05, 0.0)
            glVertex(0.05,0.0, 0.0)
            glEnd()
            glPopMatrix()

            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
            #xObstaculo2 = -1.0
                self.posicionX = 0.0
                self.posicionY = -0.9

class Obstaculo2():
    posicionX = 0.9
    posicionY = 0.9
    vivo = True

    def dibujar(self): #OCTAGONO
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(0.141, 0.078, 1.0)
            glVertex(0.01, 0.05, 0.0)
            glVertex(-0.02, 0.05, 0.0)
            glVertex(-0.05, 0.02, 0.0)
            glVertex(-0.05, -0.01, 0.0)
            glVertex(-0.02, -0.04, 0.0)
            glVertex(0.01, -0.04, 0.0)
            glVertex(0.04, -0.01, 0.0)
            glVertex(0.04, 0.02, 0.0)
            glEnd()
            glPopMatrix()

                #Obstaculo2
            if self.posicionX > 0 or self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001
                self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.9
                self.posicionY = 0.9
    
class Obstaculo3():
    posicionX = -0.6
    posicionY = -0.6
    vivo = True

    def dibujar(self):#HEXAGONO

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(0.277, 0.439, 0.760)
            glVertex(0.02, 0.05, 0.0)
            glVertex(-0.02, 0.05, 0.0)
            glVertex(-0.05, 0.01, 0.0)
            glVertex(-0.02, -0.03, 0.0)
            glVertex(0.02, -0.03, 0.0)
            glVertex(0.05, 0.01, 0.0)
            glEnd()
            glPopMatrix()

                #Obstaculo3
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionY = -0.6
                self.posicionX = -0.6

class Obstaculo4():
    posicionX = 0.5
    posicionY = -0.6
    vivo = True

    def dibujar(self):


        if self.vivo: #TRAPECIO
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(0.639, 0.239, 0.211)
            glVertex(0.03, 0.04, 0.0)
            glVertex(-0.03, 0.04, 0.0)
            glVertex(-0.05, -0.03, 0.0)
            glVertex(0.05, -0.03, 0.0)
            glEnd()
            glPopMatrix()

                #Obstaculo4
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.5
                self.posicionY = -0.6


class Obstaculo5():
    posicionX = -0.6
    posicionY = 0.6
    vivo = True

    def dibujar(self): #COHETE

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1, 0, 0)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.03 - 0.05, sin(angulo)*0.03 + 0.00,0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(1, 0, 0)
            glVertex(-0.02, 0.02, 0.0)
            glVertex(-0.02, -0.02, 0.0)
            glVertex(-0.04, 0.015, 0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(1, 0, 0)
            glVertex(-0.02, 0.02, 0.0)
            glVertex(-0.02, -0.02, 0.0)
            glVertex(-0.04, -0.015, 0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(1, 0, 0)
            glVertex(-0.02, 0.01, 0.0)
            glVertex(-0.04, 0.0, 0.0)
            glVertex(-0.02, -0.015, 0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(1, 0, 0)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.01 + 0.03,sin(angulo) * 0.01 + 0.0 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(0.03, 0.01, 0.0)
            glVertex(-0.02, 0.01, 0.0)
            glVertex(-0.02, -0.01, 0.0)
            glVertex(0.03, -0.01, 0.0)
            glEnd()
            

            glBegin(GL_POLYGON) #VENTANA
            glColor3f(0.380, 0.741, 0.909)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.005 + 0.02,sin(angulo) * 0.005 + 0.0 ,0.0) #2/ X Y Y
            glEnd()

            glPopMatrix()

                #Obstaculo5
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.6
                self.posicionY = 0.6

class Obstaculo6():
    posicionX = 0.2
    posicionY = -0.6
    vivo = True


    def dibujar(self): #PIRAMIDE

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(0.858, 0.713, 0.274)
            glVertex(0.0, 0.05, 0.0)
            glVertex(-0.05, -0.03, 0.0)
            glVertex(0.0, -0.05, 0.0)
            glVertex(0.05, -0.03, 0.0)
            glEnd()
            glPopMatrix()

                #Obstaculo6
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX =  0.2
                self.posicionY = -0.6

class Obstaculo7():
    posicionX = 0.5
    posicionY = 0.7
    vivo = True

    def dibujar(self):

        if self.vivo: #BANDERA
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(-0.02, 0.05, 0.0)
            glVertex(-0.03, 0.05, 0.0)
            glVertex(-0.03, -0.05, 0.0)
            glVertex(-0.02, -0.05, 0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(0.639, 0.239, 0.211)
            glVertex(-0.02, 0.05, 0.0)
            glVertex(-0.02, 0.0, 0.0)
            glVertex(0.03, 0.020, 0.0)
            glEnd()

            glPopMatrix()
        
            #Obstaculo7
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.5
                self.posicionY = 0.7

class Obstaculo8():
    posicionX = -0.7
    posicionY = -0.5
    vivo = True


    def dibujar(self): #ESTRELLA AZUL 6 PICOS

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.258, 0.878, 0.960)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.07 - 0.0, sin(angulo)*0.07 + 0.00,0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(0.258, 0.878, 0.960)
            glVertex(0.03, 0.03, 0.0)
            glVertex(-0.03, 0.03, 0.0)
            glVertex(0.0, -0.05, 0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(0.258, 0.878, 0.960)
            glVertex(0.03, -0.03, 0.0)
            glVertex(0.0, 0.05, 0.0)
            glVertex(-0.03, -0.03, 0.0)
            glEnd()

            glPopMatrix()

            #Obstaculo8
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.7
                self.posicionY = -0.5

class Obstaculo9():
    posicionX = 0.0
    posicionY = 0.9
    vivo = True

    def dibujar(self): #ESTRELLA 2 8 PICOS

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glRotate(10, 0.0, 0.0, 0.0)
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.619, 1.0, 0.941)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.07 - 0.0, sin(angulo)*0.07 + 0.00,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0.619, 1.0, 0.941)
            glVertex(0.03, 0.03, 0.0)
            glVertex(-0.03, 0.03, 0.0)
            glVertex(-0.03, -0.03, 0.0)
            glVertex(0.03, -0.03, 0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0.619, 1.0, 0.941)
            glVertex(0.0, 0.04, 0.0)
            glVertex(-0.04, 0.0, 0.0)
            glVertex(0.0, -0.04, 0.0)
            glVertex(0.04, 0.0, 0.0)
            glEnd()
            glPopMatrix()

        #Obstaculo9
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.0
                self.posicionY = 0.9

class Obstaculo11():
    posicionX = 0.5
    posicionY = -0.9
    vivo = True

    def dibujar(self): #SATURNO

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.721, 0.580, 0.2)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.07 - 0.05, sin(angulo)*0.07 + 0.05, 0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(1.0, 0.874, 0.529)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.025 + 0.05 ,0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.721, 0.580, 0.2)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.04 - 0.05,sin(angulo) * 0.04 + 0.05 ,0.0)
            glEnd()
            glPopMatrix()

            
            #Obstaculo11
            
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.5
                self.posicionY = -0.9   

class Obstaculo12():
    posicionX = -0.2
    posicionY = -0.9
    vivo = True

    def dibujar(self): #ALIEN 

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.521, 0.949, 0.901)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.08 - 0.05, sin(angulo)*0.08 + 0.03,0.0)
            glEnd()

            glBegin(GL_POLYGON) #LUZ NAVE
            glColor3f(0.521, 0.949, 0.901)
            glVertex(-0.04, 0.03, 0.0)
            glVertex(-0.06, 0.03, 0.0)  
            glVertex(-0.07, -0.03, 0.0)
            glVertex(-0.03, -0.03, 0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.529, 1.0, 0.788)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.025 - 0.05,sin(angulo) * 0.025 + 0.05 ,0.0)
            glEnd()
            

            glBegin(GL_POLYGON)
            glColor3f(0.368, 0.380, 0.384)
            for x in range(360): 
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.02 + 0.04 ,0.0)
            glEnd()



            glPopMatrix()

            
            #Obstaculo12
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.2
                self.posicionY = -0.9 

class Obstaculo13():
    posicionX = -0.3
    posicionY = 0.9
    vivo = True

    def dibujar(self): #PLANETA
    
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.639, 0.239, 0.211)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.08 - 0.05, sin(angulo)*0.08 + 0.05,0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.639, 0.239, 0.211)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.05 + 0.05 ,0.0)
            glEnd()
            glPopMatrix()

            
            #Obstaculo13
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.3
                self.posicionY = 0.9

class Obstaculo14():
    posicionX = 0.05
    posicionY = -0.65
    vivo = True


    def dibujar(self): #ASTONAUTA


        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_POLYGON)
            glColor3f(1, 1, 1)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.02 - 0.0,sin(angulo) * 0.02 + 0.02 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(0.01, 0.02, 0.0)
            glVertex(-0.01, 0.02, 0.0)
            glVertex(-0.01, -0.02, 0.0)
            glVertex(0.01, -0.02, 0.0)
            glEnd()


            glBegin(GL_POLYGON)
            glColor3f(0, 0, 0)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.015 - 0.0,sin(angulo) * 0.015 + 0.02 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(0.01, -0.02, 0.0)
            glVertex(0.002, -0.02, 0.0)
            glVertex(0.002, -0.04, 0.0)
            glVertex(0.01, -0.04, 0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(-0.002, -0.02, 0.0)
            glVertex(-0.01, -0.02, 0.0)
            glVertex(-0.01, -0.04, 0.0)
            glVertex(-0.002, -0.04, 0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(0.02, 0.01, 0.0)
            glVertex(0.01, 0.01, 0.0)
            glVertex(0.01, -0.01, 0.0)
            glVertex(0.02, -0.01, 0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(1, 1, 1)
            glVertex(-0.01, 0.01, 0.0)
            glVertex(-0.02, 0.01, 0.0)
            glVertex(-0.02, -0.01, 0.0)
            glVertex(-0.01, -0.01, 0.0)
            glEnd()
            glPopMatrix()
        
            #Obstaculo14
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.65
                self.posicionY = 0.9

class Obstaculo15():
    posicionX = 0.55
    posicionY = 0.8
    vivo = True

    def dibujar(self): #PLANETA HUMO


        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1, 1, 1)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.04 - 0.03, sin(angulo)*0.04 + 0.02,0.0)
            glEnd()


            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.301, 0.701, 0.788)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.06 - 0.0, sin(angulo)*0.06 + 0.05,0.0)
            glEnd()

        
            glBegin(GL_POLYGON)
            glColor3f(0.301, 0.701, 0.788)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.04 - 0.0,sin(angulo) * 0.04 + 0.05 ,0.0) #2/ X Y Y
            glEnd()


            glBegin(GL_POLYGON)
            glColor3f(1, 1, 1)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.03 - 0.03,sin(angulo) * 0.01 + 0.02 ,0.0) #2/ X Y Y
            glEnd()


            glBegin(GL_POLYGON)
            glColor3f(1, 1, 1)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.03 - 0.05,sin(angulo) * 0.01 + 0.03 ,0.0) #2/ X Y Y
            glEnd()
            glPopMatrix()

                #Obstaculo15
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.55
                self.posicionY = 0.8


class Obstaculo16():
    posicionX = -0.55
    posicionY = -0.8
    vivo = True

    def dibujar(self): #CUADRADO


        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.337, 0.231, 0.470)
            glVertex(-0.05, 0.05, 0.0)
            glVertex(0.05, 0.05, 0.0)
            glVertex(0.05, -0.05, 0.0)
            glVertex(-0.05, -0.05, 0.0)
            glEnd()
            glPopMatrix()

                
            #Obstaculo16
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.55
                self.posicionY = -0.8

class Obstaculo17():
    posicionX = -0.55
    posicionY = -0.8
    vivo = True

    def dibujar(self): #RELOJ DE ARENA


        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_TRIANGLES)
            glColor3f(0.709, 0.537, 0.243)
            glVertex(0.05, 0.05, 0.0)
            glVertex(-0.05, 0.05, 0.0)
            glVertex(0.0, -0.01, 0.0)
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(0.709, 0.537, 0.243)
            glVertex(0.00, 0.00, 0.0)
            glVertex(-0.05, -0.05, 0.0)
            glVertex(0.05, -0.05, 0.0)
            glEnd()
            glPopMatrix()

        #Obstaculo17
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.55
                self.posicionY = -0.8

class Obstaculo18():
    posicionX = 0.9
    posicionY = -0.9
    vivo = True

    def dibujar(self): #ESTRELLA


        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.870, 0.756, 0.349)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.08,sin(angulo)*0.08,0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.701, 0.654, 0.313)
            glVertex(0.0, 0.05, 0.0)
            glVertex(-0.03, 0.0, 0.0)
            glVertex(0.0, -0.05, 0.0)
            glVertex(0.03, 0.0, 0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.980, 0.949, 0.705)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.01 + 0.00,sin(angulo) * 0.01 + 0.0 ,0.0) #2/ X Y Y
            glEnd()
            glPopMatrix()

                #Obstaculo18
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX > 0:
                    self.posicionX = self.posicionX - 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = 0.9
                self.posicionY = -0.9

class Obstaculo19():
    posicionX = -0.9
    posicionY = -0.9
    vivo = True

    def dibujar(self): #SOL

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.870, 0.756, 0.349)
            glVertex3f(0.0,0.0,0.0)
            for x in range(361):
                angulo = x * 3.14159 / 180.0
                glColor3f(0.0,0.0,0.0)
                glVertex3f(cos(angulo)*0.08,sin(angulo)*0.08,0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0.988, 0.474, 0.050)
            glVertex(0.04, 0.04, 0.0)
            glVertex(-0.04, 0.04, 0.0)
            glVertex(-0.04, -0.04, 0.0)
            glVertex(0.04, -0.04, 0.0)
            glEnd()

            glBegin(GL_QUADS)
            glColor3f(0.988, 0.474, 0.050)
            glVertex(0.05, 0.0, 0.0)
            glVertex(0.0, 0.05, 0.0)
            glVertex(-0.05, 0.0, 0.0) 
            glVertex(0.0, -0.05, 0.0)
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(1, 0.760, 0.239)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.04 + 0.00,sin(angulo) * 0.04 + 0.0 ,0.0) #2/ X Y Y
            glEnd()
            glPopMatrix()

                #Obstaculo19
            if  self.posicionY < 0:
                self.posicionY = self.posicionY + 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.9
                self.posicionY = -0.9

class Obstaculo20():
    posicionX = -0.9
    posicionY = 0.9
    vivo = True

    def dibujar(self): #ASTEROIDES
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)

            glBegin(GL_POLYGON)
            glColor3f(0.368, 0.380, 0.384)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.03 + 0.0 ,sin(angulo) * 0.03 + 0.0 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.368, 0.380, 0.384)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.02 - 0.025 ,sin(angulo) * 0.013 - 0.025 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.368, 0.380, 0.384)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.013 - 0.01 ,sin(angulo) * 0.013 - 0.03 ,0.0) #2/ X Y Y
            glEnd()

            glBegin(GL_POLYGON)
            glColor3f(0.368, 0.380, 0.384)
            for x in range(360):
                angulo = x * 3.1416 / 180.0
                glVertex3f(cos(angulo) * 0.013 + 0.01 ,sin(angulo) * 0.013 - 0.05 ,0.0) #2/ X Y Y
            glEnd()
            glPopMatrix()

                #Obstaculo20
            if  self.posicionY > 0:
                self.posicionY = self.posicionY - 0.001

                if self.posicionX < 0:
                    self.posicionX = self.posicionX + 0.001
            else:
                #xObstaculo2 = -1.0
                self.posicionX = -0.9 
                self.posicionY = 0.9


