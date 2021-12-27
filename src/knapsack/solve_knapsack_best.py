def solve_knapsack_best(sack, object_dict):
    keys = object_dict.keys()
    val = [value[0] for value in object_dict.values()]
    wt = [weight[1] for weight in object_dict.values()]
    W = sack.capacity
    M = W
    n = len(val)
    contents_key = {}
    isEmpty = True

    # We initialize the matrix with 0 at first.
    t = [[0 for x in range(W + 1)] for x in range(n + 1)]

    print("\n\nWith a maximum capacity of: \t" + str(sack.capacity))

    print("Maximum Value is: \t" + str(getBestValue(sack.capacity, wt, val, n, t)))

    while n != 0:
        if t[n][W] is not t[n - 1][W]:
            contents_key[list(keys)[n - 1]] = (val[n - 1], wt[n - 1])
            print("Item : " + str(list(keys)[n - 1]) + " with weight = " +
                  str(wt[n - 1]) + " and value = " + str(val[n - 1]))
            isEmpty = False

            W = W - wt[n - 1]

        n = n - 1

    if isEmpty: print("No item was chosen in this bag with a maximum capacity of "
                      + str(M) + ". Maybe with a higher capacity ...")

    sack.content = contents_key

    return sack


def getBestValue(W, wt, val, n, t):
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                t[i][w] = 0
            elif wt[i - 1] <= w:
                t[i][w] = max(val[i - 1] + t[i - 1][w - wt[i - 1]], t[i - 1][w])
            else:
                t[i][w] = t[i - 1][w]

    return t[n][W]