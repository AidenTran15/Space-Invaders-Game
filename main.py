import pygame
import os
import time
import random

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow_small.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red_small.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green_small.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue_small.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow_small.png"))

# Background
BG = RED_LASER = pygame.image.load(os.path.join("assets", "background-black.png"))