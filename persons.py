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

import pygame


__author__="Hemanth Kumar Veeranki"
__version__ = "1.0.1"
__maintainer__ = "Hemanth Kumar Veeranki"
__email__ = "hemanth.veeranki@students.iiit.ac.in"
__status__ = "Development"

class Person:

    """ This is the super class for Player class and Donkey class """
    
    def __init__(self,xpos,ypos):

        """ 
        
        Default constructor of this class 
        xpos has xco-ordinate of person similarly ypos
        side denotes his direction of present moovment
        
        """
        
        self.xpos=xpos
        self.ypos=ypos
        self.side=0
        self.image=pygame.image.load('Monkey.jpg')
        self.image=pygame.transform.scale(self.image,(45,60))
        self.flippedimage=pygame.transform.flip(self.image,True,False)
        self.rect=self.image.get_rect()
        
    def Draw(self):
        
        """ We will modify this in derived class according to images"""
        
        raise NotImplementedError("Subclass must implement abstract method")
        
    def getPosition(self):
        return self.xpos,self.ypos
class Player(Person):
    
    """ This class takes care of methods related to player """

    def __init__(self,name,score=0,lifes=3):
        
        """ 
        This is the constructor for Player class it initialises all variables 
        1.__score contains score
        2.__lifes has number of lifes
        3.xpos has his x co-ordinate
        4.ypos has his y co-ordinate
        5.side denotes  current direction of movement
        """

        self.name=name
        self.__score=score
        self.__lifes=3
        self.ypos=28
        self.xpos=2
        self.side=0
        self.image=pygame.image.load('player.jpg')
        self.image=pygame.transform.scale(self.image,(15,20))
        self.flippedimage=pygame.transform.flip(self.image,True,False)
        self.rect=self.image.get_rect()
    
    def Draw(self,display):

        """ 
        
        This functions draws player to display 
        It takes display surface as a parameter

        """

        x=self.xpos
        y=self.ypos
        rect=self.rect
        rect=rect.move([x*15,y*20])
        if self.side==1:
            #Checking whether he is left or not 
            
            display.blit(self.flippedimage,rect)
        else:
            display.blit(self.image,rect)


    def DisplayScore(self,display):
        
        """ This function displays the score and it takes display surface as a parameter """

        myfont = pygame.font.SysFont("Monospace", 15)
        image=myfont.render("Score: "+str(self.__score),1,(255,255,255))
        display.blit(image,[200,640])
   
    def DisplayLifes(self,display):
        
        """ This function displays the lifes left and it takes display surface as a parameter """
        
        image=pygame.image.load('lifes.jpg')
        image=pygame.transform.scale(image,(60,60))
        for i in range(self.__lifes):
            display.blit(image,[400+i*55,665])
        

    def collectCoin(self,Map):
       
        """ This method checks whether the player had arrived at a coin. If he has then increments his score by 20 """

        x=self.xpos
        y=self.ypos

        
        if Map[y][x]==2:
            Map[y][x]=0
            self.__score+=5
    
    def checkCollision(self,Map):

        """
        
        This method checks whether the player had met a Fireball 
        If he had met it calls Die method and returns its value 
        else it returns 1 
        
        """
        
        x=self.xpos
        y=self.ypos
        
        # We check if its greater than 5 because of the process we followed when moving a Fireball

        if Map[y][x]>=5:
            return self.Die()
        
        return 1
    
    def Die(self):
        
        """ 
        
        This Method deals the death of players life
        If the player has lifes remaining it returns 2
        Else if  the lifes are over it returns 3
        
        """

        self.__lifes-=1
        self.__score-=25
        if self.__lifes>=1:
            return 2
        return 3
    
    def checkWall(self,Map):
        
        """

        This Method takes Map variable of Board classes instance and determines whether there is a colllision with wall 
        and returns True or False based on it
        
        """
        x=self.xpos
        y=self.ypos
        if Map[y][x]==1:
            return True
        return False
    
    def CheckRescue(self,game):
        
        """

        This Method checks whether the player had rescued princess or not 

        """
        x=self.xpos
        y=self.ypos

        if x==game.pxp and y==2:return True
        return False
    
    def Win(self):

        """ This method is used to increment score by 50 incase the player rescues princess """

        self.__score+=50


class Donkey(Person):
   
    """ 
    This Class takes care of Monkey 
    This has no special constructor . It uses constructor of previous class    
    """

    def move(self):

        """ This method takes care of Moving monkey """
        
        if self.side==1:self.xpos-=1
        else:self.xpos+=1
        if self.xpos>6:self.side=1
        if self.xpos<2:self.side=0

    def Draw(self,display):
        
        """ This Method draws Monkey to display and it takes display surface as parameter """

        x=self.xpos
        y=self.ypos
        rect=self.rect 
        rect=rect.move([(x)*15,(y-2)*20])
        if self.side==0:
            display.blit(self.flippedimage,rect)
        else: 
            display.blit(self.image,rect)
            #Checking whether its moving left or right 
        
