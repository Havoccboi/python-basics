def simple():
    print("Hello")

def plus_ten(a):
    return a+10



def plus_ten_scnd(a):
    result = a+ 10
    print(plus_ten(result))
    return result

def multiple_param(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)
    return a+b+c


def add_ten(a):
    if a >= 100:
        return a+10
    else:
        return "Save more Nigga"

def main():
    simple()
    print(plus_ten(5))
    print(plus_ten_scnd(8))
    print(add_ten(90))
    print(multiple_param(1,2,3))
    print(type(add_ten(18)))
    print("max:",max(1,2,3))
    print("min:",min(1,2,3))
    print("z", -19 ,"abs", abs(-19))
    my_list = [1,2,2,3]
    print(sum(my_list))
    print(round(2.3345,2))
    print(pow(2,10))
    print(len("HowManyCharactersHere"))
    participants = ["Rizvee", "Kashim" , "Tamanna", "Niloy"]
    print(participants[2])
    print(participants[-1],participants[-2])
    participants[1] = "Voghchod"
    print(participants[1])
    del participants[1]
    print(participants)
    participants.append("New Member")
    print(participants)
    participants.extend(["new_member","Club guy lol"])
    print(participants)
    participants.append(["Gregor", "Clegane"])
    print(participants)
    print(len(participants))
    print(participants[1:3]) #starting_index : ending(not inclusive)
    print(participants.index("Niloy"))
    newcomers = ["Joshua" , "Britney"]
    big = [participants, newcomers]

    big.sort(reverse = True)
    print(big)
    newcomers.sort(reverse = True)
    print(newcomers)
    newcomers.sort()
    print(newcomers)
    numbers= [1,5,4,2]
    numbers.sort()
    print(numbers)
    numbers.sort(reverse = True)
    print(numbers)
    
    #tuples are constant list cannot be modified shows as () paranthesis rather than [] brackets

    y= 10,22,"ccc"
    print(y)
    print(y[2])
    x = 11,23
    tuple_list= [x,y]
    print(tuple_list)

    age,school = "30,BSNMPC".split(",")
    print(age,school)
    print(tuple_return(2))


def tuple_return(a):
    area = a**2
    perimeter = 4*a
    tup = area,perimeter
    return tup

main()
