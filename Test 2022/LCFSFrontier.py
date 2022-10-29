import itertools

from search import *
import heapq


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def add(self, path):

        for entry in self.entry_finder:
            if path == entry[-1]:
                self.remove_task(entry)
                break

        count = next(self.counter)

        cost = 0
        for arc in path:
            cost += arc.cost
        new_entry = [cost, count, path]

        self.entry_finder[path] = new_entry

        heapq.heappush(self.container, new_entry)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            priority, count, path = heapq.heappop(self.container)
            if path is not self.REMOVED:
                del self.entry_finder[path]
                return path
        else:
            raise StopIteration  # don't change this one



graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)
