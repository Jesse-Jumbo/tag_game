# Tag game

import pygame                                       # for we can use pygame object

from os import path                                 # for we can find our file -> define path of our file

img_dir = path.join(path.dirname(__file__), 'img')  # define in which folder we want to find the file in the future

# define our window size and FPS
WIDTH = 600
HEIGHT = 600
FPS = 30

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tag!")
clock = pygame.time.Clock()

class  YellowPlayer(pygame.sprite.Sprite):          # for we dinfine all object of YellowPlayer in a class
    def __init__(self):                             # define all object that is we need initialize before update
        pygame.sprite.Sprite.__init__(self)         # initialize self of pygame.sprite.Sprite
        self.image = pygame.transform.scale(yellow_ghost_img, (30, 30))     # initialize image size
        self.rect = self.image.get_rect()                                   # initialize rect to get the image rectangle
        self.rect.bottomleft = (HEIGHT-600, WIDTH-600)                      # initialize where is the rece.bottomleft in
        self.speed_x = 0                            # initialize speed of x
        self.speed_y = 0                            # initialize speed of y

    def update(self):                               # define all object that is we need update in game loop
        self.speed_x = 0                            # keep our speed of x equal to 0 before we press the keys
        self.speed_y = 0                            # keep our speed of y equal to 0 before we press the keys
        keystate = pygame.key.get_pressed()         # difine keystate is to get any keys that we pressed
        if keystate[pygame.K_a]:                    # if we press the a key
            self.speed_x = -5                       # our speed of x will move to left
        if keystate[pygame.K_d]:                    # if we press the d key
            self.speed_x = 5                        # our speed of x will move to right
        if keystate[pygame.K_s]:                    # if we press the s key
            self.speed_y = 5                        # our speed of y will move up
            # new_image = pygame.transform.flip(self.image, False, True)
            # self.image = new_image
        if keystate[pygame.K_w]:                    # if we press the w key
            self.speed_y = -5                       # our speed of y will move down
        self.rect.x += self.speed_x                 # let our rect of x follow our speed of x
        self.rect.y += self.speed_y                 # let our rect of y follow our speed of y
        if self.rect.right > WIDTH:                 # if rect.right over our window of left
            self.rect.right = WIDTH                 # set the location of rect.right equal our window of left
        if self.rect.left < 0:                      # if rect.left over our window of right
            self.rect.left = 0                      # set the location of rect.left equal our window of right
        if self.rect.bottom > HEIGHT:               # if rect.bottom over our window bottom
            self.rect.bottom = HEIGHT               # set the location of rect.bottom equal our wind of bottom
        if self.rect.top < 0:
            self.rect.top = 0

    def enlarge_yellow(self):
        size = self.rect.width * 2, self.rect.height * 2
        self.image = pygame.transform.scale(yellow_ghost_img, size)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.rect = self.image.get_rect()
        self.image.blit(self.image, self.rect)
        self.rect.bottomleft = (HEIGHT - 600, WIDTH - 600)


class  BluePlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(blue_ghost_img, (30, 30))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.bottomright = (HEIGHT, WIDTH)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_j]:
            self.speed_x = -5
        if keystate[pygame.K_l]:
            self.speed_x = 5
        if keystate[pygame.K_i]:
            self.speed_y = -5
        if keystate[pygame.K_k]:
            self.speed_y = 5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def enlarge_blue(self):
        size = self.rect.width * 2, self.rect.height * 2
        self.image = pygame.transform.scale(blue_ghost_img, size)
        self.rect = self.image.get_rect()
        self.image.blit(self.image, self.rect)
        self.image.set_colorkey(RED)
        #        self.rect.bottomright = (HEIGHT, WIDTH)
        self.rect = self.rect.move(self.rect)
# Load all game graphics
background = pygame.image.load(path.join(img_dir, "Python_logo.png")).convert()
background = pygame.transform.scale(background, (600, 600))
background_rect = background.get_rect()
yellow_ghost_img = pygame.image.load(path.join(img_dir, "yellow_ghost.png")).convert_alpha()
blue_ghost_img = pygame.image.load(path.join(img_dir, "blue_ghost.png")).convert_alpha()

all_sprite = pygame.sprite.Group()
player_1 = YellowPlayer()
player_2 = BluePlayer()
all_sprite.add(player_1)
all_sprite.add(player_2)

# create a bunch of event
Enlarge = pygame.USEREVENT

# set timer for the movement events
pygame.time.set_timer(Enlarge, 6000)

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Enlarge:
            player_1.enlarge_yellow()
            player_2.enlarge_blue()


    # Update
    all_sprite.update()

    # check to see if the Yellow_Player hit the Blue_Player

    # check to see if the Green_Player hit the Yellow_Player

    hits = pygame.sprite.collide_rect(player_1, player_2)
    if hits:
        running = False


    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprite.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()