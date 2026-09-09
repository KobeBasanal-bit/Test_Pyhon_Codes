size = int(input("Enter array size: "))

arr = []

while True:
    print("MENU")
    print("1. ADD")
    print("2. SEARCH")
    print("3. UPDATE")
    print("4. DELETE")
    print("5. DISPLAY")
    print("6. EXIT")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        
        for i in range(size):
            value = int(input("Enter value: "))
            arr.append(value)
            print("Succesfully Appended")
            
        for i in range(len(arr)):
            if arr[i] >= 30:
                classification = "High"
                
            elif arr[i] >= 20:
                    classification = "Mediun"
                    
            elif arr[i] >= 10:
                classification = "Low"
                        
            else:
                classification = "Very Low"
                
    if choice == 2:
        
        for i in range (len(arr)):
        
            search = int(input("Enter number to be searched: "))
        
            found = False
        
            if arr[i] == search:
                print(f"{arr[i]} - {classification}")
            
                found = True
            
        if not found:
                print("Not Found")
            
    if choice == 3:
        
        for i in range (len(arr)):
            
            search = int(input("Enter number to be searched: "))
        
            found = False
        
            if arr[i] == search:
                new_value = int(input("Enter new value: "))
                arr[i] = new_value
                print("Updated")
            
                found = True
            
        if not found:
            print("Not Found")
            
    if choice == 4:
        
        for i in range (len(arr)):
        
            delete = int(input("Enter number to be searched: "))
        
            found = False
        
            if arr[i] == search:
                del arr[i]
            
                found = True
            
        if not found:
            print("Not Found")
            
    if choice == 5:
        
        for i in range(len(arr)):
            if arr[i] >= 30:
                classification = "High"
                
            elif arr[i] >= 20:
                    classification = "Mediun"
                    
            elif arr[i] >= 10:
                classification = "Low"
                        
            else:
                classification = "Very Low"
            
            print(f"{arr[i]} - {classification}")
        
    if choice == 6:
        
        print("Exiting....")
        break
        
        
        
                