split_odd_even([], [], []).

split_odd_even([In_Head|[]], [A_Head|A_Tail], B) :-
  In_Head = A_Head, split_odd_even([], A_Tail, B).

split_odd_even([In1, In2|In_Tail], [A_Head|A_Tail], [B_Head|B_Tail]) :-
  In1 = A_Head, In2 = B_Head, split_odd_even(In_Tail, A_Tail, B_Tail).

merge([], ListB, ListB).
merge(ListA, [], ListA).

merge([A | ListA], [B | ListB], [A | Merged]) :-
    A < B,
    merge(ListA, [B | ListB], Merged).

merge([A | ListA], [B | ListB], [B | Merged]) :-
    A >= B,
    merge([A | ListA], ListB, Merged).

merge_sort([], []).
merge_sort([Item], [Item]).

merge_sort([A, B|[]], [B, A]) :- A >= B.
merge_sort([A, B|[]], [A, B]) :- A < B.

merge_sort(List, Sorted):-
	List = [_,_|_],    % the list has two or more elements
	split_odd_even(List, SubSeq1, SubSeq2),
	merge_sort(SubSeq1, SortedSeq1),
	merge_sort(SubSeq2, SortedSeq2),
	merge(SortedSeq1, SortedSeq2, Sorted).   
