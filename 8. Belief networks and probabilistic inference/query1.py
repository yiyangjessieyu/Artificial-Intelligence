import itertools


def query(network, query_var, evidence):
    assignment = {query_var: True}

    if evidence == {}:
        # hidden_vars = network.keys() - evidence.keys() - {query_var}
        # for values in itertools.product((True, False), repeat=len(hidden_vars)):
        #     hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}

        hidden_vars = network.keys() - evidence.keys() - {query_var}
        for hidden_var in hidden_vars:
            assignment.update({hidden_var: True})
        # assignment.update(hidden_assignments)
        # print(itertools.product((True, False), repeat=len(hidden_vars)))
        p_True = joint_prob(network, assignment)
    else:
        assignment.update(evidence)

        parents, CPT = network[query_var]['Parents'], network[query_var]['CPT']

        if len(parents) == 0:
            p_True = CPT[()]
        else:
            parent_bool = ()
            for parent in parents:
                parent_bool += (assignment[parent],)
            p_True = CPT[parent_bool]

    distribution = [1 - p_True, p_True]

    return distribution


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

    answer = query(network, 'A', {})
    print("P(A=true) = {:.5f}".format(answer[True]))
    print("P(A=false) = {:.5f}".format(answer[False]))

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

    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))
    print("P(B=false|A=false) = {:.5f}".format(answer[False]))

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

    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))

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

    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
          "John and Mary have called: {:.3f}".format(answer[True]))

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

    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
          "Mary has called: {:.5f}".format(answer[True]))

if __name__ == "__main__":
    main()
