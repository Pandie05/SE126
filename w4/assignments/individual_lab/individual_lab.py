#Name: Hendry
#Date 2/5/24
#Idividual Lab W4
#Course name: SE126
#Program Prompt: Process the lists to print the them as they appear in the file
#Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)
#Re-Process the lists to print each record fully with the House Mottos
#Re-process the lists to find the average age within the list, then
#Print the total number of people in the list
#Print the average age - rounded to a whole number {:.0f}
#Print tallies/final counts for each allegiance (Field4)
#--------------------------------------------------------------------------------------
#import
import csv

#create lists
fname = []
lname = []
age = []
nickname = []
house = []

#open csv file
with open("w4/assignments/individual_lab/lab4A_GOT_NEW.txt") as csvfile:

    #read csv file
    file = csv.reader(csvfile)

    #for loop to append list
    for rec in file:

        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])

#disconnected from file--------------------------------------------

#headig
print(f"{'FIRST':15}  {'LAST':13}  {'AGE':3} \t {'NICKNAME':20}  {'HOUSE':20}")
print("-------------------------------------------------------------------------------------------------------")

#for loop to print formated lists outputs
for i in range(0, len(fname)):

    print(f"{fname[i]:15}  {lname[i]:13}  {age[i]:3} \t {nickname[i]:20}  {house[i]:20}")

print("-------------------------------------------------------------------------------------------------------")

#list for mottos
motto = []

#variables to count
stark = 0
bara = 0
tully = 0
watch = 0
lanni = 0
targ = 0

#for loop to append motto to respective house / to keep count of how many people in each houe
for i in range(0, len(fname)):

    if house[i] == "House Stark":
        stark += 1
        motto.append('Winter is Coming')
    
    if house[i] == "House Baratheon":
        bara += 1
        motto.append('Ours is the fury.')

    if house[i] == "House Tully":
        tully += 1
        motto.append('Family. Duty. Honor.')

    if house[i] == "Night's Watch":
        watch += 1
        motto.append('And now my watch begins.')

    if house[i] == "House Lannister":
        lanni += 1
        motto.append('Hear me roar!')

    if house[i] == "House Targaryen":
        targ += 1
        motto.append('Fire & Blood')


#heading
print(f"\n\n{'FIRST':15}  {'LAST':13}  {'AGE':3} \t {'NICKNAME':20}  {'HOUSE':20}   {'MOTTO'}")
print("-------------------------------------------------------------------------------------------------------")

#for loop to print formated output + mottos
for i in range(0, len(fname)):

    print(f"{fname[i]:15}  {lname[i]:13}  {age[i]:3} \t {nickname[i]:20}  {house[i]:20}  {motto[i]:20}")

print("-------------------------------------------------------------------------------------------------------")

#variables for calculating avg age
age_count = 0
avg_age = 0

#avg age calc
for i in range(0, len(fname)):

    age_count += age[i]

    avg_age = age_count / len(fname)


#final tally outputs----------------------------------------------------------
print("\n\nFinal Tallies:")
print("------------------------------------")

print(f"\nTotal Number of People in List: {len(fname)}")
print(f"Average Age: {avg_age:.0f}")

print(f"\nTotal Number of People in House Stark: {stark}")
print(f"Total Number of People in House Baratheon: {bara}")
print(f"Total Number of People in House Tully: {tully}")
print(f"Total Number of People in Night's Watch: {watch}")
print(f"Total Number of People in House Lannister: {lanni}")
print(f"Total Number of People in House Targaryen: {targ}")