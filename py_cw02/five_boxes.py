def heaviest_box(weight_of_each_two_boxes):
    weights = weight_of_each_two_boxes
    if not len(weights) == 10:
        raise ValueError("Should have 10 weight pairs")
    weights.sort()
    heavy2 = weights[9]
    light2 = weights[0]
    middle_and_heavy = weights[8]
    four_times_all = sum(weights)
    all_weight = four_times_all/4
    middle_weight = all_weight - heavy2 - light2
    heavy = middle_and_heavy - middle_weight
    # print(f'{weights=}')
    # print(f'{heavy2=}')
    # print(f'{light2=}')
    # print(f'{middle_and_heavy=}')
    # print(f'{four_times_all=}')
    # print(f'{all_weight=}')
    # print(f'{middle_weight=}')
    # print(f'{heavy=}')
    return heavy
