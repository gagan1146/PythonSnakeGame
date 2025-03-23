from display import MyScreen
from turtle import Turtle
from random import randint

FOOD_COLOR = "#FF0000"
SNAKE_SHAPE = "circle"
DISTANCE_FOOD = 40


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SNAKE_SHAPE)
        self.shapesize(0.5, 0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.random_food()

    def random_food(self):
        x = randint(-MyScreen().x_coord+DISTANCE_FOOD, MyScreen().x_coord-DISTANCE_FOOD)
        y = randint(-MyScreen().y_coord+DISTANCE_FOOD, MyScreen().y_coord-DISTANCE_FOOD)
        self.goto(x, y)


def random_color():
    
    r = randint(150, 255)
    g = randint(150, 255)
    b = randint(150, 255)
    my_color = (r, g, b)

    return my_color
