%5%
%a

% isElemInArr(L1L2..Ln, E) = false, if []
%                            true, if L1=E
%                            isElemInArr(L2..Ln, E), otherwise

% flow model: (i,i)

isElemInArr([], _):- false.
isElemInArr([H|_], E):-
    H=E.
isElemInArr([_|T], E):-
    isElemInArr(T, E).

% union(L1L2..Ln, l1l2..lm, col) =
% L1L2..Ln, if l=[]
% col, if L=[]
%union(L2..Ln, l1l2..lm, col U L1), if L1 \E l
%union(L2..Ln, l1l2..lm, col), otherwise

% union(L - list, l - list, col-list, R - list) (i,i,i,o), (i,i,i,i)

unionC(LL, [], _, LL).
unionC([],_,C, C).
unionC([H|T], L, C, R):-
    \+ isElemInArr(L, H),
    unionC(T, L, [H|C], R).
unionC([_|T], L, C, R):-
    unionC(T, L, C, R).

%mainUnionC(LL-list, L-list, R-list) (i,i,i) (i,i,o)
mainUnionC(LL, L, R):-
    unionC(LL, L, L, R).




%b

% twoPairsC(E, L1L2..Ln, col) = col, L=[]
%                               twoPairsC(E, L2..Ln, [E, L1] U col),
%                               otherwise

% twoPairsC(E-element, L-list, col-list of lists, R-list of lists)
% (i,i,i,o) (i,i,i,i)

twoPairsC(E, [], C, C).
twoPairsC(E, [H|T],C, R):-
    twoPairsC(E, T, [[E,H]|C], R).

%twoPairs(E - number, L-list, R-list of list) (i,i,o) (i,i,i)

twoPairs(E, L, R):-
    twoPairsC(E, L, [], R).

%setPairsC(L1L2.Ln, col) =
%col, L=[]
%setPairsC(L2..Ln, col U twoPairs(L1, L2..Ln), otherwise

%setPairsC(L-list, C-list, R-list) (i,i,o) (i,i,i)

setPairsC([], C, C).

setPairsC([H|T], C, R):-
    twoPairs(H, T, New_pairs),
    mainUnionC(New_pairs, C, New_C),
    setPairsC(T, New_C, R).


% setPairs(L-list, R-list of lists)
% flow model: (i,o), (i, i)
setPairs(L, R):-
    setPairsC(L, [], R).



