import random


characterList = {}

# commands
exitcommands = ["exit", "close", "quit", "end"]
helpcommands = ["help", "h"]
listpccommands = ["List","list","list pcs", "list characters"]
createPCcommands = ["1", "Create a PC", "make pc", "make character", "make char"]
commands = [exitcommands, helpcommands, listpccommands, createPCcommands, "roll"]



print ("\n\n-- Welcome to Travis' Character Generator --")

# functions

def d(dieSize):
    result = random.randint(1,dieSize)
    return result

def roll(count, size, total=0,verbose=0):

#    print("Rolling ", count, "d", size, "  - total = ",total, "  - verbose = ", verbose, sep="") #<-- Test Garbage
    i = 0
    result = 0
    rolls = []
    while i < count:
        rolls.append(d(size))
        if verbose == 1:
            print("\t - Rolled a ", rolls[i], " on a d", size, sep="")
        result += rolls[i]
        i += 1
    if total == 1:
        print ("\tYou rolled ", result," total.", sep="")
    return result 

def requestName():
    charName = str(input ("Enter a name for your character: \n\t"))
    return charName

def createPC():
    i = 0
    charName = requestName()
    while i == 0:
        if charName == "Cancel":
            break
        elif charName in characterList:
            print(charName, " is already taken by another character. Try again!", sep="")
        else:
            characterList[charName] = PlayerCharacter(charName)
            characterList[charName].generateStats()
            break
    

def listPCs():    
    if len(characterList) < 1:
        print("No Characters exist!")
    else:
        print("Here is the list of created characters:\n")
        for x in characterList:
            print("\t",x,sep="")
        print("")
        
def listCommands():
    i = 0
    if len(commands) == 0:
        print("No commands exist. Travis is an idiot.")
    else:
        print("Here is the list of available commands:\n")

        while i < len(commands):
            print ("\t", commands[i])
            i += 1



               
class PlayerCharacter:
#    stats = {
#        "str" : "10",
#        "dex" : "10",
#        "con" : "10",
#        "int" : "10",
#        "wis" : "10",
#        "cha" : "10"
#    }

    def __init__(self,name): 
        self.name = name
        self.stats = {}
#        self.race = race
#        self.level = level
#        self.stats["str"] = str
#        self.stats["dex"] = dex
#        self.stats["con"] = con
#        self.stats["int"] = int
#        self.stats["wis"] = wis
#        self.stats["cha"] = cha

    def generateStats(self):
        # select rolling method
        # You can choose a method to generate your character's ability scores:
        # 3d6 or 8+1d6
        
        dieMethod = int(input("Enter 1 for using 3d6.\nEnter 2 for using 8 + 1d6\nThe choice is yours: "))
        print ("")
        
        # roll your stats
        
        if dieMethod == 1:
            self.dieMethod3d6()

        elif dieMethod == 2:
            self.dieMethod1d6plus8()
    
        self.printStats()
        reroll = str(input

    def dieMethod3d6():
        print ("Rolling 3d6 for each stat:\n")
        self.stats["str"] = roll(3,6)
        self.stats["dex"] = roll(3,6)
        self.stats["con"] = roll(3,6)
        self.stats["int"] = roll(3,6)
        self.stats["wis"] = roll(3,6)
        self.stats["cha"] = roll(3,6)

    def dieMethod1d6plus8():
        print ("Rolling 8 + 1d6 for each stat:\n")
        self.stats["str"] = roll(1,6) + 8
        self.stats["dex"] = roll(1,6) + 8
        self.stats["con"] = roll(1,6) + 8
        self.stats["int"] = roll(1,6) + 8
        self.stats["wis"] = roll(1,6) + 8
        self.stats["cha"] = roll(1,6) + 8

            
    def printStats(self):
        print(self.name, "has the following ability scores:")
        print("\tStrength: \t", self.stats["str"])
        print("\tDexterity: \t", self.stats["dex"])
        print("\tConstitution: \t", self.stats["con"])
        print("\tIntelligence: \t", self.stats["int"])
        print("\tWisdom: \t", self.stats["wis"])
        print("\tCharisma: \t", self.stats["cha"])

    def setRace():
        i = 0
        while i < 1:
            print("What ancestory would you like", self.name, "to be?:\n\t(1) Elf\n\t(2) Human\n\t(3) Orc")
            charRace = str(input("\t -> ") )
            if ((charRace == "1") or (charRace == "Elf")):
                self.stats["str"] -= 2
                self.stats["dex"] += 2
                self.stats["cha"] += 2
                self.race = "Elf"
                i = 1
            elif ((charRace == "2") or (charRace == "Human")):
                self.race = "Human"
                i = 1
            elif ((charRace == "3") or (charRace == "Orc")):
                self.stats["str"] += 2
                self.stats["con"] += 2
                self.stats["int"] -= 2
                self.race = "Orc"
                i = 1
            else:
                print("That isnt in the list, try picking an ancestory again.")
        print(self.name, "now has the following ancestory:", self.race, "\n", printStats())

def main():
    running = 1
    while running == 1:
        command = str(input ("\nEnter a command:\n"))
        print("")
        if command in exitcommands:
            running = 0
        elif command in helpcommands:
            listCommands()
        elif command in listpccommands:
            listPCs()
        elif command in createPCcommands:
            createPC()
        elif command[:5] == "roll ":
            try:
                roll(int(command[5:command.find("d")]),int(command[command.find("d")+1:]),1,1)
            except:
                print("ERROR: Try using the format 'roll 1d6' to roll 1 die with 6 sides.")               
                
        elif command in commands:
            if command == "":
                print("incomplete logic")
            else:
                print("Error: WTF, Travis is dumb and this command isnt hooked up")
        else:
            print("Invalid command! (",command,")\n Try typing 'help' for a list of commands",sep="")

main()
