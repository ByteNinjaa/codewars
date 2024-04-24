def number(bus_stops):
    t = 0
    for i in bus_stops:
        t += i[0]
        t -= i[1]
        
    return t
