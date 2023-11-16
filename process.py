from pyswip import Prolog
import format as f

prolog = Prolog()
prolog.consult("knowledge_base.pl")
family_keywords = f.read_keywords("familyKeywords.txt")

def process_prompt(prompt):

    # TO-DO: 
    #   not all invalid statements are considered invalid
    #   same names are not considered to be invalid
    
    if '.' in prompt:
        formatted = f.format_sentence(prompt)
        process_statement(formatted)
    elif '?' in prompt:
        formatted = f.format_sentence(prompt)
        process_query(formatted)
    else: 
        print("Invalid") 

    print()

def process_statement(statement):

    # checks for relationship and converts it to prolog assertz statement
    for keyword in family_keywords:
        if keyword.lower() in statement.lower():
            assert_statement = f.to_prolog_statement(keyword, statement)
            break
    
    prolog.assertz(assert_statement)

def process_query(query): # to-do
    print("QUERY") 


