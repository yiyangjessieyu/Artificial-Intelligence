dna([Left_head|Left_tail], [Right_head|Right_tail]) :- match(Left_head, Right_head), dna(Left_tail, Right_tail).

dna([], []).

match(a, t).
match(t, a).
match(g, c).
match(c, g).

test_answer :- dna([a, t, c, g], X),
               writeln(X).
