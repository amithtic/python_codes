import turtle

def line_dimple(turtle_m, line_length):
    turtle_m.forward(line_length)
    turtle_m.left(interior_angle)
    turtle_m.forward(line_length)
    for _ in range(n - 1):
        turtle_m.right(exterior_angle)
        turtle_m.forward(line_length)
    turtle_m.left(interior_angle)
    turtle_m.forward(line_length)

# Inputs, len of lines, lines in protution, start cordinates
l = 100
n = 7
a = 0
b = 0

parts = n + 2
line_length_2 = l / 3
line_length_3 = line_length_2 / 3
interior_angle = (n - 1) * 180 / (n + 1)
exterior_angle = 180 - interior_angle

turtle_1 = turtle.Turtle()
turtle_1.color("blue")
turtle_1.goto(a, b)
turtle_2 = turtle.Turtle()
turtle_2.color("red")
turtle_2.goto(a, b)
turtle_3 = turtle.Turtle()
turtle_2.color("green")
turtle_3.goto(a, b)

for _ in range(n + 1):
    turtle_1.forward(l)
    turtle_1.right(exterior_angle)
    line_dimple(turtle_2, line_length_2)
    turtle_2.right(exterior_angle)
    
    line_dimple(turtle_3, line_length_3)
    turtle_3.left(interior_angle)
    for _ in range(n):
        line_dimple(turtle_3, line_length_3)
        turtle_3.right(exterior_angle)
    turtle_3.left(180)
    line_dimple(turtle_3, line_length_3)
    turtle_3.left(interior_angle)
    turtle_3.left(180)

turtle.done()
