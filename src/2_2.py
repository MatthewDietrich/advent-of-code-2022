with open('inputs/2.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

games = map(lambda x: x.strip().split(' '), data)

wins = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

losses = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

points = {
    'A': 1,
    'B': 2,
    'C': 3
}

total = 0
for game in games:
    game_total = 0
    if game[1] == 'X':
        holding = losses[game[0]]
    elif game[1] == 'Y':
        holding = game[0]
        game_total += 3
    else:
        holding = wins[game[0]]
        game_total += 6
    game_total += points[holding]
    total += game_total

print(total)