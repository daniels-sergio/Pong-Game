import turtle
from turtle import Screen,Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        self.CanMove = True
    def go_up(self):
        if self.CanMove:
            new_ycor =  self.ycor() + 30
            self.goto(x=self.xcor(),y= new_ycor)
    def go_down(self):
        if self.CanMove:
            new_ycor  = self.ycor() - 30
            self.goto(x=self.xcor(),y=new_ycor)









        
  
        
