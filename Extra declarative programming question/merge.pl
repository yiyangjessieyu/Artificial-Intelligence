merge([], ListB, ListB).
merge(ListA [], ListA).

merge([HeadA|TailA], [HeadB|TailB], [HeadA|TailOut]) :- HeadA < HeadB, merge(TailA, [HeadB|TailB], TailOut).
merge([HeadA|TailA], [HeadB|TailB], [HeadB|TailOut]) :- HeadA >= HeadB, merge([HeadA|TailA], TailB, TailOut).
