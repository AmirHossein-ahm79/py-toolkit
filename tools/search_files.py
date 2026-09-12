from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def search_in_files():

    folder_path = input(f"\n{Fore.CYAN}Enter folder path: ")

    keyword = input(f"{Fore.CYAN}Enter keyword: ")

    folder = Path(folder_path)

    if not folder.exists():
        print(f"{Fore.RED}Folder does not exist!")
        return

    if not folder.is_dir():
        print(f"{Fore.RED}The path is not a folder!")
        return

    total_matches = 0
    found_files = 0

    for file in folder.rglob("*"):

        if not file.is_file():
            continue

        try:
            with file.open("r", encoding="utf-8") as f:

                file_matches = 0

                for line_number, line in enumerate(f, start=1):

                    matches = line.lower().count(keyword.lower())

                    if matches > 0:

                        if file_matches == 0:
                            print(f"\n{Fore.GREEN}Found in: " f"{Fore.BLUE}{file}")

                        print(f"{Fore.YELLOW}Line {line_number}: " f"{line.strip()}")

                        file_matches += matches

                if file_matches > 0:

                    print(f"{Fore.MAGENTA}Matches in this file: " f"{file_matches}")

                    found_files += 1
                    total_matches += file_matches

        except (UnicodeDecodeError, PermissionError, OSError):
            continue

    if total_matches == 0:

        print(f"\n{Fore.RED}Keyword was not found.")

    else:

        print(f"\n" + "-" * 40)

        print(f"{Fore.GREEN}Found in {found_files} file(s)")

        print(f"{Fore.GREEN}Total matches: " f"{total_matches}")
