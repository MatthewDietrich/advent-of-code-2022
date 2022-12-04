with open('inputs/2.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

games = map(lambda x: x.strip().split(' '), data)

wins = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draws = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

total = 0
for game in games:
    game_total = points[game[1]]
    if wins[game[0]] == game[1]:
        game_total += 6
    elif draws[game[0]] == game[1]:
        game_total += 3
    total += game_total

print(total)