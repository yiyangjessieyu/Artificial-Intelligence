def depth(expression):

    if type(expression) == list:
        left, right = expression[1], expression[2]
        return 1 + max(depth(left), depth(right))

    return 0


def main():
    expression = 12
    print(depth(expression))

    expression = 'weight'
    print(depth(expression))

    expression = ['add', 12, 'x']
    print(depth(expression))

    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))

if __name__ == "__main__":
    main()
