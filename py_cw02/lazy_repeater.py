from collections.abc import Callable

def make_looper(string: str) -> Callable:
    def next_char():
        i = 0
        while True:
            yield string[i]
            i += 1
            if i >= len(string):
                i = 0
    gen = next_char()
    return lambda: next(gen)
