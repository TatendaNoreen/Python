#create sample environment which will be linked to the agents

import csv
import matplotlib.pyplot



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


#plot environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()





