#Conrad Fogdestam TE19D
#Dictionary01

kurser = {
    'tillämpad_1' : 100,
    'programmering_1' : 100,
    'daodac' : 100,
    'web_1' : 100,
    'svenska_2' : 100,
    'fysik_1' : 150,
    'idrott' : 100,
    'engelska_6' : 100,
    'matematik_4' : 100
}


points = 0

for key,value in kurser.items():
    points += value

print(points,'poång totalt')