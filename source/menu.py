def display_menu():
    print("=== Menu ===")
    print("1. Register a new wine")
    print("2. List registered wines")
    print("3. Exit")

def get_choice():
    while True:
        choice = input("Choose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return choice.strip()
        else:
            print("Invalid option. Please choose a valid option.")

def register_wine():
    print("Option to register a new wine selected.")

def list_wines():
    print("Option to list registered wines selected.")