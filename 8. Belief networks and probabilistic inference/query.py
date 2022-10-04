import itertools

network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 1/100,
            }
    },
    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.10
            }
    },
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.90,
            (False,): 0.05
            }
    }
}

def query(network, query_var, evidence):
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}

    distribution = [0, 0]  # Initialise a raw distribution to [0, 0]
    assignment = dict(evidence)  # create a partial assignment

    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment.update({query_var: query_value})
        # print("YOYANG")
        # print(assignment)

        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            # print("VALUES")
            # print(values)
            # Update the assignment (we now have a complete assignment)
            for var, val in zip(hidden_vars, values):
                assignment.update({var: val})

            # Update the raw distribution by the probability of the assignment.
            distribution[query_value] += joint_prob(network, assignment)
            # print("DISTRUBTION")
            # print(distribution)

    # Normalise the raw distribution and return it
    return [p / sum(distribution) for p in distribution]


def joint_prob(network, assignment):
    p = 1  # p will eventually hold the value we are interested in

    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT.

        parents, CPT = network[var]['Parents'], network[var]['CPT']

        # If a node does not have any parents, the value of 'Parents' = []
        # then the only key of CPT, is an empty tuple
        if len(parents) == 0:
            p_True = CPT[()]
            is_var_true = assignment[var]

            if not is_var_true:
                p_True = 1 - p_True

        else:
            parent_bool = ()
            for parent in parents:
                parent_bool += (assignment[parent],)

            p_True = CPT[parent_bool]

            is_assign_true = assignment[var]
            if not is_assign_true:
                p_True = 1 - p_True

        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.

        p *= p_True

    return p


def main():
    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))

    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
