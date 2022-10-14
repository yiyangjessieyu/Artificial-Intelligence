cartesian_product([], X, []).
cartesian_product([Head|Tail], X, Result) :- helper(Head, X, Product),
                                              append(Product, AcrossB, Result),
                                              writeln(Result),
                                              cartesian_product(Tail, X, AcrossB).

helper(Head, [X1|Remaining], [Product|RemainingProducts]) :- Product = (Head, X1), helper(Head, Remaining, RemainingProducts).
helper(_, [], []) .


test_answer :- cartesian_product([a, b], X,
                               [(a,1), (a,2), (b,1), (b,2)]),
             writeln(X).
