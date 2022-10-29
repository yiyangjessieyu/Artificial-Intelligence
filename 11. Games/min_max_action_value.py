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


def max_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree

    elif type(game_tree) == list:

        min_turn = []
        for i, child in enumerate(game_tree):
            min_turn.append((min_value(child), i))

        utility = max(min_turn)
        return utility[1], utility[0]


def min_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree

    elif type(game_tree) == list:

        max_turn = []
        for i, child in enumerate(game_tree):
            max_turn.append((max_value(child), i))

        utility = min(max_turn)
        return utility[1], utility[0]

def main():
    game_tree = [2, [-3, 1], 4, 1]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    game_tree = 3

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    game_tree = [1, 2, [3]]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)••••••••••
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)


if __name__ == "__main__":
    main()
