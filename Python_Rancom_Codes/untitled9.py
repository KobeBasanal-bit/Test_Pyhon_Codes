# 1. Ask the user for matrix dimensions
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

# 2. Create an empty 2D array (list of lists)
grades_matrix = []

print("\nEnter grades:")

# 3. Collect inputs for each student and subject
for r in range(num_students):
    student_grades = []  # Temporary list for current student
    
    for c in range(num_subjects):
        # Ask for each grade (r+1 and c+1 adjust 0-indexing to 1-based display)
        grade = int(input(f"Student {r + 1}, Subject {c + 1}: "))
        student_grades.append(grade)
        
    grades_matrix.append(student_grades)  # Add completed student row to 2D list

print("\n--- Summary of Student Grades ---")

# 4. Process and classify each grade using conditional structures
for r in range(num_students):
    print(f"\nStudent {r + 1}:")
    
    for c in range(num_subjects):
        grade = grades_matrix[r][c]
        
        # Classification rules
        if grade >= 90:
            rating = "Excellent"
        elif grade >= 80:
            rating = "Very Good"
        elif grade >= 75:
            rating = "Passed"
        else:
            rating = "Failed"
            
        print(f"  Subject {c + 1}: {grade} -> {rating}")