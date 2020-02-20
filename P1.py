import arcade

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

# Detalles
arcade.draw_rectangle_filled(535, 475, 125, 10, arcade.color.WHITE, 97.5)




arcade.finish_render()
arcade.run()
