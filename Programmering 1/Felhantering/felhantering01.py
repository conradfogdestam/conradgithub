#Uppgift 01
#conrad TE19D

'''
Först kommer alla imports, importade colorama för att det skulle bli lite fin färg.

La in en lite fin och stor titel till programmet
'''
import numpy as np
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.CYAN + '''
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░██████╗  ████████╗██╗░░██╗███████╗
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚█████╗░  ░░░██║░░░███████║█████╗░░
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██████╔╝  ░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██████╗░██╗░██████╗████████╗░█████╗░███╗░░██╗░█████╗░███████╗░█████╗░░█████╗░░█████╗░
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░╚═╝█████╗░░╚═╝███╔╝╚═╝███╔╝╚═╝███╔╝
██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██╗██╔══╝░░░░░╚══╝░░░░╚══╝░░░░╚══╝░
██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║╚█████╔╝███████╗░░░██╗░░░░░██╗░░░░░██╗░░
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝░░░╚═╝░░░░░╚═╝░░░░░╚═╝░░''')

import numpy as np

def distance(p1, p2):
    d = np.sqrt(p1+p2)  #funktion räknar distansen mellan två punkter med två parametrar och returnar svaret "d".
    return d  

print(Fore.LIGHTMAGENTA_EX + 'Distansen mellan de två punkterna är: ') #för att fä en lite finare utskrift.
print(distance(0.5,0.5)) #printar funktionen med två redan bestämda parametrar.

