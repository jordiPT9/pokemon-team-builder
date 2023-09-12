import csv
import type_utils

def remove_columns_from_csv(input_file, output_file, columns_to_remove):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = [field for field in reader.fieldnames if field not in columns_to_remove]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            new_row = {field: row[field] for field in fieldnames}
            writer.writerow(new_row)

    print("CSV file has been modified. Removed columns:", columns_to_remove)
    
def recalculate_effectiveness(csv_file, pokemon_list): 
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

    for row in rows:
        if row['name'] in pokemon_list:
            print("---")
            print(f"{row['name']}: {row['type_1']} - {row['type_2']}")
            print("")
            print('')
            row['against_normal'] = type_utils.get_multiplier("Normal", [row['type_1'], row['type_2']])
            print(f"against_normal: {row['against_normal']}")
            print('')
            row['against_fire'] = type_utils.get_multiplier("Fire", [row['type_1'], row['type_2']])
            print(f"against_fire: {row['against_fire']}")
            print('')
            row['against_water'] = type_utils.get_multiplier("Water", [row['type_1'], row['type_2']])
            print(f"against_water: {row['against_water']}")
            print('')
            row['against_electric'] = type_utils.get_multiplier("Electric", [row['type_1'], row['type_2']])
            print(f"against_electric: {row['against_electric']}")
            print('')
            row['against_grass'] = type_utils.get_multiplier("Grass", [row['type_1'], row['type_2']])
            print(f"against_grass: {row['against_grass']}")
            print('')
            row['against_ice'] = type_utils.get_multiplier("Ice", [row['type_1'], row['type_2']])
            print(f"against_ice: {row['against_ice']}")
            print('')
            row['against_fight'] = type_utils.get_multiplier("Fighting", [row['type_1'], row['type_2']])
            print(f"against_fight: {row['against_fight']}")
            print('')
            row['against_poison'] = type_utils.get_multiplier("Poison", [row['type_1'], row['type_2']])
            print(f"against_poison: {row['against_poison']}")
            print('')
            row['against_ground'] = type_utils.get_multiplier("Ground", [row['type_1'], row['type_2']])
            print(f"against_ground: {row['against_ground']}")
            print('')
            row['against_flying'] = type_utils.get_multiplier("Flying", [row['type_1'], row['type_2']])
            print(f"against_flying: {row['against_flying']}")
            print('')
            row['against_psychic'] = type_utils.get_multiplier("Psychic", [row['type_1'], row['type_2']])
            print(f"against_psychic: {row['against_psychic']}")
            print('')
            row['against_bug'] = type_utils.get_multiplier("Bug", [row['type_1'], row['type_2']])
            print(f"against_bug: {row['against_bug']}")
            print('')
            row['against_rock'] = type_utils.get_multiplier("Rock", [row['type_1'], row['type_2']])
            print(f"against_rock: {row['against_rock']}")
            print('')
            row['against_ghost'] = type_utils.get_multiplier("Ghost", [row['type_1'], row['type_2']])
            print(f"against_ghost: {row['against_ghost']}")
            print('')
            row['against_dragon'] = type_utils.get_multiplier("Dragon", [row['type_1'], row['type_2']])
            print(f"against_dragon: {row['against_dragon']}")
            print('')
            row['against_dark'] = type_utils.get_multiplier("Dark", [row['type_1'], row['type_2']])
            print(f"against_dark: {row['against_dark']}")
            print('')
            row['against_steel'] = type_utils.get_multiplier("Steel", [row['type_1'], row['type_2']])
            print(f"against_steel: {row['against_steel']}")
            print('')
            row['against_fairy'] = type_utils.get_multiplier("Fairy", [row['type_1'], row['type_2']])
            print(f"against_fairy: {row['against_fairy']}")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header
        csv_writer.writeheader()
        
        # Write the updated rows
        csv_writer.writerows(rows)


# Example usage:
# input_csv = 'input.csv'
# output_csv = 'pokemon.csv'

# columns_to_remove = [
#     '#', 'german_name', 'japanese_name', 'status', 'species', 'type_number',
#     'height_m', 'weight_kg', 'abilities_number', 'base_friendship',
#     'base_experience', 'growth_rate', 'egg_type_number', 'egg_type_1',
#     'egg_type_2', 'percentage_male', 'egg_cycles'
# ]

# remove_columns_from_csv(input_csv, output_csv, columns_to_remove)
pokemon_list = [
    'Mawile',
    'Azurill',
    'Gardevoir',
    'Kirlia',
    'Ralts',
    'Granbull',
    'Snubbull',
    'Azumarill',
    'Marill ',
    'Togetic',
    'Togepi',
    'Igglybuff',
    'Jigglypuff',
    'Wiglytuff',
    'Mr. Mime',
    'Clefairy',
    'Clefable',
    'Cleffa'
]
recalculate_effectiveness('pokemon.csv', pokemon_list)