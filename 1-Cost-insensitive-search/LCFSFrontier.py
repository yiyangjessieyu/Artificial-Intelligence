import itertools
from heapq import *
from math import sqrt

from search import *


class LCFSFrontier(Frontier):

    def __init__(self, ):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()
        self.entry_finder = {}
        self.heap = []
        heapify(self.heap)

    def add(self, path):
        """Store the given path by adding a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method. """

        if path in self.entry_finder:
            self.remove_task(path)

        order = next(self.counter)

        sum_cost = 0
        for arc in path:
            if arc == '':
                sum_cost += 0
            else:
                sum_cost += arc[3]

        entry = [sum_cost, order, path]
        self.entry_finder[path] = entry

        # for key, value in self.entry_finder.items():
        #     print("key is: ", key, '\nValue is: ', value)
        #
        # for item in self.entry_finder:
        #     print("item ", item)
        #
        # print("==========")

        heappush(self.heap, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        if len(self.heap) > 0:
            cost, order, path = heappop(self.heap)
            if path is not self.REMOVED:
                del self.entry_finder[path]
                return path
        else:
            raise StopIteration


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
    frontier = LCFSFrontier()
    frontier.add((Arc(None, None, None, 17),))
    frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

    for path in frontier:
        print(path)


    graph = LocationGraph(
        location={'A': (25, 7),
                  'B': (1, 7),
                  'C': (13, 2),
                  'D': (37, 2)},
        radius=15,
        starting_nodes=['B'],
        goal_nodes={'D'}
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    graph = ExplicitGraph(nodes=set('ABCD'),
                          edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                     ('B', 'C', 3), ('C', 'D', 1)],
                          starting_nodes=['A'],
                          goal_nodes={'D'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)


if __name__ == "__main__":
    main()
