from collections import namedtuple

State = namedtuple('State', ['open_doors','key_count','in_room'])

def analyze_dungeon(dungeon):
    # Good luck!
    pass

def initial_state(dungeon):
    open_doors = () # initially all doors are locked
    in_room = dungeon['start']
    key_count = in_room['keys']
    state = State(open_doors, key_count, in_room)
    return state

def go_to_room( state: State, passage: dict ) -> State | None:
    open_doors = state['open_doors']
    key_count = state['key_count']
    door_needed = passage['door']
    if door_needed and door_needed not in open_doors:
        if key_count > 0:
            key_count -= 1
            open_doors = open_doors + (door_needed,)
        else:
            return None # cannot take this passage if door needed and out of keys.
    next_room = passage['to']
    next_state = State(open_doors, key_count, next_room)
    return next_state
