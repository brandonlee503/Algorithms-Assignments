#CS 325 - Group Assignment 3
#Daniel Springer - Chris Nguyen - Brandon Lee
#The Most Magical Subsequence Problem

import time
from random import randint
import sys

#Python has a low recursion limit, we need a larger one for this problem
sys.setrecursionlimit(10000)

#Define input and output filenames
fileIn = "T8.txt"
fileOut = "answers.txt"


#Opens text file with the 1-d array of numbers and put it into our array A
#Also gives use the length of our 1-d array
with open(fileIn) as f:
    ALen = f.readline().split()
    A = []
    for line in f:
        for word in line.split():
            A.append(int(word))
f.close

#Test array of numbers from the GA3 document
B = [31,41,59,26,53,58,6,97,93,23]

#This will be our memo table so that we don't have to recalculate the same
#   value more than once
table = []

#Used for convenience
#0: max value, 1: x-coord in table, 2: y-coord in table
maxVals = []
maxVals.extend([-1,-1,-1])

#Create and fill our memo table with zeroes
def setupTable(h):
    for i in range (0, h):
        table.append(0)


#Greed algorithm is split into two functions for simplicity
#   This function gets called second from within greedStart()
#   greedyAlg() expands the subarray from both sides based on which element is
#    greater. Then finds the max value of the subarray sum * the smallest element
def greedyAlg(Ar,j,i,k,jLim,kLim):
    while( (k < kLim) or (j > jLim)):
        if(table[i] > maxVals[0]):     #This is saving a reference to the max values
            maxVals[0] = table[i]
            maxVals[1] = j
            maxVals[2] = k
        if(j==k):           #base case
            table[i] = Ar[i]*Ar[i]
        if (len(Ar) == 1):     #base case
            table[i] = Ar[i]*Ar[i]
            return table[i]
        elif not Ar:         #base case
            return 0
        else:
            zz = Ar[i]
            if zz == 0: zz = 1      #Prevents dividing by 0 since div by 1 wont ruin result
            if (k < kLim) and (j > jLim):
                if (Ar[j-1] >= Ar[k+1]):
                    if Ar[j-1] < Ar[i]:
                        table[j-1] = Ar[j-1]*(Ar[j-1] + table[i]/zz)
                        i = j-1
                    else:
                        table[i] = Ar[i]*(Ar[j-1] + table[i]/zz)
                    j = j-1
                    continue
                else:
                    if Ar[k+1] < Ar[i]:
                        table[k+1] = Ar[k+1]*(Ar[k+1] + table[i]/zz)
                        i = k+1
                    else:
                        table[i] = Ar[i]*(Ar[k+1] + table[i]/zz)
                    k = k+1
                    continue
            else:   #j and/or k has reached their edge in the array Ar
                if (j > jLim):     #j can still expand to the right of the Ar
                    if Ar[j-1] < Ar[i]:
                        table[j-1] = Ar[j-1]*(Ar[j-1] + table[i]/zz)
                        i = j-1
                    else:
                        table[i] = Ar[i]*(Ar[j-1] + table[i]/zz)
                    j = j-1
                    continue
                elif (k < kLim):   #k can still expand to the left of Ar
                    if Ar[k+1] < Ar[i]:
                        table[k+1] = Ar[k+1]*(Ar[k+1] + table[i]/zz)
                        i = k+1
                    else:
                        table[i] = Ar[i]*(Ar[k+1] + table[i]/zz)
                    k = k+1
                    continue
                else:       #j and k have reached both of their edges
                    return table[i]


#This was used for debugging greedAlg
#   This function gets called first
#   It runs greedyAlg() using every index as a starting point
#def greedStart():
#    for i in range(0,len(A)):
#        greedyAlg(A,i,i,i)
        #Comments are for verbosity and debugging
        #print(str(i))
            #for i in table:
            #   print(i)
            #clearTable(len(A)+1,len(A)+1)
            #print(" ")


#Divide and Conquer algorithm for the Most Magical Subsequence problem
def divideAndConquer(Ar,j,k):
    if (k==j):     #base case
        return Ar[k]*Ar[k]
    if not Ar:            #base case
        return 0
    if (int(k-j) > 1):
        s1=divideAndConquer(Ar,j,int((k-j)/2)+j)
        s2=divideAndConquer(Ar,int((k-j)/2)+j,k)
        s3=greedyAlg(Ar,int((k-j)/2)+j,int((k-j)/2)+j,int((k-j)/2)+j,j,k)
        return #max(s1,s2,s3)
    else:   #when our subarray is length 2, just run greedy, dont split (rounding)
        return greedyAlg(Ar,int((k-j)/2)+j,int((k-j)/2)+j,int((k-j)/2)+j,j,k)


#Main execution begins here
setupTable(len(A)+1)
start = time.clock()    #starting time of the alg
#greedStart()
divideAndConquer(A,0,int(len(A)-1))
end = time.clock()      #ending time of the alg

#get runtime in ms and chop off some unnecessary decimal places
myTime = str(1000*(end-start))
myTime = myTime[:10]
print(str(int(maxVals[0]))+" "+str(maxVals[1])+" "+str(maxVals[2]))
print("Divide and Conquer Algorithm executed in "+str(myTime)+" ms")


#Write to the output file as specified in the problem
fp = open(fileOut,'a+')
fp.write(str(int(maxVals[0]))+" ")
fp.write(str(maxVals[1])+" ")
fp.write(str(maxVals[2])+"\n")
fp.close()

