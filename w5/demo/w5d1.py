#w5D1 1D list review + function review + sequesnsial search

import csv 

lname = []
fname = []
test1 = []
test2 = []
test3 = []

num_avg = []
let_avg = []

#function----------------------------

def menu():

    print("\n\n~CLASS ACOUNT MENU~")
    print("1. Show All Students")
    print("2. Show Roster Only")
    print("3. Search for a Student")
    print("4. Exit")

    choice = int(input("Enter Your Choice [1 - 4]: "))

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("*INVALID ENTRY* DIGITS 1 - 4 ONLY DUMMY")

        choice = int(input("Enter Your Choice [1 - 4]: "))

    return choice

def seq_search(search_term):
     
    found_index = ""

    for i in range(0, len(lname)):

        if lname[i] == search_term:
            found_index = i

    return found_index

         


#file connection / list population-------------------
with open("w5/demo/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        lname.append(rec[0])
        fname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disc from file------------

#header
print(f"{'LAST':12} \t{' FIRST':12} \t{'test1':4} \t{'test2':4} \t{'test3':4} \t{'avg':5} {'let avg':3}")
print("----------------------------------------------------------------------------------")

for i in range(0,len(fname)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(avg)

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    elif avg < 60:
        leter = "F"
    else:
        letter = "ERROR @ I:" + str[i]

    let_avg.append(letter)

for i in range(0, len(lname)):
    print(f"{lname[i]:12} \t {fname[i]:12} \t {test1[i]:4} \t {test2[i]:4} \t {test3[i]:4} \t {num_avg[i]:5.1f} \t {let_avg[i]:3}")

print("----------------------------------------------------------------------------------")


#main code----------------------------------
menu_choice = menu()

while menu_choice != 4:

    if menu_choice == 1:
        print("\n\t--Showing all file data--")

    if menu_choice == 2:
        print("\n\t--Showing class roster--")

    if menu_choice == 3:
        print("\n\t--Search for a student--")

        search = input("Enter last name yo are looking for: ")

        found = seq_search(search)

        if found != "":
            (f"{lname[found]:12} \t {fname[found]:12} \t {test1[found]:4} \t {test2[found]:4} \t {test3[found]:4} \t {num_avg[found]:5.1f} \t {let_avg[found]:3}")

        else:
            print("The student {search} could not be found :(")
        
    menu_choice = menu()

input("\n\nEnter to Continue...")

