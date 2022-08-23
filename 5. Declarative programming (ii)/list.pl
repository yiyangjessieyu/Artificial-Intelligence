
second(List, X) :- [_, X|Tail] = List.

test_answer :-
    second([cosc, 2, Var, beethoven], X),
    writeln(X).

test_answer2 :-
    \+ second([1], X),
    writeln('OK').

test_answer2 :-
    second([_],_),
    writeln('The predicate should fail on lists of length one!').

test_answer3 :-
    second([a, b, c, d], b),
    writeln('OK').

test_answer4 :-
    second(L, X),
    writeln('OK').
