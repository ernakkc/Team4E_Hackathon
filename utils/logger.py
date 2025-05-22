from colorama import Fore, Style, init

class Logger:
    def __init__(self):
        init(autoreset=True)  # Initialize colorama with autoreset

    def info(self, message, end="\n"):
        print(f"{Fore.LIGHTBLUE_EX}[INFO] {message}{Style.RESET_ALL}", end=end)

    def warning(self, message, end="\n"):
        print(f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}", end=end)

    def error(self, message, end="\n"):
        print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}", end=end)

    def success(self, message, end="\n"):
        print(f"{Fore.GREEN}[SUCCESS] {message}{Style.RESET_ALL}", end=end)