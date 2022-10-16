import collections

from itertools import dropwhile

from search import *



class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        """Initialises an FunkyNumericGraph
        - one numeric argument which represent the single starting state.
        - The cost of outgoing arcs must be set to 1 although the cost is not used during the search.
        """

        self.starting_number = starting_number

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the sequence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """A state is considered a goal node if the number is divisible by 10."""
        return node % 10 == 0

    def outgoing_arcs(self, tail):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""

        return [Arc(tail, tail - 1, action="1down", cost=1),
                Arc(tail, tail + 2, action="2up", cost=1)]


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
        search."""

    def __init__(self, ):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = collections.deque([])

    def add(self, path):
        """Store the given path by adding a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method. """
        self.container.append(path)

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
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration

def main():
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)

    graph = FunkyNumericGraph(4)
    for arc in graph.outgoing_arcs(7):
        print(arc)

    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))


    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))

if __name__ == "__main__":
    main()


