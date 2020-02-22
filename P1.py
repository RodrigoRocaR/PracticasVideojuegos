import arcade
import random


def dibujar_brillitos_fondo():
    for i in range(11):
        coord_x = random.randint(0, 800)
        coord_y = random.randint(210, 500)  # fondo entre 100 y 550 pero para no chocar con otras cosas pongo -
        arcade.draw_circle_filled(coord_x, coord_y, 3, arcade.color.WHITE)


def dibujar_columnas_altas_fondo():
    x_coords = [10, 110, 450]
    for i in x_coords:
        arcade.draw_lrtb_rectangle_filled(i, i+50, 400, 100, arcade.color.COOL_BLACK)
        arcade.draw_circle_filled(i+25, 400, 25, arcade.color.COOL_BLACK)


def dibujar_columnas_bajas_fondo():
    x_coords = [60, 500]
    for i in x_coords:
        arcade.draw_lrtb_rectangle_filled(i, i + 25, 250, 100, arcade.color.COOL_BLACK)
        arcade.draw_circle_filled(i + 12.5, 250, 12.5, arcade.color.COOL_BLACK)


arcade.open_window(800, 600, "First draw")  # width, height
arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_BLUE_GRAY)  # suelo
arcade.draw_lrtb_rectangle_filled(0, 800, 600, 550, arcade.color.DARK_BLUE_GRAY)  # techo
# Irregularidades
arcade.draw_triangle_filled(0, 600, 100, 600, 0, 500, arcade.color.DARK_BLUE_GRAY)  # top izq
arcade.draw_triangle_filled(200, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)  # mid bot
arcade.draw_triangle_filled(400, 100, 300, 100, 300, 200, arcade.color.DARK_BLUE_GRAY)
arcade.draw_triangle_filled(650, 100, 800, 100, 800, 25, arcade.color.DARK_MIDNIGHT_BLUE)  # bot right
# Decoracion
arcade.draw_triangle_filled(525, 550, 575, 550, 550, 400, arcade.color.ICEBERG)  # tempano de hielo
arcade.draw_triangle_filled(525, 550, 535, 550, 550, 400, arcade.color.WHITE)
# Detalles
dibujar_brillitos_fondo()
dibujar_columnas_altas_fondo()
dibujar_columnas_bajas_fondo()

arcade.finish_render()
arcade.run()
