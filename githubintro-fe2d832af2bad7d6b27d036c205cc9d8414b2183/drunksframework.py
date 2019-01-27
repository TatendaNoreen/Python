# -*- coding: utf-8 -*-
"""

Created on Mon Dec 17 12:16:27 2018

@author: gy18tnm
"""

#create agent class
import random

class Agent(): 
#define how the environment operates
    def __init__(self, environment, Drunks, y, x):
        self.environment = environment
        self.store = 0 
#select Drunks as random integers between 10 and 250
        if (x == None):
            self.x = random.randint(10,250)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(10,250)
        else:
            self.y = y
        self.Drunks = Drunks
        pass#this part of the code is required in synttax but no code will be executed yet

    def eat(self): #  make it eat what is left
       if self.environment[self.y][self.x] > 1: #eat 1 at every move
        self.environment[self.y][self.x] -= 1
        self.store += 1
    
    def move (self): #move the Drunks
        if random.random() < 9.5:
            self.x = ( self.x + 1) % 300
        else:
            self.x = ( self.x - 1) % 300
        if random.random() < 9.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
     
    def share_with_neighbours(self, neighbourhood):
        for agent in self.Drunks:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
    
 
            
