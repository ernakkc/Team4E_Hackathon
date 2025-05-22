import os
import shutil
from colorama import init, Fore, Style

options =[
    (Fore.WHITE,  "\t\t(3.1) CRUD OPERATIONS"),
    (Fore.GREEN,     "🟩  1. (3.1-1) Add Data"),
    (Fore.GREEN,     "📄  2. (3.1-2) Display Data"),
    (Fore.GREEN,     "📝  3. (3.1-3) Update Data"),
    (Fore.GREEN,     "🗑️   4. (3.1-4) Delete Data"),

    (Fore.WHITE,  "\n\t\t(3.2) DATA ANALYSIS TASKS"),
    (Fore.LIGHTBLUE_EX, "📈  5. (3.2-1) Countries Above Threshold"),
    (Fore.LIGHTBLUE_EX, "⚖️   6. (3.2-2) Country Comparison"),
    (Fore.LIGHTBLUE_EX, "📊  7. (3.2-3) Countries with Emissions in a Certain Range"),
    (Fore.LIGHTBLUE_EX, "📆  8. (3.2-4) Year-to-Year Comparison"),
    (Fore.LIGHTBLUE_EX, "🧮  9. (3.2-5) Average Emission"),
    (Fore.LIGHTBLUE_EX, "📏 10. (3.2-6) Emission Intensity"),
    (Fore.LIGHTBLUE_EX, "📉 11. (3.2-7) Trend Analysis over Time"),
    (Fore.LIGHTBLUE_EX, "↕️  12. (3.2-8) Sorting Emission Data"),
    (Fore.LIGHTBLUE_EX, "🚀 13. (3.2-9) Countries with the Highest Increase and Decrease in Emissions"),
    (Fore.LIGHTBLUE_EX, "📝 14. (3.2-10) Report Generation"),

    (Fore.MAGENTA,"\n\t\t🚪 15. Exit")
]


init(autoreset=True)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    return text.center(width)

def printBanner(width):
    banner = [
    r"  _____                  _                   _          _______ ",
    r" / ___ \                | |                 | |        (_______)",
    r"| |   | |_   _  ____  _ | | ____ _   _ ____ | | ____    _____   ",
    r"| |   |_| | | |/ _  |/ || |/ ___) | | |  _ \| |/ _  )  |  ___)  ",
    r" \ \____| |_| ( ( | ( (_| | |   | |_| | | | | ( (/ /   | |_____ ",
    r"  \_____)\____|\_||_|\____|_|    \____| ||_/|_|\____)  |_______)",
    r"                                      |_|                       ",
    r"             [ Quadruple E Hackathon Team ]                    "
    ]

    print(Fore.CYAN + "=" * width)
    for line in banner:
        print(Fore.RED + Style.BRIGHT + center_text(line, width))
    print(Fore.CYAN + "=" * width)

def printMenu():
    clearScreen()
    width = shutil.get_terminal_size().columns

    printBanner(width)

    for color, opt in options:
        print(color + Style.BRIGHT + opt)

    print(Fore.CYAN + "=" * width)
    choice = input(Fore.WHITE + Style.BRIGHT + center_text("📌 Enter your choice (1-15): ", width))
    return choice

def goodbye():
    clearScreen()
    print(Fore.GREEN + Style.BRIGHT + "👋 Goodbye! Keep living with Quadruple E.")
    exit(0)
    
def wait_for_user():
    input(Fore.WHITE + Style.BRIGHT + center_text("Press Enter to continue...", shutil.get_terminal_size().columns))
    clearScreen()