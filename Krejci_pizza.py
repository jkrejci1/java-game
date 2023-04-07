#Jack Krejci


import random

#Welcome message
print("*" * 70)
print("*%s*" % "PIZZA QUEST".center(68))
print("*" * 70)
print()

#Function

#Function to load in a map given by user
#Function also assigns random health penalties to each room from 0-25
def load_map(fname):
    fvar = open(fname,"r")
    mapping = {}
    for line in fvar:
        line = line.strip()
        if line != "":
            parts = line.split("\t")
            room = parts[0]
            n = parts[1]
            s = parts[2]
            e = parts[3]
            w = parts[4]
            bee_sting = random.randint(0,25)
            mapping[room] = {"N":n,"S":s,"E":e,"W":w,"Penalty":bee_sting}
    fvar.close()
    return mapping

#Function used to give user help
def ask_for_help(north,south,east,west,health):
    #Account for if the player asks for help
    #Translate the -'s to "nothing" when there is a wall
    if north == "-":
        north = "nothing"
    if south == "-":
        south = "nothing"
    if east == "-":
        east = "nothing"
    if west == "-":
        west = "nothing"
    print("%s has %s to the north, %s to the south, %s to the east, and %s to the west" %(location,north,south,east,west))

    

#Main Code
#Open your map

#Initialize play_again to "y" to run the loop that starts the game
play_again = "y"
while play_again == "y":
    fname = input("Enter name of map file: ")
    mapping = load_map(fname)
    
    #Assign bear and pizza to a room but first create list of your rooms to randomize
    list_of_rooms = list(mapping.keys())
        
                   
    #Assign the pizza to a room
    pizza = random.choice(list_of_rooms)
    

    #Assign the bear to a room
    location = random.choice(list_of_rooms)

    #Use in order to know what's to the north/south/east/west and the health damage of each room    
    north = mapping[location]["N"]
    south = mapping[location]["S"]
    east = mapping[location]["E"]
    west = mapping[location]["W"]
    health_loss = mapping[location]["Penalty"]

    #Make sure the bear isn't in/next to the pizza's room
    while north == pizza or south == pizza or east == pizza or west == pizza or location == pizza:
        location = random.choice(list_of_rooms)
        north = mapping[location]["N"]
        south = mapping[location]["S"]
        east = mapping[location]["E"]
        west = mapping[location]["W"]
        health_loss = mapping[location]["Penalty"]
        
        
    #Tell the player where they are
    health = 100

    #While loop that runs until the player finds the pizza
    while location != pizza:
        print("You are now in %s. Your health is %d." % (location,health))
        choice = input("Enter a direction (N, S, E, W) or H for help: ").upper().strip()
        
        #Account for if the player doesn't enter the correct key
        while choice != "N" and choice != "S" and choice != "E" and choice != "W" and choice != "H":
            choice = input("That wasn't a correct choice! Enter a direction (N, S, E, W) or H for help: ").upper().strip()

        #Account for if the player asks for help
        if choice == "H":
            help_me = ask_for_help(north,south,east,west,health)
            health -= 10
            print("That advice just cost you 10 health points.")
                 
        #Account for if the player moves into a wall     
        elif mapping[location][choice] == "-": #Was originally elif!!!!!!!!!!
            print("You can't move in that direction.")
            health -= health_loss
            print("You lost %d health points." % health_loss)

        #Notify the player when they've won
        elif mapping[location][choice] == pizza:
            print("you found the pizza with %s health points to spare." % health)
            print("Enjoy!")
            print()
            break
            
        #Account for when a player moves into another room
        else:
            location = mapping[location][choice]
            health_loss = mapping[location]["Penalty"]
            health -= health_loss
            print("You have moved into room %s." % location)
            print("You have lost %d health points." % health_loss)

        #Notify the player when they've lost
        if health <= 0:
            print("You ran out of health!")
            print("RIP Mr. Bear")
            print()
            break
    
    #Ask the player if he wants to play again 
    play_again = input("Do you want to play again (y or n)? ").lower().strip()
    
    #Account for if the user enters the wrong key
    while play_again != "y" and play_again != "n":
        play_again = input("What was that? Do you want to play again (y or n)? ").lower().strip()
        
    print()

#Goodbye message
print("*" * 70)
print("*%s*" % "THANKS FOR PLAYING PIZZA QUEST".center(68))
print("*" * 70)


        
    
    
    

        




