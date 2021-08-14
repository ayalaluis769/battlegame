while True:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 115

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 85

    dragon_hp = 300
    dragon_damage = 50

    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    character  = input("Choose Your Character: ")
    


    if (character == "1") or (character == "Wizard") or (character == "WIZard") or (character == "WIZARD"):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if (character == "2") or (character == "Elf") or (character == "eLf") or (character == "ELF"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if (character == "3") or (character == "Human") or (character == "HUmaN") or (character == "HUMAN"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break  
    if (character == "4") or (character == "Orc") or (character == "orC") or (character == "ORC"):
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage  
        break    
    if character == "Quit":
        quit()

while True: 
    dragon_hp = dragon_hp - my_damage
    print("\nThe", character, "damaged the Dragon!", "\n The Dragon's healthpoints are now:", dragon_hp)
    
    my_hp = my_hp - dragon_damage
    print("\nThe Dragon strikes back at the ",character, "\n The ",character,"'s healthpoints are now", my_hp)
    
    if my_hp == 0:
        print("\nThe ", character, "has lost the battle!")
        break
    if dragon_hp == 0:
        print("\nThe Dragon has lost the battle")
        break