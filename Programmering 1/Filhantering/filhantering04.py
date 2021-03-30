#Conrad fogdestam TE19D

import random
from colorama import Fore, Back, Style, init
init(autoreset=True)


'''
¨### WELCOME ###
jag började med att importera, sedan skapade jag en funktion som sedan kan loopas 
funktionen appendar tärningskasten till en lista och sedan skrivs detta i txt filen 
med hjälp av count för antal 1 or tex, och count antal 1 or /antal tärnings kast tex.

for loopen på slutet loopar funktionen 5 gånger men varje gång så ändras antal tärnings kast med * 10
mha countern

Kaffe för det är gott



'''
filename = 'Simulering.txt'

def dice_roller(rolls_amount):
    rolls = []
    for i in range(rolls_amount):
        roll = random.randint(1, 6)
        rolls.append(roll)
    with open(filename, 'a+') as f:
        f.write(f'Antal tärningskast: {rolls_amount}\n')
        f.write(f'Ettor: {(rolls.count(1))}, Sannolikhet: {(rolls.count(1) / rolls_amount)}\n')
        f.write(f'Tvåor: {(rolls.count(2))}, Sannolikhet: {(rolls.count(2) / rolls_amount)}\n')
        f.write(f'Treor: {(rolls.count(3))}, Sannolikhet: {(rolls.count(3) / rolls_amount)}\n')
        f.write(f'Fyror: {(rolls.count(4))}, Sannolikhet: {(rolls.count(4) / rolls_amount)}\n')
        f.write(f'Femmor: {(rolls.count(5))}, Sannolikhet: {(rolls.count(5) / rolls_amount)}\n')
        f.write(f'Sexor: {(rolls.count(6))}, Sannolikhet: {(rolls.count(6) / rolls_amount)}\n\n')

counter10 = 1
for i in range(5):
    counter10 *= 10
    dice_roller(counter10)



print(Fore.LIGHTMAGENTA_EX + '''
───────────▒▒▒▒▒▒▒▒
─────────▒▒▒──────▒▒▒
────────▒▒───▒▒▒▒──▒░▒
───────▒▒───▒▒──▒▒──▒░▒
──────▒▒░▒──────▒▒──▒░▒
───────▒▒░▒────▒▒──▒░▒
─────────▒▒▒▒▒▒▒───▒▒
─────────────────▒▒▒
─────▒▒▒▒────────▒▒
───▒▒▒░░▒▒▒─────▒▒──▓▓▓▓▓▓▓▓
──▒▒─────▒▒▒────▒▒▓▓▓▓▓░░░░░▓▓──▓▓▓▓
─▒───▒▒────▒▒─▓▓▒░░░░░░░░░█▓▒▓▓▓▓░░▓▓▓
▒▒──▒─▒▒───▓▒▒░░▒░░░░░████▓▓▒▒▓░░░░░░▓▓
░▒▒───▒──▓▓▓░▒░░░░░░█████▓▓▒▒▒▒▓▓▓▓▓░░▓▓
──▒▒▒▒──▓▓░░░░░░███████▓▓▓▒▒▒▒▒▓───▓▓░▓▓
──────▓▓░░░░░░███████▓▓▓▒▒▒▒▒▒▒▓───▓░░▓▓
─────▓▓░░░░░███████▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓
────▓▓░░░░██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░▓▓
────▓▓▓░████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
─────▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
─────▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
──────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
───────▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
─────────▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
───────────▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓
───────────────▓▓▓▓▓▓▓▓

TASTY COFFEE
''')

print("kolla filen Simulering.txt för svar")

