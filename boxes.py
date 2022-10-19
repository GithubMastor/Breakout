from turtle import Turtle
COLORS = ["green", "blue","yellow","orange","red"]

class Boxes(Turtle):
    def __init__(self):
        self.all_boxes = []
        self.box_info = []
    def create_boxes(self):
        cnt = 8
        init_x,init_y,colnum = -345, 450,0 #-355, 500,0
        for rep in range(2):
            for color in range(5):
                for item in range(9):
                    self.box_info.append((init_x,init_y,COLORS[color]))
                    init_x += 85
                    cnt -= 1
                init_y -= 22
                init_x = -345
    def draw_boxes(self):
        for bx in self.box_info:
            new_box = Turtle("square")
            new_box.shapesize(stretch_wid=1, stretch_len=4)# square standard size is 21 x 21
            new_box.penup()
            new_box.color(bx[2])
            new_box.goto(bx[0], bx[1])
            self.all_boxes.append(new_box)

    def delete_box(self, boxnum):
        print(type(self.all_boxes))
        print(type(self.all_boxes[0]))
        (self.all_boxes[boxnum]).goto(1500,1500)
        print(self.all_boxes[0])
        # print(f'len b4: {len(self.box_info)}')
        # print(f'len after: {len(self.all_boxes)}')
        # del self.box_info[boxnum]
        # self.all_boxes = []
        # self.clear()
        # self.draw_boxes()
        # print(f'len after: {len(self.box_info)}')
        # print(f'len after: {len(self.all_boxes)}')




