from search import *

class RoutingGraph(Graph):

    def __init__(self, map_str):
        """
        :param map_str: The map is always rectangular.

        Positions in the map by a pair (row, col).
         * Row numbers start from 0 for the first (topmost) line, 1 for the second line, and so on.
         * Col start from 0 for the first (leftmost) position (character) in the line.

        The environment is surrounded by walls marked by '+' or '-' or '|' character.
         * Position (0,0) is a '+' (i.e. wall) and so are all other three corners of the map.
         * First and last rows and columns are '-' and '|' respectively (except for the corners).

         The obstacles are marked by 'X'

         Agents are marked by 'S' or digits 0 to 9.
          * There may be zero or more agents on the map.
          * S agents are solar and do not need fueling. AKA inf
          * 0-9 Digit agents indicated by digits have fuel tanks.
              * The capacity of the tank is 9.
              * The digit shows how much fuel is initially available in the tank.

         Agent Actions
          * Can move in four directions, N, E, S, W, as long as it has fuel and there is no obstacle or wall in the way.
          * This means that agents can also go to cells where other agents are present.
          * The agent loses one unit of fuel for each move.
          * The order of actions is clockwise starting from N. So N, E, S, W
            * eg, if from a position all four directional moves are possible,
            * then the first arc in the sequence of arcs returned by outgoing_arcs is for going north,
            * then east, and so on.
          * All single directional moves take 5 units of time.
          * This is what we regard as the cost of the action (since the objective of the problem is to minimise the service time).

          Call points / customers are potential destination marked by G
           * There may be zero or more call points (customers) on the map.
           * To simplify textual representation, we assume that an agent is never initially at a call point.

          Fuel station show by F
          * if an agent is in a cell marked as F and its current fuel amount is less than 9
          * it can take the action of "Fuel up" which fills the tank to its maximum capacity of 9.
          * In the sequence of arcs, the "Fuel up" action (if available) should appear after any other directional actions.
          * The action costs 15 units of time (regardless of how much fuel is obtained).

          Portal show by P
          * There can be zero or more portals on a map.
          * If an agent is here, in addition to the usual movements, it has the option of teleporting to any other location on the map marked as P.
          * In the sequence of arcs, the teleport action (if available) should appear after any other directional action.
          * The action does not consume any fuel but costs 10 units of time (regardless of the destination).
          * The action must be labeled as "Teleport to (row, col)" where row and col are the row and column indices of the destination portal.
          """
        self.map_str = map_str

        print(len(self.map_str))

    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self._starting_nodes

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal_nodes

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        """
        arcs = []
        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1  # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
        return arcs

def main():
    map_str = """\
    +-------+
    |  9  XG|
    |X XXX P|
    | S  0FG|
    |XX P XX|
    +-------+
    """

    graph = RoutingGraph(map_str)


if __name__ == "__main__":
    main()
