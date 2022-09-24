import heapq
import itertools
import math

from search import *


class LCFSFrontier(Frontier):
    """This is an abstract class for frontier classes. It outlines the
    methods that must be implemented by a concrete subclass. Concrete
    subclasses determine the search strategy.

    """
    def __init__(self):
        self.frontier = heapq.heapify([])
        self.count = itertools.count()
        self.entry_finder = {}

    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """

        for arc in path:

            cost = 0
            for sub_arc in arc:
                cost += sub_arc.cost

            order = next(self.count)

            entry = (cost, order, arc)
            self.entry_finder[path] = entry
            heapq.heappush(self.frontier, entry)

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.

        """
        while self.frontier > 0:
            cost, order, arc = heapq.heappop(self.frontier)
            return arc


class LocationGraph:

    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = {key: value for key, value in sorted(location.items())}
        self.radius = radius
        self.starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        return node in self.goal_nodes

    def starting_nodes(self):
        return self.starting_nodes

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""

        outgoing = []

        # sorted_dict = {key: value for key, value in sorted(self.location.items())}

        agent_x, agent_y = self.location[tail_node]

        for label, (x, y) in self.location.items():
            if label != tail_node:

                x_diff = abs(float(agent_x - x))
                y_diff = float(abs(agent_y - y))
                hypotenuse = float(math.sqrt(x_diff ** 2 + y_diff ** 2))

                if agent_x == x and agent_y - self.radius <= y <= agent_y + self.radius:
                    outgoing.append(Arc(tail_node,
                                        label,
                                        str(tail_node) + "->" + str(label),
                                        float(abs(agent_y - y)))
                                    )

                elif agent_y == y and agent_x - self.radius <= x <= agent_x + self.radius:
                    outgoing.append(Arc(tail_node,
                                        label,
                                        str(tail_node) + "->" + str(label),
                                        float(abs(agent_x - x)))
                                    )

                elif hypotenuse <= self.radius:
                    outgoing.append(Arc(tail_node,
                                        label,
                                        str(tail_node) + "->" + str(label),
                                        float(hypotenuse))
                                    )

        return outgoing
