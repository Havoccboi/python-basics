# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 03:28:47 2020

@author: Havoc
"""
"""
city = ["Kushtia", "Dhaka", "Barishal"]
for x in range(1,10,2): #range(start,stop,interval)
    print (x)
    
    


def check_range(i,j):
    for x in range(i,j):
        print (x)
        
check_range(5,10)
"""

# for loop and else ,  else blocked to be executed when the for loop is finished


for i in range (1, 10, 1):
    print (i)
    if i > 3:
        print("breaking..")
        break;
   
else:
    print("execution completed")
    
    #checking double loop operations
    
colors = [ "Red", "Green", "Ash"]
fruits = ["Apple", "Oranges", "Pear"]

for x in colors:
    for y in fruits:
        print(x +  " Not " + y) #putting comma puts a white space
        
# use pass for empty for loop

for i in range(1,19):
    pass #to avoid getting error
    
variable = input()
variable = int(variable)
if variable > 5:
    print("value greater than 5")
elif variable == 5:
    print("equal to 5")
else:
    print("less than 5")
    
    
#short hand if else
a = 5
b = 6
print("A") if a > b else print("B")

if a > 0 and b > 0 :
    print("both pos")
elif a > 0 or b > 0 :
    print("Atleast one positive")


