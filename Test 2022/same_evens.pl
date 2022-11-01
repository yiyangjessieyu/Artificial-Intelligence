same_evens([]).

same_evens([One, Two]).

same_evens([One, Two, Three, Two|Tail]) :- append([Three, Two], Tail, Result),
                                            same_evens(Result).
