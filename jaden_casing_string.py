def to_jaden_case(string):
    words = string.split()  
    jaden_case_words = []  
    for word in words:
        jaden_case_words.append(word.capitalize())  
    jaden_case_string = ' '.join(jaden_case_words)  
    return jaden_case_string
