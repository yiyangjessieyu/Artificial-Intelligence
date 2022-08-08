import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM = r"[a-z][a-zA-z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query
        self.expanded_query = query # a set of atoms

    def starting_nodes(self):

        starting_bodies = []

        for head_str, body_list in self.clauses:
            if head_str in self.query:
                starting_bodies.append(body_list)

        return starting_bodies

    def is_goal(self, node):
        # node == [] meaning when there is no head node
        return len(node) == 0

    def outgoing_arcs(self, tail_node):
        # tail node is a body

        outgoing_arcs = set()

        for head_str, body_list in self.clauses:
            if tail_node == body_list:
                self.expanded_query.remove(head_str)
                self.expanded_query.update(body_list)
                outgoing_arcs.update(body_list)

        result_arcs =[]

        for letter in outgoing_arcs:
            result_arcs.append((Arc(tail=tail_node, head=letter, action="no action", cost=0)))

        return result_arcs


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
        search."""

    def __init__(self, ):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        """Store the given path by adding a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method. """
        self.container.append(path)

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration


def main():
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

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true. - Expected")
    else:
        print("The query is not provable.")

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

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true. - Expected")
    else:
        print("The query is not provable.")

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

    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true. - Expected")
    else:
        print("The query is not provable.")

    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """

    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable. - Expected")

    kb = """
    a :- b.
    """

    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable. - Expected")

    kb = ""

    query = {'proposition'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable. - Expected")

if __name__ == "__main__":
    main()
