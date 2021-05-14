import pygame
import random
import sys
from pygame.locals import *
import time


# Global Variables for the game

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
clock=pygame.time.Clock()
white=(255,255,255)

def welcomescreen():
    #shows welcome images on screen

    playerx=int(SCREENWIDTH/5)
    playery=int((SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2)
    messegex=int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2)
    messegey=int(SCREENHEIGHT*0.13)
    basex=0

    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_RETURN):
                maingame()
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messegex,messegey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def Message(size,mess,x_pos,y_pos):
    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,white)
    SCREEN.blit(render , (x_pos,y_pos))
    pygame.display.update()


def pippos():
    y1=random.randint(int(20+SCREENHEIGHT-GAME_SPRITES['base'].get_height()-GAME_SPRITES['pipe'][0].get_height()),int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()))
    return y1

def gameover(playery,y1,y2,playerx,x):
    if (playery+GAME_SPRITES['player'].get_height()>SCREENHEIGHT-(GAME_SPRITES['base'].get_height()) or playery<0) or (x<(playerx+GAME_SPRITES['player'].get_width())<(x+GAME_SPRITES['pipe'][0].get_width()) and (playery+GAME_SPRITES['player'].get_height()>y1 or playery<(y2+GAME_SPRITES['pipe'][0].get_height()))):
            GAME_SOUNDS['hit'].play()
            GAME_SOUNDS['die'].play()
            Message(40,"Moj Kardi",40,210)            
            clock.tick(0.10)
            welcomescreen()

    
def maingame():
    score=0
    playerx=int(SCREENHEIGHT/5)
    playery=int(SCREENHEIGHT/2)
    basex=0
    Y_change=0
    x=SCREENWIDTH+10
    y1=300
    count=0
    game=True
    
    


    while game==True:
        
        y2=int(y1-150-GAME_SPRITES['pipe'][0].get_height())


        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    Y_change=+13
                    GAME_SOUNDS['wing'].play()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    Y_change=0
            
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
        
        SCREEN.blit(GAME_SPRITES['pipe'][1],(x,y1))
        SCREEN.blit(GAME_SPRITES['pipe'][0],(x,y2))
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        Message(50,f"Score :{count}",0,0)
        x=x-5
        FPSCLOCK.tick(FPS)
        pygame.display.update()
        

        if (x+GAME_SPRITES['pipe'][0].get_width())<0:
            x=SCREENWIDTH+10
            GAME_SOUNDS['point'].play()
            y1=pippos()
            count+=1
        gameover(playery,y1,y2,playerx,x)
        playery=playery-Y_change
        playery=playery+7
        


if __name__ == "__main__":
    # This will be the main point where our game will be start
    pygame.init()  # intialize all pygame mofules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Floopy Bird Game by Chandan')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )

    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(
        PIPE).convert_alpha(), 180), pygame.image.load(PIPE).convert_alpha())
    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    GAME_SOUNDS['die']=pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('gallery/audio/wing.wav')

    

    
    
    while True:
        welcomescreen()
         
