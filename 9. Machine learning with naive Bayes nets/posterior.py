def posterior(prior, likelihood, observation):
    class_false, class_true = 1 - prior, prior

    for i,  likelihood_tup in enumerate(likelihood):

        is_observed_true = observation[i]

        class_false_likelihood, class_true_likelihood = likelihood_tup

        class_false *= class_false_likelihood if is_observed_true else 1 - class_false_likelihood
        class_true *= class_true_likelihood if is_observed_true else 1 - class_true_likelihood

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
