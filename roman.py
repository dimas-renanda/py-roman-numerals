#!/usr/bin/env python3
"""Convert integers ↔ Roman numerals."""
import sys, re

VALS = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def to_roman(n):
    if not 1 <= n <= 3999: raise ValueError(f"Out of range: {n}")
    r = ''
    for val, sym in VALS:
        while n >= val: r += sym; n -= val
    return r

def from_roman(s):
    s = s.upper()
    if not re.match(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', s):
        raise ValueError(f"Invalid Roman numeral: {s}")
    m = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i, c in enumerate(s):
        if i+1 < len(s) and m[c] < m[s[i+1]]: total -= m[c]
        else: total += m[c]
    return total

for arg in sys.argv[1:]:
    try:
        try: n = int(arg); print(f"  {arg} → {to_roman(n)}")
        except ValueError: print(f"  {arg} → {from_roman(arg)}")
    except Exception as e: print(f"  Error: {e}")
