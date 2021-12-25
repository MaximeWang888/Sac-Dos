def solve_knapsack_greedy(knapsack, objects_dict):
    W = knapsack.capacity
    sorted_objects_dict = sorted(objects_dict.items(), key=lambda x: x[1][0] / x[1][1], reverse=True)

    for content in sorted_objects_dict:
        weight = content[1][1]
        if W - weight >= 0:
            key = content[0]
            knapsack.content.append(key)
            W -= weight

    return knapsack
