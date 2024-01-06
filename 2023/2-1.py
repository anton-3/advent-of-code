from sys import argv

with open(argv[1], 'r') as f:
    input_lines = f.read().splitlines()

possible_games = []

games = [line.split(': ')[1].split('; ') for line in input_lines]

for i, game in enumerate(games):
    current_game = i + 1
    max_red = 0
    max_green = 0
    max_blue = 0
    for subset in game:
        for cube in subset.split(', '):
            if cube.endswith('red'):
                max_red = max(max_red, int(cube.split(' ')[0]))
            elif cube.endswith('green'):
                max_green = max(max_green, int(cube.split(' ')[0]))
            elif cube.endswith('blue'):
                max_blue = max(max_blue, int(cube.split(' ')[0]))
    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        possible_games.append(current_game)

print(sum(possible_games))
