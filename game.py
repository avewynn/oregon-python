from random import *
import webbrowser
name = ""
day = 0
food = 0
clothing = 0
medicine = 0
difficulty = 0
distance = 0
goal = 5
alive = True


def start():
    #global allows changing of global variables
    global name, difficulty
    
    print("Welcome to the Oregon Trail!")
    
    #This gets name
    while(len(name) < 1):
        print("Input a name")
        name = input()
    #This gets difficulty
    print("Enter a number between 1-3 for your difficulty level. 3 is the most challenging.")
    level = "0"
    while(not (level == "1" or level == "2" or level == "3")):
        level = input()
    
    difficulty = int(level)
    #Moves to market phase
    market()
        

def market():
    global food, clothing, medicine
    
    print("Welcome to the market! You'll need to stock up on materials before your trip.")
    print("Each day you travel, you'll lose a random resource.")
    #Each difficulty gives a different amount of item choices
    choices = 0
    if difficulty == 1:
        choices = 12
    elif difficulty == 2:
        choices = 9
    elif difficulty == 3:
        choices = 6
    #After each choice, displays choices left and your updated inventory    
    while(choices > 0):
        print()
        print("Choices left: " + str(choices))
        print("Press 1 for food, 2 for medicine, 3 for clothing")
        item = ""
        while(not (item == "1" or item == "2" or item == "3")):
            item = input()
        if item == "1":
            food += 1
        elif item == "2":
            medicine += 1
        else:
            clothing += 1
            
        choices -= 1
        print()
        print("Food: " + str(food) + " Medicine: " + str(medicine) + " Clothing: " + str(clothing))
    
    print()
    print("Thanks for your business! Good Luck!")
    print()
    trail()
    
    
def trail():
    global day, food, medicine, clothing
    
    if alive == False:
        end()
    
    elif distance == goal:
        victory()
        
    else:
        day += 1
        if day != 1:
            x = randint(0, 2)
            if x == 0:
                food -= 1
            if x == 1:
                medicine -= 1
            if x == 2:
                clothing -= 1
    
         
        print()
        print("Day: " + str(day))
        print("Distance Travelled: " + str(distance))
        print("Distance Left: " + str(goal - distance))
        print("Food: " + str(food) + " Medicine: " + str(medicine) + " Clothing: " + str(clothing))
        
        print("What will you do today, " + name + "?")
        print()
        print("1: HUNT")
        print("2: SCAVENGE")
        print("3: REST")
        print("4: PRESS ON")
    
        decision = ""
        while(not (decision == "1" or decision == "2" or decision == "3" or decision == "4")):
            decision = input()
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
    print()
    
    x = randint(0, 4)
    if x == 0:
        print("You bagged a buffalo! Food +3")
        food += 3
    elif x == 1:
        print("You stepped on a snake, stupid! Now you're poisoned. Medicine -2")
        medicine -= 2
    elif x == 2:
        print("You successfully snagged 2 young deer. Food +3")
        food += 3
    elif x == 3:
        print("Your beef jerky fell out of your pocket. Food -1")
        food -= 1
    elif x == 4:
        badEvent()
    
    trail()
    
#Depending on chance, a random event plays out
def scavenge():
    global food, medicine, clothing, day
    print()
    x = randint(0, 4)
    if x == 0:
        print("You steal a shirt from a caravan. Clothing +1, thief.")
        clothing += 1
    elif x == 1:
        print("Those berries were poisonous! Your clothing was ruined as well. Medicine -1, Clothing -2")
        medicine -= 1
        clothing -= 2
    elif x == 2:
        print("An abandoned house! Clothing +2, Food +1.")
        clothing += 2
        food += 1
    elif x == 3:
        print("You stumble upon the corpse of a travelling medic. You leave an apple by his feet. Medicine +2, Food -1")
        medicine += 2
        food -= 1
    elif x == 4:
        badEvent()
    
        
    trail()
    
#Depending on chance, a random event plays out
def rest():
    global food, medicine, clothing, day
    print()
    
    x = randint(0, 4)
    if x == 0:
        print("A raccoon is attracted by your campfire. Good eats. Food +1, Clothing +1")
        food += 1
        clothing += 1
    elif x == 1:
        print("A wolf is attracted by your campfire. He had rabies. Medicine -2")
        medicine -= 2
    elif x == 2:
        print("You decide to imbibe on the sap of a small tree. Disgusting, but rejuvenating. Medicine ")
        medicine -= 1
    elif x == 3:
        print("You fight a jackrabbit for some herbs. Medicine +2, Clothing -1")
        medicine += 2
        clothing -= 1
    elif x == 4:
        badEvent()
        
    trail()
    
#50/50 chance of something bad happening, player moves forward regardless
def pressOn():
    global distance, day
    print()
    
    if randint(0, 1) == 0:
        print("Another day, another mile...")
        distance += 1
    else:
        badEvent()
        if alive == True:
            distance += 1
        
    trail()
        
#Random chance of triggering
def badEvent():
    global food, medicine, clothing, day, alive
    print()
    
    x = randint(0, 5)
    if x == 0:
        if food <= 0:
            print("You die of starvation. Why didn't you buy more food?")
            alive = False
        else:
            print("A traveller offers you a juicy steak. It gives you food poisoning! Food -2")
            food -= 2
    if x == 1:
        if medicine <= 0:
            print("Sickness overcomes you; your last memory is of the town medic as you pass. Why didn't you buy more medicine?")
            alive = False
        else:
            print("A scorpion sneaks into your sleeping bag. Medicine -2")
            medicine -= 2
    if x == 2:
        if clothing <= 0:
            print("You fall unconscious from frostbite. You don't wake up. Why didn't you buy more clothing?")
            alive = False
        else:
            print("You fall into a river. Clothing -2")
            clothing -= 2
    if x == 3:
        bandits()
    if x == 4: 
        print("It's your lucky day! A wealthy traveller hands you a care package. Food +2, Medicine +2, Clothing +2")
        food += 2
        medicine += 2
        clothing += 2
    if x == 5:
        print("You die of dysentery. That's the Oregon Trail!")
        alive = False
    
#Bandits! Decision making time    
def bandits():
        global food, medicine, clothing, alive
        
        print("Bandits! If you give them your food, they'll let you live. What do you do?")
        print("1: GIVE THEM YOUR FOOD")
        print("2: GIVE THEM YOUR MEDICINE INSTEAD")
        print("3: GIVE THEM YOUR CLOTHING INSTEAD")
        print("4: REFUSE")
        decision = ""
        while(not (decision == "1" or decision == "2" or decision == "3" or decision == "4")):
            decision = input()
        if decision == "1" and food > 0:
            print("The bandits leave with all of your food. Food = 0")
            food = 0
        elif decision == "1" and food <= 0:
            print("You don't even have any food. The bandits shoot you. You are dead!")
            alive = False
        elif decision == "2" and medicine > 0:
            print("The leader of the bandits thanks you; his son has a severe case of dysentery.")
            print("He gives you some food and clothes in return. Food +1, Medicine = 0, Clothing +1")
            food += 1
            medicine = 0
            clothing += 1
        elif decision == "2" and medicine <= 0:
            print("You don't even have any medicine. The bandits shoot you. You are dead!")
            alive = False
        elif decision == "3":
            print("The bandits don't want your filthy clothes. You are dead!")
            alive = False
        else:
            if randint(0, 1) == 0:
                print("What are you, stupid? The bandits shoot you. You are dead!")
                alive = False
            else:
                print("Your forceful tone of voice intimidates the bandit leader into leaving you alone.")
                print("You continue on.")
#If dead  
def end():
    print("It was a valiant effort, " + name)
    
#If goal reached
def victory():
    print("You made it to Oregon, " + name + "!")
    print("It took you " + str(days))
    print()
    
#main    
if __name__ == "__main__":
    start()