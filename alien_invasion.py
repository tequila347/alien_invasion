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
        self.pantalla=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.configuracion.pantalla_ancho=self.pantalla.get_rect().width
        self.configuracion.pantalla_largo=self.pantalla.get_rect().height
        pygame.display.set_caption("Invasion Alien")
        #Configura el color de fondo
        #self.bg_color=(230, 230, 230)
        self.nave=Nave(self)
    def correr_juego(self):
        """Inicia el bucle principal para el juego"""
        while True:
            self._chequear_eventos()
            self.nave.update()
            self._actualizar_pantalla()
    def _chequear_eventos(self): 
        """Responde a pulsaciones de teclas y eventos del raton"""
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                sys.exit()
            elif evento.type==pygame.KEYDOWN:
                self._chequear_evento_keydown(evento)
            elif evento.type==pygame.KEYUP:
                self._chequear_evento_keyup(evento)
    def _chequear_evento_keydown(self, evento):
        """Responde a las pulsaciones de teclas"""
        if evento.key==pygame.K_RIGHT:
            self.nave.movimiento_derecha=True
        elif evento.key==pygame.K_LEFT:
            self.nave.movimiento_izquierda=True
    def _chequear_evento_keyup(self, evento):
        """Responde a liberaciones de teclas"""
        if evento.key==pygame.K_RIGHT:
            self.nave.movimiento_derecha=False
        elif evento.key==pygame.K_LEFT:
            self.nave.movimiento_izquierda=False
        elif evento.key==pygame.K_q:
            sys.exit()
    def _actualizar_pantalla(self):
         """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva"""
         self.pantalla.fill(self.configuracion.bg_color)
         self.nave.blitme()
         pygame.display.flip()
if __name__=='__main__':
    #Hace una instancia del juego y lo ejecuta
    ia=InvasionAlien()
    ia.correr_juego()