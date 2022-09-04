from search import *
from collections import *
import copy

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state)  # the size of the puzzle

        # Find i and j such that state[i][j] == BLANK
        i, j = next((i, j) for i in range(n) for j in range(n) if state[i][j] == BLANK)

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])  # or blank goes right
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.puzzle]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal.
        A state is considered a goal node if the number is divisible by 10.
        """

        n = len(node)

        # goal is correct order from 1 to (n*n - 1)
        # eg. if n = 3, then goal = [1, 2, ... 8]
        goal = [num for num in range(1, n*n)]

        # eg. if n = 3, then correct node_1d = [' ', 1, 2, ... 8]
        # where the last element is at index n*n-1
        node_1d = [col for row in node for col in row]

        if node_1d[0] != ' ':
            return False

        for i in range(0, n*n-1):
            if goal[i] != node_1d[i+1]:
                return False

        return True

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

