from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random    
import sys
#from playsound import playsound
from Carrito import *
from Obstaculo import *
from Bala import *
from Fondo import *

#Llamar la clase carrito
fondo = Fondo()
bala = Bala()
carrito = Carrito()
obstaculo = Obstaculo()
obstaculo2 = Obstaculo2()
obstaculo3 = Obstaculo3()
obstaculo4 = Obstaculo4()
obstaculo5 = Obstaculo5()
obstaculo6 = Obstaculo6()
obstaculo7 = Obstaculo7()
obstaculo8 = Obstaculo8()
obstaculo9 = Obstaculo9()
obstaculo11 = Obstaculo11()
obstaculo12 = Obstaculo12()
obstaculo13 = Obstaculo13()
obstaculo14 = Obstaculo14()
obstaculo15 = Obstaculo15()
obstaculo16 = Obstaculo16()
obstaculo17 = Obstaculo17()
obstaculo18 = Obstaculo18()
obstaculo19 = Obstaculo19()
obstaculo20 = Obstaculo20()


# el desfase es debido a que el triangulo en 0 grados voltea
# hacia arriba y no hacia la derecha

tiempo_anterior = 0

#musica
#playsound('music.mp3', False)




       

def actualizar(window):
    global tiempo_anterior
    global carrito
    global bala
    global obstaculo
    global obstaculo2
    global obstaculo3
    global obstaculo4
    global obstaculo5
    global obstaculo6
    global obstaculo7
    global obstaculo8
    global obstaculo9
    global obstaculo11
    global obstaculo12
    global obstaculo13
    global obstaculo14
    global obstaculo15
    global obstaculo16
    global obstaculo17
    global obstaculo18
    global obstaculo19
    global obstaculo20

    
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    carrito.checar_colisiones(obstaculo, obstaculo2, obstaculo3, obstaculo4, obstaculo5, obstaculo6, obstaculo7, obstaculo8, obstaculo9, obstaculo11, obstaculo12, obstaculo13, obstaculo14, obstaculo15, obstaculo16, obstaculo17, obstaculo18, obstaculo19, obstaculo20)
    carrito.actualizar(window, tiempo_delta)

    bala.actualizar(tiempo_delta, carrito, obstaculo, obstaculo2, obstaculo3, obstaculo4, obstaculo5, obstaculo6, obstaculo7, obstaculo8, obstaculo9, obstaculo11, obstaculo12, obstaculo13, obstaculo14, obstaculo15, obstaculo16, obstaculo17, obstaculo18, obstaculo19, obstaculo20)    
    
    tiempo_anterior = tiempo_actual
 
  


def dibujar():
    global fondo
    global bala
    global carrito
    global obstaculo
    global obstaculo
    global obstaculo2
    global obstaculo3
    global obstaculo4
    global obstaculo5
    global obstaculo6
    global obstaculo7
    global obstaculo8
    global obstaculo9
    global obstaculo11
    global obstaculo12
    global obstaculo13
    global obstaculo14
    global obstaculo15
    global obstaculo16
    global obstaculo17
    global obstaculo18
    global obstaculo19
    global obstaculo20
       
    # rutinas de dibujo
    fondo.dibujar()
    obstaculo.dibujar()
    obstaculo2.dibujar()
    obstaculo3.dibujar()
    obstaculo4.dibujar()
    obstaculo5.dibujar()
    obstaculo6.dibujar()
    obstaculo7.dibujar()
    obstaculo8.dibujar()
    obstaculo9.dibujar()
    obstaculo11.dibujar()
    obstaculo12.dibujar()
    obstaculo13.dibujar()
    obstaculo14.dibujar()
    obstaculo15.dibujar()
    obstaculo16.dibujar()
    obstaculo17.dibujar()
    obstaculo18.dibujar()
    obstaculo19.dibujar()
    obstaculo20.dibujar()
    carrito.dibujar()
    bala.dibujar(carrito) 


def key_callback(window, key, scancode, action, mods):
    global carrito
    global bala
    if not carrito.disparando and key == glfw.KEY_SPACE and action == glfw.PRESS:
        carrito.disparando = True
        bala.posicionX = carrito.posicionX
        bala.posicionY = carrito.posicionY
        bala.anguloBala = carrito.angulo


def main():
    # inicia glfw
    if not glfw.init():
        return

    # crea la ventana,
    # independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Arcade - Asteroids", None, None)

    # Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    # Establecemos el contexto
    glfw.make_context_current(window)

    # Activamos la validación de
    # funciones modernas de OpenGL
    glewExperimental = True

    # Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    glfw.set_key_callback(window, key_callback)


    while not glfw.window_should_close(window):
        # Establece regiond e dibujo
        glViewport(0, 0, 800, 800)
        # Establece color de borrado
        glClearColor(0.0, 0.0, 0.0, 0)
        # Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        actualizar(window)
        dibujar()

        # Preguntar si hubo entradas de perifericos
        # (Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        # Intercambia los buffers
        glfw.swap_buffers(window)

    # Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    # Termina los procesos que inició glfw.init
    glfw.terminate()  


if __name__ == "__main__":
    main()