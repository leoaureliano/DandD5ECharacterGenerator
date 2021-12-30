#Ok I will try to start (again) a new D&D project today is 28/12/2021#
import random
#If the user did not set the parameters all will run rondoly
Parameters = input("Set the parameters Y/N")

#Creating the atributes#
STR = 0
DEX = 0
CON = 0
INT = 0
WIS = 0
CHA = 0
ASI = 0


#Others 
Size = 0
Speed = 0


#Languages
Language = [1]

#D&D Races#
R = ["Aarakocra", "Aasimar", "Bugbear", "Centaur","Changeling","Dragonborn","Dwarf","Elf"]
Race = R
#libraryes of Subraces and Types#

AasimarSubRace = ["Fallen", "Protector", "Scourge", "Variant"]
DragonbornSubRace = ["Draconblood", "Ravenite"]
DragonbornSubType = ["Black", "Blue", "Brass", "Broze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
DwarfSubRace = ["Gray(Duergar)", "Hill", "Mark of Warding", "Mountain"]
ElfSubRace = ["Aereni High", "Aereni Wood", "Drow", "Eladrin", "Eladrin(Variant)", "High", "Mark of Shadow", "Sea Elf", "Shadar Kai", "Valenar High", "Valenar Wood", "Wood"]

#Fist we select the gener#
Sex = ["Male", "Famale"]

if Parameters == "Y" or Parameters == "y":
    print("0 - Randon")
    print("1 - Male")
    print("2 - Famale")
    Sex = input("Sex?")

    if Sex == "0":
        Sex = random.choice(Sex)

    elif Sex == "1":
        print("Male")

    elif Sex == "2":
        print("Famale")

    elif Sex == "3":
        print("Ohh,You discovered a new gener")
        NSex = input("Write pleace")
        NSex = Sex
        print("Nice") 
    else:
        print("Please come back to school")
#Race and subrace type#

if Parameters == "Y" or Parameters == "y":        
    print("0 - Random")
    print("1 - Aarakocra")
    print("2 - Aasimar")
    print("3 - Bugbear")
    print("4 - Centaur")
    print("5 - Changeling")
    print("6 - Dragonborn")
    print("7 - Dwarf")
    print("8 - Elf")
    print("9 - Fairy")
    Race = int(input("Race?"))

    if Race == 1:
        Race = "Aarakroca"
        DEX +=2
        WIS +=1
        print("Aarakroca selected")

    if Race == 2:
        Race = "Aasimar"
        print("Aasimar selected, select the subrace number")
        while True:
            subrace = int(input("1- Fallen, 2- Protector, 3- Scourge or 4-Variant"))
            if subrace == 1:
                subrace and AasimarSubRace == "Fallen"
                CHA +=2
                SRT +=1
                print("Fallen")
                break
            
            if subrace == 2:
                subrace and AasimarSubRace == "Protector"
                CHA +=2
                WIS +=1
                print("Protector")
                break
            
            if subrace == 3:
                subrace and AasimarSubRace == "Scourge"
                CHA +=2
                CON +=1
                print("Scourge")
                break
            
            if subrace == 4:
                subrace and AasimarSubRace == "Variant"
                CHA +=2
                WIS +=1
                print("Variant")
                break

                print("You have made an invalid choice, try again.")                   
            
    elif Race == 3:
        Race = "Bugbear"
        STR +=2
        DES +=1
        print(" Bugbear selected")

    elif Race == 4:
        Race = "Centaur"
        STR +=2
        WIS +=1
        print("Centaur selected")

    elif Race == 5:
        Race = "Changeling"
        CHA +=2
        ASI +=1
        print("Changeling selected")
    
    elif Race == 6:
        Race = "Dragonborn"
        print("Dragonborn selected, select the subrace and type")
        while True:
            subraceType = int(input("1- Draconblood or 2- Ravenite"))
            if subraceType == 1:
                subraceType == "Draconblood"
                INT +=2
                CHA +=1
                print("Draconblood")
                break

            elif subraceType == 2:
                subraceType == "Revenite"
                STR +=2
                CON +=1
                print("Ravenite")
                break

#dragonborn have two different model and have a dragon type which I slash in two#
        while True:
            subrace = int(input("1- Black, 2- Blue, 3- Brass, 4- Bronze, 5- Copper, 6- Gold, 7- Green, 8- Red, 9- Silver, 10- White"))
            if subrace == 1:
                subrace == "Black"
                print("Black")
                break

            if subrace == 2:
                subrace == "Blue"
                print("Blue")
                break
            
            if subrace == 3:
                subrace == "Brass"
                print("Brass")
                break

            if subrace == 4:
                subrace == "Bronze"
                print("Bronze")
                break

            if subrace == 5:
                subrace == "Copper"
                print("Copper")
                break

            if subrace == 6:
                subrace == "Gold"
                print("Gold")
                break

            if subrace == 7:
                subrace == "Green"
                print("Green")
                break

            if subrace == 8:
                subrace == "Red"
                print("Red")
                break

            if subrace == 9:
                subrace == "Silver"
                print("Silver")
                break

            if subrace == 10:
                subrace == "White"
                print("White")
                break
            
    if Race == 7:
        Race = "Dwarf"
        print("Dwarf selected")

        while True:
            subrace = int(input("1- Gray(Duergar) 2- Hill 3- Mark of Warding 4- Mountain"))

            if subrace == 1:
                subrace = "Gray(Duergar)"
                CON +=2
                STR +=1
                print(subrace)
                break
            
            if subrace == 2:
                subrace = "Hill"
                CON +=2
                WIS +=1
                print(subrace)
                break
            
            if subrace == 3:
                subrace = "Mark of Warding"
                CON +=2
                DEX +=1
                print(subrace)
                break
            
            if subrace == 4:
                subrace = "Mountain"
                CON +=2
                STR +=2
                print(subrace)
                break

        
    if Race == 8:
        Race = "Elf"
        print("Elf selected")

        while True:
            subrace = int(input("1- Aereni High 2- Aereni Wood 3- Drow 4- Eladrin 5- Eladrin(Variant) 6- High 7- Mark of Shadow 8- Sea Elf 9- Shadar Kai 10- Valenar High 11- Valenar Wood 12- Wood"))

            if subrace == 1:
                subrace = "Aereni High"
                DEX +=2
                CON +=1
                print(subrace)
                break
            
            if subrace == 2:
                subrace = "Aereni Wood"
                DEX +=2
                WIS +=1
                print(subrace)
                break
            
            if subrace == 3:
                subrace = "Drow"
                DEX +=2
                CHA +=1
                print(subrace)
                break
            
            if subrace == 4:
                subrace = "Eladrin"
                DEX +=2
                CHA +=1
                print(subrace)
                break
            if subrace == 5:
                subrace = "Eladrin(Variant)"
                DEX +=2
                INT +=1
                print(subrace)
                break
            
            if subrace == 6:
                subrace = "High"
                DEX +=2
                INT +=1
                print(subrace)
                break
            
            if subrace == 7:
                subrace = "Mark of Shadow"
                DEX +=2
                CHA +=1
                print(subrace)
                break
            
            if subrace == 8:
                subrace = "Sea Elf"
                DEX +=2
                CON +=1
                print(subrace)
                break
            if subrace == 9:
                subrace = "Shadar Kai"
                DEX +=2
                CON +=1
                print(subrace)
                break
            
            if subrace == 10:
                subrace = "Valenar High"
                DEX +=2
                INT +=1
                print(subrace)
                break
            if subrace == 11:
                subrace = "Valenar Wood"
                DEX +=2
                WIS +=1
                print(subrace)
                break
            
            if subrace == 12:
                subrace = "Wood"
                DEX +=2
                WIS +=1
                print(subrace)
                break
        
    if Race == 9:
        Race = "Fairy"
        print(" choose to increase one ability score by 2 and another by 1, or choose to increase three different scores by 1.")
        print("You will choose forward") 
        print("Fairy selected")

    if Race == 0:
        Race = random.choice(R)
        R = Race

        if Race == "Aasimar":
            AasimarSubRace = random.choice(AasimarSubRace)
            print(AasimarSubRace)

        if Race == "Dragonborn":
            DragonobornSubRace = random.choice(DragonobornSubRace)
            DragonbornSubType = random.choice(DragonbornSubType)
            print(DragonobornSubRace)
            print(DragonbornSubType)

        if Race == "Dwarf":
            DwarfSubRace = random.choice(DwarfSubRace)
            print(DwarfSubRace)

        if Race == "Elf":
            ElfSubRace = random.choice(ElfSubRace)
            print(ElfSubRace)

        print(R)
        
elif Parameters == "N" or Parameters == "n":
    print("Good Luck")
    Sex = random.choice(Sex)
    print(Sex)
    R = random.choice(R)
    print(R)

#the same code of Race part to include the subdivision 

    if R == "Aasimar":
        AasimarSubRace = random.choice(AasimarSubRace)
        print(AasimarSubRace)

    if R == "Dragonborn":
        DragonobornSubRace = random.choice(DragonobornSubRace)
        DragonbornSubType = random.choice(DragonbornSubType)
        print(DragonobornSubRace)
        print(DragonbornSubType)

    if R == "Dwarf":
        DwarfSubRace = random.choice(DwarfSubRace)
        print(DwarfSubRace)

    if R == "Elf":
        ElfSubRace = random.choice(ElfSubRace)
        print(ElfSubRace)  
    

else:
    print('Keep Calm Bro, Try again!')




