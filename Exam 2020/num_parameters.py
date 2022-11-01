def num_parameters(unit_counts):
    layer_sum = 0

    for i in range(len(unit_counts) - 1):
        layer_sum += unit_counts[i] * (unit_counts[i + 1] + 1)
        print("hhh", layer_sum, i)

    return layer_sum


print(num_parameters([2, 4, 2]))

print(num_parameters([2, 4, 1]))
