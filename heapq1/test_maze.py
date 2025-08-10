from maze1 import find_path, parse_map, map1

def testmymaze():
    path = find_path(map1)
    lines, _, _ = parse_map(map1)
    for pos in path:
        print(f'{pos=}')
    print('===\n')
    for pos in path:
        x,y = pos
        lines[y] = replace_at(lines[y], x, 'o')
    print_maze(lines)

def replace_at(line: str, at: int, char: str):

    before = line[:at] if at > 0 else ''
    after = line[at+1:] if at < len(line) - 1 else ''
    line2 = before + char + after
    return line2

def print_maze(lines):
    print('--')
    for line in lines:
        print(line)



