#Name: Hendry
#Date 1/23/24
#Class Lab w4
#Course name: SE126
#Program Prompt: In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file below. You will perform both sequential search as well as binary search. See the lab prompt for further details. 

#variable dictionary:


#--------------------------------------------------------------------------------------

import csv

#FUNCTIONS---------------------------------

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

#LIST-----------------
id = []
last = []
first = []
class1 = []
class2 = []
class3 = []

with open('w7/assignment/lab5_students.txt') as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id.append(rec[0])
        last.append(rec[1])
        first.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])


menu_choice = menu()

if menu_choice == '1':
    print()


if menu_choice == '2':
    print()


if menu_choice == '3':
    print()


if menu_choice == '4':

    search_name = input("Please enter the name you are looking for: ")
    found = -1

    for i in range(len(id)):
        if search_name.lower() == last[i].lower():

            found = i

    if found != -1:
        print(f"\n\tWe found {search_name} at index {found} ")
        print("\tHere is their info: ")
        print(f"\t\t{first[found]} \t {last[found]} \t {id[found]} \t {class1[found]} \t {class2[found]} \t {class3[found]}")

    else:
        print(f"\n\tWe could not find {search_name} ")

