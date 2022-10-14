eats(Person, Thing) :- hungry(bob), edible(Thing);
                        hungry(alice), edible(Thing), not(fast_food(Thing)).

edible(fries).
edible(salad).
fast_food(fries).

hungry(bob).
hungry(alice).


test_answer :- eats(alice, fries),
               write('Wrong answer!').

test_answer :- write('OK').
