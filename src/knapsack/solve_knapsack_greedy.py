def solve_knapsack_greedy(knapsack, objects_dict):
    sack_weight = knapsack.capacity
    sorted_objects_dict = sorted(objects_dict.items(), key=lambda x: x[1][0] / x[1][1], reverse=True)

    for item in sorted_objects_dict:
        item_weight = item[1][1]
        if sack_weight - item_weight >= 0:
            key = item[0]
            knapsack.content.append(key)
            sack_weight -= item_weight

    return knapsack
