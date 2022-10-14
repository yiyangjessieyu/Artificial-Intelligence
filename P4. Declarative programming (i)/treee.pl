leaf(Label).

tree(Label) := left(Label).
tree()

mirror(Tree1, Tree2) :-  Tree1 = tree(B_Left1, B_Right1),
                          Tree2 = tree(B_Left2, B_Right2),
                          B_Right1 = B_Left2,
                          B_Left1, B_Right2.

test_answer :-
    mirror(leaf(foo), leaf(foo)),
    write('OK').

test_answer :-
    write('Wrong answer!').

test_answer2 :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK').

test_answer2 :-
    write('Wrong answer!').
