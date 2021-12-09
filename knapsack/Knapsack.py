class Knapsack:
      def __init__(self, capacity) -> None:
          self.capacity = capacity
          self.content = []

      def get_value_and_weight(self, objects_dict):
          valeur = 0
          poid = 0

          for content in self.content:
              value, weight = objects_dict.get(content);
              valeur += value
              poid += weight

          return valeur, poid

      def print_content(self, objects_dict) -> None:

          valeurTotal = 0
          weightTotal = 0
          nbObjects = 0
          affichage = ""

          for content in self.content:
              nbObjects += 1
              affichage += content + " "
              value, weight = objects_dict.get(content);
              affichage +=  str(value) + " " + str(weight)
              valeurTotal += value
              weightTotal += weight
              affichage += "\n"

          affichage += "Le sac a "
          affichage += str(nbObjects) + " "
          affichage += "objets, pour une valeur de "
          affichage += str(valeurTotal)
          affichage += " et un poids de "
          affichage += str(weightTotal)
          affichage += "/" + str(self.capacity)

          print(affichage)

      