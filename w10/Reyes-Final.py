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
region = []

generation = ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4','Gen 5', 'Gen 6', 'Gen 7', 'Gen 8', 'Gen 9']
grass = ['Bulbasaur', 'Chikorita', 'Treecko', 'Turtwig', 'Snivy', 'Chespin', 'Rowlet', 'Grookey', 'Sprigatito']
water = ['Squirtle', 'Totodile', 'Mudkip', 'Piplup', 'Oshawott', 'Froakie', 'Popplio', 'Sobble', 'Quaxly']
fire = ['Charmander', 'Cyndaquil', 'Torchic', 'Chimchar','Tepig', 'Fennekin', 'Litten', 'Scorbunny', 'Fuecoco']

region_list = ['Kanto','Johto','Hoenn','Sinnoh','Unova','Kalos','Alola','Galar','Paldea']

choice = menu()

while choice != '4':

    #--------------------- Choice 1 --------------------------
    if choice == '1':

        print('showing all characters made...')

        print(f"\t\t{'NAME':10} {'STARTER':10} {'REGION':10}")
        print("\t\t-------------------------------")

        for i in range(len(name)):

            print(f"\t\t{name[i]:10} {starter[i]:10} {region[i]:10}") 
        
        

    #--------------------- Choice 2 --------------------------
    if choice == '2':

        print('\n\n\tChoosing name...')

        char_name = input("Please Enter Character Name: ")

        name.append(char_name)

        print("\n\n\tchoosing starter...")

        for i in range(0, len(generation)):

            print(f"{generation[i]}{':':5} {grass[i]:12} {water[i]:12} {fire[i]}")

        gen = input("\nPlease Choose Generation [1-9]: ")


        #----------------------- Gen 1 ------------------------------------------------------
        if gen == '1':

            print(f"\n{fire[0]:10}{'|'}{water[0]:10}{'|'}{fire[0]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3]: ")

            if gen_choice == '1':

                starter.append(grass[0])

            if gen_choice == '2':
                
                starter.append(water[0])

            if gen_choice == '3':
                
                starter.append(fire[0])

        #----------------------- Gen 2 ------------------------------------------------------
        if gen == '2':

            print(f"\n{fire[1]:10}{'|'}{water[1]:10}{'|'}{fire[1]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[1])

            if gen_choice == '2':
                
                starter.append(water[1])

            if gen_choice == '3':
                
                starter.append(fire[1])

        #----------------------- Gen 3 ------------------------------------------------------
        if gen == '3':

            print(f"\n{fire[2]:10}{'|'}{water[2]:10}{'|'}{fire[2]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[2])

            if gen_choice == '2':
                
                starter.append(water[2])

            if gen_choice == '3':
                
                starter.append(fire[2])

        #----------------------- Gen 4 ------------------------------------------------------
        if gen == '4':

            print(f"\n{fire[3]:10}{'|'}{water[3]:10}{'|'}{fire[3]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[3])

            if gen_choice == '2':
                
                starter.append(water[3])

            if gen_choice == '3':
                
                starter.append(fire[3])

        #----------------------- Gen 5 ------------------------------------------------------
        if gen == '5':

            print(f"\n{fire[4]:10}{'|'}{water[4]:10}{'|'}{fire[4]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[4])

            if gen_choice == '2':
                
                starter.append(water[4])

            if gen_choice == '3':
                
                starter.append(fire[4])

        #----------------------- Gen 6 ------------------------------------------------------
        if gen == '6':

            print(f"\n{fire[5]:10}{'|'}{water[5]:10}{'|'}{fire[5]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[5])

            if gen_choice == '2':
                
                starter.append(water[5])

            if gen_choice == '3':
                
                starter.append(fire[5])

        #----------------------- Gen 7 ------------------------------------------------------
        if gen == '7':

            print(f"\n{fire[6]:10}{'|'}{water[6]:10}{'|'}{fire[6]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[6])

            if gen_choice == '2':
                
                starter.append(water[6])

            if gen_choice == '3':
                
                starter.append(fire[6])

        #----------------------- Gen 8 ------------------------------------------------------
        if gen == '8':

            print(f"\n{fire[7]:10}{'|'}{water[7]:10}{'|'}{fire[7]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[7])

            if gen_choice == '2':
                
                starter.append(water[7])

            if gen_choice == '3':
                
                starter.append(fire[7])

        #----------------------- Gen 9 ------------------------------------------------------
        if gen == '9':

            print(f"\n{fire[8]:10}{'|'}{water[8]:10}{'|'}{fire[8]:10}")

            gen_choice = input("\nPlease Choose Pokemone [1-3] ")

            if gen_choice == '1':

                starter.append(grass[8])

            if gen_choice == '2':
                
                starter.append(water[8])

            if gen_choice == '3':
                
                starter.append(fire[8])

        #------------------ Region Choice -------------------------------------

        print("\n\n\tChoose region...\n")

        #show region list----------------------------
        for i in range(0, len(region_list)):

            print(f"Region {i + 1}: {region_list[i]}\n")

        region_choice = input("\nChoose Region [1-9]: ")

        #append region---------------------------

        if region_choice == '1':

            region.append(region_list[0])


        if region_choice == '2':

            region.append(region_list[1])


        if region_choice == '3':

            region.append(region_list[2])


        if region_choice == '4':

            region.append(region_list[3])


        if region_choice == '5':

            region.append(region_list[4])


        if region_choice == '6':

            region.append(region_list[5])


        if region_choice == '7':

            region.append(region_list[6])


        if region_choice == '8':

            region.append(region_list[7])


        if region_choice == '9':

            region.append(region_list[8])


    #--------------------- Choice 3 --------------------------

    if choice == '3':

        print('\n\n\tsearching...')

        #-------------- Seq Search --------------------------

        search_name = input("\nPlease Enter name you are looking for: ")

        found = []

        for i in range(0, len(name)):

            if search_name.lower() == name[i].lower():

                found.append(i)

        if found[0] != "":

            print(f"\n\tWe found {search_name} at index {found} ")
            print("\tHere is their info: \n")

            print(f"\t\t{'NAME':10} {'STARTER':10} {'REGION':10}")
            print("\t\t-------------------------------")

            for i in range(0, len(found)):

                print(f"\t\t{name[found[i]]:10} {starter[found[i]]:10} {region[found[i]]:10}")

        else:
            print(f"\n\tWe could not find {search_name} ")

    choice = menu()

#----------------------END----------------------------------
    
print('\n\n\tshowing all characters made...\n\n')

print(f"\t\t{'NAME':10} {'STARTER':10} {'REGION':10}")
print("\t\t-------------------------------")

for i in range(len(name)):

    print(f"\t\t{name[i]:10} {starter[i]:10} {region[i]:10}")


#--------------------------------------------------------
print("\n--------------------------------------------------------")
print("Goodbye :)")