import pygame
from settings import *
import math as m
from math3d import *
from projectile import *
pyvec = pygame.math.Vector2



class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        """Set up our player"""
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0

        self.game = game
        self.image = pygame.transform.scale(image_pog, PLAYER_SIZE)
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = pyvec(WIDTH / 2 , HEIGHT / 2 - 30)
        self.vel = pyvec(0, 0)
        self.acc = pyvec(0, 0)
        self.pos = vec2(*self.rect.center)

        self.timer = 0
        self.rTimes = 1

        self.leftButton = pygame.K_a
        self.rightButton = pygame.K_d
        self.upButton = pygame.K_w
        self.downButton = pygame.K_s

        self.speed = 10

    def shoot(self):
        if len(self.game.bulletList) < 10:
            intpos = vec2(*self.rect.center)
            tempvel = vec2(self.game.mouse_x, self.game.mouse_y) - intpos
            vel = tempvel.normalized * self.speed
            tempProj = Projectile(intpos, vel)
            self.game.bulletList.add(tempProj)

    def killBullet(self):
        for bullet in self.game.bulletList:
            if bullet.rect.center[0] > WIDTH or bullet.rect.center[0] < 0:
                self.game.bulletList.remove(bullet)
            elif bullet.rect.center[1] > HEIGHT or bullet.rect.center[1] < 0:
                self.game.bulletList.remove(bullet)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.leftButton]:
            # Move Left
            self.acc.x = -PLAYER_ACC

        if keys[self.rightButton]:
            # Move Right
            self.acc.x = PLAYER_ACC

        if keys[self.upButton]:
            # Move Right
            self.acc.y = -PLAYER_ACC

        if keys[self.downButton]:
            # Move Right
            self.acc.y = PLAYER_ACC


    def rotate(self):
        pos = vec2(*self.pos)
        rel_x, rel_y = self.game.mouse_x - pos.x, self.game.mouse_y - pos.y
        angle = (180 / m.pi) * -m.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, dt):
        """Update the player"""

        self.acc = vec2(0, PLAYER_GRAV)

        self.input()
        self.killBullet()
        self.timer_inc(dt)

        self.rotate()

        #Apply Physics
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.acc.y += self.vel.y * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #Set Position
        self.rect.midbottom = self.pos

        if self.rect.left - 10 > WIDTH:
            self.pos.x = 0
        if self.rect.right + 10 < 0:
            self.pos.x = WIDTH

        if self.rect.top - 10 > HEIGHT:
            self.pos.y = 0
        if self.rect.bottom + 10 < 0:
            self.pos.y = HEIGHT


    def kill(self):
        """kill the player if they move for too long"""
        pass

    def timer_inc(self, dt):
        """increase timer"""
        if self.vel.x > 1:
            self.timer += 1 * dt
        if self.vel.x < -1:
            self.timer += 1 * dt