def get_row():
    row = -1

    while row < 1 or row > 7:

        try:
            row = int(input("\\t\tEnter the ROW you would like to sit in: "))

        except:
            print("\t\t *ERROR* ")

        return row

def get_seat():

    accept_seats = ['A','B','C','D']



l1 = ['1','2','3','4','5','6','7']
l2 = ['A','A','A','A','A','A','A']
l3 = ['B','B','B','B','B','B','B']
l4 = ['C','C','C','C','C','C','C']
l5 = ['D','D','D','D','D','D','D']

selected = []

answer = 'y'

while answer == 'y':
    print('\t\t-------------------------------------')
    print(f"\t\t{'|':5} {'ROW #':8}  {'-  -':12} {'-  -':5}  | ")

    for i in range(0,len(l1)):
        
        print(f"\t\t{'|':5}  {l1[i]:8} {l2[i]}  {l3[i]:10}{l4[i]}  {l5[i]}   | ")

    print('\t\t-------------------------------------')

    row = input("Enter the ROW you would like to sit in: ")
    seat = input("Enter the SEAT you would like to sit in: ")

    answer = ''


if seat == 'A':

    if seat[row - 1] != 'X':
        seat[row - 1] = 'X'