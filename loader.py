""" 
    Author:Hemanth Kumar Veeranki
    Nick:Harry7
     
    This File is one of modules written for the game Donkey Kong

"""

import pygame
from random import randint as rand

__author__="Hemanth Kumar Veeranki"
__version__ = "1.0.1"
__maintainer__ = "Hemanth Kumar Veeranki"
__email__ = "hemanth.veeranki@students.iiit.ac.in"
__status__ = "Development"

"""

Map values for 
1. Coins -   2
2. Fireball- 5
3. Ladders - 3
4. Walls and Floors - 1 

"""

# All Functions of type Draw are used to draw a particular object to the display and they take display surface as a parameter 

class Board:

    """ This is the basic class that implements Board Utilities such as Walls Ladders and Princess""" 
    
    def __init__(self):

        """ 
        
        Default Constructer that initialises all variables 
        1.Xpos contains starting positions of floors
        2.Ypos contains heights of floors
        3.Map conatins the mapping of blocks 
        4.pxp conatins Princess position
        5.length contains lengths of floors

        Map values for things  
        1. Coins -   2
        2. Fireball- 5
        3. Ladders - 3
        4. Walls and Floors - 1 
        
        """

        self.Xpos=[0]*4
        self.Ypos=[0]*4
        self.Map=[]
        self.length=[0]*4
        self.pxp=2
        
        for i in range(30):
            temp=[]
            for j in range(80):
                temp.append(0)
            self.Map.append(temp)


    def MapCreater(self):
        
        """ Modifies Map so that it can now produce Border Walls """

        for i in range(30):
            self.Map[i][0]=1
            self.Map[i][79]=1


        for i in range(80):
            self.Map[0][i]=1
            self.Map[29][i]=1


    def FloorCreater(self):
        
        """ This method creates all the floors for the board """

        fl=0
        ypos=6
        for i in range(4):
            length=rand(45,65)
            self.length[i]=length
            if fl==1:
                s=79
                j=0
                while j<length:
                    self.Map[ypos][s-j]=1
                    j+=1
                self.Xpos[i]=(s-j+1)
            else:
                j=0
                while j<length:
                    self.Map[ypos][j]=1
                    j+=1
                self.Xpos[i]=(0)
            self.Ypos[i]=ypos
            ypos+=6
            fl=1-fl
    
    def LadderCreater(self):

        """ This Method creates Ladders """
        i=0 
        while i < 3:
            if(self.Xpos[i]==0):
                xpos=rand(self.Xpos[i+1]+2,self.length[i]-2)
            else:
                xpos=rand(self.Xpos[i]+2,self.length[i+1]-2)
            ypos=self.Ypos[i]
            if self.Map[ypos-1][xpos]==3:continue
            for j in range(6):
                self.Map[min(ypos+j,28)][xpos]=3
            i+=1
        xpos=self.Xpos[3]+rand(2,30)
        ypos=self.Ypos[3]
        if self.Map[ypos-1][xpos]==3:xpos+=2
        for j in range(6):
                self.Map[min(ypos+j,28)][xpos]=3
        i=0
        while i<3:
            if(self.Xpos[i]==0):
                xpos=rand(self.Xpos[i+1]+2,self.length[i]-2)
            else:
                xpos=rand(self.Xpos[i]+2,self.length[i+1]-1)
            ypos=self.Ypos[i]
            if self.Map[ypos+1][xpos]==3 or self.Map[ypos+1][xpos-1] ==3 or (xpos+1 < 80 and self.Map[ypos+1][xpos+1]==3):
                continue
            mis=rand(2,5)
            for j in range(6):
                if j!=mis:self.Map[min(ypos+j,28)][xpos]=3
            i+=1
            
    def DrawWalls(self,display):
        
        """ This Method Draws Walls and Floors to the Display """
        
        x=15
        y=20
        image=pygame.image.load('wall.jpg').convert()
        image=pygame.transform.scale(image,(15,20))
        for i in xrange(30):
            for j in range(80):
                if self.Map[i][j]==1:
                    rect=image.get_rect()
                    rect=rect.move((j*x,i*y))
                    display.blit(image,rect)
     
    def DrawLadder(self,display):
        
        """ This Method Draws Ladders to the Display """
        
        x=15
        y=20
        image=pygame.image.load('ladder.jpg').convert()
        image=pygame.transform.scale(image,(15,20))
        for i in xrange(30):
            for j in range(80):
                if self.Map[i][j]==3:
                    rect=image.get_rect()
                    rect=rect.move((j*x,i*y))
                    display.blit(image,rect)
    
    def CreatePrincess(self):
        
        """ This Method creates the details of Princess """

        start=rand(9,14)
        length=rand(7,12)
        h1=rand(start+1,start+2)
        h2=rand(h1+2,start+length-2)

        for i in range(length):
            self.Map[3][start+i]=1
        self.Map[2][start+length-1]=1
        self.Map[2][start]=1
        self.Map[3][start+length-1]=1
        for i in range(3,6):
            self.Map[i][h1]=3
            self.Map[i][h2]=3
        self.pxp=rand(start+1,start+4)
    
    def DrawPrincess(self,display):

        """ This Method Draws Princess to the Display """

        image=pygame.image.load('princess.jpg').convert()
        image=pygame.transform.scale(image,(45,45))
        rect=image.get_rect()
        rect=rect.move((self.pxp*15,20))
        display.blit(image,rect)
