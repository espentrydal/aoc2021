from __future__ import annotations
#from collections import Counter, defaultdict, namedtuple, deque
from typing import *

input_type = str
cat = ''.join

def common(strs, i) -> Char:    # '1' or '0'
    """Returns the most common bit in position i in strs."""
    bits = [s[i] for s in strs]
    return '1' if bits.count('1') >= bits.count('0') else '0'

def uncommon(strs, i) -> Char:    # '1' or '0'
    """Returns the least common bit in position i in strs."""
    return '1' if common(strs, i) == '0' else '0'

def epsilon(strs) -> str:
    """The bit string formed from most common bit at each position."""
    return cat(common(strs, i) for i in range(len(strs[0])))

def gamma(strs) -> str:
    """The bit string formed from most uncommon bit at each position."""
    return cat(uncommon(strs, i) for i in range(len(strs[0])))

def power(strs) -> int: 
    """Product of epsilon and gamma rates."""
    return int(epsilon(strs), 2) * int(gamma(strs), 2)

def p1(entries):
    return power(entries)