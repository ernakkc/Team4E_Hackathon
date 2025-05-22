from colorama import Fore, Style, init

class Logger:
    def __init__(self):
        init(autoreset=True)  # Initialize colorama with autoreset

    def info(self, message):
        print(f"{Fore.BLUE}[INFO] {message}{Style.RESET_ALL}")

    def warning(self, message):
        print(f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}")

    def error(self, message):
        print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")

    def success(self, message):
        print(f"{Fore.GREEN}[SUCCESS] {message}{Style.RESET_ALL}")