"""
List is ordered, mutable list
Tuple is ordered, immutable list
Set is unordered, non-duplicated set
Dictionary: key - value
"""
#List
cars = ["Vinfast", "Honda", "Mazda", "Kia"]
print(cars[-4]) #print ["Vinfast"]
print(cars[0:4]) #print from index 0 to index 3
cars.append("Maserati") #add car in end of list
cars.insert(2, "Toyota") #insert into index 2 of list with value "Toyota"
cars.remove("Maserati") #remove "Maserati" from cars list
print(cars)


cars[0:3] = ["Lamborghini", "Nissan", "Ford", "Hyndai"] #replace from index 0 to 2 with this value
print(cars)

#Function check exist car to check car is exist or not in cars list
def check_exist_car():
    car = str(input("Enter name of car:\n"))
    if car in cars:
        print(f"{car} in list ")
        print("Number of car: ",len(cars))
    else:
        print(f"{car} is not in list")

#Tuple
colors = ("green", "blue", "red", "black")
print(colors) #print all value in tuple
print(colors[1:]) #print from index 1 to end of tuple

#Add another value to tuple through convert into list
convert_list = list(colors)
convert_list.append("orange")
colors = tuple(convert_list)
print(colors)

#Asterisk * to assign the variable name and the value as a list
(hot_tone,*cold_tone) = colors
print(hot_tone)
print(cold_tone)

#Set
devices = {"computer", "mouse", "keyboard", "earphone"}
devices.remove("computer") #remove value computer in set
print(devices)

devices.add("PC") #add PC to set
print(devices)

#Dictionary

car_brand = {
    "brand": "Honda",
    "model": "CR-V",
    "year" : 1966,
    "number_seat" : 5
}

print(car_brand["brand"])
print(len(car_brand))

car_brand.update({"model" : "BR-V"})
print(car_brand)

print(car_brand.keys())  #print all keys
print(car_brand.values()) #print all values
print(car_brand.items()) #print all key-value
