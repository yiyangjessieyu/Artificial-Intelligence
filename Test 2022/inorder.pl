inorder(left(A), [A]).

inorder(tree(Root, Left, Right), Traversal) :- inorder(Left, LeftList), inorder(Right, RightList),
                                                append(LeftList, [Root], Half),
                                                append(Half, RightList, Traversal). 
