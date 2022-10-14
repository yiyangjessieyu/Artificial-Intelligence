check_01([0|Tail]) :- check_01(Tail).
check_01([1|Tail]) :- check_01(Tail).
check_01([]).

binary_number([0, 'b'|ListOfAtoms]) :- ListOfAtoms = [Head|Tail], Head = 0, check_01(Tail);
                                        ListOfAtoms = [Head|Tail], Head = 1, check_01(Tail).


check_01([0|Tail]) :- check_01(Tail).
check_01([1|Tail]) :- check_01(Tail).
check_01([]).

binary_number([0, 'b', 0|ListOfAtoms]) :- check_01(ListOfAtoms).
binary_number([0, 'b', 1|ListOfAtoms]) :- check_01(ListOfAtoms).
