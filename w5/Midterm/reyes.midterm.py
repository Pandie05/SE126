#Name: Hendry
#Date 2/11/24
#Midterm
#Course name: SE126
#Program Prompt: For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.
#--------------------------------------------------------------------------------------

#import
import csv

#functions
def menu():

    print(f"{'FIRST':8}  |  {'POKEMON1':13}  |  {'POKEMON2':13}  |  {'REGION':7}  |  {'CITY':15}")
    print("------------------------------------------------------------------------------------")

fname = []
pokemon1 = []
pokemon2 = []
region = []
city = []


with open("w5/Midterm/pokemon.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        pokemon1.append(rec[1])
        pokemon2.append((rec[2]))
        region.append(rec[3])
        city.append(rec[4])

menu()

for i in range(0,len(fname)):

    print(f"{fname[i]:8}  |  {pokemon1[i]:13}  |  {pokemon2[i]:13}  |  {region[i]:7}  |  {city[i]:15}")

    print('---------------------------------------------------------------------------------')



