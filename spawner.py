import random as rand
from streamer import *
from math3d import *

class Spawner:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.amount_of_enemies = 5
        self.num_waves = 5
        self.spawntimer = 1
        self.wavetimer = 5
        self.resetValue = 1
        self.elapsed_time = 0
        self.enemies_killed = 0

        self.speed = 3

    def spawn(self):
        self.spawntimer -= 1 * self.game.dt
        if self.game.timer > 7:
            self.resetValue -= 0.01 * self.game.dt
            if len(self.game.enemyList) < 10:
                if self.spawntimer <= 0:
                    self.createEnemy()
                    self.spawntimer = self.resetValue


    def difficulty(self):
        pass

    def createEnemy(self):
        a = rand.randint(-10, 0)
        b = rand.randint(WIDTH, WIDTH + 10)
        c = rand.randint(0, 1)
        if c == 1:
            x = a
        else:
            x = b

        a = rand.randint(-10, 0)
        b = rand.randint(HEIGHT, HEIGHT + 10)
        c = rand.randint(0, 1)
        if c == 1:
            y = a
        else:
            y = b

        pos = vec2(x, y)
        playerPos = vec2(self.player.pos.x, self.player.pos.y)
        tempvel = playerPos - pos
        vel = tempvel.normalized * self.speed
        tempEnemy = Streamer(pos, vel)
        self.game.enemyList.add(tempEnemy)
