def order_weight(strng):
    if strng.strip() == '':
        return ''

    numbers = strng.split()
    obj_array = []

    for number in numbers:
        total = sum(int(digit) for digit in number)
        obj_array.append((number, total))

    obj_array.sort(key=lambda x: (x[1], x[0]))

    solution = ' '.join(item[0] for item in obj_array)
    return solution
