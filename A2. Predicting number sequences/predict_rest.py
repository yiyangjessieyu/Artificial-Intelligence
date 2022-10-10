import random

random.seed(99999999)

import operator

def predict_rest(sequence):

    function_symbols = ["+", "-", "*"]
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 3
    remaining_sequence_length = 5

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
        else:
            if generate_rest(sequence[:2], expression, len(sequence)-2) == sequence[2:]:
                return generate_rest(sequence, expression, remaining_sequence_length)

def generate_rest(initial_sequence, expression, length):

    if length == 0:
        return []

    else:
        x, y, i = initial_sequence[-2], initial_sequence[-1], len(initial_sequence)

        bindings = {"x": x, "y": y, "i": i,
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y}

        new = [evaluate(expression, bindings)]
        return new + generate_rest(initial_sequence + new, expression, length-1)

def evaluate(expression, bindings):

    if type(expression) == list:
        function, left, right = expression[0], expression[1], expression[2]

        if type(left) == list:
            left = evaluate(left, bindings)
        else:
            left = bindings[left] if left in bindings.keys() else left

        if type(right) == list:
            right = evaluate(right, bindings)
        else:
            right = bindings[right] if right in bindings.keys() else evaluate(right, bindings)

        if function in bindings.keys():
            function = bindings[function]
            return function(left, right)

    else:
        return bindings[expression] if expression in bindings.keys() else expression

def random_expression(function_symbols, leaves, max_depth):
    coin_toss = random.randint(0, 1)

    # If it's a head or no depth return a leaf node
    if coin_toss == 1 or max_depth == 0:
        return random.choice(leaves)

    # Otherwise return a random expression tree (a 3 - element list)
    else:
        return [random.choice(function_symbols),
                random_expression(function_symbols, leaves, max_depth - 1),
                random_expression(function_symbols, leaves, max_depth - 1)]


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
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)

    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))

    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))

    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))

    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))

    sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))

    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))

    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))

if __name__ == "__main__":
    main()
