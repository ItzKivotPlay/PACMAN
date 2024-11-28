import pyxel
#EL STR SIRVE PARA IMPRIMIR UNA CUALIDAD DEL OBJETO Y NO IMPRIMIR LA DIRECCIÓN DE ÉSTE
class PacManApp:
    def __init__(self):
        pyxel.init(1024, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        self.pacman_x = 80
        self.pacman_y = 60

        # Cargar el archivo de recursos
        #pyxel.load("assets/resourcesPACMAN.pyxres")
        
        # Crear la instancia de AnimatedSprite para el personaje animado
        self.pacman = AnimatedSprite(self.pacman_x, self.pacman_y)
        #Inicializamos el fantasma
        self.ghost1 = Ghost1()
        self.ghost2 = Ghost2()
        self.ghost3 = Ghost3()
        self.ghost4 = Ghost4()
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento del Pac-Man con las teclas W, A, S, D
        movimiento = False  # Variable para verificar si hubo movimiento

        if pyxel.btn(pyxel.KEY_W):  # Detecta si se presionó la tecla
            self.pacman_y -= 5
            
        if pyxel.btn(pyxel.KEY_S):
            self.pacman_y += 5
            
        if pyxel.btn(pyxel.KEY_A):
            self.pacman_x -= 5

        if pyxel.btn(pyxel.KEY_D):
            self.pacman_x += 5
            
        if pyxel.btnp(pyxel.KEY_F):
            self.pacman_x += 0
            movimiento = True
        
        # Actualizar la posición del pacman animado
        self.pacman.x = self.pacman_x
        self.pacman.y = self.pacman_y

        # Cambiar el fotograma solo si hubo movimiento
        if movimiento:
            self.pacman.change_frame()
        

    def draw(self):
        pyxel.cls(0)
        
        # Dibujar el Pac-Man animado
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.pacman.draw()
        #ahora el fantasma
        pyxel.load("assets/resources.pyxres")
        self.ghost1.draw()
        self.ghost2.draw()
        self.ghost3.draw()
        self.ghost4.draw()

class AnimatedSprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0
        self.frame_count = 2  # Número de fotogramas en la hoja de sprites

    def change_frame(self):
        # Cambia al siguiente fotograma
        self.frame_index = (self.frame_index + 1) % self.frame_count

    def draw(self):
        # Dibuja el fotograma actual del sprite
        pyxel.blt(self.x, self.y, 0, self.frame_index * 40, 0, 36, 39, 40)
    
class Ghost1:
    def __init__(self):
        self.ghost_x = 120
        self.ghost_y = 120
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 1, 0, 0, 16, 16, 0)

class Ghost2:
    def __init__(self):
        self.ghost_x = 45
        self.ghost_y = 190
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 1, 0, 0, 16, 16, 0)


class Ghost3:
    def __init__(self):
        self.ghost_x = 220
        self.ghost_y = 60
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 1, 0, 0, 16, 16, 0)

class Ghost4:
    def __init__(self):
        self.ghost_x = 10
        self.ghost_y = 50
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 1, 0, 0, 16, 16, 0)

# Iniciar el juego
PacManApp()



