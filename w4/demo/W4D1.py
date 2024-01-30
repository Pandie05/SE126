import csv

#create 1D list

fname = []
lname = []
test1 = []
test2 = []
test3 = []

#open file
with open("w4/demo/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #store data from file fields to their list
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconneced from file-----------------------

#heading
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("-----------------------------------------------------------------------")

#process the list
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")

#calculate student average
avg = 0
ttl_cnt = 0

average = []

for i in range(0, len(test1)):

    #calculate average
    avg = (test1[i] + test2[i] + test3[i]) / 3

    #append
    average.append(avg)


print(f"\nFIRST \t\t AVERAGE")

#display
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:8.1f}")

#sequential search -> in sequence
low_name = ""
low_avg = 100

for i in range(0, len(average)):

    #determine if current average is lower than low_avg
    if average[i] < low_avg:
        low_avg = average[i]

        low_name = fname[i]

#display total students
print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")

#2d list---------------------------------------------------------------------------------------
#use 1d list to populate 2d list
all_students = []

for i in range(0, len(fname)):

    #add sudent data to their place in 2d list
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

print("----2D - LIST----------------------")
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}, {'AVERAGE'}")
print("-----------------------------------------------------------------------")

for i in range(0, len(all_students)):
    print(f"{all_students[i]}")



    for i in range(0, len (all_students[i])):
    
        for x in range(0, len(all_students[i])):
            print(f"{all_students[i][x]}", end="\t")

        print()