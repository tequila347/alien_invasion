import pygame
from pygame.sprite import Sprite
class Bala(Sprite):
    """Una clase para gestionar las balas disparadas desde la nave"""
    def __init__(self, ia_juego):
        """Crea un objeto par la bala en la posicion actual de la nave"""
        super().__init__()
        self.panatalla=ia_juego.pantalla
        self.configuracion=ia_juego.configuracion
        self.color=self.configuracion.color_bala

        #Crea un rectangulo para la bala en (0, 0) y luego establece la posicion correcta
        self.rect=pygame.Rect(0, 0, self.configuracion.ancho_bala,
                              self.configuracion.largo_bala)
        self.rect.midtop=ia_juego.nave.rect.midtop
        #Guarda la posicion de la bala como valor decimal.
        self.y=float(self.rect.y)
    def update(self):
        """Mueve la bala hacia arriba por la pantalla"""
        #Actualiza la posicion decimal de la bala.
        self.y-=self.configuracion.velocidad_bala
        #Actualiza la posicion del rectangulo
        self.rect.y=self.y
    def dibujar_bala(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.panatalla, self.color, self.rect)