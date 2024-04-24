def pig_it(text):
    new_text = ""
    split_text = text.split()
    for word in split_text:
        new_text += word[1:] + word[:1]  + "ay "
        
    return new_text.strip()
