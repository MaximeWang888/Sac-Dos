def solve_knapsack_best(sack, object_dict):
    val = []
    wt = []
    for value in object_dict.values():
        val.append(value[0])
        wt.append(value[1])

    n = len(val)

    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(sack.capacity + 1)] for j in range(n + 1)]

    return solving(sack, wt, val, n, t)


def solving(sack, wt, val, n, t):
    W = sack.capacity
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n - 1] <= W:
        sack.capacity = sack.capacity - wt[n - 1]
        t[n][W] = max(
            val[n - 1] + solving(
                sack, wt, val, n - 1, t),
            solving(sack, wt, val, n - 1, t))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = solving(sack, wt, val, n - 1, t)
        return t[n][W]

    return sack