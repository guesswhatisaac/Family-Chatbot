import re

def read_keywords(file_path):

    my_file = open(file_path, "r") 
    data = my_file.read()
    keywords = data.split("\n")
    # print("KW" + keywords)
    my_file.close()

    return keywords

def remove_keywords(sentence, keywords):

    words = re.findall(r'\b\w+\b', sentence)
    filtered_words = []

    # remove keywords in sentence and append to list
    for word in words:
        if word.lower() not in keywords:
            filtered_words.append(word)

    modified_sentence = ' '.join(filtered_words)

    # print("FORMATTED: " + modified_sentence)
    return modified_sentence

def format_sentence(sentence):

    path = "removedKeywords.txt"
    keywords = read_keywords(path)
    output_sentence = remove_keywords(sentence, keywords)

    # print("OUTPUT: " + output_sentence)
    return output_sentence

def to_prolog_statement(family_keyword, statement): # to-do
    
    prolog = ""
    names = []

    words = statement.split()
    words = [word.lower() for word in words]
    for word in words:
        if word not in family_keyword:
            names.append(word)

    if family_keyword == "siblings":
        prolog += "siblings(" + ','.join(names) + ")"

    print(prolog)
    return prolog
    
def to_prolog_query(family_keyword): # to-do
    print("! TODO !")