import requests
from colorama import Fore, init
from bs4 import BeautifulSoup

init(autoreset=True)

URL = "https://bitpin.ir/academy/live/currency/"


def currency_tool():
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        print(Fore.RED + "\nRequest timed out.")
        return
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "\nCould not connect to Bitpin.")
        return
    except requests.exceptions.RequestException as error:
        print(Fore.RED + f"\nRequest error: {error}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    currencies = soup.select("[data-price-symbol]")

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.CYAN + 'CURRENCY PRICES'.center(50))
    print(Fore.CYAN + "=" * 50)

    for currency in currencies:
        symbol = currency.get('data-price-symbol', None)
        price = currency.select_one("[data-price-value]")

        if symbol and price:
            print(
                Fore.YELLOW
                + f"{symbol[:3]:<5}"
                + Fore.WHITE
                + " : "
                + Fore.GREEN
                + f"{price.get_text()}"
                + Fore.WHITE
                + " Toman"
            )

    print(Fore.CYAN + "=" * 50)
