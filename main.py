from source import menu

def main():
    while True:
        menu.display_menu()
        option = menu.get_choice()

        if option == "1":
            menu.register_wine()
        elif option == "2":
            menu.list_wines()
        elif option == "3":
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()