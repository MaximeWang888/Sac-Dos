# ===================================================================#
# -------------------------------------------------------------------#
#                         Knapsack Problem                           #
# -------------------------------------------------------------------#
#                          Class Knapsack                            #
# *******************************************************************#
#                                                                    #
#   V0.1       Linda Bessah, Maxime Wang  - 02/01/2022               #
#                                                                    #
# ===================================================================#


class Knapsack:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.content = []

    def get_value_and_weight(self, objects_dict) -> (int, int):
        total_value = 0
        total_weight = 0

        for content in self.content:
            value, weight = objects_dict.get(content)

            if total_weight + weight <= self.capacity:
                total_value += value
                total_weight += weight

        return total_value, total_weight

    def print_content(self, objects_dict) -> None:

        total_value = 0
        total_weight = 0
        total_content = 0
        print_content = ""

        for content in self.content:
            value, weight = objects_dict.get(content)
            total_content += 1
            total_value += value
            total_weight += weight

            print_content += content + " " + str(value) + " " + str(weight) + "\n"

        print_content += "Le sac a " + str(total_content) + " objets, pour une valeur de " \
                         + str(total_value) + " et un poids de " + str(total_weight) + "/" \
                         + str(self.capacity)

        print(print_content)
