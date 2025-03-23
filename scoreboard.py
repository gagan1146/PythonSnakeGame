from display import MyScreen
from turtle import Turtle

LEVEL_SCORE = 3
DISTANCE_FOR_SCORE = 60
GAME_OVER_IMAGE = "./image/snake.png"
FONT = ("Courier", 15, "bold")
ALIGN = "center"
file_score = "snake_game\PythonSnakeGame\score_file.txt"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.level_speed = 0.1
        self.color("#FFFFFF")
        self.penup()
        self.hideturtle()
        self.goto(0, MyScreen().y_coord - DISTANCE_FOR_SCORE)
        self.read_scoreboard_file()
        self.refresh_score()


    def read_scoreboard_file(self):
        with open(file_score, "r") as high_score_file:
            self.high_score = int(high_score_file.read())

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def increase_level(self):
        if self.score % LEVEL_SCORE == 0:
            self.level += 1
            self.level_speed *= 0.9

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file_score, "w") as high_score_file:
                high_score_file.write(str(self.score))
        self.score = 0
        self.level = 0
        self.level_speed = 0.1

    def refresh_score(self):
        self.clear()
        self.write(f"Level: {self.level} Score: {self.score}\n High Score: {self.high_score}", align=ALIGN, font=FONT)
