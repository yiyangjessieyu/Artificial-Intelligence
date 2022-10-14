new_append([], [], []).

new_append([], [Head2|Tail2], Result) :- Result = [Head2|Remaining], new_append([], Tail2, Remaining).

new_append([Head1|Tail1], B, Result) :- Result = [Head1|Remaining], new_append(Tail1, B, Remaining).
