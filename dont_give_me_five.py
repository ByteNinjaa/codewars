def dont_give_me_five(start,end):
    l = []
    for i in range(start, end+1):
        i_str = str(i)
        if "5" not in i_str:
            l.append(i_str)


    return len(l)   # amount of numberz
