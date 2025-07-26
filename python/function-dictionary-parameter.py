def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Call with dictionary-style arguments
print_details(name="Ali", course="Python", level="Beginner")
