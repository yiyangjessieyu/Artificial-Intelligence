def max_value(tree):
    if type(tree) == int:
        return tree

    elif type(tree) == list:

        min_turn = []
        for child in tree:
            min_turn.append(min_value(child))

        return max(min_turn)


def min_value(tree):
    if type(tree) == int:
        return tree

    elif type(tree) == list:

        max_turn = []
        for child in tree:
            max_turn.append(max_value(child))

        return min(max_turn)


def main():
    game_tree = 3

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, 3]

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))

    game_tree = [[1, 2], [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))


if __name__ == "__main__":
    main()
