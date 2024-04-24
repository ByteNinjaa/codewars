def is_isogram(string):    
    string = string.lower()
    for b in string:
        c = string.count(b)
        if c >= 2:
            return False
    return True
