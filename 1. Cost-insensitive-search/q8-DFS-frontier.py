from search import *


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
        search."""

    def __init__(self, ):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

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
            return self.container.pop()
        else:
            raise StopIteration


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


    available_flights = ExplicitGraph(
        nodes=['Christchurch', 'Auckland',
               'Wellington', 'Gold Coast'],
        edge_list=[('Christchurch', 'Gold Coast'),
                   ('Christchurch', 'Auckland'),
                   ('Christchurch', 'Wellington'),
                   ('Wellington', 'Gold Coast'),
                   ('Wellington', 'Auckland'),
                   ('Auckland', 'Gold Coast')],
        starting_nodes=['Christchurch'],
        goal_nodes={'Gold Coast'})

    my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
    print_actions(my_itinerary)


if __name__ == "__main__":
    main()
