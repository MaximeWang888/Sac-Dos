def solve_knapsack_best(sack, object_dict):
    keys = object_dict.keys()
    val = [value[0] for value in object_dict.values()]
    wt = [weight[1] for weight in object_dict.values()]
    sack_weight = sack.capacity
    n = len(val)
    is_empty = True

    # We initialize the matrix with 0 at first.
    t = [[0 for _ in range(sack_weight + 1)] for _ in range(n + 1)]

    print("\n\nWith a maximum capacity of: \t" + str(sack_weight))

    print("Maximum Value is: \t" + str(get_best_value(sack_weight, wt, val, n, t)))

    is_empty, sack_weight = find_solution(is_empty, keys, n, sack, sack_weight, t, val, wt)

    if is_empty:
        print("No item was chosen in this bag with a maximum capacity of "
              + str(sack_weight) + ". Maybe with a higher capacity ...")

    return sack


def find_solution(is_empty, keys, n, sack, sack_weight, t, val, wt):
    while n != 0:
        if t[n][sack_weight] is not t[n - 1][sack_weight]:
            sack.content.append((list(keys)[n - 1]))
            print("Item : " + str(list(keys)[n - 1]) + " with weight = " +
                  str(wt[n - 1]) + " and value = " + str(val[n - 1]))
            is_empty = False

            sack_weight -= wt[n - 1]

        n = n - 1
    return is_empty, sack_weight


def get_best_value(weight, wt, val, n, t):
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                t[i][w] = 0
            elif wt[i - 1] <= w:
                t[i][w] = max(val[i - 1] + t[i - 1][w - wt[i - 1]], t[i - 1][w])
            else:
                t[i][w] = t[i - 1][w]

    return t[n][weight]
