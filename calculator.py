import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero!"
    return x / y

def second_power(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number!"
    return math.sqrt(x)

def display_menu():
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Second Power")
    print("6. Square Root")
    print("7. Exit")

def get_operation_choice():
    while True:
        choice = input("Enter your choice (1-7): ")
        if choice.isdigit() and 1 <= int(choice) <= 7:
            return int(choice)
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

def get_numbers():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            return x, y
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice == 7:
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in [1, 2, 3, 4]:
            x, y = get_numbers()
            if choice == 1:
                print("Result:", addition(x, y))
            elif choice == 2:
                print("Result:", subtraction(x, y))
            elif choice == 3:
                print("Result:", multiplication(x, y))
            elif choice == 4:
                print("Result:", division(x, y))
        elif choice in [5, 6]:
            x = float(input("Enter the number: "))
            if choice == 5:
                print("Result:", second_power(x))
            elif choice == 6:
                print("Result:", square_root(x))
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
