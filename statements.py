import import_prolog as p
import map_values as m

def siblingsStatement(names):

    p.prolog.assertz("def_sibling(" + names[0].lower() + ", " + names[1].lower() + ")")

    if m.map["parents"] == True:
        p.prolog.assertz("not_sibling_parent(X, Y) :- not(parent(X, Y)), not(parent(Y, X))")
        parent_sibling = list(p.prolog.query("not_sibling_parent(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not parent_sibling:
            print("That's impossible!")
            return

    if m.map["siblings"] == False:
        p.prolog.assertz("sibling(X, Y) :- def_sibling(X, Y); def_sibling(Y, X)")
        m.map["siblings"] = True

    print("OK! I learned something.")


def sisterStatement(names):

    p.prolog.assertz("def_sister(" + names[0].lower() + ", " + names[1].lower() + ")")
    p.prolog.assertz("female(" + names[0].lower() + ")")
    m.map["isFemale"] = True

    if m.map["parents"] == True:
        p.prolog.assertz("not_sibling_parent(X, Y) :- not(parent(X, Y)), not(parent(Y, X))")
        parent_sibling = list(p.prolog.query("not_sibling_parent(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not parent_sibling:
            print("That's impossible!")
            return
        
    if m.map["sister"] == False:
        p.prolog.assertz("sister(X, Y) :- female(X), def_sister(X, Y)")
        p.prolog.assertz("sibling(X, Y) :- sister(X, Y)")
        p.prolog.assertz("sibling(Y, X) :- sister(X, Y)")
        m.map["sister"] = True
        m.map["siblings"] = True

    print("OK! I learned something.")


def motherStatement(names):

    p.prolog.assertz("def_mother(" + names[0].lower() + ", " + names[1].lower() + ")")
    p.prolog.assertz("female(" + names[0].lower() + ")")
    m.map["isFemale"] = True

    if m.map["siblings"] == True: 
        p.prolog.assertz("not_mother_sibling(X, Y) :- not(sibling(X, Y))")
        mother_sibling = list(p.prolog.query("not_mother_sibling(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not mother_sibling:
            print("That's impossible!")
            return
        
    if m.map["isMale"] == True:
        p.prolog.assertz("not_male(X) :- not(male(X))")
        mother_female = list(p.prolog.query("not_male(" + names[0].lower() + ")"))
        if not mother_female:
            print("That's impossible!")
            return

    if m.map["mother"] == False:
        p.prolog.assertz("mother(X, Y) :- female(X), def_mother(X, Y)")
        p.prolog.assertz("parent(X, Y) :- mother(X, Y)")
        m.map["mother"] = True
        m.map["parents"] = True

    print("OK! I learned something.")


def parentStatement(names):

    p.prolog.assertz("def_parent(" + names[0].lower() + ", " + names[2].lower() + ")")
    p.prolog.assertz("def_parent(" + names[1].lower() + ", " + names[2].lower() + ")")

    if m.map["siblings"] == True:
        p.prolog.assertz("not_parent_sibling(X, Y) :- not(sibling(X, Y))")
        sibling_parent = list(p.prolog.query("not_parent_sibling(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not sibling_parent:
            print("That's impossible!")
            return

    if m.map["parents"] == False:
        p.prolog.assertz("parent(X, Y) :- def_parent(X, Y)")
        m.map["parents"] = True
    
    print("OK! I learned something.")


def brotherStatement(names):

    p.prolog.assertz("def_brother(" + names[0].lower() + ", " + names[1].lower() + ")")
    p.prolog.assertz("male(" + names[0].lower() + ")")
    m.map["isMale"] = True

    if m.map["parents"] == True:
        p.prolog.assertz("not_sibling_parent(X, Y) :- not(parent(X, Y)), not(parent(Y, X))")
        parent_sibling = list(p.prolog.query("not_sibling_parent(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not parent_sibling:
            print("That's impossible!")
            return
        
    if m.map["brother"] == False:
        p.prolog.assertz("brother(X, Y) :- male(X), def_brother(X, Y)")
        p.prolog.assertz("sibling(X, Y) :- brother(X, Y)")
        p.prolog.assertz("sibling(Y, X) :- brother(X, Y)")
        m.map["brother"] = True
        m.map["siblings"] = True

    print("OK! I learned something.")

def fatherStatement(names):

    p.prolog.assertz("def_father(" + names[0].lower() + ", " + names[1].lower() + ")")
    p.prolog.assertz("male(" + names[0].lower() + ")")
    m.map["isMale"] = True

    if m.map["siblings"] == True: 
        p.prolog.assertz("not_father_sibling(X, Y) :- not(sibling(X, Y))")
        father_sibling = list(p.prolog.query("not_father_sibling(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if not father_sibling:
            print("That's impossible!")
            return
        
    if m.map["father"] == False:
        p.prolog.assertz("father(X, Y) :- male(X), def_father(X, Y)")
        p.prolog.assertz("parent(X, Y) :- father(X, Y)")
        m.map["father"] = True
        m.map["parents"] = True
    
    print("OK! I learned something.")