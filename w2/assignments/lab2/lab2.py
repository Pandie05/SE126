#Name: Hendry
#Date 1/23/24
#In Clas Lab
#Course name: SE126
#Program Prompt: Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.
#variable dictionary:
#ttl_rcd = total records processed
#rms_ovr = rooms over the maximum allowed number
#max = maximun allowed guests per room
#min = current number of guests in room
#---------------------------------------------
import csv

#ttl counter
ttl_records = 0

print(f"\n{'TYPE':8} {'MANU':8} {'PROC':6} {'PROC':6} {'RAM':6} {'HDD1':6} {'#HDD':6} {'HDD2':6} {'YEAR':6}")
print("----------------------------------------------------------------")

with open("w3/demo/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #print(rec) #shown as list

        #keep count
        ttl_records += 1

        #Filter for Display

        #--comp type-- rec[0]

        if rec[0] == "D":
            comp_type = "Desktop"

        elif rec[0] == "L":
            comp_type = "Laptop"

        else:
            comp_type = "*ERROR -- " + str(rec[0])

        #--manufacturer--rec[1]
        if rec[1] == "DL":
            manu = "Dell"

        elif rec[1] == "GW":
            manu = "Gateway"
        
        elif rec[1] == "HP":
            manu = rec[1]

        else:
            manu = "*ERROR -- " + str(rec[1])

       #--processor / ram / hdd_1 / num_hdd - exact from file

        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd =rec[5]

        if rec[5] == "1":
            hdd_2 = "   "#"---" #none
            os = rec[6]
            year = rec[7]

        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        
        else:
            hdd_2 = "ERROR -- " + str(rec[5])
            os = "ERROR"
            year = "ERROR"




        #final print for each record
        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:6} {hdd_2:6} {os:6} {year:6}")

#----DISCONNECTED FROM FILE-------------------------------------

print("----------------------------------------------------------------")
print(f"TOTAL RECORDS: {ttl_records}")