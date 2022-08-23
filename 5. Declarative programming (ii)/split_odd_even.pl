split_odd_even([], [], []).

split_odd_even([In_Head|[]], [A_Head|A_Tail], B) :-
  In_Head = A_Head, split_odd_even([], A_Tail, B).

split_odd_even([In1, In2|In_Tail], [A_Head|A_Tail], [B_Head|B_Tail]) :-
  In1 = A_Head, In2 = B_Head, split_odd_even(In_Tail, A_Tail, B_Tail).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer2 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

test_answer3 :-
    split_odd_even([], A, B),
    write(A),
    writeln(B).
