import pygame
import math
import keyboard
import numpy as np
import random


class Button():
    def __init__(self, x, y, image, scale = 1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen):
        action = False
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def detectClick(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pos):
            return True


def draw_text(screen, text, font, text_col, x, y):
    image = font.render(text, True, text_col)
    screen.blit(image, (x, y))


def predictMove(playerMoves):
    if len(playerMoves) == 0:
        return random.choice(["rock", "paper", "scissors"])



def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True
    text_font = pygame.font.SysFont("Arial", 30)


    rockButton = Button(100, 200, pygame.image.load('images\pock.png').convert_alpha(), 1)
    paperButton = Button(500, 200, pygame.image.load('images\paper.png').convert_alpha(), 0.85)
    scissorsButton = Button(850, 250, pygame.image.load('images\scissors.png').convert_alpha(), 0.9)

    text = ""

    player_moves = []
    

    while running:
        for event in pygame.event.get():
            if rockButton.detectClick(event):
                print("Rock Clicked")

            if paperButton.detectClick(event):
                print("Paper Clicked")
            
            if scissorsButton.detectClick(event):
                print("Scissors Clicked")

            if event.type == pygame.QUIT:
                running = False
        
        
        
        pygame.display.flip()
        clock.tick(60)
        screen.fill((255,155,155))


        rockButton.draw(screen)
        paperButton.draw(screen)
        scissorsButton.draw(screen)
        text = "You have won:"

        draw_text(screen, text, text_font, (0,0,0), 620,150)

        
        

    pygame.quit()


main()
