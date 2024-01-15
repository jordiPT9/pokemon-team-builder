import csv
from itertools import combinations
from Pokemon import Pokemon 

class TeamBuilder:
  def __init__(self, pokemon_list):
    self.pokemon_list = pokemon_list
    self.best_teams = []  
    self.best_overall_resistances_score = 0sada
    pokedex = []
    with open(csv_file, 'r', encoding='utf-8') as file:
            'hp': int(row['hp']),
            'attack': int(row['attack']),
            'defense': int(row['defense']),
            'sp_attack': int(row['sp_attack']),
            'sp_defense': int(row['sp_defense']),
            'speed': int(row['speed']),
            'weaknesses': sum(float(row[column]) for column in row.keys() if column.startswith('against_')),
            'against_bug': float(row['against_bug']),
            'against_dark': float(row['against_dark']),
            'against_dragon': float(row['against_dragon']),
            'against_electric': float(row['against_electric']),
            'against_fairy': float(row['against_fairy']),
            'against_fight': float(row['against_fight']),
            'against_fire': float(row['against_fire']),
            'against_flying': float(row['against_flying']),
            'against_ghost': float(row['against_ghost']),
            'against_grass': float(row['against_grass']),
            'against_ground': float(row['against_ground']),
            'against_ice': float(row['against_ice']),
            'against_normal': float(row['against_normal']),
            'against_poison': float(row['against_poison']),
            'against_psychic': float(row['against_psychic']),
            'against_rock': float(row['against_rock']),
            'against_steel': float(row['against_steel']),
            'against_water': float(row['against_water'])
        }

        pokemon = Pokemon(**attributes)
        pokedex.append(pokemon)

    return pokedex

  def get_weakness_score(self, damage_multiplier):
    weakness_score = 1 if damage_multiplier == 2 or damage_multiplier == 4 else 0
    return weakness_score
  
  def get_resistance_score(self, damage_multiplier):
    resistance_score = 1 if damage_multiplier == 0.5 or damage_multiplier == 0.25 or damage_multiplier == 0 else 0
    return resistance_score
  
  def evaluate_team(self, team):
    total_team_stats = sum(pokemon.base_total for pokemon in team)
    
    weaknesses = {}
    resistances = {}

    # Define the types you want to calculate weaknesses and resistances for
    types_to_evaluate = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", 
                        "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", 
                        "Psychic", "Rock", "Steel", "Water"]

    for type_to_evaluate in types_to_evaluate:
      type_to_evaluate = type_to_evaluate.lower()
      weaknesses[type_to_evaluate] = sum(self.get_weakness_score(pokemon.__dict__.get(f"against_{type_to_evaluate}", 0)) for pokemon in team)
      resistances[type_to_evaluate] = sum(self.get_resistance_score(pokemon.__dict__.get(f"against_{type_to_evaluate}", 0)) for pokemon in team)

    max_weakness = max(weaknesses.values())
    
    return total_team_stats, sum(weaknesses.values()), sum(resistances.values()), max_weakness

  def get_pokemon(self, name):
    return next((pokemon for pokemon in self.pokedex if pokemon.name == name), None)
  
  def already_exists_with_that_typing(self, pokemon, team):
    for pkmn in team:
      if pkmn.name != pokemon.name:
        if all(item in pokemon.typing for item in pkmn.typing):
          return True
    return False
  
  def build_pokemon_team_from_names(self, team_combination):
    MINIMUM_GOOD_STAT = 95
    team = []
    for pokemon_name in team_combination:
      pokemon = self.get_pokemon(pokemon_name)
      team.append(pokemon)
      if pokemon.attack >= MINIMUM_GOOD_STAT:
        # print(f"phys_atk: {pokemon.name}")
        self.good_stats_count['phys_atk'] += 1
      if pokemon.sp_attack >= MINIMUM_GOOD_STAT:
        # print(f"sp_atk: {pokemon.name}")
        self.good_stats_count['sp_atk'] += 1
      if pokemon.defense >= MINIMUM_GOOD_STAT:
        # print(f"phys_def: {pokemon.name}")
        self.good_stats_count['phys_def'] += 1
      if pokemon.sp_defense >= MINIMUM_GOOD_STAT:
        # print(f"sp_def: {pokemon.name}")
        self.good_stats_count['sp_def'] += 1
    return team
  
  def build_best_teams(self):
    for team_combination in list(combinations(self.pokemon_list, 6)):
      self.good_stats_count = {
        'phys_atk': 0,
        'sp_atk': 0,
        'phys_def': 0,
        'sp_def': 0
      }
      team = self.build_pokemon_team_from_names(team_combination)
      not_eligible_team = False

      for i, pokemon in enumerate(team):
        if self.already_exists_with_that_typing(pokemon, team[i + 1:]):
          not_eligible_team = True
          break
      
      if not all(count >= 1 for count in self.good_stats_count.values()):
        continue

      found_mandatory_pkm = False
      for pokemon in team:
        if pokemon.name == 'Magneton':
          found_mandatory_pkm = True
          break
      
      if not_eligible_team or not found_mandatory_pkm:
        continue  

      total_stats, weaknesses, resistances, max_weakness = self.evaluate_team(team)
      diff = resistances-weaknesses
      if total_stats >= self.best_overall_stats_score and diff >= self.best_diff and max_weakness <= self.MAX_WEAKNESS_VALUE:
        self.best_overall_stats_score = total_stats
        self.best_overall_weaknesses_score = weaknesses
        self.best_overall_resistances_score = resistances
        self.best_diff = diff
        self.best_teams = [team]
    print("")
    print(f"Best total stats: {self.best_overall_stats_score}")
    print(f"Best weaknesses: {self.best_overall_weaknesses_score}")
      base_totals = 0
      print("")
