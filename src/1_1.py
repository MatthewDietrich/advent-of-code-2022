with open('inputs/1.txt', 'r', encoding='utf-8') as f:
    print(max(map(lambda x: sum(map(int, x.split('\n'))), f.read().split('\n\n'))))