from turtle import *
from paddle import Paddle
from boxes import Boxes
from scoreboard import Scoreboard
from ball import Ball
import time

########## SCREEN ##########
screen = Screen()
screen.bgcolor("black")
screen.setup(width=770, height=1000)
screen.title("BREAKOUT")
screen.tracer(0)

########## PADDLE ##########
paddle = Paddle((0, -450))
########## BOXES ##########
box = Boxes()
box.create_boxes()
########## SCORE ##########
score = Scoreboard()

ball = Ball()



game_is_on = True
while game_is_on:
    screen.update()
########## PADDLE ##########

# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()