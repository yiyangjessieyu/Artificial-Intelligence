import operator


def generate_rest(initial_sequence, expression, length):

    if length == 0:
        return []

    bindings = {"i": operator.add}

    return [evaluate(initial_sequence[-1], bindings)] + generate_rest(initial_sequence, expression, length-1)


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

if __name__ == "__main__":
    main()
