from array import*

arr = array('i', [])

number = int(input("Enter size of elements: "))

even = 0
for i in range(number):
    num = int(input("Enter a number: "))
    if num %2 == 0:
        arr.append(num)
        
for x in arr:
    print(x, end=" ")