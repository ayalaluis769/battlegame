while True:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20

    dragon_hp = 300
    dragon_damage = 50

    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character  = input("Choose Your Character: ")

    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break  
    if character == "4":
        print("Unknown Character")      
print("You have chosen the character: ", character ,"\nHealth: ", my_hp, "\nDamage: ", my_damage)  

while True: 
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the Dragon!", "\n The Dragon's hitpoints are now:", dragon_hp)
    print("The Dragon strikes back at the ",character, "\n The ",character,"'s hitpoints are now", my_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    if my_hp <= 0:
        print("The ", character, "has lost the battle!")
        break
