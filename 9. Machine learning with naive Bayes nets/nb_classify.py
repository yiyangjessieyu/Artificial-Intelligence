import csv


def nb_classify(prior, likelihood, input_vector):
    certainty = posterior(prior, likelihood, input_vector)
    return ("Spam", certainty) if certainty > 0.5 else ("Not Spam", 1 - certainty)


def posterior(prior, likelihood, observation):
    class_true, class_false = prior, 1 - prior

    for i, value_tup in enumerate(likelihood):
        observed = observation[i]

        value_class_false, value_class_true = value_tup

        class_true *= value_class_true if observed else 1 - value_class_true
        class_false *= value_class_false if observed else 1 - value_class_false

    sum = class_true + class_false

    normalized = class_true / sum

    return normalized


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


def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    sum_prior = 0
    for row_tup in training_examples[1:]:
        prior = int(row_tup[-1])
        sum_prior += prior

    return (sum_prior + pseudo_count) / (len(training_examples) + (pseudo_count * 2) - 1)


def main():
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
        (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ]

    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))

    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    input_vectors = [
        (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
        (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ]

    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))


if __name__ == "__main__":
    main()
