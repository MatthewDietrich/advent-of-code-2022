with open('inputs/1.txt', 'r', encoding='utf-8') as f:
    print(sum(sorted(map(lambda x: sum(map(int, x.split('\n'))), f.read().split('\n\n')))[-3:]))