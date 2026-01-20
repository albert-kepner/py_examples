p_array = []

def partitions(n_param: int) -> int:
    '''define a function which returns the number of integer partitions of n'''
    result = None
    if n_param < 0:
        return 0
    for n in range(1, n_param + 1, 1):
        result = partitions_helper((int(n)))
    return result

def partitions_helper(n_param: int) -> int:
    '''define a function which returns the number of integer partitions of n'''
    global p_array
    if n_param < 0:
        return 0
    elif n_param == 0:
        if len(p_array) < 2:
            p_array = [1, 1]
        return p_array[n_param]
    elif n_param == 1:
        if len(p_array) < 2:
            p_array = [1, 1]
        return p_array[n_param]
    ## Here n_param > 1
    ## We should be discovering new partition values in ascending order...
    assert n_param <= len(p_array)
    if n_param < len(p_array):
        return p_array[n_param]
    change: bool = True
    p: int = 0
    k: int = 0
    while change:
        change = False
        k += 1
        isign = 1 if k % 2 == 1 else -1
        index1: int = n_param - int(k * (3 * k - 1)/2)
        index2: int = n_param - int(k * (3 * k + 1)/2)
        p1 = partitions_helper(index1) if index1 >= 0 else 0
        p2 = partitions_helper(index2) if index2 >= 0 else 0
        change = p1 > 0 or p2 > 0
        if change:
            p += isign * (p1 + p2)
    p_array.append(p)
    return p