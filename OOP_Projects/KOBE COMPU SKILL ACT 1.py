class Student:
    
    def __init__(self, id, last, first, mi, course, section, motto):
        self.id=id
        self.last=last
        self.first=first
        self.mi=mi
        self.course=course
        self.section=section
        self.motto=motto
        
    def display_student(self):
        print(f"Student Id: {self.id} ")
        print(f"Full Name: {self.last} {self.first} {self.mi}")
        print(f"Course and Section: {self.course} {self.section}")
        print(f"Motto: {self.motto} ")
        print( " ")

        
s1=Student(
    "7251340",
    "Basanal",
    "Kobe", 
    "D.",
    "BSIT",
    "2A - Algorithm",
    "It is what It is"
    )

s2=Student(
    "7251256",
    "Balderas",
    "Krista Innova", 
    "S.",
    "BSIT",
    "2A - Algorithm",
    "Art is Freedom"
    )

s3=Student(
    "7251387",
    "Basanal",
    "Simba", 
    "B.",
    "BSIT",
    "1A - Microsoft",
    "All bark no bite is key"
    )

s1.display_student()
s2.display_student()
s3.display_student()
