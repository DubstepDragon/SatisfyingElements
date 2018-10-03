import pygame as pg
from settings import *
pyvec = pg.math.Vector2
from math3d import *



class Projectile(pg.sprite.Sprite):
    def __init__(self, position, vel):
        """Set up our platforms"""

        pg.sprite.Sprite.__init__(self) # Call parent class init
        self.image = pg.transform.scale(image_fireball, (10, 10))
        self.rect = self.image.get_rect()
        self.pos = position
        self.vel = vel



    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos










