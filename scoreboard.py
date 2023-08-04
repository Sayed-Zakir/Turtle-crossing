from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !", align="center", font=FONT)

    def next_level(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
