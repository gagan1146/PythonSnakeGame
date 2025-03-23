from turtle import Turtle
from display import MyScreen
# For snake random position uncomment
# from screen import MyScreen
# from random import randint

# Declare variable and CONSTANT
RIGHT = 0
LEFT = 180
TOP = 90
DOWN = 270
STEP_TO_MOVE = 20
SNAKE_SPEED = "normal"
SNAKE_HEAD_COLOR = "#ffffff"
SNAKE_TAIL_COLOR = "#CCCCCC"
snake_shape = "square"

starting_position = [(0, 0), (-20, 0)]

# For snake random position uncomment
# x = randint(-MyScreen().x_coord, MyScreen().x_coord)
# y = randint(-MyScreen().y_coord, MyScreen().y_coord)
# starting_position = [(x, y), (x-20, y)]


# Class Snake
class Snake:
    """Class Snake
    # Instance
    list_of_piece, head
    Method:
    create_snake, tail, add_tail, reset_snake, move_snake
    snake_right, snake_left, snake_up, snake_down
    """
    def __init__(self):
        self.list_of_piece = []
        self.create_snake()
        self.head = self.list_of_piece[0]

    # Method to create snake
    def create_snake(self):
        """Method to create snake"""
        for position in starting_position:
            self.add_tail(position)

    def tail(self):
        self.add_tail(self.list_of_piece[-1].position())

    # Method to add piece of tail
    def add_tail(self, position):
        """
        Method to add piece of tail
        position -> Tuples
        """
        snake = Turtle()
        snake.penup()
        snake.shape(snake_shape)
        if position != (0, 0):
            snake.color(SNAKE_TAIL_COLOR)
        else:
            snake.color(SNAKE_HEAD_COLOR)
        snake.speed(SNAKE_SPEED)
        snake.goto(position)
        self.list_of_piece.append(snake)

    def reset_snake(self):
        for piece in self.list_of_piece:
            piece.goto(MyScreen().x_coord + 10000, MyScreen().y_coord + 10000)
        self.list_of_piece.clear()
        self.create_snake()
        self.head = self.list_of_piece[0]

    # method to move snake
    def move_snake(self):
        """Method to move snake"""
        # Cycle "for" to read all piece of tail and position in snake
        for piece in range(len(self.list_of_piece) - 1, 0, -1):
            x_pos = self.list_of_piece[piece - 1].xcor()
            y_pos = self.list_of_piece[piece - 1].ycor()
            self.list_of_piece[piece].goto(x_pos, y_pos)
        self.head.forward(STEP_TO_MOVE)

    def snake_right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def snake_up(self):
        if self.head.setheading != DOWN:
            self.head.setheading(TOP)

    def snake_down(self):
        if self.head.setheading != TOP:
            self.head.setheading(DOWN)
