# ===================================================================#
# -------------------------------------------------------------------#
#                         Knapsack Problem                           #
# -------------------------------------------------------------------#
#                          Best Algorithm                            #
# *******************************************************************#
#                                                                    #
#   V0.1       Linda Bessah, Maxime Wang  - 02/01/2022               #
#                                                                    #
# ===================================================================#


def solve_knapsack_best(sack, object_dict):
    keys = object_dict.keys()
    values = [value[0] for value in object_dict.values()]
    weights = [weight[1] for weight in object_dict.values()]
    n = len(values)

    # We initialize the matrix with 0 at first.
    t = [[0 for _ in range(sack.capacity + 1)] for _ in range(n + 1)]

    get_best_value(sack.capacity, weights, values, n, t)

    find_solution(keys, n, sack, t, weights)

    return sack


def find_solution(keys, n, sack, t, wt):
    sack_weight = sack.capacity

    while n != 0:
        if t[n][sack_weight] is not t[n - 1][sack_weight]:
            sack.content.append((list(keys)[n - 1]))

            sack_weight -= wt[n - 1]

        n = n - 1


def get_best_value(sack_capacity, wt, val, n, t):
    # Build table K[][] in bottom up manner
    for i in range(n + 1):  # item
        for w in range(sack_capacity + 1):  # weight
            if i == 0 or w == 0:
                t[i][w] = 0
            elif wt[i - 1] <= w:
                t[i][w] = max(val[i - 1] + t[i - 1][w - wt[i - 1]], t[i - 1][w])
            else:
                t[i][w] = t[i - 1][w]

    return t[n][sack_capacity]
