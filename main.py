import turtle
from turtle import Screen,Turtle
import time
from paddles import *
from ball import *
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collsion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()




    #detect collision with paddles

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect when ball misses paddle

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()



    elif ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()
