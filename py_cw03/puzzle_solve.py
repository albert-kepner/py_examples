import copy
import math
from enum import Enum

class TaskState(Enum):
    BasicRow = 1
    LastOfRow = 2
    LastButOneRow = 3
    PlaceLastTwoRow = 4
    FinishLastTwoRow = 5
    ColumnPlaceLastRowItem = 6
    ColumnLastButOneRowItem = 7
    PlaceLastTwoInColumn = 8
    FinishLastCorner = 9
    ColumnLastButOneRowItemVer2 = 10
    ColumnPlaceLastRowItemVer2 = 11
    PlaceLastTwoInColumnVer2 = 12
    FinishLastCornerVer2 = 13


puzzle: list[list[int]] = []
goal_puzzle: list[list[int]] = []
freeze_array: list[list[bool]] = []
square_size: int = 0
completed_rows: int = 0
last_number_placed: int = 0
count_numbers_placed: int = 0
goal_number: int = 0
goal_location: tuple[int, int] = (0, 0)
move_number_history: list[int] = []
steps_toward_goal: int = 0
completed_columns: int = 0
debug_path: bool = False

task_state: TaskState = TaskState.BasicRow

def slide_puzzle(ar: list[list[int]]) -> list[int]:
    global freeze_array
    global square_size
    global completed_rows
    global last_number_placed
    global count_numbers_placed
    global goal_number
    global goal_location
    global puzzle
    global steps_toward_goal
    global completed_columns
    puzzle = copy.deepcopy(ar)
    make_goal_puzzle(puzzle)
    square_size = len(ar[0])
    freeze_array = [[False] * square_size for _ in range(square_size)]
    completed_rows = 0
    last_number_placed = 0
    count_numbers_placed = 0
    completed_columns = 0
    while update_goal():
        print(f'{task_state=}')
        print_puzzle(puzzle,label='After update_goal()')
        steps_toward_goal = 0
        seek_goal()
    print('update_goal() returns False')
    print_puzzle(puzzle,label='THE END')
    print(f'{last_number_placed=}')
    # print(f'freeze_array:')
    # print_puzzle(freeze_array)
    print(f'{completed_rows=}')
    return move_number_history

def update_goal() -> bool:
    global goal_location
    global goal_number
    global task_state
    print(f'In update_goal() {last_number_placed=} {count_numbers_placed=} {task_state=}')
    if completed_rows <= square_size - 3:
        if task_state == TaskState.LastButOneRow:
            print('DDDD')
            task_state = TaskState.PlaceLastTwoRow
            finish_row(row_number=completed_rows)
            if completed_rows <= square_size - 3:
                print('EEEE')
                task_state = TaskState.FinishLastTwoRow
                return update_goal()
            else:
                print('FFFF')
                task_state = TaskState.ColumnPlaceLastRowItem
                return update_goal()
        if count_numbers_placed % square_size <= square_size - 3:
            print('AAAA')
            goal_number = count_numbers_placed + 1
            goal_location = find_item(goal_puzzle, goal_number)
            print(f'in update_goal() {goal_number=} {goal_location=}')
            task_state = TaskState.BasicRow
            return True
        if last_number_placed % square_size == square_size - 2:
            print('BBBB')
            goal_number = last_number_placed + 2
            goal_location = find_item(goal_puzzle, goal_number-1)
            task_state = TaskState.LastOfRow
            return True
        if last_number_placed % square_size == 0:
            print('CCCC')
            goal_number = last_number_placed - 1
            goal_location = find_item(goal_puzzle, goal_number)
            goal_location = tuple_add(goal_location, (1,0))
            task_state = TaskState.LastButOneRow
            return True
    else:
        if completed_columns <= square_size - 3:
            if task_state == TaskState.ColumnPlaceLastRowItem:
                print('GGGG')
                goal_number = 1 + completed_columns + (square_size - 1) * square_size
                goal_number_at = 1 + completed_columns + (square_size - 2) * square_size
                goal_location = find_item(goal_puzzle, goal_number_at)
                task_state = TaskState.ColumnLastButOneRowItem
                return True
            if task_state == TaskState.ColumnLastButOneRowItem:
                print('HHHH')
                goal_number = 1 + completed_columns + (square_size - 2) * square_size
                goal_number_at = 2 + completed_columns + (square_size - 2) * square_size
                goal_location = find_item(goal_puzzle, goal_number_at)
                task_state = TaskState.PlaceLastTwoInColumn
                return True
            if task_state == TaskState.PlaceLastTwoInColumn:
                print('IIII')
                finish_column()
                if completed_columns <= square_size - 3:
                    print('JJJJ')
                    task_state = TaskState.ColumnPlaceLastRowItem
                    return update_goal()
                else:
                    print('KKKK')
                    task_state = TaskState.FinishLastCorner
                    rotate_last_corner()
                    return False
                    # if test_ready_for_last_corner():
                    #     finish_last_corner()
                    #     return False
                    # else:
                    #     print('OOOO')
                    #     unfreeze_and_redo_last_column()
                    #     task_state = TaskState.ColumnLastButOneRowItemVer2
                    #     return update_goal()
            if task_state == TaskState.ColumnLastButOneRowItemVer2:
                print('LLLL')
                ## put the next to last row item in the last row,
                ## follow up by putting the last row item next to it.
                goal_number = 1 + completed_columns + (square_size - 2) * square_size
                goal_number_at = 1 + completed_columns + (square_size - 1) * square_size
                goal_location = find_item(goal_puzzle, goal_number_at)
                task_state = TaskState.ColumnPlaceLastRowItemVer2
                return True
            if task_state == TaskState.ColumnPlaceLastRowItemVer2:
                print('MMMM')
                ## place the last row item in the last row offset right from the next to last row item.
                goal_number = 1 + completed_columns + (square_size - 1) * square_size
                goal_number_at = 2 + completed_columns + (square_size - 1) * square_size
                goal_location = find_item(goal_puzzle, goal_number_at)
                task_state = TaskState.PlaceLastTwoInColumnVer2
                return True
            if task_state == TaskState.PlaceLastTwoInColumnVer2:
                print('NNNN')
                finish_column_ver2()
                task_state = TaskState.FinishLastCorner
                finish_last_corner()
                return False

    return False

def rotate_last_corner():
    target_number = (square_size - 1) * square_size - 1
    target_position = (square_size - 2, square_size - 2)
    zero_position = (square_size - 1, square_size - 1)
    positions: list[tuple[int, int]] = [
        (square_size - 2, square_size - 2),
        (square_size - 2, square_size - 1),
        (square_size - 1, square_size - 1),
        (square_size - 1, square_size - 2),
    ]
    ## Locate the zero:
    zero_location = find_item(puzzle, 0)
    ## zero_location should start at (square_size - 2, square_size - 2)
    zero_index = positions.index(zero_location)
    print(f'in rotate_last_corner() {zero_location=} {zero_index=} (should be zero)')
    found_positions: bool = False
    for i in range(16):
        ## Test if target number and the zero are both in position,
        ## Rotating the zero clockwise up to 16 times
        zero_location = find_item(puzzle, 0)
        target_location = find_item(puzzle, target_number)
        if zero_location == zero_position and target_location == target_position:
            found_positions = True
            break
        next_index = (zero_index + 1) % 4
        swap_numbers(positions[zero_index], positions[next_index])
        zero_index = next_index

    if found_positions:
        print(f'in rotate_last_corner() SUCCESS')
    else:
        print(f'in rotate_last_corner() FAIL')
    print_puzzle(puzzle, label='Ending rotate_last_corner')




def test_ready_for_last_corner() -> bool:
    ## The zero will be at location (square_size - 2, square_size - 2)

    ## The item that needs to be here
    goal_number1 = (square_size - 1) * square_size - 1

    # We are ready to fix the last corner if the goal_number is adjacent to this location
    if (puzzle[square_size - 1][square_size - 2] == goal_number1
            or puzzle[square_size - 2][square_size - 1] == goal_number1):
        print_puzzle(puzzle, label='Yes Ready for last corner')
        return True
    else:
        print_puzzle(puzzle, label='No, Not Ready for last corner')
        return False

def finish_last_corner():
    global goal_location
    zero_location = find_item(puzzle, 0)
    goal_number_at = (square_size - 1) * square_size - 1
    print(f'finish_last_corner() {goal_number_at=}')
    goal_location = find_item(puzzle, goal_number_at)
    print(f'finish_last_corner() {goal_location=}')
    swap_numbers(zero_location, goal_location)
    corner_location = ((square_size - 1) , (square_size - 1))
    swap_numbers(goal_location, corner_location)

def unfreeze_and_redo_last_column():
    global task_state
    global completed_columns
    global count_numbers_placed
    completed_columns -= 1
    count_numbers_placed += 1
    freeze_array[square_size - 2][completed_columns] = False
    freeze_array[square_size - 1][completed_columns] = False
    task_state = TaskState.ColumnLastButOneRowItemVer2
    print('in unfreeze_and_redo_last_column()')
    print_puzzle(freeze_array, label = 'in unfreeze_and_redo_last_column()')


def finish_column():
    print('in finish_column() ***************************************************************** *********')
    global completed_columns
    zero_location = find_item(puzzle, 0)
    zero_targets = [(square_size - 1, completed_columns)]
    print_puzzle(puzzle, label='in finish_column()')
    zero_best_path = find_zero_path(zero_location, zero_targets, goal_location)
    print(f'{zero_best_path=}')
    move_zero_along_path(zero_best_path)
    target  = zero_best_path[-1]
    target_last_row = tuple_add(target, (-1,0))
    target_previous_row = tuple_add(target, (-1,1))
    swap_numbers(target, target_last_row)
    swap_numbers(target_last_row, target_previous_row)
    freeze_array[target[0]][target[1]] = True
    freeze_array[target_last_row[0]][target_last_row[1]] = True
    freeze_array[target_previous_row[0]][target_previous_row[1]] = False
    completed_columns += 1
    print_puzzle(puzzle, label='AT END in finish_column()')

def finish_column_ver2():
    print('in finish_column() ***************************************************************** *********')
    global completed_columns
    zero_location = find_item(puzzle, 0)
    zero_targets = [(square_size - 2, completed_columns)]
    print_puzzle(puzzle, label='in finish_column_ver2()')
    zero_best_path = find_zero_path(zero_location, zero_targets, goal_location)
    print(f'{zero_best_path=}')
    move_zero_along_path(zero_best_path)
    target  = zero_best_path[-1]
    target_previous_row = tuple_add(target, (1, 0))
    target_last_row = tuple_add(target_previous_row, (0, 1))

    swap_numbers(target, target_previous_row)
    swap_numbers(target_previous_row, target_last_row )
    freeze_array[target[0]][target[1]] = True
    freeze_array[target_previous_row[0]][target_previous_row[1]] = True
    freeze_array[target_last_row[0]][target_last_row[1]] = False
    completed_columns += 1
    print_puzzle(puzzle, label='AT END in finish_column_ver2()')

def finish_row(row_number):
    print('in finish_row() ***************************************************************** *********')
    global puzzle
    global freeze_array
    global completed_rows
    global last_number_placed
    zero_location = find_item(puzzle, 0)
    zero_targets = [(row_number,square_size-1)]
    print_puzzle(puzzle,label='in finish_row()')
    zero_best_path = find_zero_path(zero_location, zero_targets, goal_location)
    print(f'{zero_best_path=}')
    move_zero_along_path(zero_best_path)
    target  = zero_best_path[-1]
    swap_numbers(target, (row_number,square_size-2))
    swap_numbers((row_number,square_size-2),(row_number+1,square_size-2))
    freeze_array[target[0]][target[1]] = True
    freeze_array[row_number+1][square_size-2] = False
    completed_rows += 1
    print_puzzle(puzzle, label='AT END in finish_row()')

def find_item(arr, item):
    for i,row in enumerate(arr):
        for j,elem in enumerate(row):
            if elem == item:
                return i,j
    return None

def make_goal_puzzle(puzzle1):
    global goal_puzzle
    n = len(puzzle1)
    goal_puzzle = copy.deepcopy(puzzle1)
    count = 0
    for i,row in enumerate(goal_puzzle):
        for j,elem in enumerate(row):
            count += 1
            goal_puzzle[i][j] = count
    goal_puzzle[n - 1][n - 1] = 0

def seek_goal():
    global last_number_placed
    global count_numbers_placed
    global puzzle
    global move_number_history
    global freeze_array
    global steps_toward_goal
    goal_number_location = find_item(puzzle, goal_number)
    while goal_number_location != goal_location:
        goal_number_location = step_toward_goal(goal_number_location)
        steps_toward_goal += 1
    last_number_placed = goal_number

    count_numbers_placed += 1
    print(f'Seek Goal Setting {last_number_placed=} {count_numbers_placed=}')
    freeze_array[goal_location[0]][goal_location[1]] = True

def step_toward_goal(goal_number_location: tuple[int, int]) -> tuple[int, int]:
    global puzzle
    global move_number_history
    global debug_path
    direction = goal_direction(goal_number_location)
    zero_location = find_item(puzzle, 0)
    # print(f'{zero_location=}')
    zero_targets = [tuple_add((direction[0],0), goal_number_location), tuple_add((0, direction[1]), goal_number_location)]
    # print(f'{zero_targets=}')
    # print(f'{last_number_placed=}')
    # print(f'{goal_number=}')
    # print(f'{steps_toward_goal=}')
    zero_best_path = find_zero_path(zero_location, zero_targets, goal_number_location)
    print('zero_best_path: ', zero_best_path)
    move_zero_along_path(zero_best_path)
    target  = zero_best_path[-1]
    swap_numbers(target, goal_number_location)
    goal_number_location = target
    return goal_number_location

def swap_numbers(zero_location: tuple[int,int], number_to_move: tuple[int, int]) -> None:
    global move_number_history
    number_at = puzzle[number_to_move[0]][number_to_move[1]]
    move_number_history.append(number_at)
    puzzle[number_to_move[0]][number_to_move[1]] = 0
    puzzle[zero_location[0]][zero_location[1]] = number_at
    # print(f'{number_at=}')
    # print_puzzle(puzzle)

def  move_zero_along_path(zero_best_path: list[tuple[int, int]]) -> None:
    global puzzle
    global move_number_history
    prev_location = None
    for ix, location in enumerate(zero_best_path):
        if ix > 0:
            swap_numbers(prev_location, location)
        prev_location = location



def goal_direction(goal_number_location: tuple[int, int]) -> tuple[int, int]:
    diff = tuple_diff(goal_location, goal_number_location)
    x = 0 if diff[0] == 0 else int(math.copysign(1, diff[0]))
    y = 0 if diff[1] == 0 else int(math.copysign(1, diff[1]))
    return x, y

def tuple_diff(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]

def tuple_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def find_zero_path(zero_location, zero_targets,  goal_number_location) -> list[tuple[int, int]]:
    if debug_path:
        print('in find_zero_path puzzle =')
        print_puzzle(puzzle)
        print(f'{zero_location=}')
        print(f'{zero_targets=}')
        print(f'{goal_number_location=}')
    n = square_size
    grid = [[-1] * n for _ in range(n)]
    grid[zero_location[0]][zero_location[1]] = 0
    stack = [zero_location]
    if debug_path:
        print(f'{stack=}')
    if zero_location in zero_targets:
        print('zero trivially at target location')
        return [zero_location]
    while True:
        if not stack:
            raise Exception('No zero path found')
        next_location = stack.pop(0)
        adjacents = find_adjacents(next_location)
        for nxt in adjacents:
            if nxt == goal_number_location:
                continue
            if grid[nxt[0]][nxt[1]] != -1:
                continue
            if freeze_array[nxt[0]][nxt[1]]:
                continue
            grid[nxt[0]][nxt[1]] = grid[next_location[0]][next_location[1]] + 1
            stack.append(nxt)
            if debug_path:
                print(f'{nxt=}')
                print(f'{stack=}')
                print_puzzle(grid)
            if nxt in zero_targets:
                return retrace_path(grid, nxt)

def find_adjacents(location: tuple[int, int]) -> list[tuple[int, int]]:
    adjacents = []
    offsets = [(-1, 0),(1, 0),(0, 1), (0, -1)]
    for offset in offsets:
        result = tuple_add(location, offset)
        if result[0] < 0 or result[0] >= square_size or result[1] < 0 or result[1] >= square_size:
            continue
        adjacents.append(result)
    return adjacents

def retrace_path(grid: list[list[int]], next_location: tuple[int, int]) -> list[tuple[int, int]]:
    if debug_path:
        print(f'retrace path: {next_location=}')
        print_puzzle(grid)
    back_path = [next_location]
    while True:
        adjacents = find_adjacents(next_location)
        step = grid[next_location[0]][next_location[1]]
        for adjacent in adjacents:
            if grid[adjacent[0]][adjacent[1]] == step - 1:
                back_path.append(adjacent)
                next_location = adjacent
                if grid[adjacent[0]][adjacent[1]]  == 0:
                    back_path.reverse()
                    return back_path
                break

def print_puzzle(maze, label=None):
    if label:
        print(f'{label=}')
    print('[')
    for row in maze:
        print(row)
    print(']')