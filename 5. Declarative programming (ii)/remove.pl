remove(X, [], []).
remove(X, [X|In_tail], ListOut) :- remove(X, In_tail, ListOut).
remove(X, [Head|In_tail], [Head|Out_Tail]) :- remove(X, In_tail, Out_Tail), \+ X = Head.

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer1 :-
    remove(2, [2], L),
    writeln(L).

test_answer2 :-
    remove(d, [a, b, c], L),
    write(L).

test_answer3 :-
    remove(a, [], L),
    write(L).

test_answer4 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').

test_answer5 :-
    \+ remove(a, [a,a,a], [a,a,a]),
    writeln('OK').
