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

    return int(conflicts/2)


def main():
    print(n_queens_cost((1, 2)))
    # 1

    print(n_queens_cost((1, 3, 2)))
    # 1

    print(n_queens_cost((1, 2, 3)))
    # 3

    print(n_queens_cost((1,)))
    # 0

    print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
    # 28

    print(n_queens_cost((2, 3, 1, 4)))

if __name__ == "__main__":
    main()
