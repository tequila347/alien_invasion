class Configuracion:
    """Una clase para guardar toda la configuracion de Invasion Alien"""
    def __init__(self):
        """Inicializa la configuracion del juego"""
        #Configuracion de la pantalla
        self.pantalla_ancho=1200
        self.pantalla_largo=800
        self.bg_color=(230, 230, 230) 
        self.velocidad_nave = 2
        #Configuracion de las balas
        self.velocidad_bala=3
        self.ancho_bala=3
        self.largo_bala=15
        self.color_bala=(255,0,0)
        self.balas_permitidas=3
        #Configuraciones de alien
        self.velocidad_alien=1.0
        self.velocidad_caida_flota=10
        #flota_direccion de 1 representa derecha; -1 representa izquierda
        self.flota_direccion=1
        

