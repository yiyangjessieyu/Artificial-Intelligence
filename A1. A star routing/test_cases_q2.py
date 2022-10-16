def main():
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
        +----------+
        |    X     |
        | S  X  G  |
        |    X     |
        +----------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    There is no solution!
    '''
    map_str = """\
    +----------------+
    |2              F|
    |XX     G 123    |
    |3XXXXXXXXXXXXXX |
    |  F             |
    |          F     |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
        +-------+
        |   G   |
        |       |
        |   S   |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      N,
      N.
    Total cost: 10
    '''

    map_str = """\
        +-------+
        |  GG   |
        |S    G |
        |  S    |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      N,
      N.
    Total cost: 10'
    '''

    map_str = """\
        +-------+
        |     XG|
        |X XXX  |
        | S     |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      E,
      E,
      E,
      E,
      N,
      E,
      N.
    Total cost: 35
    '''

    map_str = """\
        +-------+
        |  F  X |
        |X XXXXG|
        | 3     |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      N,
      N,
      E,
      Fuel up,
      W,
      S,
      S,
      E,
      E,
      E,
      E,
      E,
      N.
    Total cost: 75
    '''

    map_str = """\
        +--+
        |GS|
        +--+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      W.
    Total cost: 5
    '''

    map_str = """\
        +---+
        |GF2|
        +---+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      W,
      W.
    Total cost: 10
    '''

    map_str = """\
        +----+
        | S  |
        | SX |
        |GX G|
        +----+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      W,
      S.
    Total cost: 10
    '''

    map_str = """\
        +---------+
        |         |
        |    G    |
        |         |
        +---------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    There is no solution!
    '''

    map_str = """\
        +------------+
        |    P       |
        | 7          |
        |XXXX        |
        |P F X  G    |
        +------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      E,
      E,
      E,
      N,
      Teleport to (4, 1),
      E,
      E,
      Fuel up,
      W,
      W,
      Teleport to (1, 5),
      E,
      E,
      E,
      S,
      S,
      S.
    Total cost: 105
    '''

    map_str = """\
        +----------+
        |    X     |
        | S  X  G  |
        |    X     |
        +----------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    There is no solution!
    '''

    map_str = """\
        +----+
        |1FG |
        |    |
        |    |
        |    |
        |  S |
        +----+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    '''
    Actions:
      N,
      N,
      N,
      N.
    Total cost: 20
    '''


def Q3test():
    map_str = """\
        +----------------+
        |                |
        |                |
        |                |
        |                |
        |                |
        |                |
        |        S       |
        |                |
        |                |
        |     G          |
        |                |
        |                |
        |                |
        +----------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |     ...S       |
    |     ...*       |
    |     ...*       |
    |     G***       |
    |                |
    |                |
    |                |
    +----------------+
    '''

    map_str = """\
        +----------------+
        |                |
        |                |
        |                |
        |                |
        |                |
        |                |
        |        S       |
        |                |
        |                |
        |     G          |
        |                |
        |                |
        |                |
        +----------------+
        """
    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +----------------+
    |        .       |
    |       ...      |
    |      .....     |
    |     .......    |
    |    .........   |
    |   ...........  |
    |   .....S...... |
    |    ....*.....  |
    |     ...*....   |
    |     G***...    |
    |      .....     |
    |       ...      |
    |        .       |
    +----------------+
    '''

    map_str = """\
        +-------------+
        | G         G |
        |      S      |
        | G         G |
        +-------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +-------------+
    | G....*****G |
    | .....S..... |
    | G.........G |
    +-------------+
    '''

    map_str = """\
        +-------+
        |     XG|
        |X XXX  |
        |  S    |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +-------+
    |     XG|
    |X XXX**|
    |  S***.|
    +-------+
    '''

    map_str = """\
        +--+
        |GS|
        +--+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +--+
    |GS|
    +--+
    '''

    map_str = """\
        +----+
        |    |
        | SX |
        | X G|
        +----+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +----+
    | ***|
    |.SX*|
    |.X G|
    +----+
    '''

    map_str = """\
        +---------------+
        |    G          |
        |XXXXXXXXXXXX   |
        |           X   |
        |  XXXXXX   X   |
        |  X S  X   X   |
        |  X        X   |
        |  XXXXXXXXXX   |
        |               |
        +---------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +---------------+
    |    G********  |
    |XXXXXXXXXXXX*  |
    |.********..X*  |
    |.*XXXXXX*..X*  |
    |.*X.S**X*..X*  |
    |.*X...***..X*  |
    |.*XXXXXXXXXX*  |
    |.************  |
    +---------------+
    '''

    map_str = """\
        +------------+
        |         X  |
        | S       X G|
        |         X  |
        |         X  |
        |         X  |
        +------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +------------+
    |.........X  |
    |.S.......X G|
    |.........X  |
    |.........X  |
    |.........X  |
    +------------+
    '''

    map_str = """\
        +---------+
        |         |
        |    G    |
        |         |
        +---------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    '''

    map_str = """\
        +-------------+
        |         G   |
        | S           |
        |         S   |
        +-------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +-------------+
    |         G   |
    | S       *   |
    |         S   |
    +-------------+
    '''

    map_str = """\
        +------+
        |      |
        |S X   |
        |XXXXX |
        |G X   |
        |      |
        +------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +------+
    |****..|
    |S.X***|
    |XXXXX*|
    |G*X***|
    |.***..|
    +------+
    '''

    map_str = """\
        +-------------+
        |S            |
        |             |
        |   G      S  |
        |             |
        | G           |
        +-------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +-------------+
    |S***         |
    |...*         |
    |...G      S  |
    |..           |
    |.G           |
    +-------------+
    '''

    map_str = """\
        +-------------+
        |    XG       |
        |    XXXXX  X |
        |S        X   |
        +-------------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    '''
    +-------------+
    |....XG       |
    |....XXXXX  X |
    |S........X   |
    +-------------+
    '''


if __name__ == "__main__":
    main()
