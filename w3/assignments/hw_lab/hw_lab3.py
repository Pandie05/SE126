#Name: Hendry
#Date 1/26/24
#HW Lab
#Course name: SE126
#Program Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.
#variable dictionary:
#cnt_vote = Number of individuals not eligible to register.
#not_reg = Number of individuals who are old enough to vote but have not registered.
#not_voted = Number of individuals who are eligible to vote but did not vote.
#num_voted = Number of individuals who did vote.
#num_entrd = Number of records processed.

#-------------------------------------------------

#import
import csv

#list---------------------
cnt_vote_list = []
not_reg_list = []
not_voted_list = []
num_voted_list = []

#starting values
cnt_vote = 0
not_reg = 0
not_voted = 0
num_voted = 0
num_entrd = 0

#open csv file
with open("w3/assignments/hw_lab/voters_202040.csv") as csvfile:

    #read file
    file = csv.reader(csvfile)

    #for loop--------------------------------------
    for rec in file:
        #update count
        num_entrd += 1

        #if statements------------------
        if int(rec[1]) < 18:
            cnt_vote += 1

        if rec[2] == "N":
            not_reg += 1

        if rec[3] == "Y":
            num_voted += 1

        else:
            not_voted += 1
                
        #append
        cnt_vote_list.append(cnt_vote)
        not_reg_list.append(not_reg)
        not_voted_list.append(not_voted)
        num_voted_list.append(num_voted)

#for loop end-------------------------------------------------------
        
#final print message
print(f"\n\nBASED ON {num_entrd} ENTRY(s):")
print(f"{cnt_vote} people are not eligible to vote.")
print(f"{not_reg} people are old enough to vote but have not registered.")
print(f"{not_voted} people are eligible to vote but did not vote.")
print(f"{num_voted} people voted")

#goodbyem message
print("\nThank You!!  \nGoodbye :)")