import random

charLevel = 1

print ("D&D Character Generator\n\n")

# You can choose a method to generate your character's ability scores:
# 3d6 or 8+1d6

class PlayerCharacter:
    stats = {
        "str" : "10",
        "dex" : "10",
        "con" : "10",
        "int" : "10",
        "wis" : "10",
        "cha" : "10"
    }

    def __init__(self, name, race, level, str, dex, con, int, wis, cha): 
        self.name = name
        self.race = race
        self.level = level
        self.stats["str"] = str
        self.stats["dex"] = dex
        self.stats["con"] = con
        self.stats["int"] = int
        self.stats["wis"] = wis
        self.stats["cha"] = cha

        


charName = str(input ("Enter a name for your character: \n\t"))

dieMethod = int(input("Enter 1 for using 3d6.\nEnter 2 for using 8 + 1d6\nThe choice is yours: "))
print ("")

if dieMethod == 1:
    print ("Rolling 3d6 for each stat:\n")
    statStr = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    statDex = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    statCon = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    statInt = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    statWis = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    statCha = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

if dieMethod == 2:
    print ("Rolling 8 + 1d6 for each stat:\n")
    statStr = random.randint(1,6) + 8
    statDex = random.randint(1,6) + 8
    statCon = random.randint(1,6) + 8
    statInt = random.randint(1,6) + 8
    statWis = random.randint(1,6) + 8
    statCha = random.randint(1,6) + 8

print(charName, "has the following ability scores:")
print("\tStrength: \t", statStr)
print("\tDexterity: \t", statDex)
print("\tConstitution: \t", statCon)
print("\tIntelligence: \t", statInt)
print("\tWisdom: \t", statWis)
print("\tCharisma: \t", statCha)

print("What ancestory would you like", charName, "to be?:\n\t(1) Elf\n\t(2) Human\n\t(3) Orc")
charRace = str(input("\t -> ") )


if ((charRace == "1") or (charRace == "Elf")):
    statStr += -2
    statDex += 2
    statCha += 2
    if charRace == "1":
        charRace = "Elf"
elif ((charRace == "2") or (charRace == "Human")):
    if charRace == "2":
        charRace = "Human"
elif ((charRace == "3") or (charRace == "Orc")):
    statStr += 2
    statCon += 2
    statInt -= 2
    charRace = "Orc"
    if charRace == "3":
        charRace = "Orc"
else:
    print("Not a valid input! Your race has been assigned to Human as a default.")


print(charName, "now has the following ancestory:", charRace, "\n", charName, "now has the following ability scores:")
print("\tStrength: \t", statStr)
print("\tDexterity: \t", statDex)
print("\tConstitution: \t", statCon)
print("\tIntelligence: \t", statInt)
print("\tWisdom: \t", statWis)
print("\tCharisma: \t", statCha)

