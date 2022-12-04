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

elf_groups = [data[i:i+3] for i in range(0, len(data), 3)]

badge_items = []
for group in elf_groups:
    for item in priorities:
        if all(item in elf_sack for elf_sack in group):
            badge_items.append(item)

item_sum = sum(priorities[item] for item in badge_items)
print(item_sum)