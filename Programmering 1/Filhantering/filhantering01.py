#Conrad fogdestam TE19D
#Filhantering 01 a) b) c)
'''
Först importerar jag random (och colorama för fin faktor)
sen en for loop som körs 10 gånger och appendas varje gång till listan 'kastadiceman'
sedan skrivs en osorterad lista ut och sen en sorteradlista med sort()
'''

from colorama import Fore, Back, Style, init
init(autoreset=True)
import random

kastadediceman = []

for i in range(1,11):
    dice = random.randint(1,6)
    kastadediceman.append(dice)
with open("diceRoll.txt", "a") as f:
    f.write("10 random dice rolls: " + str(kastadediceman) + "\n")
    kastadediceman.sort()
    f.write("Sorterad lista: " + str(kastadediceman) + "\n")
    f.write("Antal femmor: " + str(kastadediceman.count(5)) + "\n")

print(Fore.GREEN + "Kolla filen diceRoll.txt för svar")
print(Fore.CYAN + '''
───▄▀▀▀▀▀   ▄█▀▀▀█▄
──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██
──▐▒▒▒▒▒▒▒▒███▌▀▐███
───▌▒▓▒▒▒▒▓▒██▌▀▐██
───▌▓▐▀▀▀▀▌▓ ▀▀▀▀▀

''')