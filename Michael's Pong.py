#***********************************************
# Author: Michael Zhou
# Date: Apr 29, 2019
# Name: Pong
# Description: Pong game
#***********************************************

import random
import pygame
import time

pygame.init()

#resolution
DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 726

#shade
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#paddle dimensions
paddle_height = DISPLAY_HEIGHT/50
paddle_width = paddle_height**2

#game display
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

#declare functions


    

def mainmenu():
    running = True
    gameDisplay.fill(BLACK)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #labels
        font = pygame.font.SysFont(None, 50)
        main = font.render("PONG", True, WHITE)
        gameDisplay.blit(main, (DISPLAY_WIDTH * 0.45, 0))
        start = font.render("START", True, WHITE)
        gameDisplay.blit(start, (DISPLAY_WIDTH * 0.45, DISPLAY_HEIGHT * 0.3))
        info = font.render("INSTRUCTIONS", True, WHITE)
        gameDisplay.blit(info, (DISPLAY_WIDTH * 0.38, DISPLAY_HEIGHT * 0.5))
        
        #boxes for text
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.45, 0, 120, 40), 1)
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.45, DISPLAY_HEIGHT * 0.3, 120, 40), 1)
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.38, DISPLAY_HEIGHT * 0.5, 280, 40), 1)

        #mouse
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        
        if DISPLAY_WIDTH * 0.45+120 > mousePos[0] > DISPLAY_WIDTH * 0.45 and DISPLAY_HEIGHT * 0.3+40 > mousePos[1] > DISPLAY_HEIGHT * 0.3:
            if mouseClick[0] == 1:
                game()

        if DISPLAY_WIDTH * 0.38+280 > mousePos[0] > DISPLAY_WIDTH * 0.38 and DISPLAY_HEIGHT * 0.5+40 > mousePos[1] > DISPLAY_HEIGHT * 0.5:
            if mouseClick[0] == 1:
                instructions()                    


        pygame.display.update()


        

def instructions():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(BLACK)
        #mouse
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        #fonts
        font = pygame.font.SysFont(None, 50)
        instructionfont = pygame.font.SysFont(None, 25)
        instructions = font.render("INSTRUCTIONS", True, WHITE)
        gameDisplay.blit(instructions, (DISPLAY_WIDTH * 0.38, 0))

        #player1 information
        player1 = font.render("PLAYER 1", True, WHITE)
        gameDisplay.blit(player1, (DISPLAY_WIDTH * 0.15, DISPLAY_HEIGHT * 0.2))
        player1text = instructionfont.render("Use left arrow key to move left and right arrow key to move right", True, WHITE)
        gameDisplay.blit(player1text, (DISPLAY_WIDTH * 0.02, DISPLAY_HEIGHT * 0.3))
        player1text1 = instructionfont.render("Player 1 is the bottom paddle", True, WHITE)
        gameDisplay.blit(player1text1, (DISPLAY_WIDTH * 0.02, DISPLAY_HEIGHT * 0.35))

        #player2 information
        player2 = font.render("PLAYER 2", True, WHITE)
        gameDisplay.blit(player2, (DISPLAY_WIDTH * 0.7, DISPLAY_HEIGHT * 0.2))
        player2text = instructionfont.render("Use 'a' to move left and 'd' to move right", True, WHITE)
        gameDisplay.blit(player2text, (DISPLAY_WIDTH * 0.65, DISPLAY_HEIGHT * 0.3))
        player2text1 = instructionfont.render("Player 2 is the top paddle", True, WHITE)
        gameDisplay.blit(player2text1, (DISPLAY_WIDTH * 0.65, DISPLAY_HEIGHT * 0.35))


        #score
        points = font.render("First to 20 points win", True, WHITE)
        gameDisplay.blit(points, (DISPLAY_WIDTH * 0.35, DISPLAY_HEIGHT * 0.5))

        


        #start
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9, 120, 40), 1)
        start = font.render("START", True, WHITE)
        gameDisplay.blit(start, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9))
        
        if DISPLAY_WIDTH * 0.3+120 > mousePos[0] > DISPLAY_WIDTH * 0.3 and DISPLAY_HEIGHT * 0.9+40 > mousePos[1] > DISPLAY_HEIGHT * 0.9:
            if mouseClick[0] == 1:
                game()



                
        pygame.display.update()


    
def score(score1, score2):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(score1) + "-" + str(score2), True, WHITE)
    gameDisplay.blit(text, (DISPLAY_WIDTH * 0.4, 0))

def winner1():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(BLACK)

        font = pygame.font.SysFont(None, 75)
        win = font.render("CONGRATULATIONS! PLAYER 1 WINS!", True, WHITE)
        gameDisplay.blit(win, (DISPLAY_WIDTH * 0.01, DISPLAY_HEIGHT * 0.4))
        
        #play again
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        
        startfont = pygame.font.SysFont(None, 25)
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9, 100, 20), 1)
        start = startfont.render("Play again?", True, WHITE)
        gameDisplay.blit(start, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9))
        
        if DISPLAY_WIDTH * 0.3+100 > mousePos[0] > DISPLAY_WIDTH * 0.3 and DISPLAY_HEIGHT * 0.9+20 > mousePos[1] > DISPLAY_HEIGHT * 0.9:
            if mouseClick[0] == 1:
                game()

        pygame.display.update()
                
def winner2():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(BLACK)
        
        font = pygame.font.SysFont(None, 75)
        win = font.render("CONGRATULATIONS! PLAYER 2 WINS!", True, WHITE)
        gameDisplay.blit(win, (DISPLAY_WIDTH * 0.01, DISPLAY_HEIGHT * 0.4))
        
        #play again
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()

        startfont = pygame.font.SysFont(None, 25)
        pygame.draw.rect(gameDisplay, WHITE, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9, 100, 20), 1)
        start = startfont.render("Play again?", True, WHITE)
        gameDisplay.blit(start, (DISPLAY_WIDTH * 0.3, DISPLAY_HEIGHT * 0.9))
        
        if DISPLAY_WIDTH * 0.3+100 > mousePos[0] > DISPLAY_WIDTH * 0.3 and DISPLAY_HEIGHT * 0.9+20 > mousePos[1] > DISPLAY_HEIGHT * 0.9:
            if mouseClick[0] == 1:
                game()

        pygame.display.update()
        

def ball(ballX, ballY, ballWidth, colour):
    pygame.draw.circle(gameDisplay, WHITE, [int(ballX), int(ballY)], int(ballWidth), )

def paddle(x, y, w, h):
    pygame.draw.rect(gameDisplay, WHITE, (x, y, w, h))



def game():
    x1 = (DISPLAY_WIDTH * 0.40)
    y1 = (DISPLAY_HEIGHT * 0.9)
    x2 = (DISPLAY_WIDTH * 0.40)
    y2 = (DISPLAY_HEIGHT * 0.1)
    xVelocity1 = 0
    xVelocity2 = 0
    ballX = (DISPLAY_WIDTH * 0.5)
    ballY = (DISPLAY_HEIGHT * 0.5)
    ballWidth = 12
    ballxVelocity = 0
    ballyVelocity = DISPLAY_HEIGHT/60
    right_paddle1 = 1000
    right_paddle2 = 0
    score1 = 0
    score2 = 0
    gameExit = False

    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #movement
            if event.type == pygame.KEYDOWN:
                #left
                if event.key == pygame.K_LEFT:
                    xVelocity1 = -10
                #right
                elif event.key == pygame.K_RIGHT:
                    xVelocity1 = 10
                elif event.key == pygame.K_a:
                    xVelocity2 = -10
                elif event.key == pygame.K_d:
                    xVelocity2 = 10
            #released key
            #stops image
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xVelocity1 = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    xVelocity2 = 0
            
        gameDisplay.fill(BLACK)
    

        #bottom paddle
        if (ballY+ballyVelocity > y1) and (ballY+ballyVelocity < y1+paddle_height) and ((x1 < ballX+ballxVelocity+ballWidth) and (ballX+ballxVelocity-ballWidth < x1+paddle_width)):
            ballyVelocity = -ballyVelocity
            ballxVelocity = ((x1+(x1+paddle_width))/2)-ballX
            ballxVelocity = -ballxVelocity/((5*ballWidth)/7)
        #score
        elif ballY+ballyVelocity < 0:
            score2 += 1
            ballX = (DISPLAY_WIDTH * 0.5)
            ballY = (DISPLAY_HEIGHT * 0.5)
            ballxVelocity = 0
            ballyVelocity = -DISPLAY_HEIGHT/60
            y2 = (DISPLAY_HEIGHT * 0.1)
            y1 = (DISPLAY_HEIGHT * 0.9)
            yVelocity1 = 0
            yVelocity2 = 0
            paddle(x1, y1, paddle_width, paddle_height)
            paddle(x2, y2, paddle_width, paddle_height)
            
        #top paddle
        if (ballY+ballyVelocity < y2+paddle_height) and (ballY+ballyVelocity > y2) and ((x2 < ballX+ballxVelocity+ballWidth) and (ballX+ballxVelocity-ballWidth < x2+paddle_width)):
            ballyVelocity = -ballyVelocity
            ballxVelocity = ((x2+(x2+paddle_width))/2)-ballX
            ballxVelocity = -ballxVelocity/((5*ballWidth)/7)
        #score
        elif ballY+ballyVelocity > DISPLAY_HEIGHT:
            score1 += 1
            ballX = (DISPLAY_WIDTH * 0.5)
            ballY = (DISPLAY_HEIGHT * 0.5)
            ballxVelocity = 0
            ballyVelocity = DISPLAY_HEIGHT/60
            y2 = (DISPLAY_HEIGHT * 0.1)
            y1 = (DISPLAY_HEIGHT * 0.9)
            yVelocity1 = 0
            yVelocity2 = 0
            paddle(x1, y1, paddle_width, paddle_height)
            paddle(x2, y2, paddle_width, paddle_height)
        #bounce off wall    
        if ballX+ballxVelocity > DISPLAY_WIDTH or ballX+ballxVelocity < 0:
            ballxVelocity = -ballxVelocity

        
            
        ballX += ballxVelocity
        ballY += ballyVelocity
        
        ball(ballX, ballY, ballWidth, WHITE)
        
            

        if x1 < 0:
            x1 = 1            
            xVelocity1 = 0
        if x1 > DISPLAY_WIDTH - paddle_width:
            x1 = DISPLAY_WIDTH - paddle_width
            xVelocity1 = 0
        if x2 < 0:
            x2 = 1
            xVelocity2 = 0
        if x2 > DISPLAY_WIDTH - paddle_width:
            x2 = DISPLAY_WIDTH - paddle_width
            xVelocity2 = 0

            
        x1 += xVelocity1
        x2 += xVelocity2  

        paddle(x1, y1, paddle_width, paddle_height)
        paddle(x2, y2, paddle_width, paddle_height)


        if score1 == 20:
            winner1()

        if score2 == 20:
            winner2()
        score(score1, score2)

         
        pygame.display.update()
        clock.tick(60)
        
mainmenu()


