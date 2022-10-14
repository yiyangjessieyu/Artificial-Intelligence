unique([], []).

unique([H|T], [H|Set]) :-
    \+ member(H, T),
    unique(T, Set).

unique([H|T], Set) :-
    member(H, T),
    unique(T, Set).
