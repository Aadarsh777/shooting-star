from turtle import Turtle

POSITIONS = [(270, 270), (-270, 270), (-270, -270), (270, -270)]


class EnemiesHealth:
    def __init__(self):
        self.healths = [100, 100, 100, 100]
        self.enemies_health = []
        self.create_health()

    def create_health(self):
        for i in range(4):
            new_health = Turtle()
            new_health.hideturtle()
            new_health.penup()
            new_health.color("orange")
            new_health.goto(POSITIONS[i])
            self.enemies_health.append(new_health)
            self.update_health(i)

    def update_health(self, i):
        self.enemies_health[i].clear()
        self.enemies_health[i].write(f"{self.healths[i]}%", align="center", font=("Carousel", 10, "normal"))

    def decrease_health(self, i):
        self.healths[i] -= 2
        self.update_health(i)
