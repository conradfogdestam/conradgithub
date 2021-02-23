#Uppgift 04

import statistics
from colorama import Fore, Back, Style, init
init(autoreset=True)

tal_lista = []

print(Fore.CYAN +

'''
██╗░░██╗███████╗██████╗░███████╗██╗░░░░░██╗░█████╗░██╗░░██╗
██║░░██║██╔════╝██╔══██╗╚════██║██║░░░░░██║██╔══██╗██║░░██║
███████║█████╗░░██████╔╝░░███╔═╝██║░░░░░██║██║░░╚═╝███████║
██╔══██║██╔══╝░░██╔══██╗██╔══╝░░██║░░░░░██║██║░░██╗██╔══██║
██║░░██║███████╗██║░░██║███████╗███████╗██║╚█████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝

░██╗░░░░░░░██╗██╗██╗░░░░░██╗░░░░░██╗░░██╗░█████╗░███╗░░░███╗███╗░░░███╗███████╗███╗░░██╗
░██║░░██╗░░██║██║██║░░░░░██║░░░░░██║░██╔╝██╔══██╗████╗░████║████╗░████║██╔════╝████╗░██║
░╚██╗████╗██╔╝██║██║░░░░░██║░░░░░█████═╝░██║░░██║██╔████╔██║██╔████╔██║█████╗░░██╔██╗██║
░░████╔═████║░██║██║░░░░░██║░░░░░██╔═██╗░██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██║╚████║
░░╚██╔╝░╚██╔╝░██║███████╗███████╗██║░╚██╗╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝

''')



while True: #loop för input av första talet
    try:
        tal1 = int(input(Fore.MAGENTA + "Mata in ditt första tal: "))

        if tal1 < 0:
            print(Fore.RED + 'ERROR \nAnge positivt heltal')
            pass
        else:
            break

    except:
        print(Fore.RED + 'ERROR \nAnge ett heltal')#simpel felhantering så användaren inte krashar progrmmet

while True: #loop för input av andra talet
    try:
        tal2 = int(input(Fore.MAGENTA + "Mata in ditt andra tal: "))

        if tal2 < 0:
            print(Fore.RED + 'ERROR \nAnge positivt heltal')
            pass
        else:
            break

    except:
        print(Fore.RED + 'ERROR \nAnge ett heltal')#simpel felhantering så användaren inte krashar progrmmet

while True: #loop för input av tredje talet
    try:
        tal3 = int(input(Fore.MAGENTA + "Mata in ditt tredje tal: "))

        if tal3 < 0:
            print(Fore.RED + 'ERROR \nAnge positivt heltal')
            pass
        else:
            break

    except:
        print(Fore.RED + 'ERROR \nAnge ett heltal')#simpel felhantering så användaren inte krashar progrmmet

while True: #loop för input av fjärde talet
    try:
        tal4 = int(input(Fore.MAGENTA + "Mata in ditt fjärde tal: "))

        if tal4 < 0:
            print(Fore.RED + 'ERROR \nAnge positivt heltal')
            pass
        else:
            break

    except:
        print(Fore.RED + 'ERROR \nAnge ett heltal') #simpel felhantering så användaren inte krashar progrmmet

while True: #loop för input av femte talet
    try:
        tal5 = int(input(Fore.MAGENTA + "Mata in ditt femte tal: "))

        if tal5 < 0:
            print(Fore.RED + 'ERROR \nAnge positivt heltal')
            pass
        else:
            break

    except:
        print(Fore.RED + 'ERROR \nAnge ett heltal') #simpel felhantering så användaren inte krashar progrmmet

tal_lista.extend([tal1,tal2,tal3,tal4,tal5])

#prints för största, minsta, median och medelvärde, använde mig utav statistics som jag importerade för att underlätta
print(Fore.CYAN + f"\nStörsta talet du skrivit in är: {max(tal_lista)}")
print(Fore.CYAN + f"Minsta talet du skrivit in är: {min(tal_lista)}")
print(Fore.CYAN + f"Medianen av talen du skrivit in är: {statistics.median(tal_lista)}")
print(Fore.CYAN + f"Medelvärdet av talen du skrivit in är: {statistics.mean(tal_lista)}")
