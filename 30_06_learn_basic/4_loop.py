#count odd number and even number from 1 to n
n = int(input('Enter n:'))
odd_number = even_number = 0

for i in range (1,n+1):
    if i % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
print("Amount of odd number", odd_number)
print("Amount of even number: ", even_number)

# Enter an int number, if this number is not an int number, require to enter again
while True:
    n = input("Enter an integer number: ")
    try:
        n = int(n)
        break 
    except ValueError:
        print("Invalid number! Please enter again.")

print("You entered:", n)


