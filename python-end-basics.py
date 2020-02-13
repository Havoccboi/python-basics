team = {}
team['Center'] = "Al Horford"
print(team['Center'])

#iterations for loop

even = [0,2,4,6,8,10]

for n in even:
    print (n, end = " ")

print()
x=0
while x <= 20:
    print(x,end=" ")
    x+=1
print()
for x in range (10):
    if(x%2 == 0):
        print(2**x , end = " ")
    else:
        print("Odd", end= " ")




def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total+=1
    return total

print()

fun_list = [19,20,21,18,17]

print(count(fun_list))



prices = {
    "spag" : 4,
    "lasagna" : 5,
    "hamburger": 2
}

quantity = {
    "spag" : 6,
    "lasagna": 10,
    "hamburger" : 0
}

print("answer")
def totalPrice (prices , quantity):
    total = 0
    for i in quantity:
        total+= prices[i]*quantity[i]
    return total

print(totalPrice(prices,quantity))


import math as m
print(m.sqrt(4))
from math import sqrt as s #from math import *
print(s(49))


print(s(64))
help(s)

