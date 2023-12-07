import turtle
import random

class Polygon:
    # reduction_ratio = 0.618
    def __init__(self,num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move_polygon(self, reduction_ratio):
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

        # adjust the size according to the reduction ratio
        self.size *= reduction_ratio

        # draw the second polygon embedded inside the original
        self.draw_polygon()


reduction_ratio = 0.618

art = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
if art == 1:
    for i in range(20):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
    turtle.done()

elif art == 2:
    for i in range(20):
        num_sides = 4
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
    turtle.done()

elif art == 3:
    for i in range(20):
        num_sides = 5
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
    turtle.done()

elif art == 4:
    for i in range(20):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
    turtle.done()

elif art == 5:
    for i in range(20):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
        polygon.move_polygon(reduction_ratio)
        polygon.move_polygon(reduction_ratio)
    turtle.done()

elif art == 6:
    for i in range(20):
        num_sides = 4
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
        polygon.move_polygon(reduction_ratio)
        polygon.move_polygon(reduction_ratio)
    turtle.done()

elif art == 7:
    for i in range(20):
        num_sides = 5
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
        polygon.move_polygon(reduction_ratio)
        polygon.move_polygon(reduction_ratio)
    turtle.done()

elif art == 8:
    for i in range(20):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        polygon = Polygon(num_sides, size, orientation, location, color, border_size)
        polygon.draw_polygon()
        polygon.move_polygon(reduction_ratio)
        polygon.move_polygon(reduction_ratio)
    turtle.done()