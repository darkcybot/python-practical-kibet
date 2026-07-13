#creating a set (unordered collectin, no duplicates allowed)
from multiprocessing.reduction import duplicate

numbers = {1,2,3,4}

#Adding elements
numbers.add(5)

#Removing elements
numbers.remove(2)

print("Set after changes:", numbers)

#Demonstrating duplicates are removed automatically
duplicates ={1,2,2,3,3,3}
print("Set removes duplicates automatically:",duplicates)