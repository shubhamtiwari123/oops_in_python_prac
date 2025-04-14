class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

class Customer:
    def __init__(self, name, account: BankAccount):
        self.name = name
        self.account = account

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.account.account_number}")
        print(f"Balance: ₹{self.account.get_balance()}")
        
class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.status = "Success"

def main():
    account = BankAccount("12345678", "Alice", 1000)
    customer = Customer("Alice", account)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Show Details\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            customer.display_details()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

