class Student:
    # Class variable — shared by ALL objects of this class
    school_name = "Co-operative University of Kenya"

    def __init__(self, name):
        self.name = name  # instance variable — unique to each object

# Creating objects
s1 = Student("Chebo")
s2 = Student("Amina")

# Accessing the class variable from different objects
print(s1.name, "studies at", s1.school_name)
print(s2.name, "studies at", s2.school_name)

# Changing the class variable affects all objects that haven't overridden it
Student.school_name = "CUK"
print(s1.name, "now studies at", s1.school_name)