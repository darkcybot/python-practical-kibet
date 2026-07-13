#creating a tuple(ordered,unchangeable collection)
student = ("kibet" ,21 ,"computer science")

#accessing elements by index
print("Name:", student[0])
print("age:", student[1])
print("course:", student[2])

#Tuples cannot be modified - this line would cause an error if uncommented:
#student[0] = "john"
#TypeError: 'tuple' object does not support item assignment