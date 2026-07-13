# for loop: print numbers 1 to 20
for i in range(1, 21):
    print(i)

# for loop: multiplication table
number = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# while loop: sum of numbers 1 to 100
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print("Sum of 1 to 100:", total)

# even numbers between 1 and 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)