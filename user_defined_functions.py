# Add two numbers
def add_numbers(a, b):
    return a + b

# Area of a rectangle
def rectangle_area(length, width):
    return length * width

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Display student details
def display_student(name, course):
    print("Student Name:", name)
    print("Course:", course)

# Testing the functions
print("Add:", add_numbers(5, 3))
print("Rectangle Area:", rectangle_area(4, 6))
print("Is 7 prime?", is_prime(7))
print("Factorial of 5:", factorial(5))
display_student("Chebo", "Computer Science")