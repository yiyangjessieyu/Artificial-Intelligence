import random
random.seed(99999999)

def random_expression(function_symbols, leaves, max_depth):

    coin_toss = random.randint(0, 1)

    # If it's a head or no depth return a leaf node
    if coin_toss == 1 or max_depth == 0:
        return random.choice(leaves)

    # Otherwise return a random expression tree (a 3 - element list)
    else:
        return [random.choice(function_symbols),
                random_expression(function_symbols, leaves, max_depth-1),
                random_expression(function_symbols, leaves, max_depth-1)]



def _is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int:
        return True

    elif object in leaf_symbols:
        return True

    elif type(object) == list and len(object) == 3:
        function, left, right = object
        return function in function_symbols and \
               _is_valid_expression(left, function_symbols, leaf_symbols) and \
               _is_valid_expression(right, function_symbols, leaf_symbols)

    else:
        return False

def main():
    # All the generated expressions must be valid

    function_symbols = ['f', 'g', 'h']
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not _is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")

    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]

    # Out of 10000 expressions, at least 1000 must be distinct
    _check_distinctness(expressions)

    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]

    # Out of 10000 expressions, there must be at least 100 expressions
    # of depth 0, 100 of depth 1, ..., and 100 of depth 4.

    _check_diversity(expressions, max_depth)

if __name__ == "__main__":
    main()
