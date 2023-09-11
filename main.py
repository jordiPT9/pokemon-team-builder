import csv
import time
from itertools import permutations, combinations

class Pokemon:
    def __init__(self,
                 name,
                 type1,
                 type2,
                 base_total,
                 hp,
                 attack,
                 defense,
                 sp_attack,
                 sp_defense,
                 speed,
                 weaknesses,
                 against_bug,
                 against_dark,
                 against_dragon,
                 against_electric,
                 against_fairy,
                 against_fight,
                 against_fire,
                 against_flying,
                 against_ghost,
                 against_grass,
                 against_ground,
                 against_ice,
                 against_normal,
                 against_poison,
                 against_psychic,
                 against_rock,
                 against_steel,
                 against_water):
        self.name = name
        self.typing = [type1, type2]
        self.base_total = base_total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.weaknesses = weaknesses
        self.against_bug = against_bug
        self.against_dark = against_dark
        self.against_dragon = against_dragon
        self.against_electric = against_electric
        self.against_fairy = against_fairy
        self.against_fight = against_fight
        self.against_fire = against_fire
        self.against_flying = against_flying
        self.against_ghost = against_ghost
        self.against_grass = against_grass
        self.against_ground = against_ground
        self.against_ice = against_ice
        self.against_normal = against_normal
        self.against_poison = against_poison
        self.against_psychic = against_psychic
        self.against_rock = against_rock
        self.against_steel = against_steel
        self.against_water = against_water

class PokemonTeamBuilder:
    def __init__(self, pokemon_list):
        self.pokedex = self._load_pokemon_data('pokemon.csv')
        self.pokemon_list = pokemon_list
        self.best_teams = []  
        self.best_total_stats_score = 0
        self.best_weaknesses_score = float('-inf')
        self.MAX_WEAKNESS_VALUE = 10

    def _load_pokemon_data(self, csv_file):
        pokedex = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_weaknesses = float(row['against_bug']) + \
                    float(row['against_dark']) + \
                    float(row['against_dragon']) + \
                    float(row['against_electric']) + \
                    float(row['against_fairy']) + \
                    float(row['against_fight']) + \
                    float(row['against_fire']) + \
                    float(row['against_flying']) + \
                    float(row['against_ghost']) + \
                    float(row['against_grass']) + \
                    float(row['against_ground']) + \
                    float(row['against_ice']) + \
                    float(row['against_normal']) + \
                    float(row['against_poison']) + \
                    float(row['against_psychic']) + \
                    float(row['against_rock']) + \
                    float(row['against_steel']) + \
                    float(row['against_water'])
                pokemon = Pokemon(
                    row['name'],
                    row['type_1'], 
                    row['type_2'], 
                    int(row['total_points']),
                    int(row['hp']),
                    int(row['attack']),
                    int(row['defense']),
                    int(row['sp_attack']),
                    int(row['sp_defense']),
                    int(row['speed']),
                    total_weaknesses,
                    float(row['against_bug']),
                    float(row['against_dark']),
                    float(row['against_dragon']),
                    float(row['against_electric']),
                    float(row['against_fairy']),
                    float(row['against_fight']),
                    float(row['against_fire']),
                    float(row['against_flying']),
                    float(row['against_ghost']),
                    float(row['against_grass']),
                    float(row['against_ground']),
                    float(row['against_ice']),
                    float(row['against_normal']),
                    float(row['against_poison']),
                    float(row['against_psychic']),
                    float(row['against_rock']),
                    float(row['against_steel']),
                    float(row['against_water']))
                pokedex.append(pokemon)
        return pokedex

    def _evaluate_team(self, team):
        total_team_stats = sum(pokemon.base_total for pokemon in team)
        weaknesses = {
            "Bug": 0,
            "Dark": 0,
            "Dragon": 0,
            "Electric": 0,
            "Fairy": 0,
            "Fight": 0,
            "Fire": 0,
            "Flying": 0,
            "Ghost": 0,
            "Grass": 0,
            "Ground": 0,
            "Ice": 0,
            "Normal": 0,
            "Poison": 0,
            "Psychic": 0,
            "Rock": 0,
            "Steel": 0,
            "Water": 0
        }

        for pokemon in team:
            weaknesses["Bug"] += pokemon.against_bug
            weaknesses["Dark"] += pokemon.against_dark
            weaknesses["Dragon"] += pokemon.against_dragon
            weaknesses["Electric"] += pokemon.against_electric
            weaknesses["Fairy"] += pokemon.against_fairy
            weaknesses["Fight"] += pokemon.against_fight
            weaknesses["Fire"] += pokemon.against_fire
            weaknesses["Flying"] += pokemon.against_flying
            weaknesses["Ghost"] += pokemon.against_ghost
            weaknesses["Grass"] += pokemon.against_grass
            weaknesses["Ground"] += pokemon.against_ground
            weaknesses["Ice"] += pokemon.against_ice
            weaknesses["Normal"] += pokemon.against_normal
            weaknesses["Poison"] += pokemon.against_poison
            weaknesses["Psychic"] += pokemon.against_psychic
            weaknesses["Rock"] += pokemon.against_rock
            weaknesses["Steel"] += pokemon.against_steel
            weaknesses["Water"] += pokemon.against_water

        return total_team_stats, sum(weaknesses.values()), max(weaknesses.values())

    def _get_pokemon(self, name):
        return next((pokemon for pokemon in self.pokedex if pokemon.name == name), None)
    
    def _already_exists_with_that_typing(self, pokemon, team):
        for pkmn in team:
            if pkmn.name != pokemon.name:
                if pokemon.typing[0] == pkmn.typing[0] and pokemon.typing[1] == pkmn.typing[1]:
                    return True
                if pokemon.typing[0] == pkmn.typing[1] and pokemon.typing[1] == pkmn.typing[0]:
                    return True
            return None
    
    def build_best_teams(self):
        self.best_total_stats_score = 0
        self.best_weaknesses_score = float('inf')

        for team_combination in list(combinations(self.pokemon_list, 6)):
            team = []
            for pokemon_name in team_combination:
                pokemon = self._get_pokemon(pokemon_name)
                team.append(pokemon)

            found = False
            found_c = False
            found_s = False
            for pokemon in team:
                if pokemon.name == 'Cacturne':
                    found_c = True
                if pokemon.name == 'Shiftry':
                    found_s = True

                found_p = self._already_exists_with_that_typing(pokemon, team)
                if found_p:
                    found = True
                    break

            # if found_c and found_s:
            #     for pokemon in team:
            #         print(pokemon.name)

            if found:
                for pokemon in team:
                    print(pokemon.name)
                break


            total_stats, weaknesses, max_weakness = self._evaluate_team(team)

            if total_stats > self.best_total_stats_score and weaknesses <= self.best_weaknesses_score and max_weakness < self.MAX_WEAKNESS_VALUE:
                self.best_total_stats_score = total_stats
                self.best_weaknesses_score = weaknesses
                self.best_teams = [team]

        for team_combination in list(combinations(self.pokemon_list, 6)):
            team = []
            for pokemon_name in team_combination:
                pokemon = self._get_pokemon(pokemon_name)
                team.append(pokemon)

            found = False
            for pokemon in team:
                found_p = self._already_exists_with_that_typing(pokemon, team)
                if found_p != False:
                    # print(f"{pokemon.name} - {pokemon_2.name}")
                    found = True

            if found:
                break

            total_stats, weaknesses, max_weakness = self._evaluate_team(team)

            if (abs((total_stats - self.best_total_stats_score) / total_stats) * 100) <= 1 and (abs((weaknesses - self.best_weaknesses_score) / weaknesses) * 100) <= 1 and max_weakness < self.MAX_WEAKNESS_VALUE:
                self.best_teams.append(team)


if __name__ == "__main__":
    pokemon_list = [
        # 'Wigglytuff',
        'Beedrill',
        'Persian',
        'Linoone',
        'Beautifly',
        # 'Togetic',
        'Camerupt',
        'Cacturne',
        'Jynx',
        'Ampharos',
        # 'Clefable',
        'Murkrow',
        'Shiftry',
        'Dewgong',
        # 'Gardevoir',
        'Manectric',
        'Pupitar',
        'Hypno',
        'Nidoqueen',
        'Noctowl',
        'Quagsire',
        'Lanturn',
        'Kingler',
        'Gengar',
        'Marowak',
        'Swampert',
        'Dodrio',
        # 'Granbull',
        'Sceptile',
        'Houndoom',
        'Magneton',
    ]

    start_time = time.time()

    team_builder = PokemonTeamBuilder(pokemon_list)
    team_builder.build_best_teams()
    end_time = time.time()

    elapsed_time = end_time - start_time

    best_teams = team_builder.best_teams
    
    print("")
    print(f"Best total stats: {team_builder.best_total_stats_score}")
    print(f"Best weaknesses: {team_builder.best_weaknesses_score}")
    print("Best Teams:")
    print("")
    for i, team in enumerate(best_teams, start=1):
        print(f"Team {i}:")
        base_totals = 0
        total_weaknesses = 0
        for pokemon_list in team:
            base_totals += pokemon_list.base_total 
            total_weaknesses += pokemon_list.weaknesses 
            print(f"Pokemon: {pokemon_list.name}, Typing: {pokemon_list.typing}, Total Stats: {pokemon_list.base_total}")
        print(f"Total stats: {base_totals}")
        print(f"Total weaknesses: {total_weaknesses}")
        print("")
    
    print(f"Elapsed ime: {elapsed_time:.6f} seconds")
