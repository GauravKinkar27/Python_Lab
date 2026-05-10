# Program to handle invalid input exception
def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(f"You entered: {num}")
            return num
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

print("=== Invalid Input Handler ===")
get_integer()

# Multiple inputs
def process_numbers():
    try:
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [int(x) for x in numbers]
        print(f"Sum: {sum(numbers)}")
        print(f"Average: {sum(numbers)/len(numbers)}")
    except ValueError:
        print("Error: Please enter only numbers")
    except Exception as e:
        print(f"Error: {e}")

process_numbers()