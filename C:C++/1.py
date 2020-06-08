# Project: Spacecraft Game

# Import modules
import pygame
import sys
import random
from math import pi

# Initialize library itself
pygame.init()

# Initialize mixer
pygame.mixer.init()

# Title of the game
pygame.display.set_caption("Spacecraft Game")

# Set the screen value to 800*480
WIDTH = 800
HEIGHT = 480

# Set the FPS value
FPS = 60

# Set the RGB values
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 231, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (255, 255, 255)

# Create the screen window with 800*480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Run variable to control the game over
Run = True

# set the FPS value to be controlled
clock = pygame.time.Clock()

# Create sprite list for the game
all_sprites_list = pygame.sprite.Group()

# Set initial variables for the game
Speed = 10
Score = 0
health = 10
enemies_health = 4
visible = False
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]
enemy_size = 40
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
hitbox = (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
Jump_speed = 8
JUMP = False

# Set the font style for the Score
font = pygame.font.SysFont('SKT', 30, True)


class Enemy(pygame.sprite.Sprite):
    """this class is designed for non-player-controlled sprite"""
    def __init__(self):
        # set itself
        pygame.sprite.Sprite.__init__(self)

        # set the image size to 40*40 square
        self.image = pygame.Surface((40, 40))

        # set the color for the sprite
        self.image.fill(WHITE)

        # set the Enemy to rect shape
        self.rect = self.image.get_rect()

        # set the speed and the position where it will appears
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-120, -36)
        self.speedy = random.randrange(2, 9)
        self.speedx = random.randrange(-2, 4)

    # Update itself with position
    def update(self):
        """find the position for the Enemy"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # update its position
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-120, -36)
            self.speedy = random.randrange(2, 9)


class Bullet(object):
    """this class represents the player-controlled bullet shot by Player"""
    def __init__(self, x, y, radius, color):
        # set the initial position
        self.x = x
        self.y = y

        # set the radius for the bullet
        self.radius = radius

        # set the color for the bullet
        self.color = color

        # set the hitbox when it hits with enemy
        self.hitbox = (radius ,radius, radius, radius)

    def draw(self, screen):
        """draw the bullet on the screen when player input"""
        # draw the bullet hit_box
        self.hitbox = (5, 5, 5, 5)

        # draw the shape for the bullet
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


def drop_enemies(enemy_list):
    """this function controls the frequency for drop the enemies"""
    # set the delay value to random decimal number
    delay = random.random()

    # set the frequency for enemy appears when enemy less than 20
    if len(enemy_list) < 10 and delay < 0.1:
        player_x = random.randint(0, WIDTH-enemy_size)
        player_y = 0

        # as the condition satisfies it wll append new enemy to the list
        enemy_list.append([player_x, player_y])


def draw_enemies(enemy_list):
    """this function draw the enemies in different shape"""
    # for loop used for all the enemies in enemy list
    for enemy_pos in enemy_list:
        # draw the enemy in arc and ellipse shape
        pygame.draw.arc(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size), 3*pi/2, 2*pi, 2)
        pygame.draw.ellipse(screen, WHITE, [enemy_pos[0], enemy_pos[1], enemy_size, enemy_size])


def collision(player_pos, enemy_pos):
    """this function defines collision between player and enemy"""
    # set the horizontal and vertical position for player
    player_x = player_pos[0]
    player_y = player_pos[1]

    # set the horizontal and vertical position for enemy
    enemy_x = enemy_pos[0]
    enemy_y = enemy_pos[1]

    # when enemy and player collide returns True
    if ((enemy_x >= player_x) and enemy_x < (player_x + player_size)) or ((player_x >= enemy_x) and player_x < (enemy_x + enemy_size)):
        if ((enemy_y >= player_y) and enemy_y < (player_y + player_size)) or ((player_y >= enemy_y) and player_y < (enemy_y+enemy_size)):
            return True


def draw_screen():
    """this function draw all the stuff on the screen"""
    # fill the screen with black color(which represents the space^^)
    screen.fill(BLACK)

    # set the score font
    text = font.render('Score: ' + str(Score), 1, WHITE)

    # set the score to the top left side of the screen
    screen.blit(text, (10, 10))

    # draw the moon
    pygame.draw.ellipse(screen, YELLOW, (player_size, player_size, player_size, player_size))

    # draw the player shape
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # draw the health bar for player
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1] - 20, 50, 10))

    # draw the red health bar if player collides with enemy
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0], player_pos[1] - 20, 50 - 5 * (10 - health), 10))

    # draw the enemy on the screen
    for enemy_pos in enemy_list:
        # draw the hit box
        hitbox = (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)

        # draw the hit box in rect shape
        pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)

    # for loop used for all the bullet in bullets_list
    for bullet in bullets:

        # draw the bullets
        bullet.draw(screen)

    # Update the display as the variable changes
    pygame.display.update()


# list of all sprites in the game
all_sprites = pygame.sprite.Group()

# Enemies class used
Enemies = pygame.sprite.Group()

# initialize the bullets_list
bullets = []

# set the frequency which Enemy(Class) appears
for i in range(5):
    E = Enemy()
    all_sprites.add(E)
    Enemies.add(E)

####################
# MAIN LOOP
####################

while Run:
    # set the FPS value
    clock.tick(FPS)

    # check if there as been any event
    for event in pygame.event.get():
        # close window button has been pressed
        if event.type == pygame.QUIT:
            sys.exit()
    # for loop used for every single bullet in bullets_list
    for bullet in bullets:

        # set the speed for bullet
        if (bullet.x < 800) and (bullet.x > 0):
            bullet.y -= 15

        # delete the bullet if it is out of screen
        if bullet.y < 0:
            bullets.pop(bullets.index(bullet))

    # define the keys as ket get pressed
    keys = pygame.key.get_pressed()

    # set the player position
    x = player_pos[0]
    y = player_pos[1]

    # Space bar controls the bullet shot
    if keys[pygame.K_SPACE]:
        # controls the frequency of shots
        if len(bullets) < 2:
            bullets.append(Bullet(round(player_pos[0]+player_size//2), round(player_pos[1]+player_size//2), 5, YELLOW))
    # LEFT movement and it will stop when collides with left edge
    if keys[pygame.K_LEFT] and x > 0:
        x -= Speed
    # RIGHT movement and it will stop when collides with right edge
    if keys[pygame.K_RIGHT] and x < WIDTH - player_size:
        x += Speed
    # controls the jump movement
    if not JUMP:
        if keys[pygame.K_UP]:
            JUMP = True
    else:
        # set Jump movement as a quadratic function
        if Jump_speed >= -8:
            neg = 1
            if Jump_speed < 0:
                neg = -1
            y -= (Jump_speed ** 2) * 0.5 * neg
            Jump_speed -= 1
        # Initialize the JUMP to False
        else:
            JUMP = False
            Jump_speed = 8

    # update the position of player
    player_pos = [x, y]

    # Draw everything on the screen
    draw_screen()

    # Call the functions
    drop_enemies(enemy_list)
    draw_enemies(enemy_list)

    for index, enemy_pos in enumerate(enemy_list):
        """this loop function represents the enemy"""
        # for loop used for all the bullets, if bullets collides with enemy, then Score + 1 and enemy get "popped"
        for bullet in bullets:

            # collision statement
            if ((enemy_pos[0] >= bullet.x) and enemy_pos[0] < (bullet.x + bullet.radius)) or ((bullet.x >= enemy_pos[0]) and bullet.x < (enemy_pos[0] + enemy_size)):
                if ((enemy_pos[1] >= bullet.y) and enemy_pos[1] < (bullet.y + bullet.radius)) or ((bullet.y >= enemy_pos[1]) and bullet.y < (enemy_pos[1] + enemy_size)):

                    # Pop enemy in enemy_list
                    enemy_list.pop(index)

                    # Score += 1
                    Score += 1

        # for enemies on the screen range
        if (enemy_pos[1] >= 0) and (enemy_pos[1] < HEIGHT):

            # set the enemy movement
            enemy_pos[1] += Speed

        # as it falls out of the screen, it will get delete
        else:
            enemy_list.pop(index)

        # call the function to deals with collision between player and enemy
        if collision(player_pos, enemy_pos):

            # minus health value
            if health > 0:
                health -= 1

            # as the health value < 0, game over
            else:
                Run = False

    # updates the data of all sprites
    all_sprites.update()

    # draw the sprites on the screen
    all_sprites.draw(screen)

    # Flip the screen
    pygame.display.flip()
