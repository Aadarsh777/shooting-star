from turtle import Turtle


class PlayerHealth(Turtle):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(0, -70)
        self.update_health()

    def update_health(self):
        self.clear()
        self.write(f"{self.health}%", align="center", font=("Carousel", 10, "normal"))

    def decrease_health(self):
        self.health -= 5
        self.update_health()
