from colorama import Fore, Back, Style, init
init(autoreset=True)

'''
Uppgift A använder jag readline som körs 19 gånger för att det finns 19 personer alltå 19 rader

'''

filename = 'Provresultat.txt'

# A)
with open(filename, 'r') as f:
    print(Fore.LIGHTMAGENTA_EX + 'CONTENTS OF "Provresultat.txt": ')
    for i in range(1,20):
        print(Fore.CYAN + f.readline().strip('\n'))

    print(Fore.LIGHTMAGENTA_EX + '----------------------------------------------')


'''
Uppgift B använder jag samma readline for loop man appendar istället för att printas, sedan använder jag .sort() 
och sedan har jag en till for loop för att printa ut den nu sorterade listan i txt filen med f.write

'''

# B)
with open(filename, "r+") as f:
    infile = []
    for i in range(1,21):
        infile.append(f.readline())
    infile.sort()
    f.write("\n------------------\n")
    f.write("SORTED IN ALPHABETICAL ORDER")
    f.write("\n------------------\n")
    for i in infile:
        f.write(i)

    f.write("\n")
    print(Fore.LIGHTMAGENTA_EX + f"\nAlphabetical order list in '{filename}\n")

'''
Uppgift C anväder jag listor för alla olika betyg, sen har jag en for loop som appendar namnen och betygen från txt doc
sen en yttiligare for loop som loopar igenom 'infile' och kollar vilket betyg eleven ska få och lägger till dom i den listan de ska tillhöra.
(deta görs mha variabeln elev_betyg som kollar de sista karaktärerna på motsvarande rad och gör dom till en intager, 
'elev_betyg' åker igenom if satserna och hamnar i rätt lista)
'''

# C)
F = []
E = []
D = []
C = []
B = []
A = []
infile = []
with open(filename, "r+") as f:
    for i in range(1,20):
        infile.append(f.readline())
    for elev in infile:
        elev_betyg = int(elev[-3:])
        if elev_betyg < 20:
            F.append(elev)
        elif elev_betyg >= 20 and elev_betyg <= 29:
            E.append(elev)
        elif elev_betyg >= 30 and elev_betyg <= 39:
            D.append(elev)
        elif elev_betyg >= 40 and elev_betyg <= 49:
            C.append(elev)
        elif elev_betyg >= 50 and elev_betyg <= 59:
            B.append(elev)
        elif elev_betyg >= 60 and elev_betyg <= 70:
            A.append(elev)
    f.write("\n------------------\n")
    f.write("SORTED BY GOOD GRADES TO BAD GRADES")
    f.write("\n------------------\n")
    f.write("\n(A) ELEVER \n")
    for elev in A:
        f.write(elev)
    f.write("\n(B) ELEVER:\n")
    for elev in B:
        f.write(elev)
    f.write("\n(C) ELEVER:\n")
    for elev in C:
        f.write(elev)
    f.write("\n(D) ELEVER:\n")
    for elev in D:
        f.write(elev)
    f.write("\n(E) ELEVER:\n")
    for elev in E:
        f.write(elev)
    f.write("\n(F) ELEVER: \n")
    for elev in F:
        f.write(elev)

    print(Fore.LIGHTMAGENTA_EX + f"In order by grades list in '{filename}'")

print(Fore.LIGHTMAGENTA_EX + '''
              ▄▀█▀█▀▄
             ▀▀▀▀▀▀▀▀▀ 
             ▄ ░░░░░▄
   █  ▄ ▄   ▐▌▌░░░░░▌▌
▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌
''')
