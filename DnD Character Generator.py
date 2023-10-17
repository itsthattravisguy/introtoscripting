import random


characterList = {}


print ("\n\n-- Welcome to Travis' Character Generator --")

# functions

def d(dieSize):
    result = random.randint(1,dieSize)
    return result

def roll(count, size, total=0,verbose=0):
    
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

def requestName(args=None):
    charName = str(input ("Enter a name for your character: \n\t"))
    return charName

def createPC(args=None):
    charName = requestName()
    if (charName == "Cancel"):
        pass
    elif charName in characterList:
        print(charName, " is already taken by another character. Try again!", sep="")
    else:
        characterList[charName] = PlayerCharacter(charName)
        characterList[charName].generateStats()
        characterList[charName].setRace()
        characterList[charName].setClass()
    

def listPCs(args=None):    
    if len(characterList) < 1:
        print("\tNo Characters exist!")
    else:
        print("Here is the list of created characters:\n\n\tName\t\tAncestory\tClass\n\t----\t\t---------\t-----")
        for x in characterList:
            print("\t",x,"\t\t",characterList[x].race,"\t\t",characterList[x].charClass,sep="")
        print("")
        
'''        
def listCommands(args=None):
    i = 0
    if len(commands) == 0:
        print("No commands exist. Travis is an idiot.")
    else:
        print("Here is the list of available commands:\n")

        while i < len(commands):
            print ("\t", commands[i])
            i += 1
'''

def listCommands(args=None):
    print("Here is the list of available commands:")
    for x in commands:
        print("\n\t", end="")
        print(*commands[x]["aliases"],sep=", ", end="")
        print("\n\t\t- ",commands[x]["description"])
              
commands = {
    "exit" : {
        "aliases" : ["exit", "close", "quit", "end"],
        "description" : "Closes the character generator.",
        "function" : exit
        },
    "help" : {
        "aliases" : ["help", "h", "commands"],
        "description" : "Displays help text and available commands",
        "function" : listCommands
        },
    "list" : {
        "aliases" : ["list", "pcs", "characters"],
        "description" : "Displays a list of created characters",
        "function" : listPCs
        },

#### Figuring out how to pass args better to this
#    "roll" : {
#        "aliases" : ["roll"],
#        "description" : "Rolls dice in the 1d6 format. The example command 'roll 1d6' would roll one six sided die.",
#        "function" : roll
#        },
    "createpc" : {
        "aliases" : ["1","create a pc", "make pc", "make pc", "make character", "make char"],
        "description" : "Starts the process of making a character.",
        "function" : createPC
        }    
    }

playerClasses = {
    "Warrior" : {
        "Key Ability Score" : "Strength",
        "Weapon" : "Great Sword",
        "Base HP" : 10,
        "HP per Level": "1d10",
        "Trained Skills" : ["Athletics"],
        "Speed" : 30
        },
    "Rogue" : {
        "Key Ability Score" : "Dexterity",
        "Weapon" : "Dagger",
        "Base HP" : 6,
        "HP per Level": "1d6",
        "Trained Skills" : ["Stealth"],
        "Speed" : 30
        },
    "Paladin" : {
        "Key Ability Score" : "Charisma",
        "Weapon" : "Long Sword",
        "Base HP" : 8,
        "HP per Level": "1d8",
        "Trained Skills" : ["Diplomacy"],
        "Speed" : 25
        },
    "Cleric" : {
        "Key Ability Score" : "Wisdom",
        "Weapon" : "Mace",
        "Base HP" : 8,
        "HP per Level": "1d6",
        "Trained Skills" : ["Religion"],
        "Speed" : 20
        },
    "Wizard" : {
        "Key Ability Score" : "Inteligence",
        "Weapon" : "Staff",
        "Base HP" : 4,
        "HP per Level": "1d6",
        "Trained Skills" : ["Arcana"],
        "Speed" : 20
        }
    }

playerWeapons = {
    "Great Sword" : {
        "Damage" : "1d12",
        "Damage Type" : "Slashing",
        },
    "Long Sword" : {
        "Damage" : "1d8",
        "Damage Type" : "Slashing",
        },
    "Dagger" : {
        "Damage" : "1d4",
        "Damage Type" : "Piercing",
        },
    "Mace" : {
        "Damage" : "1d8",
        "Damage Type" : "Bludgeoning",
        },
    "Fists" : {
        "Damage" : "1d4",
        "Damage Type" : "Bludgeoning",
        },
    "Bow" : {
        "Damage" : "1d6",
        "Damage Type" : "Piercing",
        },
    "Staff" : {
        "Damage" : "1d4",
        "Damage Type" : "Bludgeoning",
        }
    }
               
class PlayerCharacter:

    def __init__(self,name): 
        self.name = name
        self.stats = {}
        self.race = "None"


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
        else:
            print("Invalid stat method selected")
    
        self.printStats()
        reroll = str(input("Hit any key to continue."))
        if reroll == "reroll":
            print("Rerolling")
            self.generateStats()
            
                     

    def dieMethod3d6(self):
        print ("Rolling 3d6 for each stat:\n")
        self.stats["str"] = roll(3,6)
        self.stats["dex"] = roll(3,6)
        self.stats["con"] = roll(3,6)
        self.stats["int"] = roll(3,6)
        self.stats["wis"] = roll(3,6)
        self.stats["cha"] = roll(3,6)

    def dieMethod1d6plus8(self):
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

    def setRace(self):
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
        print("\n",self.name, " now has the following ancestory: ", self.race, "\n",sep="")
        self.printStats()

    def setTitle(self):
        pass
    
    def setClass(self):
        i = 1
        availableClasses = []
        print("\nPlease select one of the following classes:")     
        for x in playerClasses.keys():
            print("\t(",i,") ", x,sep="")
            availableClasses.append(x)
            i += 1
        self.charClass = str(input("\t-> "))
        if self.charClass.isnumeric():
            try:
                self.charClass = availableClasses[int(self.charClass)-1]
            except:
                print(self.charClass)
                print(availableClasses)
                print("\nNot a valid selection. Try again")
                self.setClass()
            else:
                print(self.name, " is now a ", self.charClass, "!", sep="") 
        else:  # Not a number, check the class list next
            if self.charClass in playerClasses.keys():
                print(self.name, " is now a ", self.charClass, "!", sep="")                   
            else:
                print("Thats not a valid character class, try again!")
                self.setClass()

def main():
    running = 1
    while running == 1:
        command = str(input ("\nEnter a command:\n"))
        args = None
        if command.find(" ") != -1:
            args = command[command.find(" "):]
            command = command[:command.find(" ")]
        command = command.casefold()
        print("")
        for x in commands:
            if command in commands[x]["aliases"]:
                commands[x]["function"](args)
                break
        else:
            print("Invalid command! (",command,")\n Try typing 'help' for a list of commands",sep="")

main()
