cartesian_product([], X, []).
cartesian_product([Head|Tail], X, [Product|AcrossB]) :- helper(Head, X, Product), writeln(Product), writeln([Product|AcrossB]), cartesian_product(Tail, X, AcrossB).

helper(Head, [X1|Remaining], [Product|RemainingProducts]) :- Product = (Head, X1), helper(Head, Remaining, RemainingProducts).
helper(_, [], []) .

test_answer :- cartesian_product([a, b], [1, 2], X),
               writeln(X).
