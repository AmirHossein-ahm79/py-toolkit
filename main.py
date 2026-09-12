from colorama import Fore, Style, init

from tools.search_files import search_in_files
from tools.website_checker import website_checker
from tools.currency import currency_tool
from tools.caesar_cipher import caesar_cipher

init(autoreset=True)


def show_menu():
    print("\n" + Fore.BLUE + "=" * 40)

    print(Fore.CYAN + Style.BRIGHT + "         PYTHON TOOLKIT")

    print(Fore.BLUE + "=" * 40)

    print("1. Search keyword in files")
    print("2. Caesar Cipher")
    print("3. Website status checker")
    print("4. Currency price")
    print("5. Exit")

    print(Fore.BLUE + "=" * 40)


def main():
    while True:
        show_menu()

        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == "1":
            search_in_files()

        elif choice == "2":
            caesar_cipher()

        elif choice == "3":
            website_checker()

        elif choice == "4":
            currency_tool()

        elif choice == "5":
            print(Fore.GREEN + "\nGoodbye!")
            break

        else:
            print(Fore.RED + "\nInvalid choice!")


if __name__ == "__main__":
    main()
