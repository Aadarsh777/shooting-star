from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION1 = (20, 20)
STARTING_POSITION2 = (-20, 20)
STARTING_POSITION3 = (-20, -20)
STARTING_POSITION4 = (20, -20)


class PlayerArrow:
    def __init__(self):
        self.arrows1 = []
        self.arrows2 = []
        self.arrows3 = []
        self.arrows4 = []

    def create_arrows(self, angle):
        if angle == 45:
            new_arrow1 = Turtle(shape="arrow")
            new_arrow1.color("orange")
            new_arrow1.penup()
            new_arrow1.setheading(45)
            new_arrow1.goto(STARTING_POSITION1)
            self.arrows1.append(new_arrow1)
        elif angle == 135:
            new_arrow2 = Turtle(shape="arrow")
            new_arrow2.color("orange")
            new_arrow2.penup()
            new_arrow2.setheading(135)
            new_arrow2.goto(STARTING_POSITION2)
            self.arrows2.append(new_arrow2)
        elif angle == 225:
            new_arrow3 = Turtle(shape="arrow")
            new_arrow3.color("orange")
            new_arrow3.penup()
            new_arrow3.setheading(225)
            new_arrow3.goto(STARTING_POSITION3)
            self.arrows3.append(new_arrow3)
        elif angle == 315:
            new_arrow4 = Turtle(shape="arrow")
            new_arrow4.color("orange")
            new_arrow4.penup()
            new_arrow4.setheading(315)
            new_arrow4.goto(STARTING_POSITION4)
            self.arrows4.append(new_arrow4)

    def move_arrows1(self):
        for arrow in self.arrows1:
            arrow.forward(MOVE_DISTANCE)

    def move_arrows2(self):
        for arrow in self.arrows2:
            arrow.forward(MOVE_DISTANCE)

    def move_arrows3(self):
        for arrow in self.arrows3:
            arrow.forward(MOVE_DISTANCE)

    def move_arrows4(self):
        for arrow in self.arrows4:
            arrow.forward(MOVE_DISTANCE)
