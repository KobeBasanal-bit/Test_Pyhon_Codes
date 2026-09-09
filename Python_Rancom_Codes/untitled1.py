size = input("Enter Coffee Size (small/medium/large): ")
milk = input("Enter Milk Type (oat/almond/whole): ")

if size == "small":
    price = 3.50
    
    if milk == "oat":
        price += 0.75
        
    elif milk == "almomd":
        price += 0.50
        
    elif milk == "whole":
        price += 0.00
        
elif size == "medium":
    price = 4.50
    
    if milk == "oat":
        price += 0.75
        
    elif milk == "almond":
        price += 0.50
        
    elif milk == "whole":
        price += 0.00
        
elif size == "large":
    price = 5.50
    
    if milk == "oat":
        price += 0.75
        
    elif milk == "almond":
        price += 0.50
        
    elif milk == "whole":
        price += 0.00
        
else:
    price = None
    
if price is None :
    print("Invalid")
    
print("Total: ", price)