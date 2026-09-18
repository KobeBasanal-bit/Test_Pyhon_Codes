class BankAccount:
    bank_name = "CTU Community Bank"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance  # Triggers the property setter immediately

    # Property for balance validation
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = value

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Uses the setter/property safely
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_account(self):
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance: ${self.balance}")
        print("-" * 30)


# --- Testing the BankAccount Class ---
if __name__ == "__main__":
    account1 = BankAccount("ACC-001", "Krista", 5000)
    account1.display_account()

    account1.deposit(1500)
    account1.withdraw(2000)
    account1.display_account()

    # Testing validation error
    try:
        print("Attempting to set a negative balance...")
        account1.balance = -500
    except ValueError as e:
        print(f"Validation Error caught: {e}\n")