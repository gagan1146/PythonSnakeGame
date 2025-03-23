from snake import Snake
from food import Food
from scoreboard import Scoreboard
from display import MyScreen
from bord import BordGame
import time

# Declare variable and CONSTANT
game_on = True
DISTANCE_TO_DIE = 35

# call class and initialize "MyScreen", "BordGame", "Snake", "Food", Scoreboard
new_screen = MyScreen()
new_bord = BordGame()
little_snake = Snake()
new_food = Food()
new_scoreboard = Scoreboard()

# Create bord
new_bord.create_bord()

# call method "listen_snake"
new_screen.listen_snake(little_snake)

# Cycle "while" condition to exit game_on equal to false
while game_on:
    new_screen.this_window.update()
    time.sleep(new_scoreboard.level_speed)
    little_snake.move_snake()

    # snake collision food
    # "if" to check distance between food and head of snake
    if little_snake.head.distance(new_food) < 15:
        new_food.random_food()
        little_snake.tail()
        new_scoreboard.increase_score()
        new_scoreboard.increase_level()

        new_scoreboard.refresh_score()

    # snake collision wall
    # "if" to check distance between wall and head of snake
    if little_snake.head.xcor() > new_screen.x_coord-DISTANCE_TO_DIE\
            or little_snake.head.xcor() < -new_screen.x_coord+DISTANCE_TO_DIE\
            or little_snake.head.ycor() > new_screen.y_coord-DISTANCE_TO_DIE\
            or little_snake.head.ycor() < -new_screen.y_coord+DISTANCE_TO_DIE:
        # game_on = False
        # new_scoreboard.game_over()
        new_scoreboard.update_high_score()
        new_scoreboard.refresh_score()
        little_snake.reset_snake()

    # snake collision tail
    for piece_of_tail in little_snake.list_of_piece:
        if piece_of_tail == little_snake.head:
            pass
        # "if" to check distance between head and piece of tail
        elif little_snake.head.distance(piece_of_tail) < 15:
            new_scoreboard.update_high_score()
            new_scoreboard.refresh_score()
            little_snake.reset_snake()
            # game_on = False
            # new_scoreboard.game_over()

new_screen.this_window.exitonclick()
