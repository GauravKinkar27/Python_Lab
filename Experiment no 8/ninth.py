# Program to demonstrate encapsulation
class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no        # Public
        self.holder_name = holder_name      # Public
        self._branch = "Main Branch"        # Protected (convention)
        self.__balance = balance            # Private (name mangling)
    
    # Public method to access private balance
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def display_info(self):
        print(f"Account: {self.account_no}")
        print(f"Holder: {self.holder_name}")
        print(f"Branch: {self._branch}")
        print(f"Balance: ₹{self.__balance}")

print("=== Encapsulation Demonstration ===")
acc = BankAccount("SB12345", "Alice Johnson", 5000)
acc.display_info()
print(f"\nAccessing public: {acc.account_no}")
print(f"Accessing protected (convention): {acc._branch}")
# print(acc.__balance)  # This will raise AttributeError
print(f"Accessing private via getter: {acc.get_balance()}")
acc.deposit(2000)
acc.withdraw(1000)