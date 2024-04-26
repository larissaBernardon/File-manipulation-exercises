import os

class Wine:
    def __init__(self, code,  name, type, alcohol_content, price):
        self.code = code
        self.name = name
        self.type = type
        self.alcohol_content = alcohol_content
        self.price = price

    def __str__(self):
        return f"{self.code}\t{self.name.ljust(20)}\t{self.type}\t{self.alcohol_content}%\t\tR${self.price}"

# Decorator to check file existence before function execution.
# *args and **kwargs allow it to be used with any function.
def ensure_file_exists(func):
    def wrapper(*args, **kwargs):
        if not os.path.exists("data/wines.txt"):
            print("File 'data/wines.txt' does not exist.")
            return
        return func(*args, **kwargs)
    return wrapper

@ensure_file_exists
def register_wine():
    code = input("Enter the code of the wine: ")
    name = input("Enter the name of the wine: ")
    wine_type = input("Enter the type of the wine: ")
    price = float(input("Enter the price of the wine: "))
    price = '{:.2f}'.format(price)
    alcohol_content = float(input("Enter the alcohol content of the wine (%): "))
    alcohol_content = '{:.1f}%'.format(alcohol_content)

    new_wine = Wine(code, name, wine_type, alcohol_content, price)

    with open("data/wines.txt", "a") as file:
        file.write(f"{new_wine.code},{new_wine.name},{new_wine.type},{new_wine.alcohol_content},{new_wine.price}\n")

    print("Wine registered successfully!")

@ensure_file_exists
def list_wines():
    with open("data/wines.txt", "r") as file:
        print("=== List of Wines ===")
        print("Code\tName\t\t\tType\tAlcohol Content\tPrice")
        print("-" * 60)
        for line in file:
            wine_data = line.strip().split(",")
            if len(wine_data) >= 5:
                wine = Wine(*wine_data[:5])
                print(wine)
            else:
                print(f"Invalid data: {line.strip()}")
        print("-" * 60)

@ensure_file_exists
def update_wine(code, new_name=None, new_type=None, new_alcohol_content=None, new_price=None):
    with open("data/wines.txt", "r") as file:
        wines = [Wine(*line.strip().split(",")) for line in file]

    for wine in wines:
        if wine.code == code:
            if new_name:
                wine.name = new_name
            if new_type:
                wine.type = new_type
            if new_alcohol_content:
                wine.alcohol_content = new_alcohol_content
            if new_price:
                wine.price = new_price

            with open("data/wines.txt", "w") as file:
                file.writelines(f"{wine.code},{wine.name},{wine.type},{wine.alcohol_content},{wine.price}\n" for wine in wines)

            print("Wine updated successfully!")
            return

    print("Wine not found with the provided code.")

@ensure_file_exists
def delete_wine(code):
    with open("data/wines.txt", "r") as file:
        wines = [Wine(*line.strip().split(",")) for line in file]

    for wine in wines:
        if wine.code == code:
            print("=== Wine Found ===")
            print(wine)
            confirmation = input("Are you sure you want to delete this wine? (1 - Yes, 2 - No): ")
            if confirmation == "1":
                wines.remove(wine)
                with open("data/wines.txt", "w") as file:
                    file.writelines(f"{wine.code},{wine.name},{wine.type},{wine.alcohol_content},{wine.price}\n" for wine in wines)
                print("Wine deleted successfully!")
                return
            elif confirmation == "2":
                print("Deletion canceled.")
                return
            else:
                print("Invalid input. Please enter 1 for Yes or 2 for No.")
                return

    print("Wine not found with the provided code.")

@ensure_file_exists
def search_wine(value):
    with open("data/wines.txt", "r") as file:
        wines = [Wine(*line.strip().split(",")) for line in file]

    search_results = [wine for wine in wines if value.lower() in (wine.name.lower(), wine.type.lower())]

    if search_results:
        print("=== Search Results ===")
        print("Code\tName\t\t\tType\tAlcohol Content\tPrice")
        print("-" * 60)
        for wine in search_results:
            print(wine)
        print("-" * 60)
    else:
        print("No wines found matching the search criteria.")