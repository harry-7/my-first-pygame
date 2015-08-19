""" 
    Author:Hemanth Kumar Veeranki
    Nick:Harry7
     
    This File is one of modules written for the game Donkey Kong
"""

from random import randint as rand
import pygame 

__author__="Hemanth Kumar Veeranki"
__version__ = "1.0.1"
__maintainer__ = "Hemanth Kumar Veeranki"
__email__ = "hemanth.veeranki@students.iiit.ac.in"
__status__ = "Development"

class CoinUtil:

    """ This class takes care of creating and displaying coins """

    def __init__(self):

        """ 
        Default Constructor. It initialises the class variables 
        1.Xpos contains x co-ordinates of all coins
        2.Ypos contains y co-ordinates of all coins
        """
        
        self.Xpos=[]
        self.Ypos=[]
        self.image=pygame.image.load('Coin.jpg')
        self.image=pygame.transform.scale(self.image,(15,20))
        self.rect=self.image.get_rect()

    def Makecoins(self,Map,start,ypos,length):
        
        """ 
        
        This functions takes care of generating coins for a given floor 
        It takes starting position of floor and its y co-ordinate (height) and length of floor as parameters
        It also take Map variable of Board Class's Instance created 

        """

        number=rand(5,20)
        ypos=ypos-1
        if ypos==5:strt=10
        else:strt=0
        for i in range(number):
            xpos=start+rand(strt,length-5)
            self.Xpos.append(xpos)
            self.Ypos.append(ypos)
            if Map[ypos][xpos]==0:
                Map[ypos][xpos]=2

    def DrawCoin(self,Map,display):
        
        """ 
        This Function Draws coins to display 
        It takes Map variable of Board class's instance and display surface as parameters
        """
        
        x=15
        y=20
        for k in xrange(len(self.Xpos)):
            i=self.Ypos[k]
            j=self.Xpos[k]
            if Map[i][j]==2:
                    rect=self.rect
                    rect=rect.move((j*x,i*y))
                    display.blit(self.image,rect)
