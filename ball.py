from turtle import Turtle
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.shapesize(.5)
        self.penup()
        self.D = 0
        self.direction()


    def direction(self):
        DIRECTION_1 = random.randint(45, 85)
        DIRECTION_2 = random.randint(93, 135)
        DIRECTIONS = (DIRECTION_1, DIRECTION_2)
        DIRECTION = random.choice(DIRECTIONS)
        self.D = DIRECTION
        self.seth(self.D)

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        print("down")
        self.D += 90
        self.seth(self.D)

    def bounce_wall_up(self):
        print("up")
        self.D += 90
        self.seth(self.D)

    def bounce_x(self):
        self.D += 90
        self.seth(self.D)

    def ball_reset(self):
        self.home()
        self.direction()
        self.seth(self.D)
        self.move()