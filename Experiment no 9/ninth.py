# Program to create user-defined exception
class AgeError(Exception):
    """Custom exception for age validation"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InsufficientBalanceError(Exception):
    """Custom exception for bank balance"""
    pass

def validate_age():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise AgeError("Age cannot be negative")
        if age > 150:
            raise AgeError("Age cannot exceed 150")
        print(f"Valid age: {age}")
    except AgeError as e:
        print(f"Age Error: {e}")
    except ValueError:
        print("Error: Please enter a valid number")

def bank_withdraw():
    try:
        balance = 5000
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            raise InsufficientBalanceError(f"Insufficient balance! Available: {balance}")
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
    except InsufficientBalanceError as e:
        print(f"Transaction Error: {e}")
    except ValueError:
        print("Error: Please enter valid amount")

print("=== User-Defined Exceptions ===")
print("1. Age Validation")
validate_age()
print("\n2. Bank Withdrawal")
bank_withdraw()