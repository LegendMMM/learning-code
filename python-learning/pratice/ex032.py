#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 1.001
n = 1
while True:
    if a**n > (n+1)**2:
        break
    n += 1
print(f"當 n={n}, a^{n} > ({n}+1)^2")

a = 0.999
n = 1
while True:
    if a**n < (10)**(-3):
        break
    n += 1
print(f"當 n={n}, a^{n} < 10^(-3)")

N = int(input("請輸入一個正整數 N: "))
sum = 0
i = 1
while i <= N:
    sum += i
    i += 1
print(f"1 到 {N} 之和是 {sum}")