def printString():
    score = 90
    scoreString = str(score)
    print("Your score is " + scoreString)

def check_int_number():
    while True:
        number = input("Enter string")
        try:
            number = int(number)
            break
        except:
            print("Enter again")
    print(number)


#calculate BMI
def check_valid_input(infor):
    while True:
        try:
            value = float(input(infor))
            if(value <= 0 ):
                print("The number must be greater than 0")
                continue
            return value
        except ValueError:
            print("Invalid number ! Please enter number again")

def calculateBMI():
    weight = check_valid_input("Enter your weight:\n")
    height = check_valid_input("Enter your height:\n")
    BMI = weight / (height ** 2)
    print("Your BMI is: ", round(BMI,1))

calculateBMI()

