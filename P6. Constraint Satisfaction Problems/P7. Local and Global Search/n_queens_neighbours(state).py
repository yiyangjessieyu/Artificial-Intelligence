from copy import deepcopy
import itertools
from operator import indexOf
from os import stat

def n_queens_neighbours(state):

    result = set()
    state_list = list(state)

    swap_choices = list(itertools.combinations(state_list, 2))

    for tup in swap_choices:
        a, b = tup
        a_i, b_i = state_list.index(a), state_list.index(b)

        swap_list = deepcopy(state_list)
        swap_list[a_i], swap_list[b_i] = swap_list[b_i], swap_list[a_i]

        result.add(tuple(swap_list))

    return sorted(list(result - set(state)))

print(n_queens_neighbours((1, 2)))

print(n_queens_neighbours((1, 3, 2)))

print(n_queens_neighbours((1, 2, 3)))

print(n_queens_neighbours((1,)))

for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
    print(neighbour)

for neighbour in n_queens_neighbours((2, 3, 1, 4)):
    print(neighbour)