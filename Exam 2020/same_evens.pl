same_evens_helper([], _).

same_evens_helper([Head, Same|Tail], Same) :- same_evens_helper(Tail, Same).


same_evens([]).

same_evens([Head, Same|Tail]) :- same_evens_helper(Tail, Same).
