#Name: Hendry
#Date 3/11/24
#Class Lab w4
#Course name: SE126
#Program Prompt: 

#variable dictionary:

#------------------------------------------------------------------------

#Lists
num_list = [' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
seat1 = ['A','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat2 = ['B','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat3 = ['C','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat4 = ['D','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat5 = ['E','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat6 = ['F','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat7 = ['G','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat8 = ['H','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat9 = ['I','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat10 = ['J','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat11 = ['K','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat12 = ['L','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat13 = ['M','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat14 = ['N','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat15 = ['O','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat16 = ['P','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat17 = ['Q','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat18 = ['R','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat19 = ['S','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat20 = ['T','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat21 = ['U','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat22 = ['V','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat23 = ['W','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat24 = ['X','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat25 = ['Y','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat26 = ['Z','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat27 = ['1','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat28 = ['2','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat29 = ['3','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
seat30 = ['4','#','#','#','#','#','#','#','#','#','#','#','#','#','#']


seats_sold = []

#funtions------------------------------------------------------------------

def menu():

    print("\n\n1. Purchase Seat(s)")
    print("2. View Total Ticket Sales")
    print("3. View Sales Information")
    print("4. Checkout")
    print("5. Quit")

    response = input("Pick action [1-5]")

    if response != '1' and response != '2' and response != '3' and response != '4' and response != '5':
        
        print("*ERROR*")
        
        response = input("Pick action [1-5]")


    return response

def row_get():#function will get the row choice from the user

    row_choice = -1 #initalize the row

    while row_choice < 1 or row_choice > 7:

        try:
            row_choice = int(input("\n\t\tEnter the ROW you wish to sit in [1-7]: "))

            if row_choice < 1 or row_choice > 7:
                print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-7]")

        except:#will not show an error if you enter a string(ex:letter) but will ask you to enter a valid row choice
            print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-7]")
    
    
    return row_choice


def seat_get():#function will get the seat choice from the user
    acceptable_seats = ["A", "B", "C", "D"]

    seat_choice = input("\t\tEnter the SEAT you wish to sit in: ").upper()

    while seat_choice not in acceptable_seats:#will only accept actual seats
        seat_choice = input("\n\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ").upper()

    return seat_choice


def more_seats():#ask the user if they want to continue to add more seats

    choice = input("\n\t\tDo you want to continue to add more seats [Y/N]: ").upper()

    return choice

def map():

    print(f"{'Row':46} {'Seats'}")

    for i in range(0,15):
        print(f"{num_list[i]:5} {seat1[i]:2} {seat2[i]:2} {seat3[i]:2} {seat4[i]:2} {seat5[i]:2} {seat6[i]:2} {seat7[i]:2} {seat8[i]:4} {seat9[i]:2} {seat10[i]:2} {seat11[i]:2} {seat12[i]:2} {seat13[i]:2} {seat14[i]:2} {seat15[i]:2} {seat16[i]:2} {seat17[i]:2} {seat18[i]:2} {seat19[i]:2} {seat20[i]:2} {seat21[i]:2} {seat22[i]:4} {seat23[i]:2} {seat24[i]:2} {seat25[i]:2} {seat26[i]:2} {seat27[i]:2} {seat28[i]:2} {seat29[i]:2} {seat30[i]:2} {seat3[i]:2}")

#------------------------MAIN--------------------------------------------------------

#variables 

sold_seat = 0
seats_avail = 450
tickets = 0
cost = 0
row1_5 = 200
row6_10 = 175
row11_15 = 150

answer = "Y"

row = []
seat = []


menu_choice = menu()

while menu_choice != '5':

    if menu_choice == '1':
        
        map()

        row_input = row_get()
        seat_input = seat_get()

        row.append(row_input)
        seat.append(seat_input)

        tickets += 1

        menu_choice = menu()


    if menu_choice == '4':

        for i in range(0, len(num_list)):

            if seat[i] == 'A':
                if seat1 != "*":
                    seat1[row[i]- 1] = "*"
    
        map()