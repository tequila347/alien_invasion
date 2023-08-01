import pygame
class Nave:
    """Una clase para gestionar la nave"""
    def __init__(self, ia_juego):
        """Inicializa la nave y configura la poscicion inicial"""
        self.pantalla=ia_juego.pantalla
        self.configuracion=ia_juego.configuracion
        self.pantalla_rect=ia_juego.pantalla.get_rect()
        #Carga la imagen de la nave y obtiene su rect
        self.imagen=pygame.image.load('imagenes/ship.bmp')
        self.rect=self.imagen.get_rect()
        #Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom=self.pantalla_rect.midbottom
        #Guarda un valor decimal para la posicion horizontal de la nave
        self.x=float(self.rect.x) 
        #Bandera en movimiento
        self.movimiento_derecha=False
        self.movimiento_izquierda=False
    def update(self):
        """Actualiza la posicion de la nave en funcion de la bandera en movimiento"""
        if self.movimiento_derecha and self.rect.right < self.pantalla_rect.right:
            self.x+=self.configuracion.velocidad_nave
        if self.movimiento_izquierda and self.rect.left>0:
            self.x-=self.configuracion.velocidad_nave
        #Actualiza el objeto rect de self.x
        self.rect.x=self.x
    def blitme(self):
        """Dibuja l anve en su ubicacion actual"""
        self.pantalla.blit(self.imagen, self.rect) 