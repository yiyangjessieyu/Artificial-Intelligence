import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(knowledge_base):

    kb_list = list(clauses(knowledge_base))

    complete_atoms = {''}

    more_clauses = True
    added_to_set = False
    while more_clauses:
        for pdc_tuple in kb_list:
            head_str, body_list = pdc_tuple
            print(head_str, body_list)
            body_in_set = True
            for body_str in body_list:
                print(body_str)
                if body_str not in complete_atoms:
                    body_in_set = False

            if body_in_set:
                complete_atoms.add(head_str)
                added_to_set = True

        print(added_to_set)
        if not added_to_set:
            more_clauses = False

    return complete_atoms

def main():
    kb = """
    a :- b.
    b.
    """

    print(list(clauses(kb)))

    print(", ".join(sorted(forward_deduce(kb))))


if __name__ == "__main__":
    main()

