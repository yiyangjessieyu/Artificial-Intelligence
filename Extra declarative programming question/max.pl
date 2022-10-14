max_between_two(Num1, Num2, Max) :- Num1 < Num2, Max = Num2;
                        Num1 > Num2, Max = Num1.

max([], M) :- halt.
max([OneItem|[]], OneItem).


max([Num1, Num2|Tail], Max) :- max_between_two(Num1, Num2, PotentialMax), append([PotentialMax], Tail, NewList), max(NewList, Max).
