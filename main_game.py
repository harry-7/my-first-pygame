""" 
    Author:Hemanth Kumar Veeranki
    Nick:Harry7
     
    This File is one of modules written for the game Donkey Kong

"""

"""

Map values for 
1. Coins -   2
2. Fireball- 5
3. Ladders - 3
4. Walls and Floors - 1 

"""

__author__="Hemanth Kumar Veeranki"
__version__ = "1.0.1"
__maintainer__ = "Hemanth Kumar Veeranki"
__email__ = "hemanth.veeranki@students.iiit.ac.in"
__status__ = "Development"

# Importing modules required

import pygame
from loader import Board
from coins import CoinUtil
from fireballs import Fireball
from persons import *
import time

class Gameloader:	
    
    """ This class takes care of loading and running the Game"""

    def __init__(self):

        """ Default Constructor Nothing to do here"""

        pass
    def Gameloop(self):

        """ This method runs the Game """


        #Setting caption for window

        pygame.display.set_caption('My Game')

        #Some variables used in the game loop

        BLACK=(0,0,0)
        clock=pygame.time.Clock()
        FPS=60

        #Creating an Instance of Player and Monkey

        player=Player("Player1")
        monkey=Donkey(2,5)
        GameEnd=False

        display=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #Loading Images required 
        died=pygame.image.load('Died.jpg').convert()
        
        complete=pygame.image.load('Completion.png').convert()
        
        success=pygame.image.load('Success.png').convert()
        
        #Displaying Instructions

        image=pygame.image.load('Instructions.jpg').convert()
        rect=image.get_rect()
        rect.move(0,0)
        display.blit(image,rect)
        pygame.display.update()
        myfl=False 
        while True:
	    for i in pygame.event.get():
	        if i.type==pygame.QUIT:
                    return False
                if i.type==pygame.KEYDOWN:
                    myfl=True
                    break
            if myfl==True:
                states=pygame.key.get_pressed()
                if 1 in states:break
            rect.move(0,0)
            display.blit(image,rect)
            pygame.display.update()
        
        level=512
        level1=1
        display=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        myfont=pygame.font.SysFont("Monaco",15)
        inFall=False
        while not GameEnd:

	    #Initialising Board and creating Walls Floors Princess and Ladders
                    	
            game=Board()
            game.MapCreater()
	    game.FloorCreater()
	    game.LadderCreater()
	    game.CreatePrincess()
            surface=pygame.Surface((1500,600))

            #Creating Instances of Utilities to deal with Coins and Fireballs

            coins=CoinUtil()
	    fireballs=Fireball()

	    #Generating Coins in each floor

	    for i in range(4):
	        coins.Makecoins(game.Map,game.Xpos[i],game.Ypos[i],game.length[i])

	    #Some Variables used inside gameloop

	    injump=False
	    cnt=st=0
	    fl1=0
	    gameExit=False

	    #Generating Static things for Game like Walls and Ladders

	    game.DrawPrincess(surface)
	    game.DrawWalls(surface)
	    game.DrawLadder(surface)

	    # Main loop for Game
            xdiff=0
	    while not gameExit:

    	    #Filling display with a required color

    	        display.fill(BLACK)    

	    #Marking positions of player to check conditions
                x,y=player.getPosition()
	     
	        #Checking whether close button is pressed

	        for i in pygame.event.get():
	            if i.type==pygame.QUIT:
	                gameExit=True
                        GameEnd=True
	    
	        # Variable to store the state of Keys Pressed
	        #The Keys pressed will have a value 1
	
	        states=pygame.key.get_pressed()
	        
	        #If the player is in Jump implement
                if states[pygame.K_q]:
		    GameEnd=True
		    break
                if inFall:
                    player.ypos+=1
                    y+=1
                    if game.Map[y+1][x]!=0 and game.Map[y+1][x]!=2:
                        inFall=False
	        elif injump or states[pygame.K_SPACE]==1:
	            if game.Map[y][x+1]==1 or game.Map[y][x-1]==1:pass
                    mycnt=0
                    myfl=True
                    if not injump:
                        if game.Map[y][x]==3:mycnt+=1
                        if game.Map[y+1][x]==3:mycnt+=1
                        if game.Map[y-1][x]==3:mycnt+=1
                        if mycnt>=2 and game.Map[y+1][x]!=1 :
                            myfl=False
                    if not myfl:pass
                    else:
                        if not injump:
	                    injump=True
                            if states[pygame.K_a]==1:
                                xdiff=-1
                                player.side=1
                            elif states[pygame.K_d]==1:
                                xdiff=1
                                player.side=0
	                    cnt=1
	                else: cnt+=1
	                if cnt<3:player.ypos-=1
	                elif cnt>3:player.ypos+=1
	                player.xpos+=xdiff
                        if cnt==5:
                            xdiff=0
	                    injump=False
	    
                #To move left 
	    
	        elif states[pygame.K_a]==1:
	            if game.Map[y][x]==3 and game.Map[y+1][x-1]==0:pass
	            else:
                        mycnt=0
                        if game.Map[y][x]==3:mycnt+=1
                        if game.Map[y+1][x]==3:mycnt+=1
                        if game.Map[y-1][x]==3:mycnt+=1
                        if mycnt>=2 and game.Map[y+1][x-1]==0 :pass
                        else:
                            player.xpos-=1
	                    player.side=1
	    
	        #To move right
	
	        elif states[pygame.K_d]:
	            if game.Map[y][x]==3 and game.Map[y+1][x-1]==0:pass
	            else:    
                        mycnt=0
                        if game.Map[y][x]==3:mycnt+=1
                        if game.Map[y+1][x]==3:mycnt+=1
                        if game.Map[y-1][x]==3:mycnt+=1
                        if mycnt>=2 and game.Map[y+1][x-1]==0 :pass
                        else:
	                    player.xpos+=1
	                    player.side=0

	        #To climb a ladder basically
	
	        elif states[pygame.K_w]:
                    if game.Map[y][x]==3 :
                        #and not (game.Map[y-1][x]==0 and game.Map[y][x]==0):
	                 player.ypos-=1
	    
	        #To get down a ladder
	
	        elif states[pygame.K_s]:
                    if game.Map[y][x]==3 and game.Map[y+1][x]==0:pass
	            elif game.Map[y+1][x]==3 or (game.Map[y][x]==3 and game.Map[y][x+1]==1 or game.Map[y][x-1]==1):
	                player.ypos+=1
	    
	        #Checking whether there is a collision with the wall
	
	        if player.checkWall(game.Map)==True: player.xpos=x
	    
	        #Checking whether player had met a Fireball

                """

                The Flag values of fl :

                1 - No collision
                2 - Died but lifes are remaining
                3 - Lifes completed

                """

                fl=player.checkCollision(game.Map)
	        if fl==3:
		    GameEnd=True
                    rect=died.get_rect()
                    rect.move(0,0)
                    display.blit(died,rect)
                    pygame.display.update()
                    time.sleep(2)
                    break
	        elif fl==1:pass
	    
                else:
                    time.sleep(0.5)
                    rect=died.get_rect()
                    rect.move(0,0)
                    display.blit(died,rect)
                    pygame.display.update()
	            player.ypos=28
	            player.xpos=2
	            injump=False
	            cnt=0
	            player.side=0
                    time.sleep(2)
	    
                x=player.xpos
	        y=player.ypos
	        #Checking whether the player has crossed the limit of floor and in air 
	
	        if not inFall and not injump and game.Map[y][x]==0 and game.Map[y+1][x]==0:
                    inFall=True
                
                #Genereating Fireballs
	    
                if st%level==1 or (level1<5 and player.ypos==5 and st%(level/2)==1): fireballs.Makefireballs(game.Map,monkey.xpos+1,game.Ypos[0]-1)

	    
	        #Moving Fireballs
		    
                if st%2==1:num=fireballs.move(game)
	    
	        #Checking whether Player has arrived at a coin
	
	        player.collectCoin(game.Map)
                player.xpos=x
                player.ypos=y
                #Checking Whether Player has rescued the princess or not 
            
                fl1=player.CheckRescue(game)
            
                if fl1==True:
                    player.Win()
	            player.ypos=28
	            player.xpos=2
	            injump=False
	            cnt=0
	            player.side=0
                    gameExit=True
                    rect=success.get_rect()
                    rect.move(0,0)
                    display.blit(success,rect)
                    pygame.display.update()
                    time.sleep(1)
                    myfl=False
                    while True:
	                for i in pygame.event.get():
	                    if i.type==pygame.QUIT:
                                return False
                            if i.type==pygame.KEYDOWN:
                                myfl=True
                                break
                        if myfl==True:
                                states=pygame.key.get_pressed()
                                if 1 in states:break
                        rect.move(0,0)
                        display.blit(image,rect)
                        pygame.display.update()
                    time.sleep(1)
                    
                    #time.sleep(1)
                    #Checking Whether game has completed or not 
                
                    if level1>4:
                        rect=complete.get_rect()
                        rect.move(0,0)
                        display.blit(complete,rect)
                        pygame.display.update()
                        time.sleep(2)
                    else:
                        #Increasing the level 
                        level/=2
                        level1+=1
        
	        #Checking Once again whether player had met a Fireball

                fl=player.checkCollision(game.Map)
                if fl==3: 
		    GameEnd=True
                    rect=died.get_rect()
                    rect.move(0,0)
                    display.blit(died,rect)
                    pygame.display.update()
                    time.sleep(2)
		    break
	    
                elif fl==1: pass
	    
                else:
                    time.sleep(0.5)
                    rect=died.get_rect()
                    rect.move(0,0)
                    display.blit(died,rect)
                    pygame.display.update()
	            player.ypos=28
	            player.xpos=2
	            injump=False
	            cnt=0
	            player.side=0
                    time.sleep(2)

	        #Moving the Monkey
	
	        if st%4==1:monkey.move()
	    
	        #Drawing all items on screen
	    
	        display.blit(surface,[0,0])
	        player.DisplayScore(display)
	        player.DisplayLifes(display)
	        fireballs.DrawFireball(game.Map,display)
	        coins.DrawCoin(game.Map,display)
	        player.Draw(display)
	        monkey.Draw(display)
                myfont = pygame.font.SysFont("Monospace", 15)
                image=myfont.render("Level: "+str(level1),1,(255,255,255))
                display.blit(image,[200,620])
	        pygame.display.update()
	        clock.tick(12)
	        st+=1
	        st%=256

        #Displaying Final Words 
        
        image=pygame.image.load('FinalWords.jpg').convert()
        fl=False
        rect=image.get_rect()
        rect.move(0,0)
	pygame.display.update()
        myfl=False
        time.sleep(0.5)
        while not fl:
	    for i in pygame.event.get():
	        if i.type==pygame.QUIT:
                    return False
                if i.type==pygame.KEYDOWN:
                    myfl=True
                    break
            if myfl==True:
                states=pygame.key.get_pressed()
                if states[pygame.K_q]==1:
                    fl=True
                if states[pygame.K_r]==1:
                    return True
            rect=image.get_rect()
            rect.move(0,0)
            display.blit(image,rect)
            pygame.display.update()
        
        return False

if __name__=="__main__":
    
    #Initialising pygame display 
    pygame.init()
    
    Game=Gameloader()
    fl=Game.Gameloop()
    while fl==True:
        fl=Game.Gameloop()
    
    #Quitting   
    pygame.quit()
    exit(0)
