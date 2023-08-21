class Configuracion:
    """Una clase para guardar toda la configuracion de Invasion Alien"""
    def __init__(self):
        """Inicializa la configuracion del juego"""
        #Configuracion de la pantalla
        self.pantalla_ancho=1200
        self.pantalla_largo=800
        self.bg_color=(230, 230, 230) 
        self.velocidad_nave = 5
        #Configuracion de las balas
        self.velocidad_bala=4
        self.ancho_bala=3
        self.largo_bala=15
        self.color_bala=(255,0,0)
        self.balas_permitidas=3
        

