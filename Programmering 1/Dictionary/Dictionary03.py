#Conrad Fogdestam TE19D
#Dictionary03


pokedex = {}

with open('pokemonlist.txt', 'r') as f: # läser in alla pokemon till pokedex från txt filen. sedan split och asignar pokemon som key och typ och index som values
    for line in f:
        index, pokemon, typ = line.split()
        pokedex[pokemon] = [typ, index]



print('typ:', pokedex['Gastly'][0], ', index', pokedex['Gastly'][1]) # print första value av key, sen andra value av key
print('typ:', pokedex['Pikachu'][0], ', index', pokedex['Pikachu'][1])
