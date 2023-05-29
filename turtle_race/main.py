import random
import turtle
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "purple", "blue"]

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Pick a color: ")
y_pos = [-70, -40, -10, 20, 50, 80]
print(bet)
turtles = []

for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.setpos(x=-230, y=y_pos[turtle_index])
	new_turtle.pendown()
	turtles.append(new_turtle)

if bet:
	is_race_on = True

while is_race_on:
	for turtle in turtles:
		if turtle.xcor() > 230:	
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == bet:
				print(f"You've won! The {winning_color} turtle won the race. ")
			else: 
				print(f"You've lost. The {winning_color} turtle won, not the {bet} turtle. ")

		random_distance = random.randint(0,10)
		turtle.forward(random_distance)


screen.exitonclick()