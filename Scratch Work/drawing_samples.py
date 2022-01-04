""" 
This is a sample program.

Multi-line comments are surrounded by three double quotes.
"""

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Drawing code here

# Draw rectangle by spedifing (l)eft, (r)ight, (t)op, (b)ottom
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Draw rectangle from center 100, 320
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with an ellipse top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Anthoer tree, with a trunk and arc for the top
# Arc is centered at (300, 340) with a width of 60 and height of 100
# Starting angle is 0, and ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree with a trunk and a triangle
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Drawn with polygon
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)),
                           arcade.csscolor.DARK_GREEN)

# Draw sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Sun rays
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.csscolor.YELLOW, 3)

arcade.draw_line(500, 550, 550, 600, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.csscolor.YELLOW, 3)

# Text
arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()
