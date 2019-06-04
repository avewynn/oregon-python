from flask import Flask, render_template, request, json
from random import *
import os
app = Flask(__name__)

#global variables
inputs = "" #what user typed
output = [] #list of things to display, cleared once shown
started = False
name = ""
day = 0
food = 0
clothing = 0
medicine = 0
difficulty = 0
distance = 0
goal = 10
alive = True


def start():
    #global allows changing of global variables
    global name, difficulty
    
    myPrint("Welcome to the Oregon Trail!")
    
    #This gets name
    while(len(name) < 1):
        myPrint("Input a name")
        name = myInput()
    myPrint()
    #This gets difficulty
    myPrint("Enter a number between 1-3 for your difficulty level. 3 is the most challenging.")
    level = "0"
    while(not (level == "1" or level == "2" or level == "3")):
        level = myInput()
    
    difficulty = int(level)
    myPrint()
    #Moves to market phase
    market()
        

def market():
    global food, clothing, medicine
    
    myPrint("Welcome to the market! You'll need to stock up on materials before your trip.")
    myPrint("Each day you travel, you'll lose a random resource.")
    #Each difficulty gives a different amount of item choices
    choices = 0
    if difficulty == 1:
        choices = 9
    elif difficulty == 2:
        choices = 7
    elif difficulty == 3:
        choices = 5
    #After each choice, displays choices left and your updated inventory    
    while(choices > 0):
        myPrint()
        myPrint("Choices left: " + str(choices))
        myPrint("Press 1 for food, 2 for medicine, 3 for clothing")
        item = ""
        while(not (item == "1" or item == "2" or item == "3")):
            item = myInput()
        if item == "1":
            food += 1
        elif item == "2":
            medicine += 1
        else:
            clothing += 1
            
        choices -= 1
        myPrint()
        myPrint("Food:" + str(food) + " Medicine:" + str(medicine) + " Clothing:" + str(clothing))
    
    myPrint()
    myPrint("Thanks for your business! Good Luck!")
    myPrint()
    trail()
    
    
def trail():
    global day, food, medicine, clothing
    
    #Checks for alive
    if alive == False:
        end()
        
    #Checks for distance = goal
    elif distance == goal:
        victory()
        
    #If alive and not goal, day increase 
    else:
        day += 1
        if day != 1: #if not first day, will subtract a random resource
            x = randint(0, 2)
            if x == 0:
                food -= 1
            if x == 1:
                medicine -= 1
            if x == 2:
                clothing -= 1
    
        #displays the day, distance, and resources
        myPrint()
        myPrint("Day: " + str(day))
        myPrint("Distance Travelled: " + str(distance))
        myPrint("Distance Left: " + str(goal - distance))
        myPrint("Food:" + str(food) + " Medicine:" + str(medicine) + " Clothing:" + str(clothing))
        #if any resources below 0
        if(food < 0 or medicine < 0 or clothing < 0): 
            myPrint("You are ill! Gather some supplies soon!")
        
        #Options to choose
        myPrint("What will you do today, " + name + "?")
        myPrint()
        myPrint("1: HUNT")
        myPrint("2: SCAVENGE")
        myPrint("3: REST")
        myPrint("4: PRESS ON")
        
        #Checks for decision
        decision = ""
        while(not (decision == "1" or decision == "2" or decision == "3" or decision == "4")):
            decision = myInput()
        if decision == "1":
            hunt()
        elif decision == "2":
            scavenge()
        elif decision == "3":
            rest()
        else:
            pressOn()
        
#Depending on chance, a random event plays out  
def hunt():
    global food, medicine, day
    myPrint()
    
    x = randint(0, 4)
    if x == 0:
        myPrint("You bagged a buffalo! Food +3")
        food += 3
    elif x == 1:
        myPrint("You stepped on a snake, stupid! Now you're poisoned. Medicine -2")
        medicine -= 2
    elif x == 2:
        myPrint("You successfully snagged 2 young deer. Food +3")
        food += 3
    elif x == 3:
        myPrint("Your beef jerky fell out of your pocket. Food -1")
        food -= 1
    elif x == 4:
        badEvent()
    
    trail()
    
#Depending on chance, a random event plays out
def scavenge():
    global food, medicine, clothing, day
    myPrint()
    x = randint(0, 4)
    if x == 0:
        myPrint("You steal some shirts from a caravan. Clothing +2, thief.")
        clothing += 2
    elif x == 1:
        myPrint("Those berries were poisonous! Your shirt was ruined as well. Medicine -1, Clothing -1")
        medicine -= 1
        clothing -= 1
    elif x == 2:
        myPrint("An abandoned house! Clothing +3")
        clothing += 3
    elif x == 3:
        myPrint("You stumble upon the corpse of a travelling medic. You leave an apple by his feet. Medicine +2, Food -1")
        medicine += 2
        food -= 1
    elif x == 4:
        badEvent()
    
    trail()
    
#Depending on chance, a random event plays out
def rest():
    global food, medicine, clothing, day
    myPrint()
    
    x = randint(0, 4)
    if x == 0:
        myPrint("You see a deserted beehive above you, and take the honey. Medicine +2")
        medicine += 2
    elif x == 1:
        myPrint("A wolf is attracted by your campfire. He had rabies. Medicine -2")
        medicine -= 2
    elif x == 2:
        myPrint("You decide to imbibe on the sap of a small tree. Disgusting, but rejuvenating. Medicine +3, Food -1")
        medicine += 3
        food -= 1
    elif x == 3:
        myPrint("You fight a feral raccoon. Clothing -1, Food +2")
        clothing -= 1
        food += 2
    elif x == 4:
        badEvent()
        
    trail()
    
#player moves forward unless bad event
def pressOn():
    global distance, day
    myPrint()
    
    x = randint(0, 2)
    if x == 0:
        myPrint("Another day, another mile...")
        distance += 1
    if x == 1:
        badEvent()
        if alive == True:
            distance += 1
    if x == 2:
        badEvent()
        if alive == True:
            distance += 1
    if x == 3:
        badEvent()
        if alive == True:
            distance += 1
    if x == 4:
        bazaar()
        if alive == True:
            distance += 1
    trail()
        
#Random chance of triggering
def badEvent():
    global food, medicine, clothing, day, alive
    myPrint()
    
    x = randint(0, 5)
    if x == 0:
        if food < 0:
            myPrint("You die of starvation. Why didn't you buy more food?")
            alive = False
        else:
            myPrint("A traveller offers you a juicy steak. It gives you food poisoning! Food -2")
            food -= 2
    if x == 1:
        if medicine < 0:
            myPrint("Sickness overcomes you; your last memory is of the town medic as you pass. Why didn't you buy more medicine?")
            alive = False
        else:
            myPrint("A scorpion sneaks into your sleeping bag. Medicine -2")
            medicine -= 2
    if x == 2:
        if clothing < 0:
            myPrint("You fall unconscious from frostbite. You don't wake up. Why didn't you buy more clothing?")
            alive = False
        else:
            myPrint("You fall into a river. Clothing -2")
            clothing -= 2
    if x == 3:
        bandits()
    if x == 4: 
        myPrint("It's your lucky day! A wealthy traveller hands you a care package. Food +1, Medicine +1, Clothing +1")
        food += 1
        medicine += 1
        clothing += 1
    if x == 5:
        myPrint("You die of dysentery. That's the Oregon Trail!")
        alive = False
    
#Bandits! Decision making time    
def bandits():
        global food, medicine, clothing, alive
        
        myPrint("Bandits! If you give them your food, they'll let you live. What do you do?")
        myPrint("1: GIVE THEM YOUR FOOD")
        myPrint("2: GIVE THEM YOUR MEDICINE INSTEAD")
        myPrint("3: GIVE THEM YOUR CLOTHING INSTEAD")
        myPrint("4: REFUSE")
        
        #Checks for decision
        decision = ""
        while(not (decision == "1" or decision == "2" or decision == "3" or decision == "4")):
            decision = myInput()
        if decision == "1" and food > 0:
            myPrint("The bandits leave with all of your food. Food = 0")
            food = 0
        elif decision == "1" and food <= 0:
            myPrint("You don't even have any food. The bandits shoot you. You are dead!")
            alive = False
        elif decision == "2" and medicine > 0:
            myPrint("The leader of the bandits thanks you; his son has a severe case of dysentery.")
            myPrint("He gives you some food and clothes in return. Food +1, Medicine = 0, Clothing +1")
            food += 1
            medicine = 0
            clothing += 1
        elif decision == "2" and medicine <= 0:
            myPrint("You don't even have any medicine. The bandits shoot you. You are dead!")
            alive = False
        elif decision == "3":
            myPrint("The bandits don't want your filthy clothes. You are dead!")
            alive = False
        else:
            if randint(0, 1) == 0:
                myPrint("What are you, stupid? The bandits shoot you. You are dead!")
                alive = False
            else:
                myPrint("Your forceful tone of voice intimidates the bandit leader into leaving you alone.")
                myPrint("You continue on.")
                
#Another series of choices, this time less deadly (usually)           
def bazaar():
    
    myPrint("The Bazaar! Stock up on supplies, loot the wealthy, have a brawl... The Bazaar has it all!")
    myPrint("What will you do, " + name + "?")
    myPrint("1: BUY SUPPLIES")
    myPrint("2: STEAL")
    myPrint("3: BRAWL")
    
    decision = ""
    while(not (decision == "1" or decision == "2" or decision == "3")):
        decision = myInput()
        
    if decision == "1":
        buy()
    if decision == "2":
        steal()
    if decision == "3":
        brawl()
    myPrint("Hope you enjoyed your time at The Bazaar!")
    
def buy():
    global food, medicine, clothing
    
    myPrint("Welcome to the shop! Buy some supplies for the road.")
    choices = 2
    while(choices > 0):
            myPrint()
            myPrint("Choices left: " + str(choices))
            myPrint("Press 1 for food, 2 for medicine, 3 for clothing")
            item = ""
            while(not (item == "1" or item == "2" or item == "3")):
                item = myInput()
            if item == "1":
                food += 1
            elif item == "2":
                medicine += 1
            else:
                clothing += 1
            
            choices -= 1
            myPrint()
            myPrint("Food:" + str(food) + " Medicine:" + str(medicine) + " Clothing:" + str(clothing))
    
    myPrint()
    myPrint("Thanks for your business! Good Luck!")
    
    
def steal():
    global food, medicine, clothing
    
    myPrint("You attempt to burgle the nearest merchant stand.")
    p = randint(0, 2)
    if p == 0:
        myPrint("Success! You steal 3 food from a wealthy merchant.")
        food += 3
    if p == 1:
        myPrint("You snatch some potions from a medic, but he grabs your tunic in the process. Medicine +2, Clothing -1")
        medicine += 2
        clothing -= 1
    if p == 2:
        myPrint("Massive failure! You're beaten to a bloody pulp. Food -2, Medicine -2, Clothing -2")
        food -= 2
        medicine -= 2
        clothing -= 2
        
def brawl():
    global food, medicine, clothing, alive
    
    myPrint("Welcome to the arena, challenger! Battle for glory and honor (as well as supplies)!")
    b = randint(0, 2)
    if b == 0:
        myPrint("You face a scrawny child. You give him a light beating. You win! Food +2, Medicine +2, Clothing +2")
        food += 2
        medicine += 2
        clothing += 2
    if b == 1:
        myPrint("You face an average-looking teenage boy. The announcer calls a tie after 10 minutes of noodly slaps and punches. You gain nothing.")
    if b == 2:
        myPrint("You face a seasoned gladiator. The announcer declares trial by spear. You are dead!")
        alive == False

#If dead  
def end():
    myPrint()
    myPrint("It was a valiant effort, " + name)
    exit()
    
#If goal reached
def victory():
    myPrint()
    myPrint("You made it to Oregon, " + name + "!")
    myPrint("It took you " + str(day) + " days.")
    exit()
    
#main    
if __name__ == "__main__":
    start()

#starts story if not already started
def begin():
    global started
    if started == False:
        started = True
        start()

#waits until the user inputs (based on python input())
def myInput():
    global inputs
    while(inputs == ""):
        1 #does literally nothing
        
    temp = inputs
    #clear inputs for next myInput()
    inputs = ""
    return temp

#adds everything that should be printed to list
def myPrint(*toPrint):
    if len(toPrint) == 0: #no arguments
        output.append("")
    for x in toPrint:
        output.append(x)


#homepage - this is where I want the game to go
@app.route("/", methods=['GET', 'POST']) #handles traffic
def homePage():
    #resets global variables in case refresh page
    global inputs, output_buffer, started, name, day, food, clothing, medicine, difficulty, distance, goal, alive
    inputs = ""
    output = []
    started = False
    name = ""
    day = 0
    food = 0
    clothing = 0
    medicine = 0
    difficulty = 0
    distance = 0
    goal = 10
    alive = True
    #index.html is homepage
    return render_template("index.html")

#Receives and outputs data
@app.route("/server", methods=['GET', 'POST'])
def server():
    global inputs, output
    begin()
    #Request is the state of the user, sending or receiving
    if request.method == 'POST':
        #reads the text of the inputbox
        inputs = request.form['inp']
        #has to return something
        return "Success! You did it."
    
    #get request
    else:
        #output is the text to print
        tempOutput = output
        output = []
            #dumps output into json format, sends to site for later display
        return json.dumps({'output': tempOutput})

#main
if __name__ == "__main__":
    app.run(debug=True)