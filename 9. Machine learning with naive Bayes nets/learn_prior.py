import csv


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
    print("Prior probability of spam is {:.5f}.".format(prior))

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))

    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    print(format(prior, ".5f"))

    prior = learn_prior("spam-labelled.csv", pseudo_count=2)
    print(format(prior, ".5f"))

    prior = learn_prior("spam-labelled.csv", pseudo_count=10)
    print(format(prior, ".5f"))

    prior = learn_prior("spam-labelled.csv", pseudo_count=100)
    print(format(prior, ".5f"))

    prior = learn_prior("spam-labelled.csv", pseudo_count=1000)
    print(format(prior, ".5f"))


if __name__ == "__main__":
    main()
