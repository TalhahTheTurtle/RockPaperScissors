import pygame
import math
import keyboard
import numpy as np
import random
from collections import defaultdict

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


def predictMove(transitionMatrix, lastMove):
    if lastMove not in transitionMatrix:
        return random.choice(["rock", "paper", "scissors"])

    moveProbs = transitionMatrix[lastMove]
    predictedMove = max(moveProbs, key=moveProbs.get)

    if predictedMove == "rock":
        return "paper"
    elif predictedMove == "paper":
        return "scissors"
    else:
        return "rock"

def determineWinner(player, computer):
    if player == computer:
        return "Draw"
    
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"


def updateMarkoxChain(transitionMatrix, previousMove, currentMove):
    transitionMatrix[previousMove][currentMove] += 1



def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True
    text_font = pygame.font.SysFont("Arial", 30)

    transitionMatrix = defaultdict(lambda: {"rock": 0, "paper": 0, "scissors": 0})



    rockButton = Button(100, 200, pygame.image.load('images\pock.png').convert_alpha(), 1)
    paperButton = Button(500, 200, pygame.image.load('images\paper.png').convert_alpha(), 0.85)
    scissorsButton = Button(850, 250, pygame.image.load('images\scissors.png').convert_alpha(), 0.9)

    text = ""

    picked = ""
    playerWins = 0
    aiWins = 0
    playerMoves = []
    lastMove = None
    click = False
    

    while running:
        for event in pygame.event.get():
            if rockButton.detectClick(event):
                print("Rock Clicked")
                click = True

                picked = "rock"

            if paperButton.detectClick(event):
                print("Paper Clicked")
                click = True
                picked = "paper" 
            
            if scissorsButton.detectClick(event):
                print("Scissors Clicked")
                click = True
                picked = "scissors"

            if event.type == pygame.QUIT:
                running = False
        

        if click:
            if picked in ["rock", "paper", "scissors"]:

                if lastMove is not None:
                    updateMarkoxChain(transitionMatrix, lastMove, picked)
                lastMove = picked

                computerChoice = predictMove(transitionMatrix, lastMove)
                #print(transitionMatrix)
                result = determineWinner(picked, computerChoice)
                
                if result == "player":
                    playerWins+=1
                elif result == "computer":
                    aiWins +=1
                click = False

                print (computerChoice)
                print()
        

        
        pygame.display.flip()
        clock.tick(60)
        screen.fill((255,155,155))


        rockButton.draw(screen)
        paperButton.draw(screen)
        scissorsButton.draw(screen)
        text = "You have won: " + str(playerWins) + "    AI has won: " + str(aiWins)


        draw_text(screen, text, text_font, (0,0,0), 620,150)

        
        

    pygame.quit()


main()
