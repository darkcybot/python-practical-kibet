# creating strings
first_name ="collin"
last_name ="bet"

# Concatenation(joining strings)
full_name = first_name + "" + last_name
print("Full name:",full_name)

# Indexing (accessing a single character by position, starts with 0)
print("First letter:", full_name[0])
print("Last letter:", full_name[-1])

# slicing (extracting a portion of the string)
print("First 5 characters:",full_name[0:5])

# String methods
print("Uppercase:",full_name.upper())
print("Lowercase:",full_name.lower())
print("Replace:",full_name.replace("collin","ian"))
print("Split by space:",full_name.split(" "))
