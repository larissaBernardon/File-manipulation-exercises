from source import wine

def display_menu():
    print("=== Menu ===")
    print("1. Register a new wine")
    print("2. List registered wines")
    print("3. Update a wine")
    print("4. Delete a wine")
    print("5. Search for a wine")
    print("6. Exit")

def get_choice():
    while True:
        choice = input("Choose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return choice.strip()
        else:
            print("Invalid option. Please choose a valid option.")

def register_wine():
    wine.register_wine()

def list_wines():
    wine.list_wines()

def update_wine():
    code = input("Enter the code of the wine you want to update: ")
    new_name = input("Enter the new name of the wine (leave blank to keep current): ")
    new_type = input("Enter the new type of the wine (leave blank to keep current): ")
    new_alcohol_content = input("Enter the new alcohol content of the wine (leave blank to keep current): ")
    new_price = input("Enter the new price of the wine (leave blank to keep current): ")
    wine.update_wine(code, new_name, new_type, new_alcohol_content, new_price)

def delete_wine():
    code = input("Enter the code of the wine you want to delete: ")
    wine.delete_wine(code)

def search_wine():
    value = input("Enter the name or type of the wine you want to search for: ")
    wine.search_wine(value) 