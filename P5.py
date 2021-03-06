import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    for row in range(30):
        for column in range(30):
            x = column * 10 + 300
            y = row * 10
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        for column in range(30):
            x = column * 10 + 600
            y = row * 10
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 900
            y = row * 10
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.BLACK)


def draw_section_5():
    num_columnas = 0
    for row in range(30):
        for column in range(num_columnas):
            x = row * 10
            y = column * 10 + 300
            arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)
        num_columnas += 1


def draw_section_6():
    num_columnas = 30
    for row in range(30):
        for column in range(num_columnas):
            x = column * 10 + 300
            y = row * 10 + 300
            arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)
        num_columnas -= 1


def draw_section_7():
    num_columnas = 0
    for row in range(30):
        for column in range(num_columnas):
            x = column * 10 + 600
            y = row * 10 + 300
            arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.color.WHITE)
        num_columnas += 1


def draw_section_8():
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
