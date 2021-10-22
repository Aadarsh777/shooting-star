from turtle import Turtle


class LevelScore(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.goto(0, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}%", align="center", font=("Carousel", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Siiiuuu", align="center", font=("Carousel", 20, "bold"))
