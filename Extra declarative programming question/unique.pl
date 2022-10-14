member(Head, [Head|_]).
member(ItemInTail, [_|Tail]) :- member(ItemInTail, Tail).

unique([], []).

unique([Head|Tail], Set) :- \+member(Head, Set), append(Head, Remaining, Set), unique(Tail, Remaining).
