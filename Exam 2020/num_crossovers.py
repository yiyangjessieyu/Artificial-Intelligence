def tree_size(tree):
    if type(tree) != list:
        return 1
    else:
        count = 0
        for item in tree:
            count += tree_size(item)

        return count


def num_crossovers(parent_expression1, parent_expression2):
    return tree_size(parent_expression1) * tree_size(parent_expression2)
