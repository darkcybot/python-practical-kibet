class Student:
    # Constructor runs automatically when a new object is created
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Admission No: {self.admission_number}, Course: {self.course}")

# Creating three Student objects
student1 = Student("Collin", "T006/303936/2024", "Computer Science")
student2 = Student("kibet", "T007/304789/2026", "Information Technology")
student3 = Student("vader", "T008/305638/2026", "Business IT")

student1.display_info()
student2.display_info()
student3.display_info()