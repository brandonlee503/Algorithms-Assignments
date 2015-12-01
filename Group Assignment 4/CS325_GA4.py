#CS325 - Group Assignment 4
#Daniel Springer - Chris Nguyen - Brandon Lee

from pulp import *
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

#Use for days
d = []

#Use for average temps
T = []

# For the following, select one location you wish to ignore and comment out.
# Corvallis Location
with open('Corvallis.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
            average = row[7].strip()
            if(not average.isalpha()):
                    T.append(float(average))
            day = row[8].strip()
            if(not day.isalpha()):
                    d.append(float(day))

# Boston Location
# with open('Boston.csv', 'rb') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#             average = row[4].strip()
#             if(not average.isalpha()):
#                     # To remove all the temperature anomalies
#                     if(float(average) < -100):
#                                 continue
#                     T.append(float(average))
#             day = row[5].strip()
#             if(not day.isalpha()):
#                     d.append(float(day))

n = len(d)

#Initialize Our LpProblem
lprob = LpProblem("Best Fit Line Problem", LpMinimize)

#Set Our Decision Variables
Z = LpVariable("Z",0)
x0 = LpVariable("x0", 0)
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)

#These are the separate parts of main equation
linear = 0
seasonal = 0
solar = 0

#This is what we want to minimize for our LpProblem
lprob += Z

#Here we want to get the max deviation
for i in range(0,n):
    linear = (x0 + x1 * d[i])
    seasonal = (x2 * math.cos(2*math.pi * d[i]/364.25) + x3 * math.sin(2*math.pi * d[i]/364.25))
    solar = (x4 * math.cos(2*math.pi * d[i]/(364.25*10.7)) + x5 * math.sin(2*math.pi*d[i]/(364.25 * 10.7)))
    lprob += Z >= (linear + seasonal + solar - T[i])
    lprob += Z >= -(linear + seasonal + solar - T[i])

status = lprob.solve()

print("Objective: "+ str(value(lprob.objective)))
print("x0: " + str(value(x0)))
print("x1: " + str(value(x1)))
print("x2: " + str(value(x2)))
print("x3: " + str(value(x3)))
print("x4: " + str(value(x4)))
print("x5: " + str(value(x5)))

# Calculate Best Fit
m, b = np.polyfit(np.array(d), np.array(T), 1)

# Create Graph
fig = plt.figure()
ax1 = fig.add_subplot(111)

# For the following, select one location you wish to ignore and comment out.
ax1.set_title("Corvallis Data")
#ax1.set_title("Boston Data")

ax1.set_xlabel('Day')
ax1.set_ylabel('Average Temp')

# Raw Data
ax1.plot(d, T, c='r', label='Raw Data')

# Best Fit
ax1.plot(np.array(d), np.array(m)*np.array(d) + np.array(b), 'b-', label='Best Fit')

leg = ax1.legend()
plt.show()
