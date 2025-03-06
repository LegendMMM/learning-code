#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print(f"{a}, {b}, {c} 三邊形成的三角形不成立")
elif a**2 + b**2 == c**2:
    print(f"{a}, {b}, {c} 三邊形成的三角形是直角三角形")
elif a**2 + b**2 > c**2:
    print(f"{a}, {b}, {c} 三邊形成的三角形是銳角三角形")
elif a**2 + b**2 < c**2:
    print(f"{a}, {b}, {c} 三邊形成的三角形是鈍角三角形")
else:
    print(f"{a}, {b}, {c} 三邊形成的三角形不成立")
