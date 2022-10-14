merge([], ListB, ListB).
merge(ListA, [], ListA).

merge([A | ListA], [B | ListB], [A | Merged]) :-
    A < B,
    merge(ListA, [B | ListB], Merged).

merge([A | ListA], [B | ListB], [B | Merged]) :-
    A >= B,
    merge([A | ListA], ListB, Merged).
