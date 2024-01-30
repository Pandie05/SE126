#Name: Hendry
#Date 1/23/24
#Class Lab w4
#Course name: SE126
#Program Prompt: 
#Part 1
#Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

#Part 2
#Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.  

#Part 3
#After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student.

#variable dictionary:


#--------------------------------------------------------------------------------------
#import
import csv

#create list
fname = []
lname = []
test1 = []
test2 = []
test3 = []

with open("w4/assignments/class_lab/listPractice1.txt") as csvfile:

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

#process list
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t")

#calculate student average
avg = 0
ttl_cnt = 0

average = []

for i in range(0, len(test1)):

    #calculate average
    avg = (test1[i] + test2[i] + test3[i]) / 3

    #append
    average.append(avg)


print(f"\n\n{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} {'AVERAGE'}")
print("-----------------------------------------------------------------------")

#process list
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {average[i]:.1f}")

print(f"\n\n{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} {'AVERAGE'} {'GRADE'}")
print("--------------------------------------------------------------------------")

let_grade = []

for i in range(0, len(fname)):
    if average[i] >= 90:
        let_grade.append('A')

    elif average[i] >= 80:
        let_grade.append('B')

    elif average[i] >= 70:
        let_grade.append('C')

    elif average[i] >= 60:
        let_grade.append('D')

    else:
        let_grade.append('F')

for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {average[i]:.1f} \t {let_grade[i]}")

