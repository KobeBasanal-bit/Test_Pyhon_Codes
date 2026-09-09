

size = int(input("Enter array size: "))
arr = []



while True:
	print("MENU")
	print("1. ADD")
	print("2. Search")
	print("3. Update")
	print("4. Delete")
	print("5. Display")
	print("6. Exit")

	choice = int(input("Enter your choice: "))
	
	if choice == 1:

		for i in range(size):
			value = float(input("Enter value: "))	
			arr.append(value)
			print("Value added")
	

	elif choice == 2:
        search = float(input("Enter search input: "))
	
		found = False

		for i in range(len(arr)):

			if arr[i] == search:
				print(f"Value: {arr[i]}---{classification}")

				found = True
				break

		if not found:
			print("Not found")

	elif choice == 3:
	
		search = float(input("Enter value to update: "))
		found = False

		for i in range(len(arr)):
			if arr[i] == search:

				new_value = int(input("Enter value to update: "))
    
				arr[i] = new_value
				print("Value Updated")
                
				found = True

		if not found:
			print("Not found")

	elif choice == 4:
		
		delete = float(input("Enter value to be deleted: "))
		found = False
		for i in range (len(arr)):	
			if arr[i] == delete:
			
				del arr[i]
				print("Value deleted.")
				
				found = True
				break
		if not found:
				print("Value not Found")


	elif choice == 5:
		
		for i in range(len(arr)):

			if arr[i] >= 35001:
				classification = "Very High- cost purchase"

			elif arr[i] >=20001:
				classification = "High Cost purhase"
			elif arr[i] >= 10001:
				classification = "Moderat Purchase"

			else:
				classification = "Low-cost purchase"

			print(f"Value: {arr[i]}---{classification}")
				

	

	elif choice == 6:

		print("Exiting........")
		break	

	else: 
	
		print("Invalid Choice.")	