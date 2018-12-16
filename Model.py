import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import matplotlib.backends.backend_tkagg
import tkinter
import requests
import bs4
import random

#GET X AND Y DATA FROM THE WEBSITE
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


#create environment in which agents will operate
environment=[]

#read csv downloaded file 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist=[]		# A list of rows
    environment.append(rowlist)
    for value in row:				# A list of value
        #print(value) 				# Floats
        rowlist.append(value)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
        



#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + 
#        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = len(td_ys)
num_of_iterations = 10
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
# Make the agents and connecting with the environment.
agents = []

for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(agentframework.Agent(environment,agents, y, x))

carry_on = True	
def update(frame_number):
    
    fig.clear()
    global carry_on
   
# Move and eat agents with every move or iteration.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
# Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    # distance = self.distance_between(agent) 
    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop         
      
# plot
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)    
    
    if random.random() < 0.001:
        carry_on = False
        print("stopping condition")
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on == True) :
        yield a			# Returns control and waits next call.
        a = a + 1


#add a function that will run our model.
#We'll connect this to our menu such that when the menu is clicked, 
#this function will run, in line with the event based programming model.
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

#BUILDING THE GUI
#builds the main window ("root"); sets its title, 
#then creates and lays out a matplotlib canvas embedded within our window 
#and associated with fig, our matplotlib figure.
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#make a menu, and associate the menu with the function run
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()#WAIT FOR ACTION

