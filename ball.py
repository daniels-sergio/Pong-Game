import turtle
from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto((0,0))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)



    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1 # so that the ball speed doesnt increase indefinitetly
        self.bounce_x()
    def bounce_y(self):
        self.y_move *= -1

    def faster(self):
        self.x_move += 2
        self.y_move += 2







