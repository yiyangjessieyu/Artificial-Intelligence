

postorder(leaf(Label), [Label]).

postorder(tree(Root, Left, Right), Traversal) :- postorder(Left, LeftList),
                                                  postorder(Right, RightList),
                                                  append(LeftList, RightList, BranchList),
                                                  append(BranchList, [Root], Traversal).

test_answer :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).
