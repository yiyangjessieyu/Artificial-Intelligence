from search import Arc, Graph
from math import sqrt


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        # a dictionary,
        # with keys that are string representation of the graph nodes
        # with value that are pair of numbers that designates a location for that node.
        self.location = location

        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def is_within_radius(self, tail_coord, node_coord):

        return tail_coord + self.radius >= node_coord >= tail_coord - self.radius

    def outgoing_arcs(self, tail):

        tail_x, tail_y = self.location[tail]

        result_string = ""

        for node, location in self.location.items():
            if node != tail:

                x, y = location

                x_diff = abs(tail_x - x)
                y_diff = abs(tail_y - y)

                if x == 0 and self.is_within_radius(tail_y, y):
                    result_string += str(Arc(tail, node,
                                             tail + '->' + node,
                                             cost=y_diff
                                             ))

                elif y == 0 and self.is_within_radius(tail_x, x):
                    result_string += str(Arc(tail, node,
                                             tail + '->' + node,
                                             cost=x_diff
                                             ))
        return result_string
                #
                # hypotenuse = sqrt(x_diff ** 2 + y_diff ** 2)
                # elif hypotenuse <= float(self.radius):
                #     return True


def main():
    graph = LocationGraph(
        location={'A': (0, 0),
                  'B': (3, 0),
                  'C': (3, 4),
                  'D': (7, 0), },
        radius=5,
        starting_nodes=['A'],
        goal_nodes={'C'}
    )

    for arc in graph.outgoing_arcs('A'):
        print(arc)
    print()

    for arc in graph.outgoing_arcs('B'):
        print(arc)
    print()

    for arc in graph.outgoing_arcs('C'):
        print(arc)


if __name__ == "__main__":
    main()
