import import_prolog as p
import statements
import questions
import re
import map_values as m

def processSentence(sentence):

    names = re.findall(r'\b[A-Z][a-z]*\b', sentence)

    if "siblings" in sentence:
        if "." in sentence:
            statements.siblingsStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.siblingsQuestion(names)
            return True
    
    elif "sister" in sentence:
        if "." in sentence:
            statements.sisterStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.sisterQuestion(names)
            return True
    
    elif "mother" in sentence:
        if "." in sentence:
            statements.motherStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.motherQuestion(names)
            return True
        
    elif "parents" in sentence:
        if "." in sentence:
            statements.parentStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.parentsQuestion(names)
            return True
        
    elif "brother" in sentence:
        if "." in sentence:
            statements.brotherStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.brotherQuestion(names)
            return True
        
    elif "father" in sentence:
        if "." in sentence:
            statements.fatherStatement(names)
            return True
        elif "?" in sentence:
            names.pop(0)
            questions.fatherQuestion(names)
            return True
    else:
        return False

if __name__ == "__main__":
    print("Enter a prompt below.")
    sentence = " "
    while (sentence != "quit"):
        sentence = input("\n> ")
        if not processSentence(sentence) and sentence != "quit":
            print("Invalid input given.")