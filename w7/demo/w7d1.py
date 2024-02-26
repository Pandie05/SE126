import csv

#--Functions----------------------



#--Main---------------------------



#--List--

id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open('w7/demo/w7_demoFile.txt') as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

for i in range(0,len(id_stud)):
    print(f"{id_stud[i]} \t {lname[i]} \t {fname[i]}")

search_name = input("Please enter the name you are looking for: ")
found = -1

for i in range(len(id_stud)):
    if search_name.lower() == lname[i].lower():

        found = i

if found != -1:
    print(f"\n\tWe found {search_name} at index {found} ")
    print("\tHere is their info: ")
    print(f"\t\t{fname[found]} \t {lname[found]} \t {id_stud[found]} \t {class1[found]} \t {class2[found]} \t {class3[found]}")

else:
    print(f"\n\tWe could not find {search_name} ")

#bubble sort - - - - - - - - - - - - - - - - - - - - 

nums = [100,75,32,250,47,9,2,3,99,200]

for i in range(0, nums - 1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, nums - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):

            print("\t\t SWAP! ", nums[index], "<-->", nums[index + 1])

            #if above is true, swap places!

            temp = nums[index]

            nums[index] = nums[index + 1]

            nums[index + 1] = temp