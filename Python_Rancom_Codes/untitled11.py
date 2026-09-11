class Student:
    # 1. CLASS ATTRIBUTE
    # Shared by all instances of the class
    school_name = "CTU Argao"
    student_count = 0  # Class-level counter

    # 2. CONSTRUCTOR (Initialization Method)
    def __init__(self, name, student_id, major, age, section, grade):
        # 3. INSTANCE ATTRIBUTES
        # Specific to each individual instance
        self.name = name
        self.student_id = student_id
        self.major = major
        self.section = section
        self._age = age        # Private variable managed by property
        self._grade = grade    # Private variable managed by property

        # Increment class counter every time a new object is created
        Student.student_count += 1

    # 4. PROPERTIES (@property Decorator)
    # Getter for grade
    @property
    def grade(self):
        return self._grade

    # Setter for grade with input validation
    @grade.setter
    def grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self._grade = new_grade
        else:
            print("Invalid grade! Grade must be between 0 and 100.")

    # Getter for age
    @property
    def age(self):
        return self._age

    # 5. INSTANCE METHODS
    # Operate on specific instances using 'self'
    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")

    def update_grade(self, new_grade):
        self.grade = new_grade  # Uses the setter property

    def is_deans_list(self):
        # Example condition: Grade of 90 or higher qualifies for Dean's List
        return self.grade >= 90

    # 6. CLASS METHOD (@classmethod Decorator)
    # Operates on the class itself using 'cls'
    @classmethod
    def get_total_students(cls):
        return f"Total students created: {cls.student_count}"


# --- CREATING AND USING OBJECTS (INSTANCES) ---

# Creating instances
student1 = Student("Alice", "S001", "Information Technology", 20, "IT-2A", 92)
student2 = Student("Bob", "S002", "Computer Science", 21, "CS-2B", 85)

# Displaying info
student1.display_student_info()

# Checking Dean's List status
print(f"Is {student1.name} on Dean's List? {student1.is_deans_list()}")

# Updating grade using method/property setter
student2.update_grade(95)
print(f"{student2.name}'s new grade: {student2.grade}")

# Accessing Class Method
print(Student.get_total_students())