# Define a tuple
my_tuple = (1, 2, 3, "Python", 2)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple [1:4]:", my_tuple[1:4])
print("Reversed tuple:", my_tuple[::-1])

# Concatenation and repetition
t1 = (10, 20)
t2 = (30, 40)
print("Concatenated:", t1 + t2)
print("Repeated:", t1 * 2)

# Looping through tuple
print("Looping:")
for item in my_tuple:
    print(item)

# Membership test
print("Is 'Python' in my_tuple?", 'Python' in my_tuple)

# Tuple methods
print("Count of 2:", my_tuple.count(2))
print("Index of 'Python':", my_tuple.index("Python"))
