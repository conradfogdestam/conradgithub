#Conrad fogdestam TE19D
#Filhantering 01 a) b) c)
'''
Först importerar jag random (och colorama för fin faktor)
sen en for loop som körs 10 gånger och appendas varje gång till listan 'kastadiceman'
sedan skrivs en osorterad lista ut och sen en sorteradlista med sort()
'''

from colorama import Fore, Back, Style, init
init(autoreset=True)
import random as rnd

kastadediceman = []

for i in range(1,11):
    dice = rnd.randint(1,6)
    kastadediceman.append(dice)
with open("diceFile.txt", "a") as f:
    f.write("10 random dice rolls: " + str(kastadediceman) + "\n")
    kastadediceman.sort()
    f.write("Sorterad lista: " + str(kastadediceman) + "\n")
    f.write("Antal femmor: "+ str(kastadediceman.count(5)) + "\n")

print(Fore.GREEN + "Kolla filen diceFile.txt för svar")
print(Fore.CYAN + '''
───▄▀▀▀▀▀   ▄█▀▀▀█▄
──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██
──▐▒▒▒▒▒▒▒▒███▌▀▐███
───▌▒▓▒▒▒▒▓▒██▌▀▐██
───▌▓▐▀▀▀▀▌▓ ▀▀▀▀▀

''')