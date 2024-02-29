#Name: Hendry
#Date 2/28/24
#Class Lab #5
#Course name: SE126
#Program Prompt: In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file below. You will perform both sequential search as well as binary search. See the lab prompt for further details. 
#--------------------------------------------------------------------------------------

import csv

#FUNCTIONS---------------------------------

#menu------------------------

def menu():

    print("\n\n1. See All Student Report")
    print("2. Search for a Student [ID]")
    print("3. Search for a Student [Last]")
    print("4. View a Class Roster [class1, class2, and class3]")
    print("5. Exit/Quit Program")

    choice = input("\n\nWhich action would you like to do? [1-5] ")

    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':

        print("\n\t* ERROR * wrong input try again")

        choice = input("\nWhich action would you like to do? [1-5] ")

    return choice

#MAIN CODE----------------------------------------------------------

#LIST-----------------
id = []
last = []
first = []
class1 = []
class2 = []
class3 = []

#OPEN AND READ FILE--------------------------------------------
with open('w7/assignment/lab5_students.txt') as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id.append(rec[0])
        last.append(rec[1])
        first.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#show user menu
menu_choice = menu()

#MAIN LOOP- - - - - - - - - - - - - - - - - - - - 
while menu_choice != '5':


#PART1 ----------------- SHOW ALL FILE DATA --------------------------
    if menu_choice == '1':

        print(f"\n\n{'ID':10}{'LAST':10}{'FIRST':13}{'CLASS1':10}{'CLASS2':10}{'CLASS3':10}")

        print('-------------------------------------------------------------------')

        for i in range(0, len(id)):
            print(f"{id[i]:10}{last[i]:13}{first[i]:10}{class1[i]:10}{class2[i]:10}{class3[i]:10}")


        input('Press ENTER to continue... ')
        menu_choice = menu()

#PART 2 --------------------- BINARY SEARCH FOR ID ---------------------

    if menu_choice == '2':

        search_name = input("Enter the ID you are looking for: ")

        min = 0
        max = len(id) - 1
        mid = int((min + max ) / 2)

        while (min < max and search_name != id[mid]):

            if search_name < id[mid]:
                max = mid - 1

            else:
                min = mid + 1

            mid = int((min + max ) / 2)

        if search_name == id[mid]: 
        
            print(f"\n\t\t{first[mid]} \t{last[mid]} \t{id[mid]} \t{class1[mid]}\t{class2[mid]}\t{class3[mid]}")

        else:
    
            print(f"\n\tWe could not find {search_name}")
            print("\tPlease try again.\n")
        

        input('Press ENTER to continue... ')
        menu_choice = menu()

#PART 2 ----------------------- BINARY SEARCH FOR LAST -------------------------
        
#this part only works with exact capitalization
#i tried to figure it out (i know its probably really simple) but this assignment is already late enough


    if menu_choice == '3':

        search_name = input("Enter the LAST NAME you are looking for: ")

        min = 0
        max = len(last) - 1
        mid = int((min + max ) / 2)

        while (min < max and search_name != last[mid]):

            if search_name < last[mid]:
                max = mid - 1

            else:
                min = mid + 1

            mid = int((min + max ) / 2)

        if search_name == last[mid]:
        
            print(f"\n\t\t{first[mid]} \t{last[mid]} \t{id[mid]} \t{class1[mid]}\t{class2[mid]}\t{class3[mid]}")

        else:
    
            print(f"\n\tWe could not find {search_name}")
            print("\tPlease try again.\n")


        input('Press ENTER to continue... ')
        menu_choice = menu()

# ----------------------- SEQ SEARCH FOR CLASS ROSTER ------------------------------

    if menu_choice == '4':

        search_name = input("Please enter a class roster: ")

        found = []

        for i in range(0, len(id)):

            if search_name.lower() == class1[i].lower():

                found.append(i)

        for i in range(0, len(id)):
                
                if search_name.lower() == class2[i].lower():

                    found.append(i)

        for i in range(0, len(id)):

            if search_name.lower() == class3[i].lower():

                found.append(i)


        if found[0] != "":

            print(f"\n\tWe found {search_name} at index {found} ")
            print("\tHere is their info: ")

            print(f"\t\t{'ID':10} {'FIRST':13} {'LAST':10}")
            print("\t\t-------------------------------")

            for i in range(0, len(found)):

                print(f"\t\t{id[found[i]]:10} {first[found[i]]:13} {last[found[i]]:10}")

        else:
            print(f"\n\tWe could not find {search_name} ")


        input('Press ENTER to continue... ')
        menu_choice = menu()


print("Goodbye :) ")
