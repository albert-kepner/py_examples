import copy
from collections import namedtuple, deque

MazeState = namedtuple('MazeState',
                       [
                           'zero_loc',
                           'move_history',
                           'move_number_history',
                           'maze'])
first_maze = None
goal_maze = None
maze_history: set[tuple[list[int]]] = set()
maze_state_queue: deque[MazeState] = deque()
first_state: MazeState | None = None


def convert_maze(maze_p: list[list[int]]) -> tuple[tuple[int]]:
    new_rows = []
    for row in maze_p:
        new_rows.append(tuple(row))
    return tuple(new_rows)

def unfreeze(maze_p: tuple[tuple[int]]) -> list[list[int]]:
    new_rows = []
    for row in maze_p:
        cells = list(row)
        new_rows.append(cells)
    return new_rows


def slide_puzzle(ar) -> list[int]:
    global first_maze
    global first_state
    global maze_history
    global maze_state_queue
    maze_history = set()
    maze_state_queue = deque()
    first_maze1 = convert_maze(ar)
    zero_loc = find_zero(ar)
    make_goal_maze(ar)
    print_maze(ar)
    print(f'{zero_loc=}')
    first_state = MazeState(zero_loc=zero_loc, move_history=[], move_number_history=[], maze=ar)
    maze_state_queue.append(first_state)
    maze_history.add(first_maze1)
    goal_state: MazeState | None = None
    while not goal_state:
        goal_state = next_moves()
    # for i in range(10):
    #     goal_state = next_moves()
    # print('stopping..')
    # return None
    print('GOAL STATE FOUND: ***********************************************************************************')
    print_state(goal_state)
    return goal_state.move_number_history

def next_moves() -> MazeState | None:
    print(f'in next_moves: {len(maze_state_queue)=}')
    if len(maze_state_queue) == 0:
        raise Exception('maze_state_queue.is_empty')
    this_state = maze_state_queue.popleft()
    maze = this_state.maze
    print(f'in next_moves: Expanding from this maze.')
    print(f'len(max_history): {len(maze_history)=}')
    print_maze(maze)
    n = len(maze)
    zero_loc = this_state.zero_loc
    last_move = this_state.move_history[-1] if len(this_state.move_history) > 0 else None
    valid_moves = get_valid_moves(zero_loc=zero_loc, last_move=last_move, n=n)
    ## print(f'valid_moves: {valid_moves}')
    for move in valid_moves:
        next_state = compute_next_state(move, this_state)
        ## print_state(next_state)
        if next_state and next_state.maze == goal_maze:
            return next_state
    return None

def print_state(state: MazeState) -> None:
    if not state:
        print('state is none')
        return
    print(f'{state.zero_loc=}')
    print(f'{state.move_history=}')
    print(f'{state.move_number_history=}')
    print_maze(state.maze)

def compute_next_state(move: tuple[int,int], this_state: MazeState) -> MazeState | None:
    new_maze = copy.deepcopy(this_state.maze)
    zero_loc = this_state.zero_loc
    number_moved = this_state.maze[move[0]][move[1]]
    new_maze[zero_loc[0]][zero_loc[1]] = number_moved
    new_maze[move[0]][move[1]] = 0
    ## print(f'in compute_next_state: {this_state.move_history=}')
    new_move_history = copy.deepcopy(this_state.move_history)
    new_move_history.append(move)
    new_move_number_history = copy.deepcopy(this_state.move_number_history)
    new_move_number_history.append(number_moved)
    new_maze1 = convert_maze(new_maze)
    if not new_maze1 in maze_history:
        new_state = MazeState(zero_loc=move,
                              move_history=new_move_history,
                              move_number_history=new_move_number_history,
                              maze=new_maze)
        maze_state_queue.append(new_state)
        maze_history.add(new_maze1)

        ## print(f'in compute_next_state: {new_state.move_history=}')
        return new_state
    else:
        return None

def get_valid_moves(zero_loc: int, last_move: int, n: int) -> list[tuple[int, int]]:
    i,j = zero_loc
    possible_moves = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
    valid_moves = []
    for r,c in possible_moves:
        if r >= 0 and r < n and c >= 0 and c < n:
            if  last_move is None or not last_move == (r, c):
                valid_moves.append((r, c))
    return valid_moves


def find_zero(arr):
    for i,row in enumerate(arr):
        for j,elem in enumerate(row):
            if elem == 0:
                return i,j
    return None

def find_item(arr, item):
    for i,row in enumerate(arr):
        for j,elem in enumerate(row):
            if elem == item:
                return i,j
    return None

def make_goal_maze(maze):
    global goal_maze
    n = len(maze)
    goal_maze = unfreeze(maze)
    count = 0
    for i,row in enumerate(goal_maze):
        for j,elem in enumerate(row):
            count += 1
            goal_maze[i][j] = count
    goal_maze[n - 1][n - 1] = 0

def print_maze(maze):
    print('[')
    for row in maze:
        print(row)
    print(']')

def maze_score(maze):
    score = 0
    for i, row in enumerate(maze):
        for j, elem in enumerate(row):
            goal_i, goal_j = find_item(goal_maze, elem)
            score += int(1.05 ** elem * (abs(goal_i - i)  + abs(goal_j - j)) )
    return score