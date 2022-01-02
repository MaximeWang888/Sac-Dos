# ===================================================================#
# -------------------------------------------------------------------#
#                         Knapsack Problem                           #
# -------------------------------------------------------------------#
#                         Optimal Algorithm                          #
# *******************************************************************#
#                                                                    #
#   V0.1       Linda Bessah, Maxime Wang  - 02/01/2022               #
#                                                                    #
# ===================================================================#


def solve_knapsack_optimal(sack, object_dict):
    keys = list(object_dict.keys())
    values = [value[0] for value in object_dict.values()]
    weights = [weight[1] for weight in object_dict.values()]
    optimal_value, cell = get_optimal_value(keys, values, weights, sack.capacity, 0)

    for item in cell.selected:
        sack.content.append(item[0])

    return sack


def get_optimal_value(keys, values, weights, capacity, current_index):
    # base checks
    if capacity <= 0 or current_index >= len(values):
        return 0, None

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    cell1 = Cell()
    if weights[current_index] <= capacity:
        cell1.selected.append((keys[current_index], (values[current_index], weights[current_index])))
        cell1.total_weight += weights[current_index]
        max_value1, cell = get_optimal_value(keys, values, weights,
                                             capacity - weights[current_index], current_index + 1)
        cell1.total_value = values[current_index] + max_value1
        if cell is not None and len(cell.selected) != 0:
            for item in cell.selected:
                cell1.selected.append(tuple(item))
                cell1.total_weight += cell.total_weight

    # recursive call after excluding the element at the currentIndex
    cell2 = Cell()
    max_value2, cell = get_optimal_value(keys, values, weights, capacity, current_index + 1)
    cell2.total_value = max_value2

    if cell1.total_value >= cell2.total_value:
        return cell1.total_value, cell1
    return cell2.total_value, cell


class Cell:

    def __init__(self):
        self.selected = []
        self.total_weight = 0
        self.total_value = 0
