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

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))

