import math
import random

import pygame

# initializing pygame
pygame.init()

from pygame import mixer

# Setting screen , icon , name , background
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('~~> HOT POTATO <~~ @Sanx')
icon = pygame.image.load('potato.png')
pygame.display.set_icon(icon)
background = pygame.image.load('sk1.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

# player
pl_img = pygame.image.load('wicker-basket.png')
pl_x = 360
pl_y = 520
pl_x_change = 0


def player(x, y):
    screen.blit(pl_img, (x, y))


# Background cloud
cloud_img = []
cloud_x = []
cloud_y = []
cloud_y_change = []
for i in range(10):
    cloud_img.append(pygame.image.load('clouds.png'))
    cloud_x.append(random.randint(0, 746))
    cloud_y.append(random.randint(0, 550))
    cloud_y_change.append(0.2)


def cloud(x, y, i):
    screen.blit(cloud_img[i], (x, y))


# potato
number_of_potato = 5
x = 0
potato_img = []
potato_x = []
potato_y = []
potato_y_change = []
for po in range(number_of_potato):
    potato_img.append(pygame.image.load('potato.png'))
    potato_x.append(random.randint(0, 746))
    potato_y.append(x)
    x += -300
    potato_y_change.append(0.4)


def potato(x, y, po):
    screen.blit(potato_img[po], (x, y))


# collision
def collision(potato_x, potato_y, pl_x, pl_y):
    distance = math.sqrt((math.pow(potato_x - pl_x, 2)) + (math.pow(potato_y - pl_y, 2)))
    if distance < 30:
        return True


over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over = over_font.render('GAME OVER', True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    screen.blit(over, (200, 250))


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


def show_score(x, y):
    score = font.render('Score : ' + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


score = 0
running = True
# game loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # changing values of player at x axis
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pl_x_change = -2.5
            if event.key == pygame.K_RIGHT:
                pl_x_change = 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pl_x_change = 0
    # Background Cloud
    for i in range(10):
        if cloud_y[i] >= 0:
            cloud_y[i] += cloud_y_change[i]
        if cloud_y[i] >= 650:
            cloud_y[i] = 0
            cloud_x[i] = random.randint(0, 746)
        cloud(cloud_x[i], cloud_y[i], i)

    # potato
    for po in range(number_of_potato):
        if potato_y[po] <= 550:
            potato_y[po] += potato_y_change[po]
        col = collision(potato_x[po], potato_y[po], pl_x, pl_y)
        if col:
            catch = mixer.Sound('laser.wav')
            catch.play()
            score_value += 1
            potato_y[po] = 0
            potato_x[po] = random.randint(0, 746)

        if potato_y[po] > 549:
            for k in range(number_of_potato):
                potato_y[k] = 2000
            game_over_text()
            break
        potato(potato_x[po], potato_y[po], po)
    # creating boundaries
    if pl_x <= 0:
        pl_x = 0
    elif pl_x >= 746:
        pl_x = 746
    show_score(text_x, text_y)
    pl_x += pl_x_change
    player(pl_x, pl_y)
    pygame.display.update()
