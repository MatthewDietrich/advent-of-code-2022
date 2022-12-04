priorities = {
    v: k for k, v in dict(
        enumerate(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            1
        )
    ).items()
}

with open('inputs/3.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f.readlines()]

sacks = map(
    lambda x: (
        x[:int(len(x)/2)], x[int(len(x)/2):]
    ), 
    data
)

in_both = []
for sack in sacks:
    for item in priorities:
        if item in sack[0] and item in sack[1]:
            in_both.append(item)


priority_sum = sum(map(lambda x: priorities[x], in_both))
print(priority_sum)