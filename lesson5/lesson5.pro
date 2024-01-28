% male(egor).
% male(vasiliy).
% male(ivan).
% male(foma).
% female(ekaterina).
% female(sofya).
% female(maria).

% parent(ivan, vasiliy).
% parent(ivan, maria).
% parent(egor, sofya).
% parent(egor, ivan).
% parent(sofya, ekaterina).
% parent(sofya, foma).


% father(X, Y):- parent(X, Y), male(Y).
% mother(X, Y):- parent(X, Y), female(Y).

% grandfather(X, Z):- parent(X, Y), father(Y, Z).
% grandmother(X, Z):- parent(X, Y), mother(X, Z).


% houses(Hs, 5) :-
%     length(Hs, 5),
%     member(h(english,_,_,_,red), Hs),
%     member(h(spanish,dog,_,_,_), Hs),
%     member(h(_,_,_,coffee,green), Hs),
%     member(h(ukrainian,_,_,tea,_), Hs),
%     next(h(_,_,_,_,green), h(_,_,_,_,white), Hs),
%     member(h(_,snail,oldgold,_,_), Hs),
%     member(h(_,_,kool,_,yellow), Hs),
%     Hs = [_, _, h(_, _, _, milk, _), _, _],
%     Hs = [h(norwegian, _, _, _, _)| _],
%     next(h(_,fox,_,_,_), h(_,_,chesterfield,_,_), Hs),
%     next(h(_,_,kool,_,_), h(_,horse,_,_,_), Hs),
%     member(h(_,_,lucky,juice,_), Hs),
%     member(h(japanese,_,parliament,_,_), Hs),
%     next(h(norwegian,_,_,_,_), h(_,_,_,_,blue), Hs),
%     member(h(_, zebra,_,_,_), Hs),
%     member(h(_,_,_,water,_), Hs).


% next(A, B, Ls) :- append(_, [A,B|_], Ls).
% next(A, B, Ls) :- append(_, [B,A|_], Ls).
    

% zebra_owner(Owner) :-
%     houses(Hs),
%     member(h(Owner,zebra,_,_,_), Hs).   


palindrome(List) :-
    reverse(List, List).

% palindrome([1,2,3,2,1]).
% palindrome([10,35,40]).