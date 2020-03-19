import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


def dibujar_suelo_y_techo():
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_BLUE_GRAY)  # suelo
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 550, arcade.color.DARK_BLUE_GRAY)  # techo
    # Irregularidades
    arcade.draw_triangle_filled(0, 600, 100, 600, 0, 500, arcade.color.DARK_BLUE_GRAY)  # top izq
    arcade.draw_triangle_filled(200, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)  # mid bot
    arcade.draw_triangle_filled(400, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)
    arcade.draw_triangle_filled(650, 100, 800, 100, 800, 25, arcade.color.DARK_MIDNIGHT_BLUE)  # bot right


def dibujar_brillitos_fondo():
    coord_x = [100, 125, 300, 350, 200, 250, 325, 600, 675, 750]
    coord_y = [210, 250, 475, 500, 400, 350, 300, 430, 510, 465]
    for i in range(len(coord_x)):
        arcade.draw_circle_filled(coord_x[i], coord_y[i], 3, arcade.color.WHITE)


def dibujar_ojos(x, y, radio):
    arcade.draw_circle_filled(x, y, radio, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, radio / 2, arcade.color.BLACK)


def dibujar_murcielago(x, y, ancho):
    distancia_alas = ancho * 1.5
    altura = 50
    # detalles: se ponen antes para que no se vean contornos
    dibujar_ojos(x + ancho / 2.5, y + ancho + 0.5 * ancho, ancho / 4.5)  # ojo der
    dibujar_ojos(x - ancho / 2.5, y + ancho + 0.5 * ancho, ancho / 4.5)  # ojo izq
    arcade.draw_ellipse_outline(x, y, ancho, altura, arcade.color.DARK_BROWN, 5)  # contornos
    arcade.draw_triangle_outline(x, y, x + distancia_alas, y + altura / 2, x + distancia_alas / 2, y - altura / 2,
                                 arcade.color.DARK_BROWN, 5)
    arcade.draw_triangle_outline(x, y, x - distancia_alas, y + altura / 2, x - distancia_alas / 2, y - altura / 2,
                                 arcade.color.DARK_BROWN, 5)
    arcade.draw_circle_outline(x, y + ancho, ancho / 2.5, arcade.color.DARK_BROWN, 5)

    # Dibujo base
    arcade.draw_ellipse_filled(x, y, ancho, altura, arcade.color.WOOD_BROWN)
    arcade.draw_circle_filled(x, y + ancho, ancho / 2.5, arcade.color.WOOD_BROWN)
    arcade.draw_triangle_filled(x, y, x + distancia_alas, y + altura / 2, x + distancia_alas / 2, y - altura / 2,
                                arcade.color.WOOD_BROWN)
    arcade.draw_triangle_filled(x, y, x - distancia_alas, y + altura / 2, x - distancia_alas / 2, y - altura / 2,
                                arcade.color.WOOD_BROWN)


class Murcielago:
    def __init__(self, centro_x, centro_y, width, cambio_x, cambio_y):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.width = width
        self.cambio_x = cambio_x
        self.cambio_y = cambio_y
        # Cargamos sonidos
        self.choque = arcade.Sound("D:\\Audio stuff\\AudiosPrueba\\Choque.wav")

    def dibujar(self):
        dibujar_murcielago(self.centro_x, self.centro_y, self.width)

    def update(self):  # Mover murcielago
        self.centro_x += self.cambio_x
        self.centro_y += self.cambio_y
        # Poner limites para que no se salga de la ventana
        if self.centro_x < 2 * self.width:
            self.centro_x = 2 * self.width
            arcade.play_sound(self.choque)
        # lo de arriba se puede hacer tambien: self.choque.play(0.01) (asi podemos cambiar el volumen y bajrlo al 1%)
        elif self.centro_x > SCREEN_WIDTH - 2 * self.width:
            self.centro_x = SCREEN_WIDTH - 2 * self.width
            arcade.play_sound(self.choque)
        elif self.centro_y < 50:  # 50 = altura murcielago
            self.centro_y = 50
            arcade.play_sound(self.choque)
        elif self.centro_y > SCREEN_HEIGHT - 50:
            self.centro_y = SCREEN_HEIGHT - 50
            arcade.play_sound(self.choque)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)  # ocultamos el cursor
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        # Creamos un murcielago
        self.murcielago = Murcielago(100, 100, 25, 0, 0)

    def on_draw(self):
        arcade.start_render()
        dibujar_suelo_y_techo()
        dibujar_brillitos_fondo()
        self.murcielago.dibujar()

    def update(self, delta_time):
        self.murcielago.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.murcielago.cambio_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.murcielago.cambio_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.murcielago.cambio_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.murcielago.cambio_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.murcielago.cambio_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.murcielago.cambio_y = 0


# def on_mouse_motion(self, x, y, dx, dy):
#    """ Called to update our objects. Happens approximately 60 times per second."""
#    self.murcielago.centro_x = x
#    self.murcielago.centro_y = y


def main():
    window = MyGame()
    arcade.run()


main()
