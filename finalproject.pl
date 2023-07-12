seasonAll(fall, [cs15, cs17, cs141, cs126]).
seasonAll(spring, [cs16, cs18, cs22, cs32, cs166]).

season(Term, Class) :-
    seasonAll(Term, Classes),
    member(Class, Classes).

levelAll(intro, [cs15, cs17, cs16, cs18]).
levelAll(intermediate, [cs33, cs32, cs22]).
levelAll(upper, [cs141, cs166, cs126]).

level(Difficulty, Class) :-
    levelAll(Difficulty, Classes),
    member(Class, Classes).

before(cs16, cs15).
before(cs18, cs17).
beforeAll(cs33, [cs16, cs18]).
beforeAll(cs32, [cs16, cs18]).
before(cs22, none).
beforeAll(cs141, [cs16, cs18, cs22]).
before(cs166, cs33).
beforeAll(cs126, [cs22, cs32]).
beforeAll(none, [cs15, cs17, cs22]).

before(Class, Prereq) :-
    beforeAll(Class, Prereqs),
    member(Prereq, Prereqs).

studentAll(mark, [cs15, cs16, cs17, cs18, cs32]).
studentAll(elon, [cs15, cs16, cs17, cs22, cs141, cs33, cs166]).
studentAll(sherylsandberg, [cs15, cs17, cs16, cs18, cs33, cs32, cs22]).
studentAll(jeffbezos, [cs15, cs17, cs16, cs18, cs33, cs22, cs141, cs166]).

student(Name, Class) :-
    studentAll(Name, Classes),
    member(Class, Classes).

fall(Class) :-
    season(fall, Class).

spring(Class) :-
    season(spring, Class).

has_prereqs(Class, Prereq) :-
    before(Class, Prereq).

no_prereqs(Class) :-
    before(none, Class).

intro(Class) :-
    level(intro, Class).

intermediate(Class) :-
    level(intermediate, Class).

upper_level(Class) :-
    level(upper, Class).

has_taken(Name, Class) :-
    student(Name, Class).

doublereq(Name, Class) :-
    (has_taken(Name, cs22),
    has_taken(Name, cs32),
    Class == cs126);
    (has_taken(Name, cs22),
    (has_taken(Name, cs16);
    has_taken(Name, cs18)),
    Class == cs141).

can_take(Name, Class) :-
    no_prereqs(Class);
    doublereq(Name, Class);
    (has_prereqs(Class, Prereq),
    has_taken(Name, Prereq),
    Class \== cs126,
    Class \== cs141).