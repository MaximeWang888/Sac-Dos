def solve_knapsack_greedy(knapsack, objects_dict):

    sorted_objects_dict = sorted(objects_dict.items(), key=lambda x: x[1][0] / x[1][1], reverse=True)
    contents_key = []

    while len(sorted_objects_dict) != 0:
        contents_key.append(sorted_objects_dict.pop(0)[0])

    knapsack.content = contents_key

    return knapsack
