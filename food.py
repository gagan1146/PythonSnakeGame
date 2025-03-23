from display import MyScreen
from turtle import Turtle
from random import randint

# Declare variable and CONSTANT
FOOD_COLOR = "#FF0000"
SNAKE_SHAPE = "circle"
DISTANCE_FOOD = 40


# Class Food
class Food(Turtle):
    """Class Food
    Method:
    random_food
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SNAKE_SHAPE)
        self.shapesize(0.5, 0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.random_food()

    # method to create a random food
    def random_food(self):
        """Method to create a random food"""
        x = randint(-MyScreen().x_coord+DISTANCE_FOOD, MyScreen().x_coord-DISTANCE_FOOD)
        y = randint(-MyScreen().y_coord+DISTANCE_FOOD, MyScreen().y_coord-DISTANCE_FOOD)
        self.goto(x, y)
        # random color food
        # self.color(random_color())


# Function get random color R,G,B
def random_color():
    """function get random color R,G,B
    Return:
    my_color -> Tuples
    """
    r = randint(150, 255)
    g = randint(150, 255)
    b = randint(150, 255)
    my_color = (r, g, b)

    return my_color
