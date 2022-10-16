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


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):

    vectors, targets = [], []

    while max_epochs > 0:

        for i in range(len(training_examples)):
            vector, target = training_examples[i]
            vectors.append(vector)
            targets.append(target)

            perceptron = construct_perceptron(weights, bias)
            y = perceptron(vector)

            if y != target:
                weights[0] = weights[0] + learning_rate * vector[0] * (target - y)
                weights[1] = weights[1] + learning_rate * vector[1] * (target - y)
                bias = bias + learning_rate * (target - y)

        if accuracy(perceptron, vectors, targets) == 1:
            break

        max_epochs -= 1

    return weights, bias


def main():
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 0),
        ((1, 0), 0),
        ((1, 1), 1),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")

    perceptron = construct_perceptron(weights, bias)

    print(perceptron((0, 0)))
    print(perceptron((0, 1)))
    print(perceptron((1, 0)))
    print(perceptron((1, 1)))
    print(perceptron((2, 2)))
    print(perceptron((-3, -3)))
    print(perceptron((3, -1)))

    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 1), 0),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")


if __name__ == "__main__":
    main()
