class MyCalculator:
    
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
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
        return self.a ** self.b
        
    def mod(self):
        return self.a % self.b
        
    def floordiv(self):
        if self.b != 0:
            return self.a // self.b
        return "Cannot divide by zero"

C1=MyCalculator(10, 5)

print("Addition: ", C1.add())
print("Subtraction: ", C1.sub())
print("Multiplication: ",  C1.mul())
print("Division: ", C1.div())
print("Exponentiation: ", C1.exp())
print("Modulo: ", C1.mod())
print("Floor Division: ", C1.floordiv())



        