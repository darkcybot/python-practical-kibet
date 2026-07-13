#Dictionary representing a student
student = {
    "name":"kibet",
    "age":21,
    "course":"Computer Science",
    "grade":"A"
}

#Accessing values
print("Name:",student["name"])
print("Course:",student["course"])

#updating values
student["grade"] = "A"
student["age"] = 22

print("Updated student record:", student)