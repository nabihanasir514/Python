# Loop will stop when number becomes 5
num = 1

while num <= 10:
    if num == 5:
        break
    print("Number is:", num)
    num += 1

print("Loop exited using break")


# Stop loop when element equals 30
numbers = [10, 20, 30, 40, 50]

for n in numbers:
    if n == 30:
        break
    print("Current number:", n)

print("Loop exited using break")
