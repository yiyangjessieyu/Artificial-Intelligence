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

        result = []

        sorted_dict = {key: value for key, value in sorted(self.location.items())}

        for node, location in sorted_dict.items():
            if node != tail:

                node_x, node_y = location

                x_diff = abs(float(tail_x - node_x))
                y_diff = float(abs(tail_y - node_y))
                hypotenuse = float(sqrt(x_diff ** 2 + y_diff ** 2))

                if node_x == tail_x and self.is_within_radius(tail_y, node_y):
                    result.append(Arc(tail, node,
                                      tail + '->' + node,
                                      cost=y_diff
                                      )
                                  )

                elif node_y == tail_y and self.is_within_radius(tail_x, node_x):
                    result.append(Arc(tail, node,
                                      tail + '->' + node,
                                      cost=x_diff
                                      )
                                  )

                elif hypotenuse <= float(self.radius):
                    result.append(Arc(tail, node,
                                      tail + '->' + node,
                                      cost=hypotenuse
                                      )
                                  )

        return result


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

    graph = LocationGraph(
        location={'SW': (-2, -2),
                  'NW': (-2, 2),
                  'NE': (2, 2),
                  'SE': (2, -2)},
        radius=5,
        starting_nodes=['NE'],
        goal_nodes={'SW'}
    )

    for arc in graph.outgoing_arcs('NE'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('NW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SE'):
        print(arc)


if __name__ == "__main__":
    main()
