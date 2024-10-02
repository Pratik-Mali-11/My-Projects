from string import whitespace

import pygame
import random

from pyparsing import White

pygame.init()

width = 600
height = 400
screen  = pygame.display.set_mode((width,height))
pygame.display.set_caption("Word guessing game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont("Times New Roman",30)

words = ['apple', 'bicycle', 'candle', 'dragon', 'elephant', 'forest', 'honey', 'guitar',
         'island', 'lemon', 'mountain', 'notebook', 'piano', 'sunflower', 'rose', 'lion']

word = random.choice(words)

guesses = ''
chances = 12

def render_text(text,color,x,y):
    surface = font.render(text,True,color)
    screen.blit(surface,(x,y))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if chances>0:
                if event.unicode.isalpha() and len(event.unicode)==1:
                    guess = event.unicode.lower()
                    if guess not in guesses:
                        guesses+= guess

                    if guess not in word:
                        chances-=1

    display_word = ''
    wrong = 0
    for char in word:
        if char in guesses:
            display_word+=char+''
        else:
            display_word+="_"
            wrong+=1

    render_text(display_word,BLACK,100,100)

    if wrong==0:
        render_text("You win!",GREEN,100,200)

    if chances==0:
        render_text("YOU LOOSE",RED,100,200)
        running=False

    render_text(f"chances left: {chances}",BLACK,100,150)

    pygame.display.update()

screen.fill(WHITE)
render_text(f"the word was: {word}",BLACK,100,100)
pygame.display.update()

pygame.time.wait(3000)

pygame.quit()



