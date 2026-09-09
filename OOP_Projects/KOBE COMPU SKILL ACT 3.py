class MyCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        return "Cannot divide by zero"

    def exp(self):
        return self.a**self.b

    def mod(self):
        return self.a % self.b

    def floordiv(self):
        if self.b != 0:
            return self.a // self.b
        return "Cannot divide by zero"


def menu():
    print("============================")
    print("     SIMPLE CALCULATOR      ")
    print("============================")
    print("[1] ADDITION")
    print("[2] SUBTRACTION")
    print("[3] MULTIPLICATION")
    print("[4] DIVISION")
    print("[5] EXPONENTIATION")
    print("[6] MODULO")
    print("[7] FLOOR DIVISION")
    print("[8] EXIT")
    print("============================")


while True:
    menu()
    choice = input("Enter Choice: ")

    if choice == "8":
        print("Goodbye! shushushu hawa na!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        calc = MyCalculator(a, b)

        if choice == "1":
            print("Addition Result: ", calc.add())
        elif choice == "2":
            print("Subtraction Result: ", calc.sub())
        elif choice == "3":
            print(f"Multiplication Result: {calc.mul()}")
        elif choice == "4":
            print(f"Division Result: {calc.div()}")
        elif choice == "5":
            print(f"Exponentiation Result: {calc.exp()}")
        elif choice == "6":
            print(f"Modulo Result: {calc.mod()}")
        elif choice == "7":
            print(f"Floor Division Result: {calc.floordiv()}")

    else:
        print("Invalid choice! Please select an option between 1 and 8.")
        
        
        
        
        
        
        
        
        
        
            