def roulette_wheel_select(population, fitness, r):
    fitness_sum = 0
    for person in population:
        fitness_sum += fitness(person)

    fitness_p = []
    for person in population:
        fitness_p.append((person,
                          fitness(person) / fitness_sum
                          )
                         )

    running_total = 0
    for person, percent in fitness_p:
        running_total += percent
        if running_total >= r:
            return person

def main():
    population = ['a', 'b']

    def fitness(x):
        return 1  # everyone has the same fitness

    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))

    population = [0, 1, 2]

    def fitness(x):
        return x

    for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r))

if __name__ == "__main__":
    main()
