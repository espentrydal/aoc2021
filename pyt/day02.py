def p1(f):
    x = z = 0                   # z is depth based
    for line in f:
        a, b = line.split()
        b = int(b)
        if a == 'forward':
            x += b
        if a == 'down':
            z += b
        if a == 'up':
            z -= b
    return x*z

def p2(f):
    aim = x = z = 0             # z is depth based
    for line in f:
        a, b = line.split()
        b = int(b)
        if a == 'forward':
            x += b
            z += b*aim
        if a == 'down':
            aim += b
        if a == 'up':
            aim -= b
    return x*z