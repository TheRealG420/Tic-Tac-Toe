'''Please reference my name 'TheRealG' in your code if you have copied my code in any
way. DISCLAIMERS: this is the original script'''

import pygame
from pygame.locals import *

import random as r
import math, sys

pygame.init()

class CircleLine(object):
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.x = x
        self.y = y

        self.radius = radius

        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2, self.radius*2)

        self.color = (0,0,0)
        
    def update(self):
        self.rect.center = (self.x, self.y)
            
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (255,255,255), self.rect.center, self.radius, 1)

# Classes 1-4
class NoteOne(object):
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.x = x1
        self.y = y1

        self.radius = radius1

        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2, self.radius*2)

        self.color = color_white
        
    def update(self, y_speed):
        self.rect.center = (self.x, self.y)
        
        self.y += y_speed
            
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 1)

class NoteTwo(object):
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.x = x2
        self.y = y2

        self.radius = radius1

        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2, self.radius*2)

        self.color = color_blue
        
    def update(self, y_speed):
        self.rect.center = (self.x, self.y)
        
        self.y += y_speed
            
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (255,255,255), self.rect.center, self.radius, 1)

class NoteThree(object):
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.x = x3
        self.y = y3

        self.radius = radius1

        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2, self.radius*2)

        self.color = color_blue
        
    def update(self, y_speed):
        self.rect.center = (self.x, self.y)
        
        self.y += y_speed
            
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (255,255,255), self.rect.center, self.radius, 1)

class NoteFour(object):
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.x = x4
        self.y = y4

        self.radius = radius1

        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2, self.radius*2)

        self.color = color_white
        
    def update(self, y_speed):
        self.rect.center = (self.x, self.y)
        
        self.y += y_speed
            
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 1)

def musicLoop():
    pygame.mixer.init()
    
    if True:
        #pygame.mixer.music.load('Songs/The Worlds Hardest Game.mp3')
        pygame.mixer.music.load('Songs/Black Rover.mp3')
        pygame.mixer.music.play(-1)
            
        if not (True):
            pygame.mixer.music.stop()

# Creating the window
screensize = (1080, 720)

screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("StepMania (ver. Python3)")

clock = pygame.time.Clock()

# CircleLine Variables
radius = 28

x = screensize[0]*0.2
y = screensize[1]*0.8

# Notes' Variables
radius1 = 28

color_blue = (30, 144, 255)
color_white = (255,255,255)

x1 = screensize[0]*0.2
x2 = 90+(screensize[0]*0.2)
x3 = 180+(screensize[0]*0.2)
x4 = 270+(screensize[0]*0.2)

# First offset of notes speed changes so does offset
y1 = 0 - 900
y2 = 0 - 1500
y3 = 0 - 1200
y4 = 0 - 2100

y_speed = 10 # Change to whatever speed

# Arrays
circle_line_list = []

noteListOne = []
noteListTwo = []
noteListThree = []
noteListFour = []


for i in range(4):
    circle_line = CircleLine(screensize)
    circle_line_list.append(circle_line)

    x += 90

for i in range(1):
    note_one = NoteOne(screensize)
    noteListOne.append(note_one)

for i in range(1):
    note_two = NoteTwo(screensize)
    noteListTwo.append(note_two)

for i in range(1):
    note_three = NoteThree(screensize)
    noteListThree.append(note_three)

for i in range(1):
    note_four = NoteFour(screensize)
    noteListFour.append(note_four)

# Loop Variables and Bool
running = True

musicLoop()

while running:

    clock.tick(120)
    
    screen.fill((0,0,0))
    
    # Event handling phase
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()

    # Key detection/Collision with actual notes
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_x]:
        circle_line_list[0].color = color_white
        
        if note_one.rect.colliderect(circle_line_list[0].rect):
            
            for note_one in noteListOne:
                noteListOne.remove(note_one)

    elif keys[pygame.K_c]:
        circle_line_list[1].color = color_white
        
        if note_two.rect.colliderect(circle_line_list[1].rect):
            
            for note_two in noteListTwo:
                noteListTwo.remove(note_two)

    elif keys[pygame.K_COMMA]:
        circle_line_list[2].color = color_white
        
        if note_three.rect.colliderect(circle_line_list[2].rect):
            
            for note_three in noteListThree:
                noteListThree.remove(note_three)

    elif keys[pygame.K_PERIOD]:
        circle_line_list[-1].color = color_white
        
        if note_four.rect.colliderect(circle_line_list[-1].rect):
            
            for note_four in noteListFour:
                noteListFour.remove(note_four)

    else: 
        circle_line_list[0].color = (0,0,0)
        circle_line_list[1].color = (0,0,0)
        circle_line_list[2].color = (0,0,0)
        circle_line_list[-1].color = (0,0,0)

    # if noteList[:] == []:
    #     print('everythng is gone')

    # Updating/Rendering Phase
    for circle_line in circle_line_list:
        circle_line.update()
        circle_line.render(screen)

    for note_one in noteListOne:
        note_one.update(y_speed)
        note_one.render(screen)

    for note_two in noteListTwo:
        note_two.update(y_speed)
        note_two.render(screen)

    for note_three in noteListThree:
        note_three.update(y_speed)
        note_three.render(screen)

    for note_four in noteListFour:
        note_four.update(y_speed)
        note_four.render(screen)

    pygame.display.flip()
