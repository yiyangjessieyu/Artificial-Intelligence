def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int:
        return True

    elif object in leaf_symbols:
        return True

    elif type(object) == list and len(object) == 3:
        function, left, right = object
        return function in function_symbols and \
               is_valid_expression(left, function_symbols, leaf_symbols) and \
               is_valid_expression(right, function_symbols, leaf_symbols)

    else:
        return False


def main():
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1

    print(is_valid_expression(expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


if __name__ == "__main__":
    main()
