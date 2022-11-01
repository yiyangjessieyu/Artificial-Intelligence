def cost(state):

    conflicts = 0

    for col, row in enumerate(state):

        for col_neighbor, row_neighbor in enumerate(state):

            if row_neighbor != row:

                col_diff, row_diff = abs(col_neighbor - col), abs(row_neighbor - row)

                if col_diff== row_diff:
                    conflicts+=1

    return int(conflicts/2)


print(cost((1, 2)))


print(cost((1, 3, 2)))


print(cost((1, 2, 3)))


print(cost((1,)))


print(cost((1, 2, 3, 4, 5, 6, 7, 8)))


print(cost((2, 3, 1, 4)))