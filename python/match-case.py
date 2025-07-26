choice = 2

match choice:
    case 1:
        print("You chose One")
    case 2:
        print("You chose Two")
    case 3:
        print("You chose Three")
    case _:
        print("Invalid choice")


command = "start"

match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case _:
        print("Unknown command")

point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at y={y}")
    case (x, 0):
        print(f"X-axis at x={x}")
    case (x, y):
        print(f"Point at x={x}, y={y}")
