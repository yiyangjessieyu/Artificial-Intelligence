from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraints) for constraints in csp.constraints):
            yield assignment

def main():
    Q3test()


def Q3test():
    canterbury_colouring = CSP(
        var_domains={
            'christchurch': {'red', 'green'},
            'selwyn': {'red', 'green'},
            'waimakariri': {'red', 'green'},
        },
        constraints={
            lambda christchurch, waimakariri, selwyn: christchurch != waimakariri and christchurch != selwyn and selwyn != waimakariri,
        }
    )


def Q2test():
    crossword_puzzle = CSP(
        var_domains={
            # read across:
            'across1': set("bus has".split()),
            'across3': set("lane year".split()),
            'across4': set("ant car".split()),
            # read down:
            'down1': set("buys hold".split()),
            'down2': set("search syntax".split()),
        },
        constraints={
            lambda across1, down1: across1[0] == down1[0],
            lambda down1, across3: down1[2] == across3[0],
            lambda across1, down2: across1[2] == down2[0],
            lambda down2, across3: down2[2] == across3[2],
            lambda down2, across4: down2[4] == across4[0],
        })

    print(sorted(crossword_puzzle.var_domains['across1']))


def Q1test():
    simple_csp = CSP(
        var_domains={x: set(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
        })

    solutions = sorted(str(sorted(solution.items())) for solution
                       in generate_and_test(simple_csp))
    print("\n".join(solutions))

    crossword_puzzle = CSP(
        var_domains={
            # read across:
            'a1': set("ant,big,bus,car".split(',')),
            'a3': set("book,buys,hold,lane,year".split(',')),
            'a4': set("ant,big,bus,car,has".split(',')),
            # read down:
            'd1': set("book,buys,hold,lane,year".split(',')),
            'd2': set("ginger,search,symbol,syntax".split(',')),
        },
        constraints={
            lambda a1, d1: a1[0] == d1[0],
            lambda d1, a3: d1[2] == a3[0],
            lambda a1, d2: a1[2] == d2[0],
            lambda d2, a3: d2[2] == a3[2],
            lambda d2, a4: d2[4] == a4[0],
        })

    solution = next(iter(generate_and_test(crossword_puzzle)))

    # printing the puzzle similar to the way it actually  looks
    pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
        solution['d1'], "", solution['d2'], fillvalue=" ")]
    pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
    print("\n".join(pretty_puzzle))

if __name__ == "__main__":
    main()
