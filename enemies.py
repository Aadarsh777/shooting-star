from turtle import Turtle
POSITIONS = [(240, 240), (-240, 240), (-240, -240), (240, -240)]


class Enemies:
    def __init__(self):
        self.enemies = []
        self.create_enemies()

    def create_enemies(self):
        for position in POSITIONS:
            new_enemy = Turtle()
            new_enemy.shape("circle")
            new_enemy.shapesize(stretch_wid=2, stretch_len=2)
            new_enemy.color("gray")
            new_enemy.penup()
            new_enemy.goto(position)
            self.enemies.append(new_enemy)
