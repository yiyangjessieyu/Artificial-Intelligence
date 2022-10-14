def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        # Complete (a line or two)

        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        total = 0
        for i in range(len(input)):
            total += weights[i] * input[i]
        a = total + bias
        return int(a >= 0)  # what the perceptron should return

    return perceptron  # this line is fine


def accuracy(classifier, inputs, expected_outputs):
    prediction = [classifier(vector) for vector in inputs]

    true_count = 0
    n = len(expected_outputs)
    for i in range(n):
        if expected_outputs[i] == prediction[i]:
            true_count += 1

    return float(true_count / n)


def main():
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))


if __name__ == "__main__":
    main()
