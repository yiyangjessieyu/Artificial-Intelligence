def select(population, error, max_error, r):
    fitness = lambda antenna: max_error - error(antenna)
    running_total = [fitness(population[0])]
    for i in range(1, len(population)):
        running_total.append(running_total[-1] + fitness(population[i]))
    r *= running_total[-1]
    for i in range(len(running_total)):
        if running_total[i] > r:
            return population[i]


def main():
    population = ['a', 'b']

    def error(x):

        return {'a': 14,
                'b': 12}[x]

    max_error = 15

    for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
        print(select(population, error, max_error, r))

    # since the fitness of 'a' is 1 and the fitness of 'b' is 3,
    # for r's below 0.25 we get 'a', for r's above it we get 'b'.

    population = ['a', 'b']

    def error(x):

        return 1  # in this example everyone has the same error

    max_error = 6

    for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
        print(select(population, error, max_error, r))

    population = ['a', 'b', 'c']

    def error(x):

        return {'a': 2, 'b': 1, 'c': 0}[x]

    max_error = 2

    for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(select(population, error, max_error, r))


if __name__ == '__main__':
    main()
