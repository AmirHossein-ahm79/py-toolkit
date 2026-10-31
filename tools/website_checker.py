import requests
from colorama import Fore, init

init(autoreset=True)


def website_checker():
    url = input(f"\n{Fore.CYAN}Enter website URL: ").strip()
    if not url:
        print(f"{Fore.RED}URL cannot be empty!")
        return

    # Add protocol if user did not enter one
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5, allow_redirects=True)

        print(f"\n{Fore.BLUE}" + "=" * 40)
        print(f"{Fore.CYAN}" + 'WEBSITE STATUS'.center(40))
        print(f"{Fore.BLUE}" + "=" * 40)
        print(f"{Fore.CYAN}URL           : " f"{Fore.WHITE}{url}")
        print(f"{Fore.CYAN}Final URL     : " f"{Fore.WHITE}{response.url}")
        print(f"{Fore.CYAN}Status Code   : " f"{Fore.WHITE}{response.status_code}")
        print(f"{Fore.CYAN}Response Time : " f"{Fore.WHITE}{response.elapsed.total_seconds():.2f}s")

        if response.status_code == 200:
            print(f"{Fore.CYAN}Status        : " f"{Fore.GREEN}✅ Online")
        elif 300 <= response.status_code < 400:
            print(f"{Fore.CYAN}Status        : " f"{Fore.YELLOW}↪️ Redirect")
        elif 400 <= response.status_code < 500:
            print(f"{Fore.CYAN}Status        : " f"{Fore.YELLOW}⚠️ Client Error")
        elif 500 <= response.status_code < 600:
            print(f"{Fore.CYAN}Status        : " f"{Fore.RED}❌ Server Error")
        else:
            print(f"{Fore.CYAN}Status        : " f"{Fore.WHITE}ℹ️ Unknown")

        print(f"{Fore.BLUE}" + "=" * 40)

    except requests.exceptions.Timeout:
        print(f"\n{Fore.RED}❌ Request timed out.")
    except requests.exceptions.ConnectionError:
        print(f"\n{Fore.RED}❌ Could not connect to the website.")
    except requests.exceptions.RequestException as error:
        print(f"\n{Fore.RED}❌ Request error: " f"{Fore.WHITE}{error}")
