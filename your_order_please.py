#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

import re

def order(sentence):
    if sentence == "":
        return ""
    
    sent_split = sentence.split()
    sent_dict = {key: None for key in range(1, len(sent_split)+1)}
    for word in sent_split:
        num = re.findall('\d+', word)
        sent_dict[int(num[0])] = word
        final_sent = ' '.join(str(s) for s in sent_dict.values())
        
    return final_sent
        
