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
#dsk_cnt = desktop count
#dsk_mny = desktop cost
#ltp_cnt = laptop count
#ltp_mny = laptop cost


#----------------------------------------------------------------------------

import csv

#ttl counter
ttl_records = 0

#create lists
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []

#outline
print(f"\n{'TYPE':8} {'MANU':8} {'PROC':6} {'PROC':6} {'RAM':6} {'HDD1':6} {'#HDD':6} {'HDD2':6} {'YEAR':6}")
print("----------------------------------------------------------------")

#open file
with open("w3/demo/lab2b.csv") as csvfile:

    #read file
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
        num_hdd = rec[5]

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


        #append-----------------------------
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)


        #final print for each record
        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:6} {hdd_2:6} {os:6} {year:6}")

#----DISCONNECTED FROM FILE-------------------------------------

#starting values
dsk_cnt = 0
dsk_mny = 0
ltp_cnt = 0
ltp_mny = 0

#for loop (desktop) -----------------------------------------
for index in range(0, len(comp_type_list)):

    if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:

        #change count for each desktop and add hopw much each costs
        dsk_cnt += 1
        dsk_mny += 2000

#for loop (laptop) --------------------------------------------
for index in range(0, len(comp_type_list)):

    if comp_type_list[index] == "Laptop" and int(year_list[index]) <= 16:

        #change count for each laptop and add hopw much each costs
        ltp_cnt += 1
        ltp_mny += 1500


#Final Print Statements-------------------------------------------------------------
print("----------------------------------------------------------------")
print(f"TOTAL RECORDS: {ttl_records}\n")

print(f"To replace {dsk_cnt} it will cost ${dsk_mny}")
print(f"To replace {ltp_cnt} it will cost ${ltp_mny}")