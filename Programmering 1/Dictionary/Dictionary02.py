import random as rnd

amount = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
}

for i in range(100000):
    kast = rnd.randint(1,6)
    amount[str(kast)] += 1

print('Frekvenstabell')
for key, value in amount.items():
    print(f"{key}: {value}")