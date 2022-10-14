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
        result = int(a >= 0)
        return result  # what the perceptron should return

    return perceptron  # this line is fine


def main():
    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)

    print(perceptron([1, 1]))
    print(perceptron([2, 1]))
    print(perceptron([3, 1]))
    print(perceptron([-1, -1]))


if __name__ == "__main__":
    main()
