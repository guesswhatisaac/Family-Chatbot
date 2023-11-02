import import_prolog as p
import map_values as m

def siblingsQuestion(names):

    if m.map["siblings"] == True:
        result = list(p.prolog.query("sibling(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if result:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")

def sisterQuestion(names):

    if m.map["sister"] == True:
        result = list(p.prolog.query("sister(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if result:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")

def motherQuestion(names):
    
    if m.map["mother"] == True:
        result = list(p.prolog.query("mother(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if result:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")

def parentsQuestion(names):

    if m.map["parents"] == True:
        result = list(p.prolog.query("parent(" + names[0].lower() + ", " + names[2].lower() + ")"))
        result2 = list(p.prolog.query("parent(" + names[1].lower() + ", " + names[2].lower() + ")"))
        if result and result2:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")

def brotherQuestion(names):
    
    if m.map["brother"] == True:
        result = list(p.prolog.query("brother(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if result:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")

def fatherQuestion(names):

    if m.map["father"] == True:
        result = list(p.prolog.query("father(" + names[0].lower() + ", " + names[1].lower() + ")"))
        if result:
            print("Yes!")
        else:
            print("No!")
    else:
        print("No!")