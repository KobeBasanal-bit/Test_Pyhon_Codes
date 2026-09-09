rows = int(input("Enter number of students: "))
col = int(input("Enter number of subjets: "))

imissher = []

for r in range(rows):
    row_data = []
    
    for c in range(col):
        val = int(input(f"Enter value of Student {r + 1}, Subject {c + 1}: "))
        row_data.append(val)
        
    imissher.append(row_data)
    
print("\n--- Summary of Student Grades ---")
    
for r in range(rows):
    print(f"Student {r + 1}:")
    
    for c in range(col):
        grade = imissher[r][c]
        
        if grade >= 90:
            rating = "Excellent"
            
        elif grade >= 80:
            rating = "Very Good"
            
        elif grade >= 75:
            rating = "Passed"
            
        else:
            rating = "Failed"
        
        print(f"  Subject {c + 1}: {grade} - {rating}")
        
