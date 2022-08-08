import re


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(knowledge_base):
    kb_list = list(clauses(knowledge_base))

    complete_atoms = []

    more_clauses = True

    while more_clauses:
        more_clauses = False # assumeno more clauses to find unless added a new atom to the set
        for head_str, body_list in kb_list:
            if (len(body_list) == 0 or all([body_str in complete_atoms for body_str in body_list])) and \
                head_str not in complete_atoms:
                complete_atoms.append(head_str)
                more_clauses = True

    return complete_atoms


def main():
    kb = """
    a :- b.
    b.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    print(", ".join(sorted(forward_deduce(kb))))


if __name__ == "__main__":
    main()
