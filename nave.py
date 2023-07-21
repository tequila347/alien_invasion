import pygame
class Nave:
    """Una clase para gestionar la nave"""
    def __init__(self, ia_juego):
        """Inicializa la nave y configura la poscicion inicial"""
        self.pantalla=ia_juego.pantalla
        self.pantalla_rect=ia_juego.pantalla.get_rect()
        #Carga la imagen de la nave y obtiene su rect
        self.imagen=pygame.image.load('imagenes/ship.bmp')
        self.rect=self.imagen.get_rect()
        #Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom=self.pantalla_rect.midbottom
    def blitme(self):
        """Dibuja l anve en su ubicacion actual"""
        self.pantalla.blit(self.imagen, self.rect) 