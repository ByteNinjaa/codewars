def maskify(cc):
    if len(cc) < 4:
        return cc
    
    cc = ("#" * (len(cc) - 4)) + cc[-4:]    
    return cc
