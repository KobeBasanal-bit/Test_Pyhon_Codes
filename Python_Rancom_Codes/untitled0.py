
age = int(input("Enter your age: "))
weekend = input("Weekend? (yes/no)")

if age < 12:
    price = 8
elif age <= 64:
    price = 15
else:
    price = 10
    
if weekend == "yes":
    print("additional 3$")
    price += 3

print(f"Your ticket price is: ${price}")
    
    
