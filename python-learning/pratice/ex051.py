#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (1) 建造一個 factorial 函式 (不准使用內建 math.factorial)，且引數 n 預設值為 1
def factorial(n=1):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# (2) 用 for 迴圈及 factorial 列印 1!, 2! ... 10! 的結果
for i in range(1, 11):
    print(f"{i}!={factorial(i)}")

print("---------------------------")

# (3) 建造可輸入任何數目引數的函式 maxnumber，傳回值為這些引數的最大值
#     這裡可直接使用 Python 內建函式 max() 來取最大值
def maxnumber(*args):
    return max(args)

print(f"max = {maxnumber(3.14,-100,1,-6,8,12,2024)}")
print("---------------------------")

# (4) 已知一數清單 lst，請用 maxnumber 列印其中的最大數
lst = [3.14, -100, 1, -6, 8, 12, 2024]
print(f"max = {maxnumber(*lst)}")
print("---------------------------")

# (5) 使用 lambda 語法建造 area 函式來算圓面積 (pi*r^2)，若 r <= 0，則回傳 0
import math
area = lambda r: (math.pi * r**2) if r > 0 else 0

print(f"r = 5, area of circle = {area(5):.2f}")
print(f"r = -2, area of circle = {area(-2):.2f}")