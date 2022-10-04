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
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))
    # 0.20000

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))
    # 0.80000

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p))
    # 0.63000

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    p = joint_prob(network, {'A': False, 'B': False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B': False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B': True})
    print("{:.5f}".format(p))
    # 0.27000
    # 0.63000
    # 0.02000
    # 0.08000

    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': ['Burglary', 'Earthquake'],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }

    p = joint_prob(network, {'John': True, 'Mary': True,
                             'Alarm': True, 'Burglary': False,
                             'Earthquake': False})
    print("{:.8f}".format(p))
    # 0.00062811


if __name__ == "__main__":
    main()
