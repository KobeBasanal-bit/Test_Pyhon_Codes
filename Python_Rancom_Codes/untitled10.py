# Initial Setup
max_size = int(input("Enter array size: "))

# Parallel lists (arrays)
foodname = []
foodsize = []
quant = []
student_id = []
student_type = []
arr = []

while True:
    print("\nMENU")
    print("1. ADD")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(max_size):
            
            id_val = input("Enter Student ID: ")
            type_val = input("Enter Student Type (Regular/Scholar): ")
            name_val = input("Enter Food Name: ")
            size_val = input("Enter Food Size (Small/Medium/Large): ")
            quant_val = int(input("Enter Quantity: "))

            # 1. Determine Unit Price based on Size
            if size_val.lower() == "large":
                price = 230
            elif size_val.lower() == "medium":
                price = 150
            else:
                price = 120

            # 2. Calculate Base Total Cost
            total = price * quant_val

            # 3. Apply 10% Discount if quantity > 5
            if quant_val > 5:
                total = total - (total * 0.10)
                print("10% bulk discount applied!")

            # 4. Apply Student Discount
            if type_val.lower() == "regular":
                total = total - (total * 0.05)
                print("5% Regular Student discount applied!")
            elif type_val.lower() == "scholar":
                total = total - (total * 0.10)
                print("10% Scholar discount applied!")

            # 5. Save to parallel arrays
            student_id.append(id_val)
            student_type.append(type_val)
            foodname.append(name_val)
            foodsize.append(size_val)
            quant.append(quant_val)
            arr.append(total)

            print("Value added!")

            # Display after adding
            print(f"ID: {id_val} | Type: {type_val} | Food: {name_val} | Size: {size_val} | Qty: {quant_val} | Total: {total}")

    elif choice == 2:
        search_id = input("Enter Student ID to search: ")
        found = False

        for i in range(len(student_id)):
            if student_id[i].lower() == search_id.lower():
                print(f"Found! Student ID: {student_id[i]} | Type: {student_type[i]} | Food: {foodname[i]} | Size: {foodsize[i]} | Qty: {quant[i]} | Total: {arr[i]}")
                found = True
                break

        if not found:
            print("Student ID not found")

    elif choice == 3:
        search_id = input("Enter Student ID to update: ")
        found = False

        for i in range(len(student_id)):
            if student_id[i].lower() == search_id.lower():
                student_id[i] = input("Enter new Student ID: ")
                student_type[i] = input("Enter new Student Type (Regular/Scholar): ")
                foodname[i] = input("Enter new Food Name: ")
                foodsize[i] = input("Enter new Food Size (Small/Medium/Large): ")
                quant[i] = int(input("Enter new Quantity: "))

                # Recalculate price
                if foodsize[i].lower() == "large":
                    price = 230
                elif foodsize[i].lower() == "medium":
                    price = 150
                else:
                    price = 120

                total = price * quant[i]
                if quant[i] > 5:
                    total = total - (total * 0.10)

                if student_type[i].lower() == "regular":
                    total = total - (total * 0.05)
                elif student_type[i].lower() == "scholar":
                    total = total - (total * 0.10)

                arr[i] = total
                print("Value Updated")
                found = True
                break

        if not found:
            print("Student ID not found")

    elif choice == 4:
        delete_id = input("Enter Student ID to delete: ")
        found = False

        for i in range(len(student_id)):
            if student_id[i].lower() == delete_id.lower():
                del student_id[i]
                del student_type[i]
                del foodname[i]
                del foodsize[i]
                del quant[i]
                del arr[i]
                print("Value deleted.")
                found = True
                break

        if not found:
            print("Student ID not Found")

    elif choice == 5:
        if len(student_id) == 0:
            print("Inventory is empty.")
        else:
            for i in range(len(student_id)):
                # Determine Classification
                if arr[i] >= 35001:
                    classification = "Very High-cost purchase"
                elif arr[i] >= 20001:
                    classification = "High Cost purchase"
                elif arr[i] >= 10001:
                    classification = "Moderate Purchase"
                else:
                    classification = "Low-cost purchase"

                print(f"ID: {student_id[i]} | Type: {student_type[i]} | Food: {foodname[i]} | Size: {foodsize[i]} | Qty: {quant[i]} | Total: {arr[i]} --- {classification}")

    elif choice == 6:
        print("Exiting........")
        break

    else:
        print("Invalid Choice.")