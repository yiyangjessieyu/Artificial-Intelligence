eats(Person, Food) :- likes(Person, Food). # Rules
eats(Person, Food) :- hungry(Person), edible(Food). # Rules

likes(bob, chocolate).
hungry(alice).

test_answer :- eats(bob, chocolate),
               writeln('Bob eats chocolate.').
