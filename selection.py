#if...else: pass or fail based on score
score=65
if score>=50:
    print("Result: Passed")
else:
    print("Result : Failed")

#if...elif...else: even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

#Largest of the three numbers
a,b,c=12,45,7
if a>=b and a>=c:
    print("Largest is:", a)
elif b>=a and b>=c:
    print("Largest is:", b)
else:
    print("Largest is:", c)