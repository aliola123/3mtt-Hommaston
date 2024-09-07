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

print("Hi there, Welcome to my simple Calculator, Below are the operations you can carry out:")

while True: #runs the calculator continously unless a user decides to quit
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exit")

    # Prompt users for the operation to be performed 
    operation = input("Enter operation Number e.g 1 for Addition, or 5 to Exit: ")

    if operation == "5":
        break

    #Check if what user entered is a valid choice
    if operation not in ["1", "2", "3", "4", "5"]:
        print("Enter a valid operation number as shown above (1, 2, 3, 4, or 5)")
        continue  

    # Get input numbers from the user
    while True:
        try:
            firstNum = int(input("Enter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  
        while True:
            try:
                secondNum = int(input("Enter the second number: "))
                break  
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
        break


    # Perform the operation based on user's choice
    if operation == "1":
        print(f"RESULT: Sum of {firstNum} and {secondNum} is", addition(firstNum, secondNum))
    elif operation == "2":
        print(f"RESULT: Difference of {firstNum} and {secondNum} is", subtraction(firstNum, secondNum))
    elif operation == "3":
        print(f"RESULT: Multiplication of {firstNum} and {secondNum} is", multiplication(firstNum, secondNum))
    elif operation == "4":
        print(f"RESULT: Division of {firstNum} and {secondNum} is", division(firstNum, secondNum))

    # Ask the user if they want to continue
    continue_choice = input("Do you want to perform another operation? (y/n): ")
    if continue_choice != "y":
        break