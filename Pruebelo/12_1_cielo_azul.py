import sys
import pygame
from configuracion_ejercicio import Ejercicio12_1Configuracion
from personaje import Personaje
class CieloAzul:
    """Clase general para gestionar los recuersos y el comportamiento del ejercicio"""
    def __init__(self):
        """Inicializa el progrma y crea recursos"""
        pygame.init()
        self.config=Ejercicio12_1Configuracion()
        self.pantalla=pygame.display.set_mode((self.config.pantalla_ancho, self.config.pantalla_largo))
        pygame.display.set_caption("Ejercicio Cielo Azul")
        self.personaje=Personaje(self)
    def correr_sistema(self):
        """Inicializa el bucle principal para del juego"""
        while True:
            self._chequear_eventos()
            self._actualizar_pantalla()
    def _chequear_eventos(self):
        """Responde a pulsaciones de teclas y eventos del raton"""
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                sys.exit()
    def _actualizar_pantalla(self):
        """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva"""
        self.pantalla.fill(self.config.bg_color)
        self.personaje.blitme()
        pygame.display.flip()
if __name__=='__main__':
    #Hace una instancia de la plicacion y lo ejecuta
    ia=CieloAzul()
    ia.correr_sistema()    
