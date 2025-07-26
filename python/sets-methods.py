s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))         # {1, 2, 3, 4, 5}
print(s1.intersection(s2))  # {3}
print(s1.difference(s2))    # {1, 2}
print(s1.symmetric_difference(s2))  # {1, 2, 4, 5}
s1.add(6)                   # add an element
s1.remove(2)                # remove specific element
s1.discard(10)              # safe remove
s1.clear()                  # remove all elements
