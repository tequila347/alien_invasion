import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Una clase para representar un solo alien en la flota"""
    def __init__(self, ia_juego):
        """Inicializa el alien y establece su posicion inicial"""
        super().__init__()
        self.pantalla=ia_juego.pantalla
        #Carga la imagen del alien y configura su atributo rect
        self.image=pygame.image.load('imagenes/alien.bmp')
        self.rect=self.image.get_rect()
        #Inicia un nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #Guarda la posicion horizontal exacta del alien
        self.x=float(self.rect.x)
