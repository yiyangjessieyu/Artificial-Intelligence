reversed([], []).


% Complete the following
reversed([Head|Tail], Backward) :- reversed(Tail,ReversedTail), 
                                   append(ReversedTail, [Head], Backward).
