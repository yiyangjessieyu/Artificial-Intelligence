inorder(leaf(X), [X]).
inorder(tree(Root, L, Right), T) :- inorder(L, LL), inorder(Right, RL), append(L, [Root|RL], T).
