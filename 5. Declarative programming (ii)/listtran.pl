tran(tahi,one).
tran(rua,two).
tran(toru,three).
tran(wha,four).
tran(rima,five).
tran(ono,six).
tran(whitu,seven).
tran(waru,eight).
tran(iwa,nine).

listtran(List1, List2) :- List1 = [], List2 = [].
listtran(List1, List2) :- List1 = [Head1|Tail1], List2 = [Head2|Tail2], tran(Head1, Head2), listtran(Tail1, Tail2).

test_answer :-
    listtran([], []),
    writeln('OK').
