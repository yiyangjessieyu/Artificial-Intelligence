/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

/* Question 5) */
# Recommend is either hard_lenses, soft_lenses, or no_lenses;
# Age will be an integer;
# Astigmatic will be either yes or no (note that these are atoms 'yes' and 'no' not true or false.); and
# Tear_Rate will be a positive integer.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- young(Age), normal_tear_rate(Tear_Rate), Astigmatic = yes, Recommend = hard_lenses.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- young(Age), normal_tear_rate(Tear_Rate), Astigmatic = no, Recommend = soft_lenses.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate), Recommend = no_lenses.


test_answer :-
    diagnosis(hard_lenses, 21, yes, 11),
    writeln('OK').

test_answer2 :-
    diagnosis(X, 45, no, 4),
    writeln(X).

test_answer3 :-
    diagnosis(X, 19, no, 5),
    writeln(X).
