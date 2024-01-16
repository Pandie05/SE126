#Name: Hendry
#Date 1/9/24
#Lab #1
#Course name: SE126
#Program Prompt: You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#-------------------------------------------------------

#----FUNCTIONS!!----------------

def difference(ppl, max_cap):

    ans = int(ppl - max_cap)

    return ans  

def decision(response):

    if response.lower() == "y" or response.lower() == "n":
        return response
    
    else:
         
        while response.lower() != "y" and response.lower() != "n":

            print("**ERROR**")

            response = input("Continue?... [y/n]: ")

            return response

#-----------------------MAIN CODE START---------------------------

#welcome message
print("Welcome!!\n")

#starting variable for while loop
response = "y"



#-----------main loop start
while response.lower() == "y":

    #input------
    name = input("\nPlease Enter Meeting Name: ")
    cap = float(input("\nPlease Enter Room Capacity: "))
    num_ppl = float(input("\nPlease Enter Number of People Attending: "))

    ans = difference(cap, num_ppl)

    #check room capacity-----------
    if ans >= 0:
        print(f"[[\nThis room meets fire safety! {ans} more people can be added]]")

    else:
        print(f"[[\nThis room does NOT meet fire safety! {ans * -1} people need to be removed]]")

    #redo loop?---
        
    response = decision(input("\nWould you like to check another meeting room [y/n]: "))
#----------------loop end------


#goodbye message
print("\n\nGoodbye :)")