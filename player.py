from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        new_x=self.xcor()
        new_y=self.ycor() + 10
        self.goto(new_x,new_y)

    def move_down(self):
        new_x=self.xcor()
        new_y=self.ycor() - 10
        self.goto(new_x,new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

