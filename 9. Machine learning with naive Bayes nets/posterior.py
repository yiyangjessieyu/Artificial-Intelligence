def posterior(prior, likelihood, observation):
    class_true, class_false = prior, 1 - prior

    for i,  value_tup in enumerate(likelihood):

        observed = observation[i]

        value_class_false, value_class_true = value_tup

        class_true *= value_class_true if observed else 1 - value_class_true
        class_false *= value_class_false if observed else 1 - value_class_false

    sum = class_true + class_false

    normalized = class_true / sum

    return normalized

def main():
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, True, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, False)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))


if __name__ == "__main__":
    main()
