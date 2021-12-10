def solve_knapsack_greedy(knapsack, objects_dict):
    assert (knapsack.content == [])

    sorted_objects_dict = sorted(objects_dict.items(), key=lambda x: x[1][0] / x[1][1], reverse=True)
    tabObject = []

    while len(sorted_objects_dict) != 0:
        tabObject.append(sorted_objects_dict.pop(0)[0])

    knapsack.content = tabObject

    return knapsack
