import math
from search import *


class LocationGraph:
    """This is an abstract class for graphs. It cannot be directly
    instantiated. You should define a subclass of this class
    (representing a particular problem) and implement the expected
    methods."""

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
