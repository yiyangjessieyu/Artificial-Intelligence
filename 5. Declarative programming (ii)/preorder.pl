append([], L, L).
append([H|L1], L2, [H|L3]):- append(L1, L2, L3).

preorder(leaf(X), [X]).

preorder(tree(Root, L_subtree, R_subtree), Traversal) :-
  append([Root|Middle], Tail, Traversal),
  preorder(L_subtree, Middle),
  preorder(R_subtree, Tail).

test_answer :- preorder(leaf(a), L),
               writeln(L).

test_answer2 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
