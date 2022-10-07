import operator

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
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))

    bindings = {'x': 5, 'y': 10, 'time': 15}
    expression = 'y'
    print(evaluate(expression, bindings))

    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))

    bindings = dict(x=5, y=10, blah=15, add=operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings))

if __name__ == "__main__":
    main()
