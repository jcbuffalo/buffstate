#Example of static file upload
# https://docs.python.org/2/tutorial/inputoutput.html

print ('hello world')

import csv as csv

town = []
state = []
zipcode = []

f = open("C:\\Users\\john.coles\\Documents\\ActiveProjects\\Random\\Buff State\\CIS512_Part_2\\code\\SFHFCLData.csv")
csv.reader(f)
for line in f:
    if "*****" not in line:
        splitline = line.split(',')
        if len(splitline[0]) < 20:
            town.append(splitline[0])
            state.append(splitline[1])
            zipcode.append(splitline[2])
            #print (splitline)

print (town)






















