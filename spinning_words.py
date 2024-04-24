#method 1
def spin_words(sentence):
    new_sent = []
    words = sentence.split()
    
    for w in words:
        if len(w) >= 5:
            rev_word = w[::-1]
            new_sent.append(rev_word)
        else:
            new_sent.append(w)
        

        
    return ' '.join(new_sent)

#method 2
def spin_words(sentence):
    new_sent = ""
    
    words = sentence.split()
    
    for w in words:
        if len(w) >= 5:
            rev_word = w[::-1]
            new_sent += rev_word + " "
            
        else:
            new_sent += w + " "
        
    return new_sent.strip()
