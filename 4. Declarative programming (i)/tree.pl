mirror(leaf(Label), leaf(Label)).
mirror(tree(Left1, Right1), tree(Left2, Right2)) :- mirror(Left1, Right2), mirror(Right1, Left2).


test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T).

test_answer :-
    write('Wrong answer!').
