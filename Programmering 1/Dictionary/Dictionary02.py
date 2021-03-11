#Conrad Fogdestam TE19D
#Dictionary02

import random as rnd # för att simulera tärningskast

amount = { # dictionary för att hålla info om antal tärningskast på olika nummer
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
}

for i in range(100000): # loopar 100000 gånger random mellan 1-6
    kast = rnd.randint(1,6)
    amount[str(kast)] += 1 # gör random talet till en sträng och lägger till 1 i motsvaande rad i dictionary

print('Amount of rolls')
for key, value in amount.items(): # printar allt ur dictionary 
    print(f"{key}: {value}")