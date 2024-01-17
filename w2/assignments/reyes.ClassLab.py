#Name: Hendry
#Date 1/17/24
#In Clas Lab
#Course name: SE126
#Program Prompt: Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.
#variable dictionary:
#ttl_rcd = total records processed
#rms_ovr = rooms over the maximum allowed number
#max = maximun allowed guests per room
#min = current number of guests in room

#-------------------------------------------------------

#import
import csv 

#initial values
ttl_rcd = 0
rms_ovr = 0

#open csv file
with open("w2/assignments/lab2a.csv") as csvfile:
    
    #reading csv file
    file = csv.reader(csvfile)
    

#for loop start---------------------
    for rec in file:
        #keeping count of how many records were processed
        ttl_rcd += 1

        max = rec[1]
        min = rec[2]

        if min > max:

            #keeping count of how many rooms are over the limit
            rms_ovr += 1

#for loop end------------------


#final output + formating
print("{0:18} \t {1:5} \t {2:5} \t {3:5}".format("Room", "Max", "Min", "Over"))
print("-------------------------------------------------")

print("{0:18} \t {1:5} \t {2:5} \t {3:5}".format("Captain's Quarters", "300", "350", "50"))
print("{0:18} \t {1:5} \t {2:5} \t {3:5}".format("Federation", "375", "425", "50"))
print("{0:18} \t {1:5} \t {2:5} \t {3:5}".format("Voyager", "100", "102", "2"))

print(f"\n\nProcessed {ttl_rcd} records")
print(f"There are {rms_ovr} rooms over the limit\n")

input("Press any key to continue . . . ")
    