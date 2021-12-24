def solve_knapsack_best(sack, object_dict):
    keys = object_dict.keys()
    val = [value[0] for value in object_dict.values()]
    wt = [weight[1] for weight in object_dict.values()]
    W = sack.capacity
    M = W
    n = len(val)
    contents_key = {}
    isEmpty = True

    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(sack.capacity + 1)] for j in range(n + 1)]

    print("\n\nWith a maximum capacity of: \t" + str(sack.capacity))

    print("Maximum Value is: \t" + str(getBestValue(sack, wt, val, n, t)))

    print("Selected Items: ")

    while n is not 0:
        if t[n][W] is not t[n - 1][W] and W - wt[n-1] > 0:
            contents_key[list(keys)[n - 1]] = (val[n - 1], wt[n - 1])
            print("Item : " + str(list(keys)[n - 1]) + " with weight = " +
                  str(wt[n - 1]) + " and value = " + str(val[n - 1]))
            W = W - wt[n - 1]
            isEmpty = False

        n = n - 1

    if isEmpty: print("No item was chosen in this bag with a maximum capacity of "
                      + str(M) + ". Maybe with a higher capacity ...")

    sack.content = contents_key

    return sack


def getBestValue(sack, wt, val, n, t):
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
            val[n - 1] + getBestValue(
                sack, wt, val, n - 1, t),
            getBestValue(sack, wt, val, n - 1, t))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = getBestValue(sack, wt, val, n - 1, t)
        return t[n][W]


