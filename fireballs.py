""" 
    Author:Hemanth Kumar Veeranki
    Nick:Harry7
     
    This File is one of modules written for the game Donkey Kong
    
"""

import pygame
from random import randint as rand

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

class Fireball:

    """ This Class basically deals with all tasks of Fireballs """

    def __init__(self):
        
        """ 
        This is default constructor. It initialises all variable 
        1.Xpos contains x co-ordinates of fireballs similarly the Ypos has heights
        2.side determines which side the fireball has to move
        """

        self.Xpos=[]
        self.Ypos=[]
        self.side=[]
        self.infall=[]
        self.image=pygame.image.load('fireball.jpg')
        self.image=pygame.transform.scale(self.image,(15,20))
        self.rect=self.image.get_rect()
    def checkWall(self,Map,x,y):
        return Map[y][x]==1
    def Makefireballs(self,Map,xpos,ypos):
        
        """ 
        
        This Functions generates a fireball from monkey 
        It takes the Map,Xpos,Ypos variables of Board class's instance created
        
        """

        if(Map[ypos][xpos]==0):
            Map[ypos][xpos]=5
            self.Xpos.append(xpos)
            self.Ypos.append(ypos)
            self.side.append(1)
            self.infall.append(0)

    def DrawFireball(self,Map,display):
        
        """ 
        
        This Functions Draws Fireballs to the display
        It takes Map variable of Board class instance created and display surface as variables

        """

        x=15
        y=20
        for k in xrange(len(self.Xpos)):
            j=self.Xpos[k]
            i=self.Ypos[k]
            if Map[i][j]>=5 and Map[i][j]!=100:
                    rect=self.rect
                    rect=rect.move((j*x,i*y))
                    display.blit(self.image,rect)
    
    def move(self,game):
        
        """
         
         This function takes care of moving fireballs and eliminating them if they go to the end
         It takes instance of Board class created in main_game file 
        
        """

        # We store indices of fireballs came to the end in this variable 
        marked=[]
        for i in range(len(self.Xpos)):
            
            x=self.Xpos[i]
            y=self.Ypos[i]
            s=self.side[i]
            #Instead of making its value as 5 we add 5 and when removing we subtract 5 so as to  take care of fireball coming onto other objects 
            game.Map[y][x]-=5
            
            #This decides the probability of going down the ladder or getting down through end of floor
            
            p=rand(0,1)
            
            # Taking care of Ladders and getting down through a ladder
            if self.infall[i]==1:
                y+=1
                if game.Map[y+1][x]!=0:
                    self.infall[i]=0
            elif p==1 and  game.Map[y+1][x]==3:
                y+=1
                if self.checkWall(game.Map,x,y):
                    y-=1
            elif game.Map[y][x]==3 and game.Map[y+1][x]!=1:
                y+=1
                if self.checkWall(game.Map,x,y):
                    y-=1
            
            elif game.Map[y-1][x]==3 and game.Map[y+1][x]==3:
                y+=1
                if self.checkWall(game.Map,x,y):
                    y-=1
            elif y==28:
                    x-=1
                    if x==1:
                        game.Map[y][x]-=5
                        marked.append(i)
            elif self.side[i]==1:
                
                # Dealing with normal moovment on floor
                x+=1
                if self.checkWall(game.Map,x,y):
                    self.side[i]=0
                    x-=2
            else:
                
                # Dealing with normal moovment on floor
                
                x-=1
                if self.checkWall(game.Map,x,y):
                    x+=2
                    self.side[i]=1
        
            if self.infall[i]!=1 and game.Map[y][x]==0 and game.Map[y+1][x]==0:
                self.infall[i]=1
            game.Map[y][x]+=5

            self.Xpos[i]=x
            self.Ypos[i]=y

            marked.sort()
            j=0
        # Eliminating the ones which reached the end
        
        for i in marked:
                self.Xpos.pop(i-j)
                self.Ypos.pop(i-j)
                self.side.pop(i-j)
                j+=1
        
        #Same as above 
