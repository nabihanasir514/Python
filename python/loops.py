for i in range(5):
    print(i)
# Output: 0 1 2 3 4


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


for num in range(10):
    if num == 5:
        break
    print(num)
# Output: 0 1 2 3 4


i = 0
while i < 5:
    print(i)
    i += 1
# Output: 0 1 2 3 4


i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1
# Output: 1 2 3

x = 10
while x > 0:
    print(x)
    x -= 2
# Output: 10 8 6 4 2
