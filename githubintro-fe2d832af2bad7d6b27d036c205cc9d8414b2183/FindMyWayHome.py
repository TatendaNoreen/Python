# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:16:56 2019

@author: gy18tnm
"""

import random
import drunksframework
import csv
import matplotlib   # Do this line at the top of the code.
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib.backends.backend_tkagg
import tkinter
import requests
import bs4


PubsHomes = requests.get('http://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/drunk.plan')
content = PubsHomes.text
soup = bs4.BeautifulSoup(content, 'html.parser')
Pubs = soup.find_all(attrs= "1")
Homes = soup.find_all(attrs= "10,250")
EmptySpaces = soup.find_all(attrs="0")
print(Pubs)
print(Homes)
print(EmptySpaces)


numberOfDrunks = 25
num_of_iterations = 25#the number of times random Drunks are generated in a loop
neighbourhood = 250

#create environment in which Drunks will move
environment=[]
#read data from website download as text file  
f = open('drunk.plan.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist=[]		# A list of rows
    environment.append(rowlist)
    for value in row:				# A list of value
        #print(value) 				# Floats
        rowlist.append(value)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
        
#create agents
Drunks = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Loop through numberOfDrunks time adding new Drunks to model each time
for i in range(numberOfDrunks):
    y= random.randint(10,250)
    x = random.randint(10,250)
    Drunks.append(drunksframework.Agent(environment,Drunks, y, x))
print (Drunks)


# Move and eat space to prevent reselection with every move or iteration  
for j in range(num_of_iterations):#define the loop within the loop
    for i in range(numberOfDrunks):
        Drunks[i].move()
        Drunks[i].eat()
        Drunks[i].share_with_neighbours(neighbourhood)
  

# plot
#make 10- 250  the limits for the plot axes 
#because those are the houses available for the drunks to be assigned to.
matplotlib.pyplot.ylim(10, 250)
matplotlib.pyplot.xlim(10, 250)
matplotlib.pyplot.imshow(environment)
for i in range(numberOfDrunks):
        matplotlib.pyplot.scatter(Drunks[i].y,Drunks[i].x,color="white")
#        print((Drunks[i].[y0],Drunks[i].[x0])



#create GUI and animation to run the model in another window linked to the data website
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    
root = tkinter.Tk() 
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#make a menu, and associate the menu with the function run
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()#WAIT FOR ACTION


