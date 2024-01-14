import time
from itertools import permutations, combinations
from TeamBuilder import TeamBuilder 

if __name__ == "__main__":
    pokemon = [
        'Kingler',
        'Gengar',
        'Dodrio',
        'Sceptile',sadsaS
        'Houndoom',
        'Magneton',
    ]

    team_builder = TeamBuilder(pokemon)

    start_time = time.time()
    team_builder.build_best_teams()
    end_time = time.time()

    elapsed_time = end_time - start_time

    team_builder.print_best_teams()
    
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
