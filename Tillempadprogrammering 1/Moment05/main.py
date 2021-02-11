#import för färg på texten
from colorama import init
from colorama import Fore, Back, Style
init()
balance = 1000

print(Fore.GREEN + f'''
Thank you for choosing Cayman Islands National Bank™
Your available balance is: {balance}
''')
