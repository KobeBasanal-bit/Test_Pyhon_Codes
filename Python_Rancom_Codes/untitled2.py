weight = int(input("Enter package weight: "))
des = input("Enter Destination Zone(local/interntional): ")
ship = input("Shipping Option (yes/no): ")

if des == "local":
    
    if weight <= 5:
        price = 5
        
    elif weight > 5:
        price = 10
        
        if ship == "yes":
            price += 10
        

elif des == "international":
    
    if weight <= 5:
        price = 20
        
    elif weight > 5:
        price = 40
        
        if ship == "yes":
            price += 25
            
print("Total: ", price)

    
    
    
        
        
     
        
        
     