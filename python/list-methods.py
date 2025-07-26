items = [10, 20, 30, 20]

items.append(40)         # Adds 40 at the end
items.insert(1, 15)      # Inserts 15 at index 1
items.remove(20)         # Removes first occurrence of 20
items.pop()              # Removes and returns last item
items.sort()             # Sorts the list
items.reverse()          # Reverses the list
index = items.index(30)  # Gets the index of 30
count = items.count(20)  # Counts how many times 20 appears
items.clear()            # Empties the list

print(index)  # Index of 30
print(count)  # How many times 20 appears
