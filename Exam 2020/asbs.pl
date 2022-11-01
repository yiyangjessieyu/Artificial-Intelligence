asbs([Head1|Tail]) :- Head1 = a, a_check(Tail); Head1 = b, b_check(Tail).
asbs([]).
a_check([Head1|Tail]) :- Head1 = a, a_check(Tail); Head1 = b, b_check(Tail).
a_check([]).
b_check([Head1|Tail]) :- Head1 = b, b_check(Tail).
b_check([]).
#
#
#
# test_answer :-
#     asbs([a,a,a,b]),
#     writeln('OK').
#
# test_answer :-
#     \+ asbs([a,b,a]),
#     writeln('OK').

# asbs([]).
#
# asbs([X|Tail]) :- X = a, asbs(Tail); X = b, check_b(Tail).
#
# check_b([]).
# check_b([X|Tail]) :- X = b, check_b(Tail).
