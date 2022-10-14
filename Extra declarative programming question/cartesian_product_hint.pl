% The following helper predicate multiplies a single element by a list
product(_, [], []).   % base case
product(X, [H|T], [(X, H) | MorePairs]) :- product(###, ###, ###). % Complete

cartesian_product([], _, []).
cartesian_product([Head|Tail], ListB, AllPairs) :-
    product(Head, ListB, HeadPairs),
    cartesian_product(###, ListB, RemainingPairs),  % Complete
    append(###, ###, ###).  % Complete
