#UPPGIFT E

#gjorde uppgifterna inna med funktioner från början så behöver inte ändra

sida1 = []
sida2 = []
area = []
hojd = []
volym = []
kvadrat = []

global counter
counter = 0

def areafunk(s1,s2):
    a = s1*s2
    return a

def volfunk(s1,s2,h):
    v = s1*s2*h
    return v

def kvadratfunk(s1,s2):
    if s1 == s2:
        return 'ja'

while True:
    userinput = input("Vill du göra en uträkning (Y/N): ").upper()

    if userinput == 'Y':
        counter += 1

        s1 = int(input("ange rektangelns första sida: "))
        sida1.append(s1)
        s2 = int(input("ange rektangelns andra sida: "))
        sida2.append(s2)

        while True:
            try:
                h = int(input("Ange rektangelns höjd: "))
                break
            except:
                print("inte ett heltal")

        hojd.append(h)
        area.append(areafunk(s1,s2))
        volym.append(volfunk(s1,s2,h))
        kvadrat.append(kvadratfunk(s1,s2))

        if kvadratfunk(s1,s2) == 'ja':
            print(f"Arean på rektangeln med sidorna {s1} & {s2} är {areafunk(s1,s2)}, och det är en kvadrat", "\n")
        else:
            print(f"Arean på rektangeln med sidorna {s1} & {s2} är {areafunk(s1,s2)}", "\n")

        print("Höjd | Volym")
        print("-------------")
        for h in range(1,h+1):
            print(h,"  |",s1*s2*h)

    else:
        for i in range(counter):
            if kvadrat[i] == 'ja':
                print(f"Beräkning {i+1} har sidorna {sida1[i]} och {sida2[i]} och arean blir {area[i]}, och det är en kvadrat")
            else:
                print(f"Beräkning {i+1} har sidorna {sida1[i]} och {sida2[i]} och arean blir {area[i]}")

        break