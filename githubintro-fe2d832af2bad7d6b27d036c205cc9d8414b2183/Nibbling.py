import matplotlib.pyplot
import agentframework
import csv




#create environment in which agents will operate
environment=[]

#read csv downloaded file 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist=[]		# A list of rows
    environment.append(rowlist)
    for value in row:				# A list of value
        print(value) 				# Floats
        rowlist.append(value)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.



#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + 
#        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 10



# Make the agents and connecting with the environment.
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))



# Move and eat agents with every move or iteration.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
# plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.imshow(environment)    
matplotlib.pyplot.show()  

         