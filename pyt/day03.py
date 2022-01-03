import struct


def p1(f):
    for line in f:
        message = struct.unpack('iii', bytearray(int(line)))
        c = -1
        while message:
            message &= message-1
            c += 1
        print(c)
    return 0
