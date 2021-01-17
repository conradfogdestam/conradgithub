#UPPGIFT A


s1 = int(input("ange rektangelns första sida: "))
s2 = int(input("ange rektangelns andra sida: ")) #int inputs


print("Höjd | Volym")  # en liten ghetto "formatering" så att printen ska se bra ut
print("-------------")
for h in range(1,11):    # for loopen som loopar 10 ggr och en print med höjd (h) som adderar 1 varje loop
    print(h," |",s1*s2*h )
