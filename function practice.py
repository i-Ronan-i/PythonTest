""" Short piece of code just to try moving between functions
and illustrates inputs, low level list manipulation for position 
and multiple loops with boolean triggers. """
dead = False
m = 0 
xy = [0,0]

def func1():
    """docstring - lets make this do something basic 
    and pass it  onto the next function"""
    global m  
    command = input("Which direction do you want to go? (N, W, S, E)  ").upper()
    if command == "N":
        m += 1
        movefunc(command, xy)
    elif command == "W":
        movefunc(command, xy)
    elif command == "S":
        movefunc(command, xy)
    elif command == "E":
        movefunc(command, xy)
    else :
        print("Invalid command!")
        func1()

def movefunc(command, xy):
    print("You moved " + command)
    if command == "N":
        xy[1] +=1
    elif command == "W":
        xy[0] -= 1
    elif command == "S":
        xy[1] -=1
    elif command == "E":
        xy[0] += 1

def randbot(dead):
    inv = True
    while inv == True:
        botans = input("A random bot approaches you and asks for your help. \nIt's leaking black fluid. \nWill you help? (Y/N) ").upper()
        if botans == "Y":
            inv = False
            print("Duct tape removed from inventory")
            death(dead)
        elif botans == "N":
            inv = False
            print("The bot fries your brain and steals your duct tape.")
            dead = True
            death(dead)
        else :
            print("Invalid command!")
            inv = True

def death(dead):
    if dead == True:
        print("game over bro")
    else:
        print("you win bro")


#Code start#
while m < 4:
    func1()
    print("Position is " + str(xy))
else :
        randbot(dead)

input("Press any key...")
