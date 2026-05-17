# import colorgram
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

import turtle as turtle_module
turtle_module.colormode(255)
color_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203),
              (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70),
              (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31)]

tutle = turtle_module.Turtle()
tutle.speed(0)
tutle.penup()
tutle.setheading(230)
tutle.forward(300)
tutle.setheading(0)
tutle.hideturtle()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tutle.dot(20, random.choice(color_list))
    tutle.forward(40)

    if dot_count % 10 == 0:
        tutle.setheading(90)
        tutle.forward(40)
        tutle.setheading(180)
        tutle.forward(400)
        tutle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()