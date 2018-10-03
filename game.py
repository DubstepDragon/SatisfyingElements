
from player import *
from platform import *
from spawner import *
import os.path
import random as rand




class Game:
    def __init__(self):
        """Setup our game app"""
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(RATIO)
        self.space = pygame.transform.scale(image_space, (WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.running = False
        self.restartButton = pygame.K_r
        self.jumpKey = pygame.K_UP
        self.score = 0
        self.round = 1
        self.timer = 0
        self.timerCountdown = 3





    def newGame(self):
        """Setup a new game"""


        self.allSprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.spawner = Spawner(self, self.player)
        self.enemyList = pygame.sprite.Group()
        self.bulletList = pygame.sprite.Group()
        self.allSprites.add(self.player)




    def run(self):
        """Run our app"""
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.input()
            self.update(self.dt)
            self.draw()

    def input(self):
        """Process Input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.newGame()
                    self.timerCountdown = 3
                    self.timer = 0
                    self.spawner.resetValue = 1
                    self.round = 1
                    self.score = 0

            elif event.type == pygame.MOUSEMOTION:
                self.mouse_x = pygame.mouse.get_pos()[0]
                self.mouse_y = pygame.mouse.get_pos()[1]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.shoot()
                elif event.button == 3:
                    pass





    def update(self, dt):
        """We update our vars"""

        self.allSprites.update(dt)
        self.bulletList.update()
        for e in self.enemyList:
            e.changeVel(self.player.pos)
        self.enemyList.update()

        self.spawner.spawn()

        self.timer += 1 * dt

        hits = pygame.sprite.spritecollide(self.player, self.enemyList, False)
        if hits:
            self.allSprites.remove(self.player)
            self.round += 1

        for bullet in self.bulletList:
            hits = pygame.sprite.spritecollide(bullet, self.enemyList, True)
            if hits:
                self.bulletList.remove(bullet)
                self.score += 1
                self.spawner.enemies_killed += 1

# ========================================
# ========================================

    def Kills(self):
        self.werd_blit_cent(str(self.score), GREEN)


    def draw(self):
        """Draw the game scene"""

        self.screen.fill(BGCOLOR)
        #Draw all game objects
        self.screen.blit(self.space, (0, 0))
        self.bulletList.draw(self.screen)
        self.enemyList.draw(self.screen)
        self.allSprites.draw(self.screen)

        # self.Kills()

        self.ScoreBoard()

        if self.round == 1:
            self.RoundOne()
        elif self.round >= 2:
            self.gameOver()
        pygame.display.update()

    def werd_blit_cent(self, s1, color):
        string = self.font.render(s1, 1, color)
        stringSize = self.font.size(s1)

        self.screen.blit(string, (WIDTH / 2 - stringSize[0] / 2, HEIGHT / 2 - stringSize[1] / 2))

# ========================
#          ROUNDS
# ========================


    def ScoreBoard(self):
        string = self.font.render("SCORE: " + str(self.score), 1, GREEN)
        self.screen.blit(string, (10, 5))


    def RoundOne(self):
        if self.timer < 3:
            self.werd_blit_cent("WASD TO MOVE, LEFT CLICK TO SHOOT", GREEN)
        elif 3 < self.timer < 6:
            self.timerCountdown -= 1 * self.dt
            self.werd_blit_cent(str(int(self.timerCountdown + 1)), GREEN)
        elif 6 < self.timer < 7:
            self.werd_blit_cent("Begin!", GREEN)

    def gameOver(self):
        self.werd_blit_cent("GAME OVER", RED)
        string = self.font.render("Press R to Restart", 1, RED)
        stringSize = self.font.size("Press R to Restart")

        self.screen.blit(string, (WIDTH / 2 - stringSize[0] / 2, (HEIGHT / 2 - stringSize[1] / 2) + 30))
