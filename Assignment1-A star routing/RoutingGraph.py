import heapq
from search import *
import math


class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        self.collection = []
        self.map_graph = map_graph
        self.expanded = set()
        self.count = 0

    def add(self, path):
        """the fontier adds the path only if it does not end with a node that is already expanded
        otherwise the path is discarded (eg. pruned)."""
        node_to_expand = path[-1].head  # head of the last arc in the path
        if node_to_expand not in self.expanded:
            cost_sum = sum(arc.cost for arc in path) + self.map_graph.estimated_cost_to_goal(node_to_expand)
            heapq.heappush(self.collection,
                           (cost_sum, self.count, path))
            self.count += 1

    def __iter__(self):
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        while len(self.collection) > 0:
            count, cost, path = heapq.heappop(self.collection)
            node_to_expand = path[-1].head  # head of the last arc in the path
            if node_to_expand not in self.expanded:
                self.expanded.add(node_to_expand)
                return path
        else:
            raise StopIteration

class RoutingGraph(Graph):

    def __init__(self, map_str):
        """
        :param map_str: The map is always rectangular.
        Positions in the map by a pair (row, col).
            * Row numbers start from 0 for the first (topmost) line, 1 for the second line, and so on.
            * Col start from 0 for the first (leftmost) position (character) in the line.
        """

        # The environment is surrounded by walls marked by '+' or '-' or '|' character.
        self.corner_str = "+"
        self.side_str = "|"
        self.top_str = "-"
        self.obstacle_str = "X"  # The obstacles are marked by 'X'
        self.barriers = {self.corner_str, self.top_str, self.side_str, self.obstacle_str}

        self.map_str = []
        for row in map_str.strip().splitlines():
            self.map_str.append(list(row.strip()))

        self.goal_locations = set()  # Call points / customers are potential destination marked by G
        self.portal_locations = set()
        self.goal_str = "G"
        self.portal_str = "P"
        for row_i, row_list in enumerate(self.map_str):
            for col_i, char in enumerate(row_list):
                if char == self.goal_str:
                    self.goal_locations.add((row_i, col_i))
                elif char == self.portal_str:
                    self.portal_locations.add((row_i, col_i))

        # Agents are marked by 'S' or digits 0 to 9.
        self.agent_fuel_str_options = set('S')
        for num in range(0, 10):  # The capacity of the fuel tank is 9.
            self.agent_fuel_str_options.add(str(num))

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        agent_row, agent_col, agent_fuel = node

        heuristic = float(math.inf)
        for goal_row, goal_col in self.goal_locations:
            h_row = abs(agent_row - goal_row)
            h_col = abs(agent_col - goal_col)
            new_heuristic = h_row + h_col
           # hypotenuse = float(math.sqrt(h_row ** 2 + h_col ** 2))
            if new_heuristic < heuristic:
                heuristic = new_heuristic
        return heuristic * 5

    def starting_nodes(self):
        """Returns a sequence of starting nodes.
        Represent the state of the agent by a tuple of the form (row, column, fuel)
        """

        starting_agents = []

        for row_i, row_list in enumerate(self.map_str):
            for col_i, char in enumerate(row_list):
                if char == 'S':
                    fuel = math.inf  # S agents are solar and do not need fueling. AKA inf
                    starting_agents.append((row_i, col_i, fuel))
                elif char in self.agent_fuel_str_options:
                    fuel = int(char)
                    starting_agents.append((row_i, col_i, fuel))

        return starting_agents

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        row_i, col_i, fuel = node
        return (row_i, col_i) in self.goal_locations

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.
        Agent Actions
          * Can move in four directions, N, E, S, W, as long as it has fuel and there is no obstacle or wall in the way.
          * This means that agents can also go to cells where other agents are present.
        """

        # List contains tuples of directions and their actions where
        # direction_str, row_change, col_change = direction_action_tup
        direction_actions = [('N', -1, 0),
                             ('E', 0, 1),
                             ('S', 1, 0),
                             ('W', 0, -1)]
        arcs = []

        agent_row, agent_col, agent_fuel = node

        for direction_str, row_change, col_change in direction_actions:
            new_row = agent_row + row_change
            new_col = agent_col + col_change
            new_value = self.map_str[new_row][new_col]
            if new_value not in self.barriers and agent_fuel > 0:
                arcs.append((Arc(tail=node,
                                 head=(new_row, new_col, agent_fuel - 1),  # The agent loses one unit of fuel
                                 action=direction_str,  # for directions action
                                 cost=5)))  # All single directional moves take 5 units of time.

        curr_value = self.map_str[agent_row][agent_col]
        if curr_value == "F" and agent_fuel < 9:  # Fuel station
            arcs.append((Arc(tail=node,
                             head=(agent_row, agent_col, 9),  # Fuel up to max capacity of 9.
                             action="Fuel up",  # for fueling action
                             cost=15)))  # 15 units of time (regardless of how much fuel is obtained).

        if curr_value == "P":  # Portal station
            for portal_row, portal_col in self.portal_locations:
                if (portal_row, portal_col) != (agent_row, agent_col):
                    arcs.append((Arc(tail=node,
                                     head=(portal_row, portal_col, agent_fuel),  # does not consume any fuel
                                     action="Teleport to " + str((portal_row, portal_col)),  # row and col of the destination portal
                                     cost=10)))  # The action costs 10 units of time (regardless of the destination).

        return arcs

def print_map(map_graph, frontier, solution):
    """
    :param map_graph:
    :param frontier:
    :param solution: Arc objects that make up a path from a starting node to a goal node, or is None.
    :return:
    """

    expanded = frontier.expanded
    map_list = map_graph.map_str[:]

    if len(expanded) > 0:
        for row, col, fuel in expanded:
            if map_list[row][col] != "G" and map_list[row][col] != "S":
                map_list[row][col] = '.'

    if solution:
        for arc in solution[1:-1]:
            row, col, fuel = arc.head
            map_list[row][col] = '*'

    for row in map_list:
        print("".join(row))

def main():
    Q3test()

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
