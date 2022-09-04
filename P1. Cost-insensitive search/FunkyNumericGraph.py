from search import *
from collections import *


class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)
        For each state (number) n, two actions are available (in order):
        "1down" that goes to state n-1 and
        "2up" which goes to state n+2."""
        return [
            Arc(tail=tail_node,
                head=tail_node-1,
                action="1down",
                cost=1),
            Arc(tail=tail_node,
                head=tail_node+2,
                action="2up",
                cost=1)
        ]

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal.
        A state is considered a goal node if the number is divisible by 10.
        """
        return node % 10 == 0


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        # BFS uses a queue for its frontier container as it removes from the front of a list
        self.container = deque([])

    def add(self, path):
        # BFS adds a new path to the end of its frontier container
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            # The next path BFS removes from the frontier container is the first element
            # first in, will be selected to be the first out
            return self.container.popleft()
        else:
            raise StopIteration  # don't change this one


def main():
    # Example 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    # Example 2
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S', 'A'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)


if __name__ == "__main__":
    main()

