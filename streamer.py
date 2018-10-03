import pygame as pg
from settings import *
from projectile import *
import random




vec = pg.math.Vector2

class Streamer(pg.sprite.Sprite):
    def __init__(self, position, vel):
        """Set up our platforms"""
        pg.sprite.Sprite.__init__(self)  # Call parent class init
        self.index_STR = random.randint(0, len(STR_LIST) - 1)
        self.image = pygame.transform.scale(STR_LIST[self.index_STR], (50, 50))
        self.rect = self.image.get_rect()
        self.pos = position
        self.vel = vel


        self.speed = 3

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

    def changeVel(self, playerPos):
        tempvel = vec2(playerPos.x, playerPos.y) - self.pos
        self.vel = tempvel.normalized * self.speed

