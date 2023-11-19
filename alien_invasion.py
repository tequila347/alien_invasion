import sys  
import pygame
from configuracion import Configuracion
from nave import Nave
from bala import Bala
from alien import Alien
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
        self.balas=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        self._crear_flota()
    def correr_juego(self):
        """Inicia el bucle principal para el juego"""
        while True:
            self._chequear_eventos()
            self.nave.update()
            #self.balas.update()
            self._actualizar_balas()
            self._update_aliens()
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
        elif evento.key==pygame.K_q:
            sys.exit()
        elif evento.key==pygame.K_SPACE:
            self._disparar_bala()
    def _chequear_evento_keyup(self, evento):
        """Responde a liberaciones de teclas"""
        if evento.key==pygame.K_RIGHT:
            self.nave.movimiento_derecha=False
        elif evento.key==pygame.K_LEFT:
            self.nave.movimiento_izquierda=False
    def _disparar_bala(self):
        """Crea una bala nueva y añade al grupo de balas"""
        if len(self.balas)<self.configuracion.balas_permitidas:
            nueva_bala=Bala(self)
            self.balas.add(nueva_bala)
    def _actualizar_balas(self):
        """Actualiza la posicion de las balas y se deshace de las viejas"""
        #Actualiza las osiciones de las balas
        self.balas.update()
        #Se deshace de las balas que han desaparecido
        for bala in self.balas.copy():
                if bala.rect.bottom <=0:
                    self.balas.remove(bala)
        self._check_bala_alien_colision()  
    def _check_bala_alien_colision(self):
        """Responde a las colisiones bala-alien"""
        #Retira todas las balas y aliens que han chocado
        colisiones=pygame.sprite.groupcollide(
            self.balas, self.aliens, True,True)
        if not self.aliens:
            #Destruye las balas existentes y crea una flota nueva
            self.balas.empty()
            self._crear_flota()
    def _update_aliens(self):
        """Comprueba si la flota esta en un borde,
            despues actualiza las posiciones de todos los aliens de la flota."""
        #self.check_flota_borde()
        if self.check_flota_borde():
            for alien in self.aliens.sprites():
                alien.rect.y+=self.configuracion.velocidad_caida_flota
            self.configuracion.flota_direccion *=-1
        self.aliens.update()
    def _crear_flota(self):
        """Crea la flota de aliens"""
        #Crea un alien y halla el numero de aliens en una fila
        #El espacio entre aliens es igual a la anchura de un alien
        alien=Alien(self)
        alien_ancho, alien_alto = alien.rect.size
        espacio_disponible_x=self.configuracion.pantalla_ancho - (2*alien_ancho)
        numero_aliens_x=espacio_disponible_x // (2*alien_ancho)
        #Determina el numero de filas de aliens que caben en la pantalla#
        alto_nave=self.nave.rect.height
        espacio_disponible_y= (self.configuracion.pantalla_largo - 
                               (3 * alien_alto)-alto_nave)
        numero_filas=espacio_disponible_y//(2 * alien_alto)
        #Crea la flota completa de aliens
        for numero_fila in range(numero_filas):
            for numero_alien in range(numero_aliens_x):
                self._crear_alien(numero_alien, numero_fila)
    def check_flota_borde(self):
        """Responde adecuadamente si un alien ha llegado al borde"""
        for alien in self.aliens.sprites():
            if alien.check_bordes():
                self._cambiar_flota_direccion()
                break
    def _cambiar_flota_direccion(self):
        """Baja toda la flota y cambia su direccion"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.configuracion.velocidad_caida_flota
        self.configuracion.flota_direccion*=-1    
    def _crear_alien(self, numero_alien, numero_filas):
        """Crea un alien y lo coloca en una fila"""
        alien=Alien(self)
        alien_ancho,alien_alto=alien.rect.size
        alien.x=alien_ancho + 2 * alien_ancho * numero_alien
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height + 2 * alien.rect.height * numero_filas
        self.aliens.add(alien)
    def _actualizar_pantalla(self):
         """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva"""
         self.pantalla.fill(self.configuracion.bg_color)
         self.nave.blitme()
         for bala in self.balas.sprites():
                bala.dibujar_bala()
         self.aliens.draw(self.pantalla)
         pygame.display.flip()
if __name__=='__main__':
    #Hace una instancia del juego y lo ejecuta
    ia=InvasionAlien()
    ia.correr_juego()