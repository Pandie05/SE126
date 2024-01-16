#import
import csv

#init
ttl_rcd = 0
ttl_sal = 0

#init empty list - 1 list per field
names = []
ages = []
salaries = []

#connect file
with open("w2/demo/example.csv") as csvfile:

    #read file
    file = csv.reader(csvfile)

    #read each rec in file
    for rec in file:

        #display
        print(f"{rec[0]:10} \t{rec[1]:3} \t{rec[2]:10}")

        #store data from rec list to list
        #add data to list ---> .append() ; requires LIST NAME as starting object

        names.append(rec[0])
        ages.append(int(rec[1]))
        salaries.append(float(rec[2]))

        #keep count of num of records
        ttl_rcd += 1

        #keep running count of sal
        ttl_sal += float(rec[2])


print(f"TOTAL RECORDS: {ttl_rcd} | TOTAL SALARY: ${ttl_sal:.2f}")

#process the list to display text file information
#PROCESS LIST --> FOR LOOP!

for index in range(0, ttl_rcd):

    print(f"INDEX: {index} \t {names[index]} is {ages[index]} years old")

#process through list to create total age value
ttl_age = 0

for index in range(0, ttl_rcd):
    ttl_age += ages[index]

avg_age = ttl_age / ttl_rcd

print(f"AVERAGE AGE:{avg_age:.2f}")