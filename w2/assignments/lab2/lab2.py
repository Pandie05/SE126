#Name: Hendry
#Date 1/23/24
#Lab 2
#Course name: SE126
#Program Prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file. Organization of the csv file:
#variable dictionary:
#ttl_records = total records recorded in file
#comp_type = computer type
#manu = manufacturer
#processor = processor -_-
#ram = ram in computer
#hdd_1 = hard disk drive 1
#num_hdd = number of hdd
#hdd_2 = hard disk drive 2
#os = operating system
#year = year computer was made

#---------------------------------------------
#import
import csv

#ttl counter
ttl_records = 0

#header
print(f"\n{'TYPE':8} {'Brand':8} {'Cpu':6} {'RAM':6} {'HDD1':6} {'#HDD':3} {'HDD2':6} {'OS':5} {'YEAR':6}")
print("----------------------------------------------------------------")

#open csv file
with open("w3/demo/lab2b.csv") as csvfile:

    #read file
    file = csv.reader(csvfile)

    #for loop-------------------------------------------------
    for rec in file:

        #keep count
        ttl_records += 1

        #Filter for Display------

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
        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:3} {hdd_2:6} {os:6} {year:6}")

#----DISCONNECTED FROM FILE-------------------------------------

print("----------------------------------------------------------------")
print(f"TOTAL RECORDS: {ttl_records}")