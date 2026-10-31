from colorama import Fore, Style, init

init(autoreset=True)


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def caesar_cipher():
    print("\n" + Fore.CYAN + "=" * 45)
    print(Fore.YELLOW + 'CAESAR CIPHER'.center(45))
    print(Fore.CYAN + "=" * 45)

    print(Fore.GREEN + "1. Encrypt text")
    print(Fore.MAGENTA + "2. Decrypt text")

    print(Fore.CYAN + "=" * 45)

    choice = input("Choose an option: ").strip()

    if choice not in ("1", "2"):
        print(Fore.RED + "\nInvalid choice!")
        return

    text = input("\nEnter text: ")

    if not text:
        print(Fore.RED + "\nText cannot be empty!")
        return

    try:
        shift = int(input("Enter shift: "))

    except ValueError:
        print(Fore.RED + "\nShift must be a number.")
        return

    if choice == "1":
        result = encrypt(text, shift)

        print(Fore.GREEN + "\nEncrypted text:")
        print(Fore.GREEN + Style.BRIGHT + result)

    else:
        result = decrypt(text, shift)

        print(Fore.MAGENTA + "\nDecrypted text:")
        print(Fore.MAGENTA + Style.BRIGHT + result)

    print(Fore.CYAN + "=" * 45)
