from itertools import combinations


def n_queens_neighbours(state):
    result = []
    for a, b, in sorted(combinations(state, 2)):
        neighbour = list(state)
        a_i, b_i = neighbour.index(a), neighbour.index(b)
        neighbour[a_i], neighbour[b_i] = b, a  # swap
        result.append(tuple(neighbour))

    return sorted(result)

def main():

    print(n_queens_neighbours((1, 2)))

    print(n_queens_neighbours((1, 3, 2)))

    print(n_queens_neighbours((1, 2, 3)))

    print(n_queens_neighbours((1,)))

    for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)

    for neighbour in n_queens_neighbours((2, 3, 1, 4)):
        print(neighbour)

if __name__ == "__main__":
    main()
