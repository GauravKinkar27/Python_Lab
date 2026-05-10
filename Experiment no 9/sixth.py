# Program to handle division by zero
def divide_numbers():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Unexpected error: {e}")

divide_numbers()