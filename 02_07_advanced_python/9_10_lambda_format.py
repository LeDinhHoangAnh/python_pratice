def plusNumber():
    number_input = int(input("Enter number: "))
    x3 = lambda x: x + x
    print(f"Value of calculating is: {x3(number_input)}")
def arrangeByAge():
    people = [("Charlie", 30),("Alice", 25), ("Bob", 20)]
    people_sorted = sorted(people, key=lambda x: x[0])
    print(people_sorted) 

def filterEvenNumber():
    list_number = [1,2,3,4,7,8,9]
    even_number = list(filter(lambda x: x % 2 == 0, list_number))
    print(f"List even number: {even_number}")

def squareList():
    list_number = [6,7,8,9]
    square_list = list(map(lambda x: x**2, list_number))
    print(f"Square of list: {square_list}")

plusNumber()
arrangeByAge()
filterEvenNumber()
squareList()