__author__ = "Leonardo Aureliano <leomaureliano@gmail.com>"
#Ok  will try to start (again) a new D&D project today is 28/12/2021#import random#If the user did not set the parameters all will run rondolyParameters = input("Set the parameters Y/N") #Creating the atributes#STR = 0DEX = 0CON = 0INT = 0WIS = 0CHA = 0ASI = 0 #Others Size = 0Speed = 0 #LanguagesLanguage = [1] #D&D Races#R = ["Aarakocra", "Aasimar", "Bugbear", " = R#libraryes of Subraces and Types# AasimarSubRace = ["Fallen", "Protector", "Scourge", "Variant"]DragonbornSubRace = ["Draconblood", "Ravenite"]DragonbornSubType = ["Black", "Blue", "Brass", "Broze", "Copper", "Gold", "Green", "Red", "Silver", "White"]DwarfSubRace = ["Gray(Duergar)", "Hill", "Mark of Warding", "Mountain"]ElfSubRace = ["Aereni High", "Aereni Wood", "Drow", "Eladrin", "Eladrin(Variant)", "High", "Mark of Shadow", "Sea Elf", "Shadar Kai", "Valenar High", "Valenar Wood", "Wood"] #Fist we select the gener#Sex = ["Male", "Famale"] if Parameters == "Y" or Parameters == "y": print("0 - Randon") print("1 - Male") print("2 - Famale") Sex = input("Sex?") if Sex == "0": Sex = random.choice(Sex) elif Sex == "1": print("Male") elif Sex == "2": print("Famale") elif Sex == "3": print("Ohh,You discovered a new gener") NSex = input("Write pleace") NSex = Sex print("Nice") else: print("Please come back to school")#Race and subrace type# if Parameters == "Y" or Parameters == "y": print("0 - Random") print("1 - Aarakocra") print("2 - Aasimar") print("3 - Bugbear") print("4 - Centaur") print("5 - Changeling") print("6 - Dragonborn") print("7 - Dwarf") print("8 - Elf") print("9 - Fairy") Race = int(input("Race?")) if Race == 1: Race = "Aarakroca" DEX +=2 WIS +=1 print("Aarakroca selected") if Race == 2: Race = "Aasimar" print("Aasimar selected, select the subrace number") while True: subrace = int(input("1- Fallen, 2- Protector, 3- Scourge or 4-Variant")) if subrace == 1: subrace and AasimarSubRace == "Fallen" CHA +=2 SRT +=1 print("Fallen") break if subrace == 2: subrace and AasimarSubRace == "Protector" CHA +=2 WIS +=1 print("Protector") break if subrace == 3: subrace and AasimarSubRace == "Scourge" CHA +=2 CON +=1 print("Scourge") break if subrace == 4: subrace and AasimarSubRace == "Variant" CHA +=2 WIS +=1 print("Variant") break print("You have made an invalid choice, try again.") elif Race == 3: Race = "Bugbear" STR +=2 DES +=1 print(" Bugbear selected") elif Race == 4: Race = "Centaur" STR +=2 WIS +=1 print("Centaur selected") elif Race == 5: Race = "Changeling" CHA +=2 ASI +=1 print("Changeling selected") elif Race == 6: Race = "Dragonborn" print("Dragonborn selected, select the subrace and type") while True: subraceType = int(input("1- Draconblood or 2- Ravenite")) if subraceType == 1: subraceType == "Draconblood" INT +=2 CHA +=1 print("Draconblood") break elif subraceType == 2: subraceType == "Revenite" STR +=2 CON +=1 print("Ravenite") break #dragonborn have two different model and have a dragon type which I slash in two# while True: subrace = int(input("1- Black, 2- Blue, 3- Brass, 4- Bronze, 5- Copper, 6- Gold, 7- Green, 8- Red, 9- Silver, 10- White")) if subrace == 1: subrace == "Black" print("Black") break if subrace == 2: subrace == "Blue" print("Blue") break if subrace == 3: subrace == "Brass" print("Brass") break if subrace == 4: subrace == "Bronze" print("Bronze") break if subrace == 5: subrace == "Copper" print("Copper") break if subrace == 6: subrace == "Gold" print("Gold") break if subrace == 7: subrace == "Green" print("Green") break if subrace == 8: subrace == "Red" print("Red") break if subrace == 9: subrace == "Silver" print("Silver") break if subrace == 10: subrace == "White" print("White") break if Race == 7: Race = "Dwarf" print("Dwarf selected") while True: subrace = int(input("1- Gray(Duergar) 2- Hill 3- Mark of Warding 4- Mountain")) if subrace == 1: subrace = "Gray(Duergar)" CON +=2 STR +=1 print(subrace) break if subrace == 2: subrace = "Hill" CON +=2 WIS +=1 print(subrace) break if subrace == 3: subrace = "Mark of Warding" CON +=2 DEX +=1 print(subrace) break if subrace == 4: subrace = "Mountain" CON +=2 STR +=2 print(subrace) break if Race == 8: Race = "Elf" print("Elf selected") while True: subrace = int(input("1- Aereni High 2- Aereni Wood 3- Drow 4- Eladrin 5- Eladrin(Variant) 6- High 7- Mark of Shadow 8- Sea Elf 9- Shadar Kai 10- Valenar High 11- Valenar Wood 12- Wood")) if subrace == 1: subrace = "Aereni High" DEX +=2 CON +=1 print(subrace) break if subrace == 2: subrace = "Aereni Wood" DEX +=2 WIS +=1 print(subrace) break if subrace == 3: subrace = "Drow" DEX +=2 CHA +=1 print(subrace) break if subrace == 4: subrace = "Eladrin" DEX +=2 CHA +=1 print(subrace) break if subrace == 5: subrace = "Eladrin(Variant)" DEX +=2 INT +=1 print(subrace) break if subrace == 6: subrace = "High" DEX +=2 INT +=1 print(subrace) break if subrace == 7: subrace = "Mark of Shadow" DEX +=2 CHA +=1 print(subrace) break if subrace == 8: subrace = "Sea Elf" DEX +=2 CON +=1 print(subrace) break if subrace == 9: subrace = "Shadar Kai" DEX +=2 CON +=1 print(subrace) break if subrace == 10: subrace = "Valenar High" DEX +=2 INT +=1 print(subrace) break if subrace == 11: subrace = "Valenar Wood" DEX +=2 WIS +=1 print(subrace) break if subrace == 12: subrace = "Wood" DEX +=2 WIS +=1 print(subrace) break if Race == 9: Race = "Fairy" print(" choose to increase one ability score by 2 and another by 1, or choose to increase three different scores by 1.") print("You will choose forward") print("Fairy selected") if Race == 0: Race = random.choice(R) R = Race if Race == "Aasimar": AasimarSubRace = random.choice(AasimarSubRace) print(AasimarSubRace) if Race == "Dragonborn": DragonobornSubRace = random.choice(DragonobornSubRace) DragonbornSubType = random.choice(DragonbornSubType) print(DragonobornSubRace) print(DragonbornSubType) if Race == "Dwarf": DwarfSubRace = random.choice(DwarfSubRace) print(DwarfSubRace) if Race == "Elf": ElfSubRace = random.choice(ElfSubRace) print(ElfSubRace) print(R) elif Parameters == "N" or Parameters == "n": print("Good Luck") Sex = random.choice(Sex) print(Sex) R = random.choice(R) print(R) #the same code of Race part to include the subdivision if R == "Aasimar": AasimarSubRace = random.choice(AasimarSubRace) print(AasimarSubRace) if R == "Dragonborn": DragonobornSubRace = random.choice(DragonobornSubRace) DragonbornSubType = random.choice(DragonbornSubType) print(DragonobornSubRace) print(DragonbornSubType) if R == "Dwarf": DwarfSubRace = random.choice(DwarfSubRace) print(DwarfSubRace) if R == "Elf": ElfSubRace = random.choice(ElfSubRace) print(ElfSubRace) else: print('Keep Calm Bro, Try again!')
#Ok I will try to start (again) a new D&D project today is 28/12/2021#
import random

print("__________________________________________________________________________________________________________________________________________")
print("Hello, this is a character creator with rondom choices included.")
print("Good part of this program can only be answered if you choose numbers, attention please!")
print("Good luck \o/")
#If the user did not set the parameters all will run rondoly
Parameters = input("Set the parameters Y/N: ")

#Creating the atributes#
STR = 0
DEX = 0
CON = 0
INT = 0
WIS = 0
CHA = 0
#ASI will give the possibility to put points in any attribute#
ASI = 0

#Others#
Size = "Medium"
Speed = "30feet"

#Alignment#
Alignment = ("Lawful/Good", "Neutral/Good", "Chaotic/Good", "Neutral", "Chaotic/Neutral", "Lawful/Evil", "Lawful/Neutral", "Neutral/Evil", "Chaotic/Evil")

#Backgrouds / with flaws#
Background = ("Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermt", "Noble","Outlander", "Sage", "Sailor", "Soldier", "Urchin")
AcolyteFlaws = ("I judge others harshly, and myself even more severely.", "I put too much Trust in those who wield power within my Temple's hierarchy.", "My piety sometimes leads me to blindly trust those that profess faith in my god.", "I am inflexible in my thinking.", "I am suspicious of strangers and expect the worst of them.",
"Once I pick a goal, I become obsessed with it to the detriment of everylhing else in my life.")

CharlatanFlaws = ("I can't resist a pretty face.", "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.", "I'm convinced that no one could ever fool me the way I fool others.", "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.", "I can't resist swindling people who are more powerful than me.", "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.")
HermitFlaws = ("Nowthat I've returned to the world, I enjoy its delights a little too much.", "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.", "I am dogmatic in my thoughts and philosophy.", "I let my need to win arguments overshadow friendships and harmony.", "I'd risk too much to uncover a lost bit of knowledge.", "I like keeping secrets and won't share them with anyone.")
NobleFlaws = ("I secretly believe that everyone is beneath me.", "I hide a truly seandalous secret that would ruin my family forever.", "I toe often hear veiled insults and threats in every word addressed to me, and I'm quiek to anger.", "I have an insatiable desire for carnal pleasures.", "In faet, the world does revolve around me.", "By my words and actions, I often bring shame to my family.")


#Dices, I wroth this form just because we can check the rules easier#
D20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
D10 = [1,2,3,4,5,6,7,8,9,10]
D8 = [1,2,3,4,5,6,7,8]
D6 = [1,2,3,4,5,6]
D4 = [1,2,3,4]
D3 = [1,2,3]
D2 = [1,2]


#Languages
Languages = ("Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon")
Language = ("Common")
L = 0
#D&D5e Races#
R = ["Aarakocra", "Aasimar", "Bugbear", "Centaur","Changeling","Dragonborn","Dwarf","Elf", "Fairy", "Firbolg", "Genasi", "Gith", "Gnome", "Goliath", "Half-Elf", "Half-Hag", "Half-Orc", "Halfling", "Hobgoblin", "Human", "Kalashtar", "Kanku", "Kobold", "Leonin", "Lizardfolk", "Loxodon", "Mind Flayer", "Minotaur"]
Race = R

#libraryes of Subraces and Types#

AasimarSubRace = ["Fallen", "Protector", "Scourge", "Variant"]
DragonbornSubRace = ["Draconblood", "Ravenite"]
DragonbornSubType = ["Black", "Blue", "Brass", "Broze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
DwarfSubRace = ["Gray(Duergar)", "Hill", "Mark of Warding", "Mountain"]
ElfSubRace = ["Aereni High", "Aereni Wood", "Drow", "Eladrin", "Eladrin(Variant)", "High", "Mark of Shadow", "Sea Elf", "Shadar Kai", "Valenar High", "Valenar Wood", "Wood"]
GnomeSubRace = ["Florest Gnome", "Rock Gnome"]

#D&D5e Classes#
Classes = ["Artificer", "Barbarian", "Bard", "Blood Hunter","Cleric", "Fighter", "Monk", "Mystic", "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]
Class = [1]

#Fist we select the gener#
Sex = ["Male", "Famale"]

if Parameters == "Y" or Parameters == "y" or Parameters == "yes" or Parameters == "YES":
  while True: 
    print("0 - Randon")
    print("1 - Male")
    print("2 - Famale")
    print("3 - Create")
    Sex = input("Select your gener:")

    if Sex == "0":
        Sex = random.choice(Sex)
        break
        
    elif Sex == "1":
        print("Male")
        break 
        
    elif Sex == "2":
        print("Famale")
        break 
        
    elif Sex == "3":
        print("Ohh,You discovered a new gener")
        NSex = input("Write pleace:")
        NSex = Sex
        Sex == NSex
        print("Nice") 
        break 
        
    else:
        print("Error")
#Race and subrace and type#

if Parameters == "Y" or Parameters == "y" or Parameters == "yes":        
  while True:  
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
    print("10 - Genasi")
    print("11 - Gnome")
    print("12 - Goblin") 
    print("13 - Goliath")
    print("14 - Half-Elf")
    print("15 - Half-Hag")
    print("15 - Half-Orc")
    print("16 - Halfling")
    print("17 - Hobgoblin")
    print("18 - Human")
    print("19 - Kalashtar")
    print("20 - Kenku")
    print("21 - Kobold")
    print("22 - Leonin")
    print("23 - Lizardfolk")
    print("24 - Loxodon")
    print("25 - Mind Flayer")
    print("26 - Minotaur")
    Race = int(input("Choose a race?"))

    if Race == 0:
        Race = random.choice(R)
        R = Race
        print(R)
        
        if Race == "Aasimar":
            AasimarSubRace = random.choice(AasimarSubRace)
            print(AasimarSubRace)

        if Race == "Dragonborn":
            DragonbornSubRace = random.choice(DragonbornSubRace)
            DragonbornSubType = random.choice(DragonbornSubType)
            print(DragonbornSubRace)
            print(DragonbornSubType)

        if Race == "Dwarf":
            DwarfSubRace = random.choice(DwarfSubRace)
            print(DwarfSubRace)

        if Race == "Elf":
            ElfSubRace = random.choice(ElfSubRace)
            print(ElfSubRace)
   
    if Race == 1:
        Race = "Aarakroca"
        DEX +=2
        WIS +=1
        print("Aarakroca selected")

    if Race == 2:
        Race = "Aasimar"
        print("Aasimar selected, select the subrace number")
        while True:
            print("1 - Fallen")
            print("2 - Protector")
            print("3 - Scourge")
            print("4 - Variant")
            subrace = int(input("Select the subrace number"))
            if subrace == 1:
                subrace and AasimarSubRace == "Fallen"
                CHA +=2
                STR +=1
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

            else:     
               print("You have made an invalid choice, try again.")                   
            
    elif Race == 3:
        Race = "Bugbear"
        STR +=2
        DEX +=1
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
            print("1 - Draconblood")
            print("2 - Ravenite")
            
            subraceType = int(input("Select the subrace number:"))
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
            print("1 - Black")
            print("2 - Blue")
            print("3 - Brass")
            print("4 - Bronze")
            print("5 - Copper")
            print("6 - Gold")
            print("7 - Green")
            print("8 - Red")
            print("9 - Silver")
            print("10 - White")
            
            subrace = int(input("Select a type:"))
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
                
            else:     
               print("You have made an invalid choice, try again.")                   

            
    if Race == 7:
        Race = "Dwarf"
        Size = "Medium"
        Speed = "25 feet"
        Language = ("Common","Dwarvish")
        print("Dwarf selected")
        print("Select th subrace")
        
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
        Size = "Medium"
        Speed = "30feet"
        Language = ("Common","Elfvish")
        print("Elf selected")
        print("Select the subrace") 
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
                print("You can choose a additional language.")
  
                while True:
                   print("0 - Random")
                   print("1 - Dwarvish")
                   print("2 - Giant")
                   print("3 - Gnomish")
                   print("4 - Goblin")
                   print("5 - Halfling")
                   print("6 - Orc")
                   print("7 - Abyssal")
                   print("8 - Celestial")
                   print("9 - Draconic")
                   print("10 - Deep Speech")
                   print("11 - Infernal")
                   print("12 - Primordial")
                   print("13 - Sylvan")
                   print("14 - Undercommon")  
                   L = int(input("Choose Language:"))   
                   
                   if L ==1:
                       L = "Dwarvish"
                       Language += L
                       print("Dwarvish")
                       print(Language)
                       break 
                   
                   if L == 2:
                       L = "Giant"
                       Language += L
                       print("Giant")
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
                Speed = "35feet"
                DEX +=2
                WIS +=1
                print(subrace)
                break
        
            else:     
               print("You have made an invalid choice, try again.")                   

    if Race == 9 or Race == "Fairy":
        Race = "Fairy"
        ASI += 3
        print("Choose to increase one ability score by 2 and another by 1, or choose to increase three different scores by 1.")
        print("You will choose forward") 
        print("Fairy selected")
    
    
    if Race == 10 or Race == "Genasi":
        Race = "Genasi"
        CON += 2
        print(Race)
        while True:
            print("1 Air Genasi")
            print("2 - Earth Genasi")
            SubRace = int(input("Select the sub race:"))
           
            if SubRace == 1:
                DEX += 1
                print("Air Genasi Selected")
                break
           
            if SubRace == 2:
               STR += 1
               print("Earth Genasi Selected")
               break
               
            if SubRace == 3:
               INT += 1
               print("Fire Genasi Selected")
               break
              
            if SubRace == 4:
               WIS += 1
               print("Water Genasi Selected")
               break
        
    
    
    if Race == 11 or Race == "Gnome":
        Race = "Gnome"
        INT += 2
        print(Race)
        Speed = "25feet"
        Size = "Small"
        while True:
            print("1 - Florest Gnome")
            print("2 - Rock Gnome")
            SubRace = int(input("Select the sub race:"))
           
            if SubRace == 1:
                DEX += 1
                print("Florest Gnome Selected")
                break
                
            if SubRace == 2:
                CON += 1
                print("Rock Gnome Selected")
                break
            
            else:
                print("Try again")
       
    if Race == 12:
        DEX += 2
        CON += 1
        Race = "Goblin"
        print("Goblin selected")  
        
    if Race == 13:
        STR += 2
        CON += 1
        Race == "Goliath"
        
    if Race == 14:
        CHA += 2
        ASI += 2
        Race = "Half-Elf"    
        
    if Race == 15:
        STR += 2
        CON += 1
        Race = "Half-Orc"  
    
    if Race == 16:
        DEX += 2
        Race = "Halfling"
        while True:
            print("1 - Ghostwise Halfling")
            print("2 - Lightfoot Halfling")
            print("3 - Stout Halfling")
            print("4 - Lotusden Halfling")
            SubRace = int(input("Select your Sub race"))
            
            if SubRace == 1:
                WIS += 1
                SubRace = "Ghostwise Halfling"
                break
             
            if SubRace == 2:
                CHA += 1
                SubRace = "Lightfoot Halfling"
                break
                
            if SubRace == 3:
                CON += 1
                SubRace = "Stout Halfling"
                break
                
            if SubRace == 4:
                WIS += 1
                SubRace = "Lotusden Halfling"
                break
        
    if Race == 17:
        CON += 2
        INT += 1
        Race = "Hobgoblin"
        
    if Race == 18:
        Race = "Human"
        while True:
            print("1 - Standard Human")
            print("2 - Variant Human")
            SubRace = int(input("Select your type"))
            
            if SubRace == 1:
                STR += 1
                DEX += 1
                CON += 1
                INT += 1
                WIS += 1
                CHA += 1
                SubRace = "Human"
                print(SubRace)
                break
             
            if SubRace == 2:
                ASI += 2
                SubRace = "Variant Human"
                print(SubRace)
                break
    
    if Race == 19:
        WIS += 1 
        CHA += 1 
        ASI += 1
        Race = "Kalashtar"
       
    if Race == 20:
        DEX += 2
        WIS += 1
        Race = "Kenku" 
       
    if Race == 21:
        STR -= 2
        DEX += 2
        Race = "Kobold"      
    
    if Race == 22:
        STR += 1
        CON += 2
        Race = "Leonin"
        
    if Race == 23:
       CON += 2
       WIS += 1
       Race = "Lizardfolk"
        
    if Race == 24:
       STR += 2
       Race = "Loxodon"
       while True:
           print("1 - Ravnica Loxodon")
           print("2 - Mirrodin Loxodon")
           print("3 - Tarkir Loxodon")
           SubRace = int(input("Select your Sub Race:"))
        
           if SubRace == 1:
               WIS += 2
               SubRace = "Ravnica Loxodon"
               
           if SubRace == 2:
               INT += 2
               SubRace = "Mirrodin Loxodon"
               
           if SubRace == 3:
               CON += 2
               SubRace = "Tarkir Loxodon"
        
    if Race == 25:
       INT += 2
       Race = "Mind Layer"
       
    if Race == 26:
        STR += 2
        CON += 1
        Race = "Minotaur"
        
    if Race != 360:
        break

if Parameters == "Y" or Parameters == "y":
  while True:
    print("0 - Random")
    print("1 - Artificer")
    print("2 - Bararian")
    print("3 - Bard")
    print("4 - Cleric")
    print("5 - Druid")
    print("6 - Fighter")
    print("7 - Monk")
    print("8 - Paladin")
    print("9 - Ranger")
    print("10 - Rogue")
    print("11 - Sorcerer")
    print("12 - Warlock")
    print("13 - Wizard")
    C = int(input("Choose a class:"))

    if C == 0:
      Classes = random.choice(Classes)
      Classes = Classes 
      print(Classes)
      break 
        
    if C == 1:
      Class = ("Artificer")
      print(Class)
      break 
      
    if C == 2:
      Class = ("Barbarian")
      print(Class)
      break      
      
    if C == 3:
      Class = ("Bard")
      print(Class)
      break 
      
    if C == 4:
      Class = ("Cleric")
      print(Class)
      break 
      
    if C == 5:
      Class = ("Druid")
      print(Class)
      break 
      
    if C == 6:
      Class = ("Fighter")
      print(Class)
      break 
      
    if C == 7:
      Class = ("Monk")
      print(Class)
      break 
      
    if C == 8:
      Class = ("Paladin")
      print(Class)
      break 
      
    if C == 9:
      Class = ("Ranger")
      print(Class)
      break 
      
    if C == 10:
      Class = ("Rogue")
      print(Class)
      break
      
    if C == 11:
      Class = ("Sorcerer")
      print(Class)
      break 
  
    if C == 12:
      Class = ("Warlock")
      print(Class)
      break
       
    if C == 13:
      Class = ("Wizard")
      print(Class)
      break
      
      
    else:
        print("try again")  
         

#Atributes part#
Attributes = STR + DEX + CON + INT + WIS + CHA
if Parameters == "Y" or Parameters == "y" or Parameters == "yes":
   print("Select your attributes")
   print("Select the form of attributes distribution")
   print("0 - Random")
   print("1 - Fully opened")
   print("2 - 3D6 seven times")
   print("3 - 1D20 seven times")
   print("4 - 1D20 for each attribute")
   print("5 - Point buy")
   print("6 - Limited number")
   
   if Attributes != 0:
       print("You actually have:")
       print("STR +", STR)
       print("DEX +", DEX)
       print("CON +", CON)
       print("INT +", INT)
       print("WIS +", WIS)
       print("CHA +", CHA)
       
   AttributesChoice = int(input("Select:"))
   
   if AttributesChoice == 0:
      STR = random.choice(D20)
      DEX = random.choice(D20)
      CON = random.choice(D20)
      INT = random.choice(D20)
      WIS = random.choice(D20)
      CHA = random.choice(D20)
      print("STR =", STR)
      print("DEX =", DEX)
      print("CON =", CON)
      print("INT =", INT)
      print("WIS =", WIS)
      print("CHA =", CHA)
      
  
   if AttributesChoice == 1:
      STRa = int(input("STR:"))
      DEXa = int(input("DEX:"))
      CONa = int(input("CON:"))
      INTa = int(input("INT:"))
      WISa = int(input("WIS:"))
      CHAa = int(input("CHA:"))
      STR += STRa
      DEX += DEXa
      CON += CONa
      INT += INTa
      WIS += WISa
      CHA += CHAa
      print("STR:", STR)
      print("DEX:", DEX)
      print("CON:", CON)
      print("INT:", INT)
      print("WIS:", WIS)
      print("CHA:", CHA)
      
      
   if  AttributesChoice == 2:
       Dice1 = random.choice(D6)
       Dice2 = random.choice(D6)
       Dice3 = random.choice(D6)
       Dice4 = random.choice(D6)
       Dice5 = random.choice(D6)
       Dice6 = random.choice(D6)
       Dice7 = random.choice(D6)
       Dice8 = random.choice(D6)
       Dice9 = random.choice(D6)
       Dice10 = random.choice(D6)
       Dice11 = random.choice(D6)
       Dice12 = random.choice(D6)
       Dice13 = random.choice(D6)
       Dice14 = random.choice(D6)
       Dice15 = random.choice(D6)
       Dice16 = random.choice(D6)  
       Dice17 = random.choice(D6)
       Dice18 = random.choice(D6)
       Dice19 = random.choice(D6)
       Dice20 = random.choice(D6)
       Dice21 = random.choice(D6)
       
       DiceA = Dice1 + Dice2 + Dice3 
       DiceB = Dice4 + Dice5 + Dice6
       DiceC = Dice7 + Dice8 + Dice9
       DiceD = Dice10 + Dice11 + Dice12
       DiceE = Dice13 + Dice14 + Dice15
       DiceF = Dice16 + Dice17 + Dice18
       DiceG = Dice19 + Dice20 + Dice21
       
       print(DiceA)
       print(DiceB)
       print(DiceC)
       print(DiceD)
       print(DiceE)
       print(DiceF)
       print(DiceG)
       
   if  AttributesChoice == 3:
       DiceA = random.choice(D20)
       DiceB = random.choice(D20)
       DiceC = random.choice(D20)
       DiceD = random.choice(D20)
       DiceE = random.choice(D20)
       DiceF = random.choice(D20)
       DiceG = random.choice(D20)
       print("Your numbers:")
       print("Now select the possition for each of them:")
       print(DiceA)
       print(DiceB)
       print(DiceC)
       print(DiceD)
       print(DiceE)
       print(DiceF)
       print(DiceG)
       print("Now select the possition for each of them:")
       STRa = int(input("STR: "))
       DEXa = int(input("DEX: "))
       CONa = int(input("CON: "))
       INTa = int(input("INT: "))
       WISa = int(input("WIS: "))
       CHAa = int(input("CHA: "))
       STR += STRa
       DEX += DEXa
       CON += CONa
       INT += INTa
       WIS += WISa
       CHA += CHAa
       print("Results")
       print("STR:", STR)
       print("DEX:", DEX)
       print("CON:", CON)
       print("INT:", INT)
       print("WIS:", WIS)
       print("CHA:", CHA)
      
   if  AttributesChoice == 4:
       DiceA = random.choice(D20)
       DiceB = random.choice(D20)
       DiceC = random.choice(D20)
       DiceD = random.choice(D20)
       DiceE = random.choice(D20)
       DiceF = random.choice(D20)
       print("Your numbers:")
       print("Now select the possition for each of them:")
       print(DiceA)
       print(DiceB)
       print(DiceC)
       print(DiceD)
       print(DiceE)
       print(DiceF)
       print("Now select the possition for each of them:")
       STRa = int(input("STR: "))
       DEXa = int(input("DEX: "))
       CONa = int(input("CON: "))
       INTa = int(input("INT: "))
       WISa = int(input("WIS: "))
       CHAa = int(input("CHA: "))
       STR += STRa
       DEX += DEXa
       CON += CONa
       INT += INTa
       WIS += WISa
       CHA += CHAa
       print("Results")
       print("STR:", STR)
       print("DEX:", DEX)
       print("CON:", CON)
       print("INT:", INT)
       print("WIS:", WIS)
       print("CHA:", CHA)
       
   if  AttributesChoice == 5:
       print("point buy values")
       
      
   if ASI != 0:
      print("additional points floating:",ASI)

   if Attributes != 0:
       print("Results")
       print("STR:", STR)
       print("DEX:", DEX)
       print("CON:", CON)
       print("INT:", INT)
       print("WIS:", WIS)
       print("CHA:", CHA)
#Alignment#  
if Parameters == "Y" or Parameters == "y" or Parameters == "yes":
  while True:
   if Parameters != 0: 
    print("Character Alignment")
    print("0 - Random")
    print("1 - Lawful/Good")  
    print("2 - Neutral/Good")  
    print("3 - Chaotic/Good")
    print("4 - Neutral")
    print("5 - Chaotic/Neutral")
    print("6 - Lawful/Evil")
    print("7 - Lawful/Neutral")
    print("8 - Neutral/Evil")   
    print("9 - Chaotic/Evil")
    Alignment1 = int(input("Select your Alignment number:"))
    
    
   if Alignment1 == 0:
      Alignment = random.choice(Alignment)
      print("Alignment:",Alignment)
      break
           
   if Alignment1 == 1:
      Alignment = "Lawful/Good"
      print("Alignment:",Alignment)
      break 
      
   if Alignment1 == 2: 
      Alignment = "Neutral/Good"
      print("Alignment:",Alignment)   
      break
      
   if Alignment1 == 3:
       Alignment = "Chaotic/Good"
       print("Alignment:",Alignment)
       break 
       
   if Alignment1 == 4:
       Alignment = "Neutral"
       print("Alignment:",Alignment)
       break
       
   if Alignment1 == 5:
       Alignment = "Chaotic/Neutral"
       print("Alignment:",Alignment)
       break 
       
   if Alignment1 == 6:
       Alignment = "Lawful/Evil"
       print("Alignment:",Alignment)
       break 
       
   if Alignment1 == 7:
       Alignment = "Lawful/Neural"
       print("Alignment:",Alignment)
       break 
       
   if Alignment1 == 8:
       Alignment = "Neutral/Evil"
       print("Alignment:",Alignment)
       break 
       
   if Alignment1 == 9:
       Alignment = "Chaotic/Evil"
       print("Alignment:",Alignment)
       break
               
            
#Background part#
if Parameters == "Y" or Parameters == "y" or Parameters == "yes":
 while True: 
    print("Now select your background")
    print("0 - random")
    print("1 - Acolyte")
    print("2 - Charlatan")
    print("3 - Criminal")
    print("4 - Entertainment")
    print("5 - Folk Hero")
    print("6 - Guild Artisan")
    print("7 - Hermit")
    print("8 - Noble")
    print("9 - Outlander")
    print("10 - Sage")
    print("11 - Sailor")
    print("12 - Soldier")
    print("13 - Urchin")
    print("14 - Create  your own")
    Background1 = int(input("Select your background number"))
    
    if Background1 == 0:
        Background = random.choice(Background)
        print(Background)
        
    if Background1 == 1:
        Background = "Acolyte" 
        print(Background)
        AcolyteFlaws = random.choice(AcolyteFlaws)
        print("Your flaw is:",AcolyteFlaws)
        break
        
    if Background1 == 2:
        Background = "Charlatan"
        print(Background)
        CharlatanFlaws = random.choice(CharlatanFlaws)
        print("Your flaw is:",CharlatanFlaws)
        break

    if Background1 == 3:
        Background = "Criminal"
        print(Background)
        CharlatanFlaws = random.choice(CriminalFlaws)
        print("Your flaw is:", CriminalFlaws)
       
    if Background1 == 4:
        Background = "Entertainment"
        print(Background)
        CharlatanFlaws = random.choice(EntertainmentFlaws)
        print("Your flaw is:",EntertainmentFlaws)
        
    if Background1 == 5:
        Background = "Folk Hero"
        print(Background)
        CharlatanFlaws = random.choice(FolkHeroFlaws)
        print("Your flaw is:",FolkHeroFlaws)    

    if Background1 == 6:
        Background = "Guild Artisan"
        print(Background)
        CharlatanFlaws = random.choice(GuildArtisanFlaws)
        print("Your flaw is:",GuildArtisanFlaws)
        
    if Background1 == 7:
        Background = "Hermit"
        print(Background)
        CharlatanFlaws = random.choice(HermitFlaws)
        print("Your flaw is:",HermitFlaws)

    if Background1 == 8:    
       Background = "Noble"
       print(Background)
       NobleFlaws = random.choice(Nobleflaws)
       print("Your flaw is:",NobleFlaws)


    if Background1 == 9:
       Background = "Outlander"
       print(Background)
       NobleFlaws = random.choice(Outlanderflaws)
       print("Your flaw is:", OutlanderFlaws)
    
    if Background1 == 10:
       Background =  "Sage"
       print(Background)
       SageFlaws = random.choice(SageFlaws)
       print("Your flaw is:",SageFlaws)  

#------------------------------------------------------------------------------------------------# 
#Random Part  
# 
               
elif Parameters == "N" or Parameters == "n" or Parameters == "no" or Parameters == "No":
    Sex = random.choice(Sex)
    print("Gener:",Sex)
    R = random.choice(R)
    print("Race:",R)
    Language = random.choice(Languages)        

#The same code of Race part to include the subdivision 

    if R == "Aasimar":
        AasimarSubRace = random.choice(AasimarSubRace)
        print(AasimarSubRace)

    if R == "Dragonborn":
        DragonbornSubRace = random.choice(DragonbornSubRace)
        DragonbornSubType = random.choice(DragonbornSubType)
        print(DragonbornSubRace)
        print(DragonbornSubType)

    if R == "Dwarf":
        DwarfSubRace = random.choice(DwarfSubRace)
        print(DwarfSubRace) 
        print("Language: Common, Dwarvish")

    if R == "Elf":
        ElfSubRace = random.choice(ElfSubRace)
        print(ElfSubRace)
        if ElfSubRace == "Wood":
            Speed = "35feet"
            
        if ElfSubRace == "High" or ElfSubRace == "Valenar High" or ElfSubRace == "Aereni High":
            Languages = random.choice(Languages) 
            while True:
             if Languages == "Elfvish":
               Languages = random.choice(Languages)
               break 
               
             else: 
               print("Languages:Common,Elfvish,",Language)
               break 
            
        else:
            print("Languages:Common,Elfvish")
         
         
    if R == 9 or Race == "Fairy":
        Race = "Fairy"
        ASI += 3
        print("Choose to increase one ability score by 2 and another by 1, or choose to increase three different scores by 1.")
        print("You will choose forward") 
        print("Fairy selected")  
   
    if R == 10 or Race == "Gnome":
       INT += 2
       GnomeSubRace = random.choice(GnomeSubRace)
       print(GnomeSubRace)

    
    if R == 11 or Race == "Gnome":
        Race = "Gnome"
        INT += 2
        print(Race)
        print("Size: Small")
        Speed = "25feet"
        Size = "Small"
        while True:
            print("1 - Florest Gnome")
            print("2 - Rock Gnome")
            SubRace = int(input("Select the sub race:"))
           
            if SubRace == 1:
                DEX += 1
                print("Florest Gnome Selected")
                break
                
            if SubRace == 2:
                CON += 1
                print("Rock Gnome Selected")
                break
            
            else:
                print("Try again")
       
    if R == "Goblin":
        DEX += 2
        CON += 1
        Race = "Goblin"
            
    if R == "Goliath":
        STR += 2
        CON += 1
        Race == "Goliath"
        
    if R == "Half-Elf":
        CHA += 2
        ASI += 2
        Race = "Half-Elf"    
        
    if R == "Half-Orc":
        STR += 2
        CON += 1
        Race = "Half-Orc"  
    
    if R== "Halfling":
           DEX += 2
           Race = "Halfling"
           SubRace = random.choice(D4)       
           if SubRace == 1:
                WIS += 1
                SubRace = "Ghostwise Halfling"
               
             
           if SubRace == 2:
                CHA += 1
                SubRace = "Lightfoot Halfling"
                
                
           if SubRace == 3:
                CON += 1
                SubRace = "Stout Halfling"
                
                
           if SubRace == 4:
                WIS += 1
                SubRace = "Lotusden Halfling"
                
        
    if R == "Hobgoblin":
        CON += 2
        INT += 1
        Race = "Hobgoblin"
        
    if R == "Human":
            SubRace = random.choice(D2)
            
            if SubRace == 1:
                STR += 1
                DEX += 1
                CON += 1
                INT += 1
                WIS += 1
                CHA += 1
                SubRace = "Human"
                print(SubRace)
               
             
            if SubRace == 2:
                ASI += 2
                SubRace = "Variant Human"
                print(SubRace)
                                               
    
    if R == "Kalashtar":
        WIS += 1 
        CHA += 1 
        ASI += 1
        Race = "Kalashtar"
       
    if R == "Kenku":
        DEX += 2
        WIS += 1
        Race = "Kenku" 
       
    if R == "Kobold":
        STR -= 2
        DEX += 2
        Race = "Kobold"      
    
    if R == "Leonin":
        STR += 1
        CON += 2
        Race = "Leonin"
        
    if R == "Lizardfolk":
       CON += 2
       WIS += 1
       Race = "Lizardfolk"
        
    if R == "Loxodon":
       STR += 2
       Race = "Loxodon"   
       SubRace = random.choice(D3)
       
       if SubRace == 1:
           WIS += 2
           SubRace = "Ravnica Loxodon"
               
       if SubRace == 2:
           INT += 2
           SubRace = "Mirrodin Loxodon"
               
       if SubRace == 3:
           CON += 2
           SubRace = "Tarkir Loxodon"
        
    if R == "Mind Layer":
       INT += 2
       Race = "Mind Layer"
       
    if R == "Minotaur":
        STR += 2
        CON += 1
        Race = "Minotaur"       
   
    else:
        print("Languages: Common",Language)
        print("______________________________________") 
        
    Classes = random.choice(Classes)
    Classes = Classes 
    print(Classes)
   
#Atributes values#
    STRa = random.choice(D20)
    DEXa = random.choice(D20)
    CONa = random.choice(D20)
    INTa = random.choice(D20)
    WISa = random.choice(D20)
    CHAa = random.choice(D20)
    STR += STRa     
    DEX += DEXa
    CON += CONa
    INT += INTa
    WIS += WISa
    CHA += CHAa

#Atributes rule for D&D5e#   
    if STR <=21 or DEX <=21 or CON <= 21 or INT <= 21 or WIS <= 21 or CHA <= 21:
        STR == 20
        DEX == 20
        CON == 20
        INT == 20
        WIS == 20
        CHA == 20
       
    if ASI != 0:
        print("additional points floating:",ASI) 

    print("STR =", STR)
    print("DEX =", DEX)
    print("CON =", CON)
    print("INT =", INT)
    print("WIS =", WIS)
    print("CHA =", CHA)
  
    print("")
    
    print("Character Details:")
    print("______________________________________")
    print("Size:",Size)
    print("Speed:",Speed) 
    Background = random.choice(Background)
    print(Background)    
    Align = random.choice(Alignment)
    print(Align)
