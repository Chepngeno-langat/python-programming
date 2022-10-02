import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
#timmy.color("green")

#def draw_shape(num_sides):
    #angle = 360 / num_sides
    #for i in range(num_sides):
        #timmy.forward(100)
        #timmy.left(angle)

#for i in range(3, 11):
    #timmy.color(random.choice(colors))
    #draw_shape(i)
timmy.width(2)
timmy.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#for i in range(80):
    #timmy.color(random_color())
    #timmy.forward(random.randint(0, 30))
    #timmy.left(random.randint(0, 4) * 90)
for i in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(10)

screen = t.Screen()
screen.exitonclick()