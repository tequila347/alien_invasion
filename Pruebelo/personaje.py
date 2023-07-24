import pygame
class Personaje:
    def __init__(self,ia):
        """Inicializa la imagen del personaje y configura la poscicion inicial"""
        self.pantalla=ia.pantalla
        self.pantalla_rect=ia.pantalla.get_rect()
        #Carga la imagen del personaje y obtiene su rect
        self.imagen=pygame.image.load('imagenes/personaje.bmp')
        self.rect=self.imagen.get_rect()
        #Coloca inicialmente al personaje en el centro de la pantalla
        self.rect.center=self.pantalla_rect.center
    def blitme(self):
        """Dibuja al personaje en su ubicacion actual"""
        self.pantalla.blit(self.imagen, self.rect)