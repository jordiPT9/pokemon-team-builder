import csv

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

# Example usage:
input_csv = 'input.csv'
output_csv = 'pokemon.csv'

columns_to_remove = [
    '#', 'german_name', 'japanese_name', 'status', 'species', 'type_number',
    'height_m', 'weight_kg', 'abilities_number', 'base_friendship',
    'base_experience', 'growth_rate', 'egg_type_number', 'egg_type_1',
    'egg_type_2', 'percentage_male', 'egg_cycles'
]

remove_columns_from_csv(input_csv, output_csv, columns_to_remove)
