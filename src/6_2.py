with open('inputs/6.txt', 'r', encoding='utf-8') as f:
    data = f.read()

for i in range(13, len(data)+1):
    seq = data[i-14:i]
    if seq and (len(set(seq)) == len(seq)):
        print(f'Marker {seq} found at index {i}')
        break