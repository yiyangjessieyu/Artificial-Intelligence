directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(Box, Inside) :- directlyIn(Inside, Box).
contains(Box, Inside) :- directlyIn(Inside, X), contains(Box, X).

test_answer :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer2 :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer3 :-
    contains(katarina, irina),
    writeln('OK').

test_answer4 :-
    contains(katarina, natasha),
    writeln('OK').

test_answer5 :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
