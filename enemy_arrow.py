from turtle import Turtle
from enemies_health import EnemiesHealth
import random

STARTING_POSITIONS1 = [(180, 180), (200, 200), (220, 220)]
STARTING_POSITIONS2 = [(-180, 180), (-200, 200), (-220, 220)]
STARTING_POSITIONS3 = [(-180, -180), (-200, -200), (-220, -220)]
STARTING_POSITIONS4 = [(180, -180), (200, -200), (220, -220)]


class EnemyArrow:
    def __init__(self, enemy_healths: EnemiesHealth):
        self.enemy_health = enemy_healths
        self.arrows1 = []
        self.arrows2 = []
        self.arrows3 = []
        self.arrows4 = []
        self.random_list = [0, 1, 2, 3]
        self.random_value = 0
        self.MOVE_DISTANCE = 5

    def create_enemy_arrows(self):
        if self.enemy_health.healths[0] == 0.14:
            self.random_list.remove(0)
            self.enemy_health.healths[0] = 0.21
        elif self.enemy_health.healths[1] == 0.14:
            self.random_list.remove(1)
            self.enemy_health.healths[1] = 0.21
        elif self.enemy_health.healths[2] == 0.14:
            self.random_list.remove(2)
            self.enemy_health.healths[2] = 0.21
        elif self.enemy_health.healths[3] == 0.14:
            self.random_list.remove(3)
            self.enemy_health.healths[3] = 0.21
        self.random_value = random.choice(self.random_list)
        if self.random_value == 0:
            for position in STARTING_POSITIONS1:
                new_arrow1 = Turtle(shape="arrow")
                new_arrow1.color("red")
                new_arrow1.penup()
                new_arrow1.setheading(225)
                new_arrow1.goto(position)
                self.arrows1.append(new_arrow1)
        elif self.random_value == 1:
            for position in STARTING_POSITIONS2:
                new_arrow2 = Turtle(shape="arrow")
                new_arrow2.color("red")
                new_arrow2.penup()
                new_arrow2.setheading(315)
                new_arrow2.goto(position)
                self.arrows2.append(new_arrow2)
        elif self.random_value == 2:
            for position in STARTING_POSITIONS3:
                new_arrow3 = Turtle(shape="arrow")
                new_arrow3.color("red")
                new_arrow3.penup()
                new_arrow3.setheading(45)
                new_arrow3.goto(position)
                self.arrows3.append(new_arrow3)
        elif self.random_value == 3:
            for position in STARTING_POSITIONS4:
                new_arrow4 = Turtle(shape="arrow")
                new_arrow4.color("red")
                new_arrow4.penup()
                new_arrow4.setheading(135)
                new_arrow4.goto(position)
                self.arrows4.append(new_arrow4)

    def move_arrows1(self):
        for arrow in self.arrows1:
            arrow.forward(self.MOVE_DISTANCE)

    def move_arrows2(self):
        for arrow in self.arrows2:
            arrow.forward(self.MOVE_DISTANCE)

    def move_arrows3(self):
        for arrow in self.arrows3:
            arrow.forward(self.MOVE_DISTANCE)

    def move_arrows4(self):
        for arrow in self.arrows4:
            arrow.forward(self.MOVE_DISTANCE)

    def level_up(self):
        self.MOVE_DISTANCE += 5
