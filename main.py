import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.RED + "red text")
print(Fore.GREEN + "green text")
print(Back.YELLOW + "back yellow text")
print(Style.BRIGHT + "bright text")
print(Fore.RED + Back.YELLOW + Style.BRIGHT + "red text with bright yellow back")

colorama.deinit()