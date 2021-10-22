from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.goto(0, 0)
        self.shapesize(stretch_wid=3, stretch_len=2)

    def move_right(self):
        self.right(22.5)

    def move_left(self):
        self.left(22.5)

    def game_over(self):
        self.hideturtle()
        self.write("Game Over! Well Tried!", align="center", font=("Carousel", 20, "bold"))
