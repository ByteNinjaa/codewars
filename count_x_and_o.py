def xo(s):
    s = s.lower()  # Convert the string to lowercase for case insensitivity
    count_x = s.count('x')  # Count the number of 'x's
    count_o = s.count('o')  # Count the number of 'o's
    return count_x == count_o 
