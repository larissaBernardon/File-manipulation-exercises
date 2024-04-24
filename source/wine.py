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
    wines = [
        Wine("Wine 1", "Red", 12.5, 25.0),
        Wine("Wine 2", "White", 10.0, 20.0),
        Wine("Wine 3", "Rosé", 11.0, 18.0)
    ]
    print("Registered wines:")
    for index, wine in enumerate(wines, start=1):
        print(f"{index}. {wine.name} ({wine.type}) - Alcohol: {wine.alcohol_content}%, Price: ${wine.price}")