# ==========================================
# STEP 1: Create a Class
# ==========================================
class AIEngineer:

    # STEP 7: Class attribute to count objects created
    total_engineers = 0

    # STEP 3: Initialize the Object (__init__ constructor)
    def __init__(
        self,
        name: str,
        company: str,
        salary: float,
        ai_dependent: str,
        models_created: int,
    ):
        # STEP 2: Encapsulate using double underscores (__)
        self.__name = name
        self.__company = company
        self.salary = salary  # Uses property setter for validation
        self.__ai_dependent = ai_dependent
        self.models_created = models_created  # Uses property setter for validation

        # Increment total count when a new object is created
        AIEngineer.total_engineers += 1

    # ==========================================
    # STEP 4 & 5: Getters, Setters & Validation
    # ==========================================
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        if not value or not str(value).strip():
            raise ValueError("Company cannot be empty.")
        self.__company = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary must not be negative.")
        self.__salary = value

    @property
    def ai_dependent(self):
        return self.__ai_dependent

    @ai_dependent.setter
    def ai_dependent(self, value):
        if not value or not str(value).strip():
            raise ValueError("AI dependent field cannot be empty.")
        self.__ai_dependent = value

    @property
    def models_created(self):
        return self.__models_created

    @models_created.setter
    def models_created(self, value):
        if value < 0:
            raise ValueError("Models created cannot be less than zero.")
        self.__models_created = value

    # ==========================================
    # STEP 6: Implement Instance Methods
    # ==========================================
    def create_ai(self):
        return f"{self.__name} is creating a new AI model for {self.__company}."

    def train_model(self):
        return f"{self.__name} is training the AI model."

    def maintain_ai(self):
        return f"{self.__name} is performing maintenance on the {self.__ai_dependent} system."

    def deploy_model(self):
        self.__models_created += 1  # Updates attribute value dynamically
        return f"{self.__name} deployed a model to production. Total models created: {self.__models_created}."

    def debugging(self):
        return f"{self.__name} is debugging neural network algorithms."

    # ==========================================
    # STEP 7: Implement a Class Method
    # ==========================================
    @classmethod
    def display_total_count(cls):
        return f"Total AI Engineers created: {cls.total_engineers}"


# ==========================================
# STEP 8: Create and Test Objects
# ==========================================
if __name__ == "__main__":
    print("==========================================")
    print("      STEP 8: TEST CREATED OBJECTS        ")
    print("==========================================")

    # Instantiate two objects
    eng1 = AIEngineer(
        name="Kobe Basanal",
        company="Tech Corp",
        salary=85000.0,
        ai_dependent="NLP Chatbot",
        models_created=3,
    )

    eng2 = AIEngineer(
        name="Alex Mercer",
        company="AI Research Labs",
        salary=95000.0,
        ai_dependent="Vision AI",
        models_created=5,
    )

    # Call methods and display outputs for Object 1
    print(
        f"\n[Object 1] {eng1.name} | {eng1.company} | Salary: ₱{eng1.salary:,.2f}"
    )
    print(eng1.create_ai())
    print(eng1.train_model())
    print(eng1.deploy_model())

    # Call methods and display outputs for Object 2
    print(
        f"\n[Object 2] {eng2.name} | {eng2.company} | Salary: ₱{eng2.salary:,.2f}"
    )
    print(eng2.maintain_ai())
    print(eng2.debugging())

    # ==========================================
    # STEP 9: Interactive Simulation (Keyboard Input)
    # ==========================================
    print("\n==========================================")
    print("    STEP 9 & 10: INTERACTIVE SIMULATION   ")
    print("==========================================")

    user_name = input("Enter AI Engineer Name: ")
    user_company = input("Enter Company Name: ")
    user_salary = float(input("Enter Salary: "))
    user_ai_dep = input(
        "Enter AI Specialty / Dependent System (e.g., Computer Vision): "
    )
    user_models = int(input("Enter Initial Models Created Count: "))

    # Instantiate the interactive object
    user_eng = AIEngineer(
        name=user_name,
        company=user_company,
        salary=user_salary,
        ai_dependent=user_ai_dep,
        models_created=user_models,
    )

    # ==========================================
    # STEP 10: Display Results
    # ==========================================
    print("\n--- Object Information ---")
    print(f"Name: {user_eng.name}")
    print(f"Company: {user_eng.company}")
    print(f"Salary: ₱{user_eng.salary:,.2f}")
    print(f"Specialty: {user_eng.ai_dependent}")
    print(f"Initial Models Created: {user_eng.models_created}")

    print("\n--- Method Outputs ---")
    print(user_eng.create_ai())
    print(user_eng.train_model())
    print(user_eng.maintain_ai())
    print(user_eng.debugging())
    print(user_eng.deploy_model())

    print("\n--- Updated Attribute Value ---")
    print(f"Updated Models Created Count: {user_eng.models_created}")

    print("\n--- Class Method Result ---")
    print(AIEngineer.display_total_count())