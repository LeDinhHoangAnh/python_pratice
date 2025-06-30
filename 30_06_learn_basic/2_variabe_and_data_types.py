# Decalre 3 variable about name, age and job. Print into screen information
name = "Hoang Anh"
age = 24
job = "IT"

print(f"Hello, My name is {name}, I am {age}, and my job is {job}")

# Calculate perimeter and area of rectangle with given length and width
width_size = 15
length_size = 20

perimeter_of_rectangle = (width_size + length_size) *2
area_of_rectangle = width_size * length_size

print("Perimeter of rectangle: ", perimeter_of_rectangle)
print("Area of rectangle: ", area_of_rectangle)

# Check data types of variable
a = 10
b = 7.10
c = "Hello"
d = True
e = None

print(type(a), type(b), type(c), type(d), type(e))

# Many values to Multiple Variables

name_of_fruit1, name_of_fruit2, name_of_fruit3 = "Apple", "Orange", "Watermelon"
print(name_of_fruit1)

# One value to Multiple Variables
name_person1 = name_person2 = name_person3 = "Hoang"
print(name_person1)

# Scope of object

car_name = "VF5"

def printCarName():
    car_name = "VF9"
    print("This car name is", car_name)

printCarName()
print("This car name is", car_name)


