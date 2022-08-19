solution(V1,V2,V3,H1,H2,H3) :-
  word(V1, _, V1XH1, _, V1XH2, _, V1XH3, _),
  word(V2, _, V2XH1, _, V2XH2, _, V2XH3, _),
  word(V3, _, V3XH1, _, V3XH2, _, V3XH3, _),
  word(H1, _, V1XH1, _, V2XH1, _, V3XH1, _),
  word(H2, _, V1XH2, _, V2XH2, _, V3XH2, _),
  word(H3, _, V1XH3, _, V2XH3, _, V3XH3, _).


word(cookies,c,o,o,k,i,e,s).
word(squawks,s,q,u,a,w,k,s).
word(balloon,b,a,l,l,o,o,n).
word(banquet,b,a,n,q,u,e,t).
word(bejewel,b,e,j,e,w,e,l).
word(bloated,b,l,o,a,t,e,d).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!').
