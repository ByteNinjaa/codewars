def find_it(seq):
    for i in seq:
        c = seq.count(i)
        if c % 2 == 0:
            pass
        else:
            return i
