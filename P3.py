import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def dibujar_brillitos_fondo():
    coord_x = [100, 125, 300, 350, 200, 250, 325, 600, 675, 750]
    coord_y = [210, 250, 475, 500, 400, 350, 300, 430, 510, 465]
    for i in range(len(coord_x)):
        arcade.draw_circle_filled(coord_x[i], coord_y[i], 3, arcade.color.WHITE)


def dibujar_columnas_altas_fondo():
    x_coords = [10, 110, 450]
    for i in x_coords:
        arcade.draw_lrtb_rectangle_filled(i, i + 50, 400, 100, arcade.color.COOL_BLACK)
        arcade.draw_circle_filled(i + 25, 400, 25, arcade.color.COOL_BLACK)


def dibujar_columnas_bajas_fondo():
    x_coords = [60, 500]
    for i in x_coords:
        arcade.draw_lrtb_rectangle_filled(i, i + 25, 250, 100, arcade.color.COOL_BLACK)
        arcade.draw_circle_filled(i + 12.5, 250, 12.5, arcade.color.COOL_BLACK)


def dibujar_tempanos_de_hielo(y):
    if y > -300:  # choca contra el suelo (de 550 a 100)
        arcade.draw_triangle_filled(525, 550 + y, 575, 550 + y, 550, 400 + y, arcade.color.ICEBERG)  # tempano de hielo
        arcade.draw_triangle_filled(525, 550 + y, 535, 550 + y, 550, 400 + y, arcade.color.WHITE)
    else:
        arcade.draw_triangle_filled(525, 100, 525, 150, 675, 125, arcade.color.ICEBERG)
        arcade.draw_triangle_filled(525, 100, 525, 115, 675, 125, arcade.color.WHITE)

    # arcade.draw_triangle_filled(300, 550, 350, 550, 325, 400, arcade.color.ICEBERG)  # tempano de hielo 2
    # arcade.draw_triangle_filled(300, 550, 310, 550, 325, 400, arcade.color.WHITE)


def dibujar_suelo_y_techo():
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_BLUE_GRAY)  # suelo
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 550, arcade.color.DARK_BLUE_GRAY)  # techo
    # Irregularidades
    arcade.draw_triangle_filled(0, 600, 100, 600, 0, 500, arcade.color.DARK_BLUE_GRAY)  # top izq
    arcade.draw_triangle_filled(200, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)  # mid bot
    arcade.draw_triangle_filled(400, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)
    arcade.draw_triangle_filled(650, 100, 800, 100, 800, 25, arcade.color.DARK_MIDNIGHT_BLUE)  # bot right


def on_draw(delta_time):
    """dibujamos all"""
    global caida_tempano_hielo
    arcade.start_render()
    dibujar_suelo_y_techo()
    dibujar_brillitos_fondo()
    dibujar_tempanos_de_hielo(caida_tempano_hielo)
    dibujar_columnas_altas_fondo()
    dibujar_columnas_bajas_fondo()
    caida_tempano_hielo -= 5


caida_tempano_hielo = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Second draw")
    arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


main()
