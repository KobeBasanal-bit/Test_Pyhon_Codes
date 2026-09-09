class Course:

    def __init__(
        self,
        course_code: str,
        course_name: str,
        instructor: str,
        schedule: str,
    ):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self._schedule = schedule

    @property
    def schedule(self) -> str:
        return self._schedule

    @schedule.setter
    def schedule(self, value: str):
        if not value or not value.strip():
            raise ValueError("Schedule cannot be empty.")
        self._schedule = value

    def display_info(self):
        print(
            f"{self.course_code}: {self.course_name} with {self.instructor} ({self.schedule})"
        )


class Assignment:

    def __init__(
        self,
        title: str,
        due_date: str,
        max_score: float,
        submitted: bool = False,
    ):
        self.title = title
        self.due_date = due_date
        self.max_score = max_score
        self._submitted = submitted

    @property
    def submitted(self) -> bool:
        return self._submitted

    @submitted.setter
    def submitted(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Submission status must be a boolean.")
        self._submitted = status

    def mark_as_submitted(self):
        self.submitted = True


class Student:
    total_students = 0

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.assignments = []
        Student.total_students += 1

    def enroll(self, course: Course):
        self.courses.append(course)
        print(f"Successfully enrolled {self.name} in {course.course_code}.")

    def add_assignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def list_pending_assignments(self):
        pending = [a for a in self.assignments if not a.submitted]
        print(f"\n--- Pending Assignments for {self.name} ---")
        if not pending:
            print("No pending assignments.")
        else:
            for assign in pending:
                print(
                    f" - {assign.title} (Due: {assign.due_date}, Max Score: {assign.max_score})"
                )

    def calculate_workload_score(self) -> float:
        return sum(
            a.max_score for a in self.assignments if not a.submitted
        )

    @classmethod
    def from_string(cls, student_str: str, delimiter: str = ","):
        name, student_id = student_str.split(delimiter)
        return cls(name.strip(), student_id.strip())

    @classmethod
    def get_total_enrolled(cls) -> int:
        return cls.total_students


if __name__ == "__main__":
    student = Student.from_string("Alex Mercer, BSIT-2026-001")
    print(f"Student Created: {student.name} (ID: {student.student_id})")

    c1 = Course(
        "IT101",
        "Object Oriented Programming",
        "Prof. Albarracin",
        "Mon/Wed 10AM",
    )
    c2 = Course(
        "IT102",
        "Data Structures and Algorithms",
        "Prof. Smith",
        "Tue/Thu 1PM",
    )

    c1.display_info()
    c2.display_info()

    student.enroll(c1)
    student.enroll(c2)

    a1 = Assignment("OOP Lab Project", "2026-09-10", 100)
    a2 = Assignment("DSA Quiz 1", "2026-09-05", 50)

    student.add_assignment(a1)
    student.add_assignment(a2)

    student.list_pending_assignments()
    print(f"Workload Score: {student.calculate_workload_score()}")

    a2.mark_as_submitted()
    print("\n[Updated] Marked 'DSA Quiz 1' as submitted.")

    student.list_pending_assignments()
    print(f"New Workload Score: {student.calculate_workload_score()}")