:- dynamic father/2.
:- dynamic mother/2.
:- dynamic parent/2.
:- dynamic grandfather/2.
:- dynamic grandmother/2.
:- dynamic sister/2.
:- dynamic aunt/2.
:- dynamic brother/2.
:- dynamic uncle/2.
:- dynamic ancestor/2.
:- dynamic male/1.
:- dynamic female/1.

father(X,Y) :-
    male(X),
    parent(X,Y).

assertFather(X,Y) :-
    assertz(male(X)),
    assertz(parent(X,Y)).

mother(X,Y) :- 
    female(X),
    parent(X,Y).

assertMother(X,Y) :-
    assertz(female(X)),
    assertz(parent(X,Y)).

grandfather(X,Y) :-
    male(X),
    parent(X,Z),
    parent(Z,Y).

assertGrandfather(X,Y) :-
    assertz(male(X)),
    assertz(parent(X,Z)).

grandmother(X,Y) :- 
    female(X),
    parent(X,Z),
    parent(Z,Y).

assertGrandmother(X,Y) :-
    assertz(female(X)),
    assertz(parent(X,Z)).

siblings(X,Y) :-
    siblings(Y,X).

assertSiblings(X,Y) :-
    assertz(siblings(Y,X)),
    assertz(siblings(X,Y)).

sister(X,Y) :- 
    female(X),
    father(F, Y),
    father(F, X),
    mother(M, Y),
    mother(M,X),
    X \= Y.

assertSister(X,Y) :-
    assertz(female(X)),
    assertz(father(F,Y)),
    assertz(father(F,X)),
    assertz(mother(M,Y)),
    assertz(mother(M,X)),
    assertz(siblings(X,Y)).

brother(X,Y) :- 
    male(X),
    father(F,Y),
    father(F,X),
    X \= Y.

brother(X,Y) :-
    male(X),
    mother(M,Y),
    mother(M,X),
    X \= Y.
    
assertBrother(X,Y) :-
    assertz(male(X)),
    assertz(father(F,Y)),
    assertz(father(F,X)),
    assertz(mother(M,Y)),
    assertz(mother(M,X)),
    assertz(siblings(X,Y)).

