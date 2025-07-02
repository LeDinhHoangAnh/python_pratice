import sys
import argparse

def argument():
    if len(sys.argv) == 3:
        name = sys.argv[1]
        age = sys.argv[2]
        print(f"Hello {name}, you are {age} years old.")
    else:
        print("Insert name and age")

def argparse_pratice():
    parser = argparse.ArgumentParser(description="Calculate with two numbers")
    parser.add_argument("a", type=int, help="First number:")
    parser.add_argument("b",type=int, help = "Second number:")
    parser.add_argument("-o", "--operation", choices=["add","sub"], default="add", help="Calculating")
    args = parser.parse_args()
    if args.operation == "add":
        result = args.a + args.b
    else:
        result = args.a - args.b
    print(f"Result of two number: {result}")


argument()
argparse_pratice()