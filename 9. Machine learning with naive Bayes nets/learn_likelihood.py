import csv


def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    size = len(training_examples[1:])
    true_likelihoods = [0] * size
    false_likelihoods = [0] * size

    for row_tup in training_examples[1:]:
        for i, x_when_class_result in enumerate(row_tup[:-1]):
            is_class_true = int(row_tup[-1])
            if is_class_true:
                true_likelihoods[i] += int(x_when_class_result)
            else:
                false_likelihoods[i] += int(x_when_class_result)

    n_class_true = sum(int(is_class_true[-1]) for is_class_true in training_examples[1:])
    n_class_false = size - n_class_true

    result = []
    for i in range(0, 12):
        true_likelihood = true_likelihoods[i]
        false_likelihood = false_likelihoods[i]
        result.append((pseudo_count_result(false_likelihood, pseudo_count, n_class_false, 2),
                       pseudo_count_result(true_likelihood, pseudo_count, n_class_true, 2)))

    return result


def pseudo_count_result(likelihood, pseudo_count, size, domain):
    return (likelihood + pseudo_count) / (size + (pseudo_count * domain))


def main():
    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])

    likelihood = learn_likelihood("spam-labelled.csv")

    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


if __name__ == "__main__":
    main()
