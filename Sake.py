from pygame import * #pip install pygame
import pygame.event
import sys
import random
import time


class Snake():
    def __init__(self):
        self.position = [100,50]  #snake position of x & y axis
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = 'RIGHT'
        self.changeDirectionTo = self.direction

    
    def changeDirTo(self,dir):
        if dir == 'RIGHT'  and not self.direction == 'LEFT' : #if you press key RIGHT and it's not going to LEFT then it will go RIGHT. Visulize a snake game movement if you don't get this
            self.direction = 'RIGHT'

        if dir == 'LEFT'  and not self.direction == 'RIGHT' :
            self.direction = 'LEFT'

        if dir == 'UP'  and not self.direction == 'DOWN' :
            self.direction = 'UP'

        if dir == 'DOWN'  and not self.direction == 'UP' :
            self.direction = 'DOWN'

    def move(self,foodPos):
        if self.direction == 'RIGHT' :
            self.position[0] += 10 #to shift the snake toward x axis that's y position[0]
        
        if self.direction == 'LEFT' :
            self.position[0] -=10

        if self.direction == 'UP' :
            self.position[1] -= 10 
        
        if self.direction == 'DOWN' :
            self.position[1] += 10

        self.body.insert(0,list(self.position))
        
        if self.position == foodPos :
            return 1
        
        else :
            self.body.pop()
            return 0

    def checkCollision(self) :
        if self.position[0] > 490 or self.position[0] <=0 :
            self.position[0] = 500-self.position[0]
        
        elif self.position[1] > 490 or self.position[1] <=0 :
           self.position[1] = 500-self.position[1]
        
        for bodyPart in self.body[1:] :
            if self.position  == bodyPart :
                return 1
        return 0


    def getHeadPos(self) :
        return self.position
        
    def getBody(self) :
        return self.body


class FoodBrew():

    def __init__(self) :
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.IsFoodOnScreen = True

    def food (self) :
        if self.IsFoodOnScreen == False :   
             self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
             self.IsFoodOnScreen = True

        return self.position

    def setFoodOnScreen(self , b ):
        self.IsFoodOnScreen = b





def gameOver():
    pygame.display.quit()
    quit()
    sys.exit(0)


pygame.mixer.init()
crash_sound = pygame.mixer.Sound('Crash.wav')  
eat = pygame.mixer.Sound('Woosh.wav')  
pygame.mixer.music.load('Move.wav')
music = pygame.mixer.music.load('Move.wav')

window = pygame.display.set_mode ((500,500))
pygame.display.set_caption('University Snake')
fps = pygame.time.Clock()
score = 0

snake = Snake()
foodbrew = FoodBrew()
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.3)


while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            gameOver()

        if event.type == pygame.KEYDOWN :
            
            if event.key == pygame.K_ESCAPE:
                gameOver()
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT') 
            if event.key == pygame.K_UP:
                snake.changeDirTo('UP') 
            if event.key == pygame.K_DOWN:
                snake.changeDirTo('DOWN') 
            if event.key == pygame.K_LEFT:
                snake.changeDirTo('LEFT') 

    foodPos = foodbrew.food()
    if (snake.move(foodPos) == 1) :
        score+=1
        foodbrew.setFoodOnScreen(False)
        pygame.mixer.Sound.play(eat)


    window.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,0,140),pygame.Rect(snake.position[0],snake.position[1],10,10)) 
        pygame.draw.rect(window,pygame.Color(80,80,80),pygame.Rect(pos[0],pos[1],10,10)) 

    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1] ,10,10)) 

    if(snake.checkCollision() == 1):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        gameOver()
    
    pygame.display.set_caption('University Snake | Score = ' + str(score))
    pygame.display.flip()
    fps.tick(12)