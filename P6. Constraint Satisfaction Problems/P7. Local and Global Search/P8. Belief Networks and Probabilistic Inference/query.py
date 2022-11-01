from itertools import product

def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will eventually hold the value we are interested in
    for var in network:
        parents, CPT = network[var]['Parents'], network[var]['CPT']

        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 

        is_parent_observed_T = ()
        for parent in parents:
            is_parent_observed_T += (assignment[parent],)

        prob = CPT[is_parent_observed_T]
        
        is_observed_T = assignment[var]
        p *= prob if is_observed_T else 1 - prob
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
    
    return p

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Initialise a raw distribution to [0, 0]
    raw_dist = [0, 0]

    assignment = dict(evidence) # create a partial assignment
    print(assignment)
    # for query_value in {True, False}:
    #     # Update the assignment to include the query variable
    #     for values in product((True, False), repeat=len(hidden_vars)):
    #         # Update the assignment (we now have a complete assignment)
    #         # Update the raw distribution by the probability of the assignment.
    # # Normalise the raw distribution and return it

    return raw_dist


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