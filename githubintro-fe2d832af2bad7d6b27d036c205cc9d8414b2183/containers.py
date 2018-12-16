import random
import operator    # Do this line at the top of the code.
import matplotlib.pyplot

agents = []
#y0 = random.randint(0,99)
#x0 = random.randint(0,99)
#agents.append([y0,x0])
numberOfAgents = 1000

# Loop through numberOfAgents time adding new agents to agents
for i in range(numberOfAgents):
    agents.append([random.randint(0,99),random.randint(0,99)])
#print (agents)
#print(max(agents))


rightmostagent = max(agents, key=operator.itemgetter(1))
leftmostagent = min(agents, key=operator.itemgetter(1))
topmostagent = max(agents, key=operator.itemgetter(0))
bottommostagent = min(agents, key=operator.itemgetter(0))

#print(max(agents, key=operator.itemgetter(1)))    # Do this line at the bottom.


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)


for i in range(numberOfAgents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color="blue")
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.scatter(agents[2][1],agents[2][0],color='blue')
#matplotlib.pyplot.scatter(agents[3][1],agents[3][0],color='yellow')

matplotlib.pyplot.scatter(rightmostagent[1],rightmostagent[0],color='green')
matplotlib.pyplot.scatter(leftmostagent[1],leftmostagent[0],color='pink')
matplotlib.pyplot.scatter(topmostagent[1],topmostagent[0],color='purple')
matplotlib.pyplot.scatter(bottommostagent[1],bottommostagent[0],color='orange')


matplotlib.pyplot.show()

