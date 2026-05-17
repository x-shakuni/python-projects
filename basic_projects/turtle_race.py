from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
y_positions = [-70,-40,-10,20,50,80]
colors = ["red","green","blue","yellow","orange","purple"]
all_turtles = []
# hulk = Turtle("turtle")
# hulk.penup()
# hulk.goto(x=-220,y=-100)
# hulk.color("green")
#
# ironman = Turtle("turtle")
# ironman.penup()
# ironman.goto(x=-220,y=-50)
# ironman.color("red")
#
# spiderman = Turtle("turtle")
# spiderman.penup()
# spiderman.goto(x=-220,y=0)
# ironman.color("gold")
#
# hawkeye = Turtle("turtle")
# hawkeye.penup()
# hawkeye.goto(x=-220,y=50)
# hawkeye.color("blue")
#
# thanos = Turtle("turtle")
# thanos.penup()
# thanos.goto(x=-220,y=100)
# thanos.color("purple")

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -220, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} has won!")
            else:
                print(f"You've Lost! The {winning_color} has won!")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# screen.update()
screen.exitonclick()