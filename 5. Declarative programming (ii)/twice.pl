twice([], []).
twice([Head1|Tail1], [Head2, Head22|Tail2]) :- Head1 = Head2, Head1 = Head22, twice(Tail1, Tail2).

test_answer :-
    twice([a, b, c, d], L),
    writeln(L).

test_answer2 :-
    twice(L, [1, 1, 2, 2, 3, 3]),
    writeln(L).

test_answer3 :-
    twice([], []),
    writeln('OK').

test_answer4 :-
    twice(L1, L2),
    writeln('OK').

test_answer5 :-
    \+ twice(L, [a, a, b]),
    writeln('OK').
