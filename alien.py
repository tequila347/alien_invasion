import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Una clase para representar un solo alien en la flota"""
    def __init__(self, ia_juego):
        """Inicializa el alien y establece su posicion inicial"""
        super().__init__()
        self.pantalla=ia_juego.pantalla
        self.configuracion=ia_juego.configuracion
        #Carga la imagen del alien y configura su atributo rect
        self.image=pygame.image.load('imagenes/alien.bmp')
        self.rect=self.image.get_rect()
        #Inicia un nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #Guarda la posicion horizontal exacta del alien
        self.x=float(self.rect.x)
    def check_bordes(self):
        """Devuleve True si el alien esta en el borde de la pantalla"""
        pantalla_rect=self.pantalla.get_rect()
        if self.rect.right>=pantalla_rect.right or self.rect.left<=0:
            return True
    def update(self):
        """Mueve el alien hacia la derecha o hacia la izquierda"""
        self.x+=(self.configuracion.velocidad_alien *
                 self.configuracion.flota_direccion)
        self.rect.x=self.x 
        