# main.py

from math_module import add, subtract, multiply, divide
from logger_module import log_operation
from log_reader import LogIterator

add = log_operation(add)
subtract = log_operation(subtract)
multiply = log_operation(multiply)
divide = log_operation(divide)

print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(2, 6))
print("Divide:", divide(8, 2))


print("\n History log:")
for log in LogIterator("operation.log"):
    print(log)
