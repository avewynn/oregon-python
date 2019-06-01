names = []
currentDay = 0
food = 0
oxen = 0
medicine = 0

def start():
    print("Welcome to Oregon Trail!")
    print("Please enter four names for your party!")
    while(len(names) != 4):
        print("Input a name:", end="")
        tempName = input()
        names.append(tempName)
    
    #loop until input
    print("Press enter to continue")
    input()
    market()
        
start()

def market():
    print("Market")
    