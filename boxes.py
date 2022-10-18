from turtle import Turtle
COLORS = ["green", "blue","yellow","orange","red"]

class Boxes(Turtle):
    def __init__(self):
        self.all_boxes = []
    def create_boxes(self):
        cnt = 8
        init_x,init_y,colnum = -345, 450,0 #-355, 500,0
        for rep in range(2):
            for row in range(5):
                for item in range(9):
                    new_box = Turtle("square")
                    new_box.shapesize(stretch_wid=1, stretch_len=4)
                    #square natural size is 21px x 21px: 4*21 = 84 : 2*21 = 42
                    new_box.penup()
                    new_box.color(COLORS[row])
                    new_box.goto(init_x, init_y)
                    self.all_boxes.append(new_box)
                    init_x += 85
                    cnt -= 1
                init_y -= 22
                init_x = -345
