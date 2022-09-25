import random
from itertools import combinations


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    while True:
        states = random_state()
        for state in greedy_descent(states, neighbours, cost):
            print(state)
        if cost(state) == 0:  # 0 conflict
            break
        else:  # When the search reaches a local minimum that is not global
            print("RESTART")


def greedy_descent(initial_state, neighbours, cost):
    curr_state = initial_state
    lowest_cost = cost(initial_state)
    trace = [initial_state]

    while True:
        neighbours_cost = [(s, cost(s)) for s in neighbours(curr_state)]

        if len(neighbours_cost) == 0:
            yield curr_state
            break

        min_neighbour_cost = min(neighbours_cost, key=lambda neighbour_cost: neighbour_cost[1])[1]
        if min_neighbour_cost >= lowest_cost:
            yield curr_state
            break
        else:
            yield curr_state
            lowest_cost = min_neighbour_cost
            curr_state = min(neighbours_cost, key=lambda neighbour_cost: neighbour_cost[1])[0]


def n_queens_cost(state):
    conflicts = 0
    location = {}
    row = 1
    for col in state:
        location[(row, col)] = col
        row += 1

    for key, value in location.items():
        cur_x, cur_y = key
        for compare_x, compare_y in location.keys():

            if compare_x != cur_x and compare_y != cur_y:

                if compare_x == cur_x:
                    conflicts += 1
                elif compare_y == cur_y:
                    conflicts += 1
                else:
                    diff_x = abs(compare_x - cur_x)
                    diff_y = abs(compare_y - cur_y)
                    if diff_y == diff_x:
                        conflicts += 1

    return int(conflicts / 2)


def n_queens_neighbours(state):
    result = []
    for a, b, in sorted(combinations(state, 2)):
        neighbour = list(state)
        a_i, b_i = neighbour.index(a), neighbour.index(b)
        neighbour[a_i], neighbour[b_i] = b, a  # swap
        result.append(tuple(neighbour))

    return sorted(result)


from n_queens_neighbours import n_queens_neighbours as neighbours
from n_queens_cost import n_queens_cost as cost


def main():
    N = 8
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1, N + 1), N))

    greedy_descent_with_random_restart(random_state, neighbours, cost)

if __name__ == "__main__":
    main()
