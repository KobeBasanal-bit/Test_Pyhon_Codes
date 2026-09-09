n = int(input("Enter array size: "))

arr=[]
id=[]
student_type=[]
foodname=[]
size=[]
quant=[]
tot=[]

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
        for i in range(n):
            id_num = input("Enter ID number: ")
            type = input("Enter Student Type(regular/scholar): ")
            food = input("Enter Food Name: ")
            f_size = input("Enter Size(small/medium/large): ")
            quantity = int(input("Enter Quantity: "))
            
            
            if f_size == "small":
                amount = 120
                
            elif f_size == "medium":
                amount = 150
                
            elif f_size == "large":
                amount = 230
                
            total = quantity * amount  
                
            if type == "regular":
                total = total - (total * 0.05)
                print("Added regular discount - 5%")
                
            elif type == "scholar":
                total = total - (total * 0.10)
                print("Added scholar discount - 10%")
                
            if quantity > 5:
                total = total - (total * 0.10)
                print("Added overbuy discont - 10%")
                
            print("-----VALUES------")
                
            id.append(id_num)
            student_type.append(type)
            foodname.append(food)
            size.append(f_size)
            quant.append(quantity)
            tot.append(total)
            
            print(f"ID Nuumber: {id_num} ")
            print(f"Student Type: {type} ")
            print(f"Food Name: {food} ")
            print(f"Food Size: {f_size}")
            print(f"Quantity: {quantity}")
            print(f"TOTAL: {total}")
            
            
    elif choice == 2:
        search = input("Enter ID to be searched: ")
        found = False
        
        for i in range(len(id)):
            if id[i] == search:
                print(f"ID Nuumber: {id[i]} ")
                print(f"Student Type: {student_type[i]} ")
                print(f"Food Name: {foodname[i]} ")
                print(f"Food Size: {size[i]}")
                print(f"Quantity: {quant[i]}")
                print(f"TOTAL: {tot[i]}")
                
                found = True
                break
        if not found:
            print("Not found.")
                        
            
    elif choice == 3:
        search = input("Enter ID to be searched: ")
        found = False
        
        for i in range(len(id)):
            if id[i] == search:
                id[i]= input("Enter ID number: ")
                student_type[i] = input("Enter Student Type(regular/scholar): ")
                foodname[i] = input("Enter Food Name: ")
                size[i] = input("Enter Size(small/medium/large): ")
                quant[i] = int(input("Enter Quantity: "))
                
                if size[i] == "small":
                    amount = 120
                    
                elif size[i] == "medium":
                    amount = 150
                    
                elif size[i] == "large":
                    amount = 230
                    
                else:
                    print("Invalid choice!")
                    
                total = quantity * amount  
                    
                if student_type[i] == "regular":
                    total = total - (total * 0.05)
                    print("Added regular discount - 5%")
                    
                elif student_type[i] == "scholar":
                    total = total - (total * 0.10)
                    print("Added scholar discount - 10%")
                    
                if quant[i] > 5:
                    total = total - (total * 0.10)
                    print("Added overbuy discont - 10%")
                    
                tot[i] = total
                print("Value Updated")
                
                found = True
                break
        if not found:
            print("Not found.")
            
    elif choice == 4:
        delete = input("Enter ID to delete: ")
        found = False
        
        for i in range(len(id)):
            if id[i] == delete:
                del id[i]
                del student_type[i]
                del foodname[i]
                del size[i]
                del quant[i]
                del tot[i]
                
                found = True
                break
            
        if not found:
            print("Not found.")
          
    elif choice == 5:
        
        for i in range(len(id)):
            print(f"ID Nuumber: {id[i]} ")
            print(f"Student Type: {student_type[i]} ")
            print(f"Food Name: {foodname[i]} ")
            print(f"Food Size: {size[i]}")
            print(f"Quantity: {quant[i]}")
            print(f"TOTAL: {tot[i]}")
            
    elif choice == 6:
        print("EXITING............")
        break
      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            