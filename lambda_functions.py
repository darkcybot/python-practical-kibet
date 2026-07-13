# Lambda to add two numbers
add = lambda a, b: a + b
print("Add:", add(4, 5))

# Lambda to multiply two numbers
multiply = lambda a, b: a * b
print("Multiply:", multiply(4, 5))

# Sorting a list with a lambda key
students = [("Kibet", 21), ("Collin", 20), ("Vader", 25)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted by age:", sorted_students)

# filter() with a lambda: keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# map() with a lambda: square every number
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)