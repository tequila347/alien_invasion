import sys  
import pygame
from configuracion import Configuracion
from nave import Nave
class InvasionAlien:
    """Clase general para gestionar los recursos y el comportamiento del juego"""
    def __init__(self):
        """Inicializa el juego y crea recursos""" 
        pygame.init()
        self.configuracion=Configuracion()
        self.pantalla=pygame.display.set_mode((self.configuracion.pantalla_ancho, self.configuracion.pantalla_largo))
        pygame.display.set_caption("Invasion Alien")
        #Configura el color de fondo
        self.bg_color=(2130, 230, 230)
        self.nave=Nave(self)
    def correr_juego(self):
        """Inicia el bucle principal para el juego"""
        while True:
            #Busca eventos de teclado y raton
            for evento in pygame.event.get():
                if evento.type==pygame.QUIT:
                    sys.exit()
            #Redinuja la pantalla en cada paso por el bucle
            self.pantalla.fill(self.configuracion.bg_color)
            self.nave.blitme()
            #Hace visible la ultima pantalla dibiujada
            pygame.display.flip()
if __name__=='__main__':
    #Hace una instancia del juego y lo ejecuta
    ia=InvasionAlien()
    ia.correr_juego()