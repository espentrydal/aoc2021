def p1(entries):
    x = z = 0                   # z is depth based
    for entry in entries:
        a = entry[0]
        b = int(entry[1])
        if a == 'forward':
            x += b
        if a == 'down':
            z += b
        if a == 'up':
            z -= b
    return x*z


def p2(entries):
    aim = x = z = 0             # z is depth based
    for entry in entries:
        a = entry[0]
        b = int(entry[1])
        if a == 'forward':
            x += b
            z += b*aim
        if a == 'down':
            aim += b
        if a == 'up':
            aim -= b
    return x*z
