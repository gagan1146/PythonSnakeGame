from display import MyScreen
from turtle import Turtle

# Declare variable and CONSTANT
LEVEL_SCORE = 3
DISTANCE_FOR_SCORE = 60
GAME_OVER_IMAGE = "./image/snake.png"
FONT = ("Courier", 15, "bold")
ALIGN = "center"
file_score = "snake_game\score_file.txt"


# Class Scoreboard
class Scoreboard(Turtle):
    """
    Class Scoreboard
    Instance:
    score, level, high_score, level_speed
    Method:
    increase_score, increase_level,
    update_high_score, refresh_score
    """
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

#    def game_over(self):
#        self.goto(0, 0)
#        MyScreen().this_window.bgpic(GAME_OVER_IMAGE)
#        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    # Method read high score from file
    def read_scoreboard_file(self):
        """# Method read high score from file"""
        with open(file_score, "r") as high_score_file:
            self.high_score = int(high_score_file.read())

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def increase_level(self):
        if self.score % LEVEL_SCORE == 0:
            self.level += 1
            self.level_speed *= 0.9

    # Method update high score and wtite to file
    def update_high_score(self):
        """# Method update high score and wtite to file"""
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
