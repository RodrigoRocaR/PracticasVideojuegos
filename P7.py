import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_MONEDAS = 40
ESCALA_SPRITE_JUGADOR = 0.60
ESCALA_SPRITE_OBJETO = 0.10


class Moneda(arcade.Sprite):
    def __init__(self, nombre_archivo, escala_sprite):
        super().__init__(nombre_archivo, escala_sprite)
        self.change_x = 0
        self.change_y = 0

    def reset_pos_aleatoria(self):
        self.bottom = SCREEN_HEIGHT
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Codigo para mover monedas
        # self.center_y -= 1  # hacer que caigan
        self.center_x += self.change_x
        self.center_y += self.change_y
        # si cae que no se vaya de la pantalla, sino que vuelva arriba en una posicion random
        # if self.top < 0:
        #   self.reset_pos_aleatoria()
        # Que reboten las monedas
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1
        # Rotacion monedas
        self.angle += 1
        if self.angle >= 359:  # para que no se pase lo reseteamos, no es imprescondible pero conviene para que
            # no crezcan demasiado los angulos
            self.angle -= 360


class Pincho(arcade.Sprite):
    def __init__(self, nombre_archivo, escala_sprite):
        super().__init__(nombre_archivo, escala_sprite)

    def reset_pos(self):
        self.bottom = SCREEN_HEIGHT

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class ComeMonedas(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")
        # Sprite lists
        self.lista_jugador = None
        self.lista_monedas = None
        self.lista_pinchos = None
        # Info jugador
        self.sprite_jugador = None
        self.puntuacion = 0

        self.set_mouse_visible(False)  # ocultamos el cursor
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprites
        self.lista_jugador = arcade.SpriteList()
        self.lista_monedas = arcade.SpriteList()
        self.lista_pinchos = arcade.SpriteList()
        # Score
        self.puntuacion = 0
        # Set up the player
        self.sprite_jugador = arcade.Sprite(
            "C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
            "\\Sprites prestados prueba\\heroe.png", ESCALA_SPRITE_JUGADOR)
        self.sprite_jugador.center_x = 100
        self.sprite_jugador.center_y = 100
        self.lista_jugador.append(self.sprite_jugador)
        # Ponemos monedas y pinchos
        for i in range(MAX_MONEDAS):
            # Monedas
            moneda = Moneda(
                "C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                "\\Sprites prestados prueba\\Moneda.png", ESCALA_SPRITE_OBJETO)
            moneda.center_x = random.randrange(SCREEN_WIDTH)
            moneda.center_y = random.randrange(SCREEN_HEIGHT)
            moneda.change_x = random.randrange(-3, 4)
            moneda.change_y = random.randrange(-3, 4)
            # Las guardamos en la lista de monedas
            self.lista_monedas.append(moneda)
            # Pinchos
            pincho = Pincho("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                            "\\Sprites prestados prueba\\Spike_Bomb.png", ESCALA_SPRITE_OBJETO)
            pincho.center_x = random.randrange(SCREEN_WIDTH)
            pincho.center_y = random.randrange(SCREEN_HEIGHT)
            # Las guardamos en la lista de monedas
            self.lista_pinchos.append(pincho)

    def on_draw(self):
        arcade.start_render()
        self.lista_jugador.draw()
        self.lista_monedas.draw()
        self.lista_pinchos.draw()
        texto_pantalla = "Puntuación: " + str(self.puntuacion)
        arcade.draw_text(texto_pantalla, 10, 20, arcade.color.BLACK, 14)
        texto_pantalla2 = "Coge 30 puntos para ganar"
        arcade.draw_text(texto_pantalla2, SCREEN_WIDTH-200, 20, arcade.color.BLACK, 14)

        if self.puntuacion == 30:
            texto_victoria = "HAS GANADO!!"
            arcade.draw_text(texto_victoria, 250, SCREEN_HEIGHT/2, arcade.color.BLACK, 50)

    def update(self, delta_time):
        # Update each of the sprites
        # Check to see if the player is touching any coins
        # Remove any coins colliding with the player, and update the score
        if self.puntuacion < 30:     # si no hemos ganado
            self.lista_monedas.update()
            self.lista_pinchos.update()
        lista_colisiones_monedas = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_monedas)
        # Cada vez que chocamos con una moneda:
        for moneda in lista_colisiones_monedas:
            moneda.remove_from_sprite_lists()
            self.puntuacion += 1
        lista_colisiones_pinchos = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_pinchos)
        # Cada vez que chocamos con un pincho:
        for pincho in lista_colisiones_pinchos:
            pincho.remove_from_sprite_lists()
            self.puntuacion -= 1

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.puntuacion < 30:     # si no hemos ganado
            self.sprite_jugador.center_x = x
            self.sprite_jugador.center_y = y


def main():
    ventana = ComeMonedas()
    ventana.setup()
    arcade.run()


if __name__ == "__main__":
    main()
