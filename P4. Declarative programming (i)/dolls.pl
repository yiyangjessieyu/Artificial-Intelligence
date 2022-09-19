directlyIn(In, Box) :- In = irina, Box = natasha.
directlyIn(In, Box) :- In = natasha, Box = olga.
directlyIn(In, Box) :- In = olga, Box = katarina.

contains(Box, In) :- directlyIn(In, Box).
contains(Box, In) :-contains(Box, Middle), directlyIn(In, Middle).

test_answer :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer1 :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer2 :-
    contains(katarina, irina),
    writeln('OK').

test_answer3 :-
    contains(katarina, natasha),
    writeln('OK').

test_answer4 :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
