import os

class Wine:
    def __init__(self, code,  name, type, alcohol_content, price):
        self.code = code
        self.name = name
        self.type = type
        self.alcohol_content = alcohol_content
        self.price = price

def file_exists(file_path):
    return os.path.exists(file_path)

def register_wine():
    try:
        if not file_exists("data/wines.txt"):
            print("File 'data/wines.txt' does not exist.")
            return
        
        code = input("Enter the code of the wine: ")
        name = input("Enter the name of the wine: ")
        wine_type = input("Enter the type of the wine: ")
        alcohol_content = float(input("Enter the alcohol content of the wine: "))
        price = float(input("Enter the price of the wine: "))

        new_wine = f"{code},{name},{wine_type},{alcohol_content},{price}"

        with open("data/wines.txt", "a") as file:
            file.write(new_wine + "\n")

        print("Wine registered successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for alcohol content and price.")


def list_wines():
    try:
        with open("data/wines.txt", "r") as file:
            print("=== List of Wines ===")
            print("Code\tName\t\t\tType\tAlcohol Content\tPrice")
            print("-" * 60)
            for line in file:
                wine_data = line.strip().split(",")
                if len(wine_data) >= 5:
                    code, name, wine_type, alcohol_content, price = wine_data[:5]
                    print(f"{code}\t{name.ljust(20)}\t{wine_type}\t{alcohol_content}%\t\tR${price}")
                else:
                    print(f"Invalid data: {line.strip()}")
            print("-" * 60)
    except FileNotFoundError:
        print("No wines found. Please register some wines first.")



def update_wine(code, new_name=None, new_type=None, new_alcohol_content=None, new_price=None):
    try:
        if not file_exists("data/wines.txt"):
            print("File 'data/wines.txt' does not exist.")
            return
        
        with open("data/wines.txt", "r") as file:
            wines = file.readlines()

        wine_index = None
        for index, wine in enumerate(wines):
            if wine.split(",")[0] == code:
                wine_index = index
                break

        if wine_index is not None:
            current_wine = wines[wine_index].strip().split(",")

            if new_name:
                current_wine[1] = new_name
            if new_type:
                current_wine[2] = new_type
            if new_alcohol_content:
                current_wine[3] = new_alcohol_content
            if new_price:
                current_wine[4] = new_price

            updated_wine = ",".join(current_wine) + "\n"

            wines[wine_index] = updated_wine

            with open("data/wines.txt", "w") as file:
                file.writelines(wines)

            print("Wine updated successfully!")
        else:
            print("Wine not found with the provided code.")
    except FileNotFoundError:
        print("No wines found. Please register some wines first.")


def delete_wine(code):
    try:
        if not file_exists("data/wines.txt"):
            print("File 'data/wines.txt' does not exist.")
            return
        
        with open("data/wines.txt", "r") as file:
            wines = file.readlines()

        wine_found = False
        for index, wine in enumerate(wines):
            if wine.split(",")[0] == code:
                wine_found = True
                wine_info = wine.strip().split(",")
                print("=== Wine Found ===")
                print("Code:", wine_info[0])
                print("Name:", wine_info[1])
                print("Type:", wine_info[2])
                print("Alcohol Content:", wine_info[3])
                print("Price:", wine_info[4])
                while True:
                    confirmation = input("Are you sure you want to delete this wine? (1 - Yes, 2 - No): ")
                    if confirmation == "1":
                        wines[index] = "" 
                        with open("data/wines.txt", "w") as file:
                            file.writelines(wines)
                        print("Wine deleted successfully!")
                        break
                    elif confirmation == "2":
                        print("Deletion canceled.")
                        break
                    else:
                        print("Invalid input. Please enter 1 for Yes or 2 for No.")
                break

        if not wine_found:
            print("Wine not found with the provided code.")
    except FileNotFoundError:
        print("No wines found. Please register some wines first.")


def search_wine(value):
    try:
        if not file_exists("data/wines.txt"):
            print("File 'data/wines.txt' does not exist.")
            return
        
        search_results = []
        with open("data/wines.txt", "r") as file:
            for line in file:
                try:
                    code, name, wine_type, alcohol_content, price = line.strip().split(",")
                    if value.lower() in (name.lower(), wine_type.lower()):
                        search_results.append((code, name, wine_type, alcohol_content, price))
                    elif value.isdigit() and any(field == float(value) for field in (alcohol_content, price)):
                        search_results.append((code, name, wine_type, alcohol_content, price))
                except ValueError:
                    pass

        if search_results:
            print("=== Search Results ===")
            print("Code\tName\t\t\tType\tAlcohol Content\tPrice")
            print("-" * 60)
            for result in search_results:
                print("\t".join(result))
            print("-" * 60)
        else:
            print("No wines found matching the search criteria.")
    except FileNotFoundError:
        print("No wines found. Please register some wines first.")