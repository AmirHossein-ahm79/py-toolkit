import requests
import re
from colorama import Fore, init

from bs4 import BeautifulSoup

init(autoreset=True)

URL = "https://bitpin.ir/academy/live/currency/"


CURRENCIES = {
    "USD": "دلار",
    "EUR": "یورو",
    "AED": "درهم",
    "GBP": "پوند",
    "AFN": "افغانی",
    "IQD": "دینار عراق",
    "TRY": "لیر ترکیه",
    "CNY": "یوان چین",
    "OMR": "ریال عمان",
}


def normalize_digits(text):
    """
    Convert Persian and Arabic digits to English digits.
    """

    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    arabic_digits = "٠١٢٣٤٥٦٧٨٩"

    for i in range(10):
        text = text.replace(persian_digits[i], str(i))
        text = text.replace(arabic_digits[i], str(i))

    return text


def get_price(text, currency_name):
    """
    Extract the price of a currency from page text.
    """

    pattern = rf"{re.escape(currency_name)}.{{0,100}}?([\d٬,]+)\s*تومان"

    match = re.search(pattern, text)

    if not match:
        return None

    price = normalize_digits(match.group(1))

    price = price.replace(",", "")
    price = price.replace("٬", "")

    return int(price)


def format_price(price):
    return f"{price:,}"


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
    page_text = soup.get_text(" ", strip=True)

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.CYAN + "            CURRENCY PRICES")
    print(Fore.CYAN + "=" * 50)

    found = False

    for code, currency_name in CURRENCIES.items():
        price = get_price(page_text, currency_name)

        if price is None:
            continue

        found = True

        print(
            Fore.YELLOW
            + f"{code:<5}"
            + Fore.WHITE
            + " : "
            + Fore.GREEN
            + f"{format_price(price)}"
            + Fore.WHITE
            + " Toman"
        )

    if not found:
        print(Fore.RED + "\nCould not extract currency prices.")

    print(Fore.CYAN + "=" * 50)
