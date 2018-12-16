import random
import operator    # Do this line at the top of the code.
import matplotlib.pyplot
agents = []


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5



numberOfAgents =4
num_of_iterations = 10
#Loop through numberOfAgents time adding new agents to agents
for i in range(numberOfAgents):   
    agents.append([random.randint(0,99),random.randint(0,99)])
    
#for i in range(num_of_iterations ):        
#    agents.append([random.randint(0,99),random.randint(0,99)])    
print (agents)

#for each iteration...
for j in range(num_of_iterations):
    
    #for every agent...
    for i in range(numberOfAgents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][0] = (agents[i][1] + 1) % 100
        else:
            agents[i][0] = (agents[i][1] - 1) % 100
            
        # chnage y value...
#        if random.random() < 0.5:
#            agents[i][0] += 1
#        else:
#            agents[i][0] -= 1
        #change x value...
#        if random.random() < 0.5:
#            agents[i][1] += 1
#        else:
#            agents[i][1] -= 1
        print (agents)
        
    
#    if random.random() < 0.5:
#        agents[0][0] += 1
#    else:
#        agents[0][0] -= 1
#
#    if random.random() < 0.5:
#        agents[0][1] += 1
#    else:
#        agents[0][1] -= 1
    
    
    
    

list_distances = []
for k in range(numberOfAgents):
    for l in range(k+1, numberOfAgents):
        distance = distance_between(agents[k], agents[l])
        print(distance)
        list_distances.append(distance)


print(list_distances)    


max(list_distances)



for i in range(numberOfAgents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])    
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')



"""
for i in range(num_of_iterations ): 
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])    

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
"""   


