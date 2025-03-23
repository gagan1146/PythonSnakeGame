from snake import Snake
from food import Food
from scoreboard import Scoreboard
from display import MyScreen
from bord import BordGame
import time

game_on = True
DISTANCE_TO_DIE = 35

new_screen = MyScreen()
new_bord = BordGame()
little_snake = Snake()
new_food = Food()
new_scoreboard = Scoreboard()

new_bord.create_bord()

new_screen.listen_snake(little_snake)

while game_on:
    new_screen.this_window.update()
    time.sleep(new_scoreboard.level_speed)
    little_snake.move_snake()

    if little_snake.head.distance(new_food) < 15:
        new_food.random_food()
        little_snake.tail()
        new_scoreboard.increase_score()
        new_scoreboard.increase_level()

        new_scoreboard.refresh_score()

    if little_snake.head.xcor() > new_screen.x_coord-DISTANCE_TO_DIE\
            or little_snake.head.xcor() < -new_screen.x_coord+DISTANCE_TO_DIE\
            or little_snake.head.ycor() > new_screen.y_coord-DISTANCE_TO_DIE\
            or little_snake.head.ycor() < -new_screen.y_coord+DISTANCE_TO_DIE:
        new_scoreboard.update_high_score()
        new_scoreboard.refresh_score()
        little_snake.reset_snake()

    for piece_of_tail in little_snake.list_of_piece:
        if piece_of_tail == little_snake.head:
            pass
        elif little_snake.head.distance(piece_of_tail) < 15:
            new_scoreboard.update_high_score()
            new_scoreboard.refresh_score()
            little_snake.reset_snake()

new_screen.this_window.exitonclick()
