import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 40

MAX_COINS = 30


class MiniBarco(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Walls")
        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.floor_list = None
        self.coin_list = None
        # Set up the player
        self.player_sprite = None
        # This variable holds our simple "physics engine"
        self.physics_engine = None
        # Set up puntuacion
        self.score = 0
        # Manage the view port
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        arcade.set_background_color(arcade.color.WOOD_BROWN)
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        # The score
        self.score = 0
        # View port stuff setup
        self.view_left = 0
        self.view_bottom = 0
        # Create the player
        self.player_sprite = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                           "\\Sprites prestados prueba\\heroe.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)
        # Madera suelos
        # Suelo base
        for x in range(0, SCREEN_WIDTH * 3, 50):  # x30, la madera.png tiene 50 pixeles de ancho
            madera_s = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                     "\\Sprites prestados prueba\\madera.png")
            madera_s.left = x
            madera_s.bottom = 0
            self.wall_list.append(madera_s)
        # Plataformas
        for x in range(0, SCREEN_WIDTH * 3, 50):
            p1 = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                               "\\Sprites prestados prueba\\metal.png")
            p2 = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                               "\\Sprites prestados prueba\\metal.png")
            if 250 <= x <= 1000:
                p1.left = x
                p1.bottom = 250
                self.wall_list.append(p1)
            if 800 <= x <= 1500 or 2000 <= x <= SCREEN_WIDTH * 3:
                p2.left = x
                p2.bottom = 400
                self.wall_list.append(p2)
        # Madera techo
        for x in range(0, SCREEN_WIDTH * 3, 50):  # x30, la madera.png tiene 50 pixeles de ancho
            madera_t = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                     "\\Sprites prestados prueba\\madera.png")
            madera_t.left = x
            madera_t.bottom = SCREEN_HEIGHT - 50
            self.wall_list.append(madera_t)
        # Madera paredes izq
        for y in range(50, SCREEN_HEIGHT, 50):  # cada uno 50 pixeles
            madera_pl = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                      "\\Sprites prestados prueba\\maderaPared.png")
            madera_pl.left = 0
            madera_pl.bottom = y
            self.wall_list.append(madera_pl)
        # Madera paredes derecha
        for y in range(0, SCREEN_HEIGHT, 50):  # cada uno 50 pixeles
            madera_pr = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                      "\\Sprites prestados prueba\\maderaPared.png")
            madera_pr.left = SCREEN_WIDTH * 3
            madera_pr.bottom = y
            self.wall_list.append(madera_pr)
        # Poner monedas
        for i in range(MAX_COINS):
            moneda = arcade.Sprite("C:\\Users\\Rotrex\\Desktop\\Apuntes y Trabajos\\Cuatri 2\\Videojuegos"
                                   "\\Sprites prestados prueba\\moneda.png", SPRITE_SCALING_COIN)
            # PONER MONEDAS BIEN
            moneda_bien_puesta = False
            while not moneda_bien_puesta:
                moneda.center_x = random.randrange(SCREEN_WIDTH * 3)
                moneda.center_y = random.randrange(SCREEN_HEIGHT)
                # Ver si la moneda choca con una pared:
                pared_hit_list = arcade.check_for_collision_with_list(moneda, self.wall_list)
                # Ver si la moneda choca con otra moneda
                moneda_hit_list = arcade.check_for_collision_with_list(moneda, self.coin_list)
                if len(pared_hit_list) == 0 and len(moneda_hit_list) == 0:
                    moneda_bien_puesta = True
            self.coin_list.append(moneda)
        # Fisicas
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.floor_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        texto_pantalla = "Puntuación: " + str(self.score)
        arcade.draw_text(texto_pantalla, self.view_left + 10, self.view_bottom + 20, arcade.color.BLACK, 14)
        if self.score == 30:
            texto_pantalla2 = "HAS GANADO AHORA VETE A LA CAMA A DORMIR"
            arcade.draw_text(texto_pantalla2, self.view_left + SCREEN_WIDTH / 3, self.view_bottom + SCREEN_HEIGHT / 2,
                             arcade.color.BLACK, 20)

    def update(self, delta_time):
        if self.score <= 30:
            # Update each of the sprites
            self.physics_engine.update()

        lista_colisiones_monedas = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # Cada vez que chocamos con una moneda:
        for moneda in lista_colisiones_monedas:
            moneda.remove_from_sprite_lists()
            self.score += 1

        # ---Scrolling---
        changed = False
        # Izq
        limite_izq = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < limite_izq:
            self.view_left -= limite_izq - self.player_sprite.left
            changed = True
        # Dcha
        limite_dcha = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > limite_dcha:
            self.view_left += self.player_sprite.right - limite_dcha
            changed = True
        # Up
        limite_top = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > limite_top:
            self.view_bottom += self.player_sprite.top - limite_top
            changed = True
        # Down
        limite_bot = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < limite_bot:
            self.view_bottom -= limite_bot - self.player_sprite.bottom
            changed = True
        # Para evitar errores de redondeo
        self.view_bottom = int(self.view_bottom)
        self.view_left = int(self.view_left)
        # Si lo hemos cambiado actualizamos el view port
        if changed:
            arcade.set_viewport(self.view_left, self.view_left + SCREEN_WIDTH - 1, self.view_bottom,
                                self.view_bottom + SCREEN_HEIGHT - 1)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MiniBarco()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
