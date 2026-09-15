# 1. CLASS DEFINITION
# Defines the blueprint containing all attributes and methods
class Student:
    # ----------------------------------------------------
    # 2. CLASS ATTRIBUTES
    # Defined inside the class body, but outside any method.
    # Shared across ALL instances of this class.
    # ----------------------------------------------------
    school_name = "CTU Argao"  # Shared constant string across all objects
    student_count = 0        # Class-level counter tracking total instances created

    # ----------------------------------------------------
    # 3. CONSTRUCTOR (Initialization Method)
    # Special method automatically invoked when a new object is created.
    # Sets up the initial state of the object.
    # ----------------------------------------------------
    def __init__(self, name, student_id, major, age, section, grade):
        # ------------------------------------------------
        # 4. INSTANCE ATTRIBUTES
        # Attributes attached exclusively to specific instances using 'self'.
        # ------------------------------------------------
        self.name = name              # Unique to each instance
        self.student_id = student_id  # Unique to each instance
        self.major = major            # Unique to each instance
        self.section = section        # Unique to each instance
        
        # Private/protected internal attributes managed via properties below:
        self._age = age        
        self._grade = grade    

        # Increment class attribute counter every time __init__ runs
        Student.student_count += 1

    # ----------------------------------------------------
    # 5. PROPERTIES (@property Decorators)
    # Used for managing attribute access, data encapsulation, and input validation.
    # ----------------------------------------------------
    # Getter for 'grade': lets us access self._grade like a regular attribute (student.grade)
    @property
    def grade(self):
        return self._grade

    # Setter for 'grade': intercepts assignments (student.grade = 95) to validate values
    @grade.setter
    def grade(self, new_grade):
        # Input validation rule: ensures grade falls between 0 and 100
        if 0 <= new_grade <= 100:
            self._grade = new_grade
        else:
            print("Invalid grade! Grade must be between 0 and 100.")

    # Getter for 'age': allows read access to internal self._age
    @property
    def age(self):
        return self._age

    # ----------------------------------------------------
    # 6. INSTANCE METHODS
    # Standard methods operating on individual instances.
    # Always take 'self' as the first parameter to access instance data.
    # ----------------------------------------------------
    def display_student_info(self):
        # Reads instance attributes (self.name) and class attribute (Student.school_name)
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")

    def update_grade(self, new_grade):
        # Calls the setter property above to enforce validation before updating
        self.grade = new_grade  

    def is_deans_list(self):
        # Evaluation logic using instance's grade attribute
        return self.grade >= 90

    # ----------------------------------------------------
    # 7. CLASS METHOD (@classmethod Decorator)
    # Bound to the class itself using 'cls' instead of 'self'.
    # Used for accessing or modifying class-level state.
    # ----------------------------------------------------
    @classmethod
    def get_total_students(cls):
        # Accesses 'student_count' directly from the class object (cls)
        return f"Total students created: {cls.student_count}"


# ========================================================
# CREATING AND USING OBJECTS (INSTANCES)
# ========================================================

# Creating instances calls __init__ and increments Student.student_count
student1 = Student("Alice", "S001", "Information Technology", 20, "IT-2A", 92)
student2 = Student("Bob", "S002", "Computer Science", 21, "CS-2B", 85)

# Calling instance methods on specific objects
print("--- Student 1 Information ---")
student1.display_student_info()

# Accessing instance method logic
print(f"\nIs {student1.name} on Dean's List? {student1.is_deans_list()}")

# Updating grade triggers the @grade.setter property validation
student2.update_grade(95)
print(f"{student2.name}'s updated grade: {student2.grade}")

# Calling the class method on the class itself
print(f"\n{Student.get_total_students()}")