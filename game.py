from random import *
name = ""
day = 1
food = 0
clothing = 0
medicine = 0
difficulty = 0
distance = 0
goal = 5
alive = True


def start():
    global name
    print("Welcome to the Oregon Trail!")
    
    #gets name
    while(len(name) < 1):
        print("Input a name")
        name = input()
    
    print("Enter a number between 1-3")
    print("Difficulty level:")
    level = "0"
    while(not (level == "1" or level == "2" or level == "3")):
        level = input()
    
    global difficulty
    difficulty = int(level)
    
    #loop until input
    print("Press enter to continue.")
    input()
    market()
        

def market():
    global food, clothing, medicine
    print("Welcome to the market! You'll need to stock up on materials before your trip.")
    choices = 0
    print(difficulty)
    if difficulty == 1:
        choices = 10
    elif difficulty == 2:
        choices = 7
    elif difficulty == 3:
        choices = 5
        
    while(choices > 0):
        print()
        print("Choices: " + str(choices))
        print("Press 1 for food, 2 for clothing, 3 for medicine")
        item = ""
        while(not (item == "1" or item == "2" or item == "3")):
            item = input()
        if item == "1":
            food += 1
        elif item == "2":
            clothing += 1
        else:
            medicine += 1
            
        choices -= 1
        print("Food: " + str(food))
        print("Clothing: " + str(clothing))
        print("Medicine: " + str(medicine))
    
    print()
    print("Thanks for your business! Good Luck!")
    print()
    trail()
    
    
def trail():
    print("Day: " + str(day))
    if alive == False:
        end()
    else:
        print("What will you do today, traveller?")
        print("HUNT")
        print("SCAVENGE")
        print("REST")
        print("PRESS ON")
    
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
        
        
def hunt():
    global food, medicine, day
    x = randint(0, 4)
    if x == 0:
        print("You bagged a buffalo! Food +2")
        food += 2
    elif x == 1:
        badEvent()
    elif x == 2:
        print("You stepped on a snake, stupid! Now you're poisoned. Medicine -2")
        medicine -= 2
    elif x == 3:
        print("You whiffed your shot. Food -1")
        food -= 1
    else:
        print("You successfully snagged 2 young deer. Food +2")
        food += 2
    
    day += 1
    trail()
    

def scavenge():
    global food, medicine, clothing, day
    x = randint(0, 4)
    if x == 0:
        print("Tasty berries! Food +1")
        food += 1
    elif x == 1:
        print("Tasty berries were poisonous! Your clothing was ruined as well. Medicine -1, Clothing -2")
        medicine -= 1
        clothing -= 2
    elif x == 2:
        print("An abandoned house! Clothing +1, Medicine +1, thief.")
        clothing += 1
        medicine += 1
    elif x == 3:
        badEvent()
    else:
        print("You stumble upon the corpse of a travelling medic. Medicine +2")
        medicine += 2
        
    day += 1
    trail()
    

def rest():
    global food, medicine, clothing, day
    x = randint(0, 4)
    if x == 0:
        print("A raccoon is attracted by your campfire. Good eats. Food +1")
        food += 1
    elif x == 1:
        print("A wolf is attracted by your campfire. He had rabies. Medicine -2")
        medicine -= 2
    elif x == 2:
        print("You decide to imbibe on the sap of a small tree. Medicine -1")
        medicine -= 1
    elif x == 3:
        print("You fight a jackrabbit for some herbs. Medicine +2, Clothing - 1")
        medicine += 2
        clothing -= 1
    else:
        badEvent()
        
    day += 1
    trail()
    

def pressOn():
    if randint(0, 1) == 0:
        print("Another day, another mile...")
        trail()
    else:
        badEvent()
    
    day += 1
    trail()
        

def badEvent():
    global food, medicine, clothing, day
    x = randint(0, 4)
    if x == 0:
        if food <= 0:
            print("You starve to death. Why didn't you buy more food?")
            alive = False
        else:
            print("A traveller offers you a granola bar. Thanks! Food +0")
    if x == 1:
        if medicine <= 0:
            print("Your last memory is of the town medic as you pass. Why didn't you buy more medicine?")
            alive = False
        else:
            print("A scorpion sneaks into your sleeping bag. Medicine -2")
            medicine -= 2
    if x == 2:
        if clothing <= 0:
            print("You fall unconscious from frostbite. You don't wake up. Why didn't you buy more clothes?")
            alive = False
        else:
            print("You fall into a river, but catch a fish on the way. Nice! Clothing -2, Food +1")
            clothing -= 2
            food += 1
    if x == 3:
            print("A grizzly bear smells your desperation a mile away. You are dead.")
            alive = False
    if x == 4:
        print("You die of dysentery. That's the Oregon Trail!")
        alive = False
    
    
def end():
    print("It was a valiant effort, " + name)
    
    
if __name__ == "__main__":
    start()