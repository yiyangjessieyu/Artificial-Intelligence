swap12(List1, List2) :- [X1, X2|Tail] = List1, [X2, X1|Tail] = List2.

test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer2 :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer3 :-
    swap12(L, [b, a]),
    writeln(L).

test_answer4 :-
    swap12(L1, L2),
    writeln('OK').
