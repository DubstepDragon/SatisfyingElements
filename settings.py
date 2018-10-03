import pygame


#load images
image_space = pygame.image.load("assets/space_image.jpeg")
image_fireball = pygame.image.load("assets/fireball.png")
image_pog = pygame.image.load("assets/poggers.png")

STR_LIST = []

image_IWD = pygame.image.load("assets/IWD.jpg")
STR_LIST.append(image_IWD)

image_tyler = pygame.image.load("assets/tyler_1.jpg")
STR_LIST.append(image_tyler)

image_moe = pygame.image.load("assets/yassuo_moe.jpg")
STR_LIST.append(image_moe)

image_boxbox = pygame.image.load("assets/boxbox.jpg")
STR_LIST.append(image_boxbox)

image_qt = pygame.image.load("assets/qt.jpg")
STR_LIST.append(image_qt)

image_jackie = pygame.image.load("assets/jackie.jpg")
STR_LIST.append(image_jackie)

image_prof1 = pygame.image.load("assets/prof1.jpg")
STR_LIST.append(image_prof1)

image_prof2 = pygame.image.load("assets/prof2.jpg")
STR_LIST.append(image_prof2)

image_jer = pygame.image.load("assets/jer.jpeg")
STR_LIST.append(image_jer)

#Game Options & Settings
TITLE = "Satisfying elements, streamer edition"
WIDTH = 800
HEIGHT = 600
RATIO = (WIDTH, HEIGHT)
FPS = 60
NUM_STARS = 2

#Colors
BGCOLOR = (0,0,0)
PLATCOLOR = (0,255,0)

#Player Settings
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.15
PLAYER_GRAV = 0
PLAYER_JUMP_VEL = -20
PLAYER_SIZE = (50, 50)
PLAYER_COLOR = (255, 255, 0)

#Platforms
PLATFORM_LIST = [(-10, HEIGHT - 40, WIDTH+20, 40 )]


MENU_FONT = "Arial"
MENU_FONT_SIZE = 25
MENU_FONT_COLOR = (0, 0, 0)
MENU_BUTTON_COLOR = (255, 0, 0)

#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
HOTPINK = (255, 105, 180)
WHITE = (255, 255, 255)


### Text for overall game

#first Stage Text
PSM = "Please Stop Running..."
IWU = "I warned you >.> just don't press any buttons to restart, k?"

