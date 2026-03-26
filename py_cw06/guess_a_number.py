def filter_numbers(range_low, range_high, right, wrong) -> int | None:
    ## print(f"range_low = {range_low}, range_high = {range_high}, right = {right}, wrong = {wrong}")
    even_flag = False
    odd_flag = False
    if 'The number is an even number' in right:
        even_flag = True
    if 'The number is an odd number' in right:
        odd_flag = True
    if 'The number is an even number' in wrong:
        odd_flag = True
    if 'The number is an odd number' in wrong:
        even_flag = True
    ## print(f"even_flag = {even_flag}, odd_flag = {odd_flag}")
    if even_flag and odd_flag:
        return None

    return other_filters(range_low, range_high, even_flag, odd_flag, right, wrong)

def filter_divisible_by(number, divisible_by) -> bool:
    return number % divisible_by == 0

def filter_starts_with(string, prefix) -> bool:
    return string.startswith(prefix)

def filter_ends_with(string, suffix) -> bool:
    return string.endswith(suffix)

def number_generator(range_low, range_high, odd_flag, even_flag):
    if even_flag:
        return (i for i in range(range_low, range_high + 1) if i % 2 == 0)
    elif odd_flag:
        return (i for i in range(range_low, range_high + 1) if i % 2 != 0)
    else:
        return (i for i in range(range_low, range_high + 1))


def other_filters(range_low, range_high, even_flag, odd_flag, right, wrong) -> int | None:
    numbers = number_generator(range_low, range_high, odd_flag, even_flag)
    passing_numbers = []
    for number in numbers:
        right_OK = True
        wrong_OK = True
        for w in wrong:
            if w.startswith('The number is divisible by'):
                if filter_divisible_by(number, extract_trailing_int(w)):
                    wrong_OK = False
            elif w.startswith('The number is starting with'):
                if filter_starts_with(str(number), extract_trailing_digits(w)):
                    wrong_OK = False
            elif w.startswith('The number is ending with'):
                if filter_ends_with(str(number), extract_trailing_digits(w)):
                    wrong_OK = False
        for r in right:
           if r.startswith('The number is divisible by'):
               if not filter_divisible_by(number, extract_trailing_int(r)):
                   right_OK = False
           elif r.startswith('The number is starting with'):
               if not filter_starts_with(str(number), extract_trailing_digits(r)):
                   right_OK = False
           elif r.startswith('The number is ending with'):
               if not filter_ends_with(str(number), extract_trailing_digits(r)):
                  right_OK = False
        if right_OK and wrong_OK:
            passing_numbers.append(number)
    return passing_numbers[0] if len(passing_numbers) == 1 else None


def guess_number(right, wrong):
    range_high = 2000
    range_low = 0
    for r in right:
        if 'The number is more than' in r:
            range_low = max(range_low, extract_trailing_int(r) + 1)
        elif 'The number is less than' in r:
            range_high = min(range_high, extract_trailing_int(r) - 1)
    for w in wrong:
        if 'The number is more than' in w:
            range_high = min(range_high, extract_trailing_int(w) - 1)
        elif 'The number is less than' in w:
            range_low = max(range_low, extract_trailing_int(w) + 1)
    return filter_numbers(range_low, range_high, right, wrong)


import re


def extract_trailing_int(s: str) -> int | None:
    m = re.search(r"(\d+)$", s)
    return int(m.group(1)) if m else None


pattern = re.compile(r"(\d+)$")


def extract_trailing_digits(s: str) -> str | None:
    match = pattern.search(s)
    return match.group(1) if match else None

