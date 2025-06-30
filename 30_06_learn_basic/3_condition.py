# Compare between to number

def compareNumber():
    number_1 = float(input("Enter number 1: "))
    number_2 = float(input("Enter number 2: "))

    if number_1 > number_2:
        print("Number 1 is bigger than numbber 2")
    elif (number_1 < number_2):
        print("Number 1 is smaller than number 2")
    else:
        print("Number 1 is equal to number 2")

# Find max number in three number
def findMaxNumber():
    number_1 = int(input("Enter number 1: "))
    number_2 = int(input("Enter number 2: "))
    number_3 = int(input("Enter number 3: "))

    if number_1 >= number_2 and number_1 >= number_3:
        print("Max number is: ", number_1)
    elif number_2 >= number_1 and number_2 >= number_3:
        print("Max number is: ", number_2)
    else :
        print("Max number is: ", number_3)

# Rating point of student

def ratingPoint():
    while True:
         point = float(input("Enter point of student: "))

         if point <= 0 or point >= 10:
                print("Invalid point ! Point must be in range 0 to 10")
                continue                
         if point >= 0 and point <= 7:
                print("Normal point")
         elif point >7 and point <= 9:
                print("Good")
         else:
                print("Excelent")
ratingPoint()