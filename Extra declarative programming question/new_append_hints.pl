% See the lecture notes.
% Write the base case (complete the following)
new_append(  , B , B).

% Complete the following
new_append([X | Xs], B, [X|XsB]) :- new_append(Xs , B ,XsB ). 
