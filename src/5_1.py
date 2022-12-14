def int_or_none(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == '__main__':
    with open('inputs/5.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    
    crate_data, move_data = data.split('\n\n')
    crate_data = crate_data.replace('[', ' ').replace(']', ' ')

    crate_rows = crate_data.split('\n')[:-1]
    crate_rows.reverse()

    crate_columns = [[] for i in range(9)]
    for row in crate_rows:
        for col in range(9):
            col_slice = row[col*4:col*4 + 4]
            crate = col_slice[1]
            if crate != ' ':
                crate_columns[col].append(crate)
    
    col_nums = dict(enumerate(crate_columns, 1))
    
    for move in move_data.split('\n'):
        move = move.removeprefix('move ')
        num_to_move, n1, from_col, n2, to_col = [int_or_none(s) for s in move.split(' ')]
        popped_crates = []
        for i in range(num_to_move):
            popped_crates.append(col_nums[from_col].pop())
        
        for crate in popped_crates:
            col_nums[to_col].append(crate)

    top_crates = []
    for c, crates in col_nums.items():
        top_crates.append(crates.pop())
    
    print(''.join(top_crates))