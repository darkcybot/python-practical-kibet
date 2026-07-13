class Student:
    # Class variable
    school_name = "Co-operative University of Kenya"

    # Constructor with instance variables
    def __init__(self, name, course):
        self.name = name
        self.course = course

    # Regular instance method
    def display_info(self):
        print(f"{self.name} is studying {self.course} at {self.school_name}")

    # Class method — works on the class itself, not one object
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Testing
s1 = Student("Chebo", "Computer Science")
s1.display_info()

# Using the class method to change the shared school name
Student.change_school("CUK Main Campus")
s1.display_info()