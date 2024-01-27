#Name: Hendry
#Date 1/26/24
#HW Lab
#Course name: SE126
#Program Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.
#variable dictionary:

import csv

with open("w3/assignments/hw_lab/voters_202040.csv") as csvfile:

    #read file
    file = csv.reader(csvfile)

    for rec in file:
        print(" ")