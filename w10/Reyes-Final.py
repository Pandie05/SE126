#Name: Hendry
#Date 3/9/24
#Final (woooooooooooo)
#Course name: SE126
#Prompt:


#----------------------------------------------------------------------

#hello :)
print("\nWelcome to the Pokemon Character Creator :)")

#---Functions-------------------------------------

def menu():

    print("\n\n1. View All Characters Made")
    print("2. Make Character ")
    print("3. Search for character")
    print("4. Quit")

    menu_choice = input("\nPlease choose action [1-4]: ")

    while menu_choice != '1' and menu_choice != '2' and menu_choice != '3' and menu_choice != '4':

        print("\n\t*error* \n only [1-5] accepted")

        menu_choice = input("\nPlease choose action [1-4]: ")
    
    return menu_choice

#---Main Code-------------------------------------

#make list---
name = []
starter = []
legend = []
region = []

generation = ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4','Gen 5', 'Gen 6', 'Gen 7', 'Gen 8', 'Gen 9']
grass = ['Bulbasaur', 'Chikorita', 'Treecko', 'Turtwig', 'Snivy', 'Chespin', 'Rowlet', 'Grookey', 'Sprigatito']
water = ['Squirtle', 'Totodile', 'Mudkip', 'Piplup', 'Oshawott', 'Froakie', 'Popplio', 'Sobble', 'Quaxly']
fire = ['Charmander', 'Cyndaquil', 'Torchic', 'Chimchar','Tepig', 'Fennekin', 'Litten', 'Scorbunny', 'Fuecoco']

for i in range(0, len(generation)):

    print(f"{generation[i]:10}: {grass[i]:12} {water[i]:12} {fire[i]}")

choice = menu()

while choice != '5':

    if choice == '1':

        print('showing all characters made...')

        for i in range(len(name)):

            print(f"{name[i]} {starter[i]} {legend[i]} {region[i]}")



    if choice == '2':

        print('Choosing name...')

        char_name = input("Please Enter Character Name: ")

        name.append(char_name)

        print(name)

        print("choosing starter...")

        gen = input("Please Choose Generation [1-9]: ")

        if gen == '1':

            print("Gen 1: Bulbasaur, Squirtle, Charmander, Pikachu")

            gen_choice = input("Please Choose Pokemone [1-4] ")

            if gen_choice == '1':

                pokemon = "Bulbasaur"
                starter.append(pokemon)

            if gen_choice == '2':
                
                pokemon = "Squirtle"
                starter.append(pokemon)

            if gen_choice == '3':
                
                pokemon = "Charmander"
                starter.append(pokemon)

            if gen_choice == '4':
                
                pokemon = "Pikachu"
                starter.append(pokemon)

        if gen == '2':
            print('')

        if gen == '3':
            print('')

        if gen == '4':
            print('')

        if gen == '5':
            print('')

        if gen == '6':
            print('')

        if gen == '7':
            print('')

        if gen == '8':
            print('')

        if gen == '9':
            print('')



        choice = menu()

    if choice == '3':

        print('choosing pokemon...')



    if choice == '4':
        print('')
     



    
#---Seq Search--------------------------------------