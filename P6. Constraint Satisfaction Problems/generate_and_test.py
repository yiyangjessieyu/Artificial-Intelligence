from csp import *
import itertools

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


simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

solutions = sorted(str(sorted(solution.items())) for solution
                   in generate_and_test(simple_csp))
print("\n".join(solutions))
