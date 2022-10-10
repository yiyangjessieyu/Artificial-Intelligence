import operator


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

def main():
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i'
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

if __name__ == "__main__":
    main()
