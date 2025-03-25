import math

def square_root(x):
    if x < 0:
        return "Square root of a negative number is not defined in real numbers."
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        return "Natural logarithm is not defined for zero or negative numbers."
    return math.log(x)

def power(base, exponent):
    return math.pow(base, exponent)

def calculator():
	
    while True:
        print("Jenkins CI/CD is working!")
	print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number: "))
            result = square_root(x)
            print(f"Result: {result}")

        elif choice == '2':
            x = int(input("Enter a non-negative integer: "))
            result = factorial(x)
            print(f"Result: {result}")

        elif choice == '3':
            x = float(input("Enter a positive number: "))
            result = natural_log(x)
            print(f"Result: {result}")

        elif choice == '4':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = power(base, exponent)
            print(f"Result: {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()

