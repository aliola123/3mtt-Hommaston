#All functions defined here
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    else:
        return a / b

print("Hi there, Welcome to my simple Calculator, Below are the operations you can carry out:")

print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")

operation = input("Enter operation Number e.g 1 for Addition, or 5 to Exit: ")

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

if operation == "1":
    print(f"RESULT: Sum of {firstNum} and {secondNum} is", addition(firstNum, secondNum))
elif operation == "2":
    print(f"RESULT: Difference of {firstNum} and {secondNum} is", subtraction(firstNum, secondNum))
elif operation == "3":
    print(f"RESULT: Multiplication of {firstNum} and {secondNum} is", multiplication(firstNum, secondNum))
elif operation == "4":
    print(f"RESULT: Division of {firstNum} and {secondNum} is", division(firstNum, secondNum))