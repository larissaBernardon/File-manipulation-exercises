class Wine:
    def __init__(self, code,  name, type, alcohol_content, price):
        self.code = code
        self.name = name
        self.type = type
        self.alcohol_content = alcohol_content
        self.price = price

def register_wine():
    try:
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
                code, name, wine_type, alcohol_content, price = line.strip().split(",")
                print(f"{code}\t{name.ljust(20)}\t{wine_type}\t{alcohol_content}%\t\tR${price}")
            print("-" * 60)
    except FileNotFoundError:
        print("No wines found. Please register some wines first.")