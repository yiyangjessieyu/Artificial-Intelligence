import itertools, copy 
from csp import scope, satisfies, CSP


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in csp.var_domains} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                   for z in scope(cprime): # COMPLETE
                       if x != z: # COMPLETE
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

    
def generate_and_test(csp):
    # csp has attribute var_domains and constraints

    variable, domains = zip(*csp.var_domains.items())

    # for all possible variable values combination
    # # cartesian product of the domain values
    for values in itertools.product(*domains):

        # zip(variable, values) to create an iterator that produces tuples of the form (x, v)
        # assignment is a dictionary of variable names and their corresponding values
        assignment = {x: v for x, v in zip(variable, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment

domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1    :      o + o == r + 10 * c1, # one of the constraints
        lambda w, u, c2, c1   :      w + w + c1 == u + 10 * c2, # one of the constraints
        lambda t, o, c2, f    :      t + t + c2 == o + 10 * f and t != 0 and f != 0, # one of the constraints
        lambda t, w, o, f, u, r:    sorted(set([t, w, o, f, u, r])) == sorted([t, w, o, f, u, r])
        })


new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))

new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])