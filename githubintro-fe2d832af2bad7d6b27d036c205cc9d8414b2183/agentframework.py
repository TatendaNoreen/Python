#create agent class
import random

class Agent(): 

    def __init__(self, environment, agents, y, x):
        self.environment = environment
        self.store = 0 
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        self.agents = agents
        pass

    def eat(self): # can you make it eat what is left?
       if self.environment[self.y][self.x] > 10: #eat 10 at every move
        self.environment[self.y][self.x] -= 10
        self.store += 10
    
    def move (self): #move the agents
        if random.random() < 0.5:
            self.x = ( self.x + 1) % 300
        else:
            self.x = ( self.x - 1) % 300
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
     
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
    
    
    
            
            






