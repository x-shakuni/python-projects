
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |                _            _       _             
|  ___ ___ ___   ___  |               | |          | |     | |            
| | 7 | 8 | 9 | | + | |       ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |___|___|___| |___| |      / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__|
| | 4 | 5 | 6 | | - | |     | (_| (_| | | (__| |_| | | (_| | || (_) | |   
| |___|___|___| |___| |      \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
    should_continue = True
    num1 = float(input("Enter a number: "))
    while should_continue == True:

        operation = input("Enter operation('+','-','*','/': ")
        num2 = float(input("Enter the next number: "))

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to stop: ")

        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n"*30)
            calculator()

calculator()