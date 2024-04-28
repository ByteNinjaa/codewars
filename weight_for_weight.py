def order_weight(strng):
    if strng.strip() == '':
        return ''

    numbers = strng.split()
    obj_array = []

    for number in numbers:
        num = list(number)
        total = sum(int(digit) for digit in num)

        obj_array.append({'number': number, 'weight': str(total)})
        
    def sort_key(item):
        print(item)
        return (int(item['weight']), item['number'])

    obj_array.sort(key=sort_key)

    results = [item['number'] for item in obj_array]

    solution = ' '.join(results)
    return solution
