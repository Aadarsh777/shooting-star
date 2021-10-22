import time
from player_arrow import PlayerArrow
from enemy_arrow import EnemyArrow
from turtle import Screen
from player import Player
from enemies import Enemies
from player_health import PlayerHealth
from enemies_health import EnemiesHealth
from level_score import LevelScore

screen = Screen()
screen.title("Shooting Star 😉")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
is_game_on = True
count = 1

player = Player()
enemies = Enemies()

player_health = PlayerHealth()
enemy_healths = EnemiesHealth()

player_arrow = PlayerArrow()
enemy_arrow = EnemyArrow(enemy_healths)

level = LevelScore()

screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    if count % 12 == 0:
        enemy_arrow.create_enemy_arrows()
    if player.heading() == 45:
        player_arrow.create_arrows(45)
    if player.heading() == 135:
        player_arrow.create_arrows(135)
    if player.heading() == 225:
        player_arrow.create_arrows(225)
    if player.heading() == 315:
        player_arrow.create_arrows(315)
    if len(player_arrow.arrows1) > 0:
        player_arrow.move_arrows1()
    if len(player_arrow.arrows2) > 0:
        player_arrow.move_arrows2()
    if len(player_arrow.arrows3) > 0:
        player_arrow.move_arrows3()
    if len(player_arrow.arrows4) > 0:
        player_arrow.move_arrows4()
    if len(enemy_arrow.arrows1) > 0:
        enemy_arrow.move_arrows1()
    if len(enemy_arrow.arrows2) > 0:
        enemy_arrow.move_arrows2()
    if len(enemy_arrow.arrows3) > 0:
        enemy_arrow.move_arrows3()
    if len(enemy_arrow.arrows4) > 0:
        enemy_arrow.move_arrows4()

    if enemy_healths.healths[0] > 0.7:
        for arrow in player_arrow.arrows1:
            for arrows in enemy_arrow.arrows1:
                if arrow.distance(arrows) < 7:
                    player_arrow.arrows1.remove(arrow)
                    arrow.goto(1000, 1000)
                    enemy_arrow.arrows1.remove(arrows)
                    arrows.goto(1000, 1000)

    if enemy_healths.healths[1] > 0.7:
        for arrow in player_arrow.arrows2:
            for arrows in enemy_arrow.arrows2:
                if arrow.distance(arrows) < 7:
                    player_arrow.arrows2.remove(arrow)
                    arrow.goto(1000, 1000)
                    enemy_arrow.arrows2.remove(arrows)
                    arrows.goto(1000, 1000)

    if enemy_healths.healths[2] > 0.7:
        for arrow in player_arrow.arrows3:
            for arrows in enemy_arrow.arrows3:
                if arrow.distance(arrows) < 7:
                    player_arrow.arrows3.remove(arrow)
                    arrow.goto(1000, 1000)
                    enemy_arrow.arrows3.remove(arrows)
                    arrows.goto(1000, 1000)

    if enemy_healths.healths[3] > 0.7:
        for arrow in player_arrow.arrows4:
            for arrows in enemy_arrow.arrows4:
                if arrow.distance(arrows) < 7:
                    player_arrow.arrows4.remove(arrow)
                    arrow.goto(1000, 1000)
                    enemy_arrow.arrows4.remove(arrows)
                    arrows.goto(1000, 1000)

    if enemy_healths.healths[0] > 0.7:
        for arrow in enemy_arrow.arrows1:
            if arrow.distance(player) < 20:
                player_health.decrease_health()
                enemy_arrow.arrows1.remove(arrow)
                arrow.goto(1000, 1000)

    if enemy_healths.healths[1] > 0.7:
        for arrow in enemy_arrow.arrows2:
            if arrow.distance(player) < 20:
                player_health.decrease_health()
                enemy_arrow.arrows2.remove(arrow)
                arrow.goto(1000, 1000)

    if enemy_healths.healths[2] > 0.7:
        for arrow in enemy_arrow.arrows3:
            if arrow.distance(player) < 20:
                player_health.decrease_health()
                enemy_arrow.arrows3.remove(arrow)
                arrow.goto(1000, 1000)

    if enemy_healths.healths[3] > 0.7:
        for arrow in enemy_arrow.arrows4:
            if arrow.distance(player) < 20:
                player_health.decrease_health()
                enemy_arrow.arrows4.remove(arrow)
                arrow.goto(1000, 1000)

    if player_health.health == 0:
        is_game_on = False
        player.game_over()

    if enemy_healths.healths[0] > 0.7:
        for arrow in player_arrow.arrows1:
            if arrow.distance(enemies.enemies[0]) < 20:
                enemy_healths.decrease_health(0)
                player_arrow.arrows1.remove(arrow)
                arrow.goto(2000, 2000)

    if enemy_healths.healths[1] > 0.7:
        for arrow in player_arrow.arrows2:
            if arrow.distance(enemies.enemies[1]) < 20:
                enemy_healths.decrease_health(1)
                player_arrow.arrows2.remove(arrow)
                arrow.goto(2000, 2000)

    if enemy_healths.healths[2] > 0.7:
        for arrow in player_arrow.arrows3:
            if arrow.distance(enemies.enemies[2]) < 20:
                enemy_healths.decrease_health(2)
                player_arrow.arrows3.remove(arrow)
                arrow.goto(2000, 2000)

    if enemy_healths.healths[3] > 0.7:
        for arrow in player_arrow.arrows4:
            if arrow.distance(enemies.enemies[3]) < 20:
                enemy_healths.decrease_health(3)
                player_arrow.arrows4.remove(arrow)
                arrow.goto(2000, 2000)

    if enemy_healths.healths[0] == 0:
        enemies.enemies[0].goto(3000, 3000)
        enemy_arrow.level_up()
        level.increase_level()
        enemy_healths.healths[0] = 0.14
        enemy_healths.enemies_health[0].clear()

    if enemy_healths.healths[1] == 0:
        enemies.enemies[1].goto(3000, 3000)
        enemy_arrow.level_up()
        level.increase_level()
        enemy_healths.healths[1] = 0.14
        enemy_healths.enemies_health[1].clear()

    if enemy_healths.healths[2] == 0:
        enemies.enemies[2].goto(3000, 3000)
        enemy_arrow.level_up()
        level.increase_level()
        enemy_healths.healths[2] = 0.14
        enemy_healths.enemies_health[2].clear()

    if enemy_healths.healths[3] == 0:
        enemies.enemies[3].goto(3000, 3000)
        enemy_arrow.level_up()
        level.increase_level()
        enemy_healths.healths[3] = 0.14
        enemy_healths.enemies_health[3].clear()

    if level.level == 5:
        is_game_on = False
        level.game_over()

    count += 1


screen.exitonclick()
