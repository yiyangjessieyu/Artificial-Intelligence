import itertools

from search import *
import heapq


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.entry_finder = {}  # mapping of path to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def remove_task(self, path):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        path = self.entry_finder.pop(path)
        path[-1] = self.REMOVED

    def add(self, path):
        'Add a new task or update the priority of an existing task'
        if path in self.entry_finder:
            self.remove_task(path)
        count = next(self.counter)

        cost = 0
        for arc in path:
            cost += arc.cost

        entry = [cost, count, path]

        self.entry_finder[path] = entry

        heapq.heappush(self.container, entry)


    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            cost, count, path = heapq.heappop(self.container)
            if path is not self.REMOVED:
                del self.entry_finder[path]
                return path
        else:
            raise StopIteration  # don't change this one



