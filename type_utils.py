TYPE_INDEX = {
    "Normal": 0,
    "Fighting": 1,
    "Flying": 2,
    "Rock": 5,
    "Grass": 11,
    "Electric": 12,
    "Ice": 14,
    "Dragon": 15,
    "Dark": 16,
    "Fairy": 17
}

TYPE_CHART = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
[1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
[1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
[1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
[1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
[1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
[0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
[1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
[1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
[1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
[1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],

def get_multiplier(attacking_type_str, pokemon_types_str_array):
  if pokemon_types_str_array[1] == '':
    attacking_type = TYPE_INDEX.get(attacking_type_str, 1)
    defending_type_1 = TYPE_INDEX.get(pokemon_types_str_array[0], 1)
    damage_multiplier_1 = TYPE_CHART[attacking_type][defending_type_1]
    print(f"{attacking_type_str} * {pokemon_types_str_array[0]} = {damage_multiplier_1}")

    return damage_multiplier_1

  attacking_type = TYPE_INDEX.get(attacking_type_str, 1)
  defending_type_1 = TYPE_INDEX.get(pokemon_types_str_array[0], 1)
  defending_type_2 = TYPE_INDEX.get(pokemon_types_str_array[1], 1)
  damage_multiplier_1 = TYPE_CHART[attacking_type][defending_type_1]

    return 1
  return damage_multiplier_1 * damage_multiplier_2

# attacking_type = 'Psychic'
# pokemon_types = ['Dark', None]
# damage_multiplier = get_multiplier(attacking_type, pokemon_types)