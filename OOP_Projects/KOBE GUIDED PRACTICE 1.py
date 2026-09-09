class Student:
    total_students = 0

    def __init__(self, name: str, age: int, section: str, grade: float):
        self.name = name
        self.age = age
        self.section = section
        self.grade = grade
        Student.total_students += 1

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")
        print(f"Grade: {self.grade}")

    def update_grade(self, new_grade: float):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}")

    def is_deans_list(self, cutoff: float = 1.75) -> bool:
        return self.grade <= cutoff

    @classmethod
    def get_total_students(cls) -> int:
        return cls.total_students


if __name__ == "__main__":
    s1 = Student("Sealtiel", 18, "BSIT 2 Chrome", 1.2)
    s2 = Student("Jasmine", 22, "BSIT 2 Explorer", 2.6)

    print("--- Student 1 Info ---")
    s1.display_information()
    print(f"Dean's List: {s1.is_deans_list()}\n")

    print("--- Student 2 Info ---")
    s2.display_information()
    print(f"Dean's List: {s2.is_deans_list()}\n")

    print(f"Total Student Objects Created: {Student.get_total_students()}")