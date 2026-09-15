

n = int(input("Enter array size: "))

arr = []

while True:
    print("=====MENU=====")
    print("1. ADD")
    print("2. SEARCH")
    print("3. DISPLAY ALL")
    print("4. EXIT")
    choice = int(input("Enter choice: "))

    if choice == 1:
        if len(arr) >= n:
            print("Array is full!")
            continue

        order_id = int(input("Enter order id: "))
        name = input("Enter name: ")
        flavor = input("Enterflavor(cheese/hawaiian/pepperoni):")
        size = input("Enter size(small/medium/large): ")
        quant = int(input("Enter quantity: "))

        total = 0.0

        if flavor == "cheese":
            amount = 200

            if size == "small":
                print("Size: small")

            elif size == "medium":
                amount += 50
                print("Size: medium")

            elif size == "large":
                amount += 100
                print("Size: large")

            if quant > 5:
                print("15% discount")
                discount = 0.15

            elif quant >= 4:
                print("10% discount")
                discount = 0.10

            else:
                print("no discount")
                discount = 0

        elif flavor == "hawaiian":
            amount = 230

            if size == "small":
                print("Size: small")

            elif size == "medium":
                print("Size: medium")
                amount += 50

            elif size == "large":
                print("Size: large")
                amount += 100

            if quant > 5:
                print("15% discount")
                discount = 0.15

            elif quant >= 4:
                print("10% discount")
                discount = 0.10

            else:
                print("no discount")
                discount = 0

        elif flavor == "pepperoni":
            amount = 260

            if size == "small":
                print("Size: small")

            elif size == "medium":
                print("Size: medium")
                amount += 50

            elif size == "large":
                print("Size: large")
                amount += 100

            if quant > 5:
                print("15% discount")
                discount = 0.15

            elif quant >= 4:
                print("10% discount")
                discount = 0.10

            else:
                print("no discount")
                discount = 0

        else:
            print("Invalid flavor entered.")
            continue

        amount = amount * quant
        total = amount - (amount * discount)

        arr.append([order_id, name, flavor, size, quant, total])
        print(f"Order ID: {order_id} is successfully added")
        print(f"Total: {total}")

    elif choice == 2:
        search = int(input("Enter ID to be searched: "))
        found = False

        for i in range(len(arr)):
            if arr[i][0] == search:
                found = True
                print("Order Found")
                print(f"Order ID: {arr[i][0]}")
                print(f"Name: {arr[i][1]}")
                print(f"Flavor: {arr[i][2]}")
                print(f"Size: {arr[i][3]}")
                print(f"Quantity: {arr[i][4]}")
                print(f"Total: {arr[i][5]}")
                break

        if not found:
            print("Not found")

    elif choice == 3:
        for i in range(len(arr)):
            print(f"Order ID: {arr[i][0]}")
            print(f"Name: {arr[i][1]}")
            print(f"Flavor: {arr[i][2]}")
            print(f"Size: {arr[i][3]}")
            print(f"Quantity: {arr[i][4]}")
            print(f"Total: {arr[i][5]}")

    elif choice == 4:
        print("EXITING .........")
        break

    else:
        print("Invalid choice")