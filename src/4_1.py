def either_contains(r1, r2):
    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        return True
    elif r2[0] <= r1[0] and r2[1] >= r1[1]:
        return True
    return False

if __name__ == '__main__':
    with open('inputs/4.txt', 'r', encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]

    pairs = [line.split(',') for line in data]

    bad_pairs = 0
    for pair in pairs:
        ranges = [r.split('-') for r in pair]
        ranges = list(map(lambda r: [int(x) for x in r], ranges))
    
        if either_contains(*ranges):
            bad_pairs += 1
    
    print(bad_pairs)