pokedex = {}

with open('pokemonlist.txt', 'r') as f:
    for line in f:
        index, pokemon, typ = line.split()
        pokedex[pokemon] = [typ, index]


user_input = str(input("Select a pokemon: ")).capitalize()

print(f"Din valda pokemon: {user_input}")
print(f"Typ: {pokedex[user_input][0]}, Index: {pokedex[user_input][1]}")