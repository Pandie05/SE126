#Name: Hendry
#Date 2/11/24
#Midterm
#Course name: SE126
#Program Prompt: I asked my friends to give me 2 pokemon, a pokemon city and a pokemon town. I took that info and put it into a csv to then display

#Variable Disctionary
#snore = Snorelax Count
#geng = Gengar Count
#charm = Charmander Count
#kanto = kanto Region Count
#lav = Lavender Town Count

#--------------------------------------------------------------------------------------

#import
import csv

#function
def menu():

    #display options
    print("\n\n\t-- Menu --")
    print("1. Show All Data")
    print("2. Show Pokemon Only")
    print("3. Show Stats")
    print("4. Exit")

    #gather option
    choice = (input("Enter Your Choice [1 - 4]: "))

    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print("\n\n*INVALID ENTRY* DIGITS 1 - 4 ONLY DUMMY\n\n")

        choice = (input("Enter Your Choice [1 - 4]: "))

    #return choice
    return choice

#make lists
fname = []
pokemon1 = []
pokemon2 = []
region = []
city = []

#open csv file
with open("w5/Midterm/pokemon.csv") as csvfile:

    #read and append file
    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        pokemon1.append(rec[1])
        pokemon2.append(rec[2])
        region.append(rec[3])
        city.append(rec[4])

#display menu
answer = menu()

print('\n--------------------------------------------------\n')

#starting variables
snore = 0
geng = 0
charm = 0
kanto = 0
lav = 0

#While Loop start----------------------------------------------------
while answer != '4':

    #display all file data
    if answer == '1':

        print("\n\t-- Showing all Data --")

        print(f"\n\n{'FIRST':8}  |  {'POKEMON 1':13}  |  {'POKEMON 2':13}  |  {'REGION':7}  |  {'CITY':15}")
        print("------------------------------------------------------------------------------------")

        for i in range(0,len(fname)):

            print(f"{fname[i]:8}  |  {pokemon1[i]:13}  |  {pokemon2[i]:13}  |  {region[i]:7}  |  {city[i]:15}")

            print('---------------------------------------------------------------------------------')

    #display all pokemon
    if answer == '2':

        print("\n\t-- Showing Pokemon --")

        for i in range(0,len(fname)):

            print(f"\n\n{pokemon1[i]:13}  |  {pokemon2[i]:13}")

            print('--------------------------------------------')

    #gather stats
    if answer == '3':

        print("\t-- Showing Stats --")

        for i in range(0, len(fname)):

            if pokemon1[i] == "Snorlax" or pokemon2[i] == "Snorlax":

                snore += 1


            if pokemon1[i] == "Gengar" or pokemon2[i] == "Gengar":

                geng += 1


            if pokemon1[i] == "Charmander" or pokemon2[i] == "Charmander":

                charm += 1


            if region[i] == "Kanto":

                kanto += 1


            if city[i] == "Lavender Town":

                lav += 1

        #display stats
        print(f"\n\nSnorelax was chosen {snore} times!")
        print(f"Gengar was chosen {geng} times!")
        print(f"Charmander was chosen {charm} times!")
        print(f"Kanto was the most popular region and was chosen {kanto} times!")
        print(f"Lavender Town was the most popular city in the Kanto region chosen {lav} times!")

        print('\n-------------------------------------------------------------------------------------------')

    #show menu again 
    answer = menu()

#While Loop end------------------------------------------------------------------------------------------
        
#goodbye 
print("\nGoodbye :)\n")