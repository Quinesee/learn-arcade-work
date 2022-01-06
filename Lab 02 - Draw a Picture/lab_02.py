""" 
Lab 2
Drawing a picture
"""

import arcade

# Open window
arcade.open_window(600, 600, "Lab 2 - Drawing a Picture")

# Background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()


# Draw table
arcade.draw_rectangle_filled(300, 50, 600, 100, arcade.color.BLUSH)
arcade.draw_rectangle_filled(300, 100, 600, 75, arcade.color.BRANDEIS_BLUE)

# Draw Vase
arcade.draw_arc_filled(420, 115, 100, 40, arcade.color.BOTTLE_GREEN, 0, 180)
arcade.draw_ellipse_filled(420, 210, 80, 180, arcade.color.BOTTLE_GREEN)
arcade.draw_arc_filled(
    420, 300, 60, 20, arcade.color.BOTTLE_GREEN, 0, 180, 180)


# Finish the rendering process. This must be done after the drawing commands
arcade.finish_render()

# Keep window open
arcade.run()
