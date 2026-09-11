def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = input("Enter choice (1-4): ").strip()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            print("Invalid choice.")
            return

        print("Result:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    calculator()
