#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本練習(1)-(3)以 str.format() 格式化輸出

print("(1)")
# (1) 以格式: $ 號填充, 靠右對齊, 最小欄位寬度12 來輸出字串 " is good!"
print("{:$>12}".format(" is good!")) 


print("\n(2)")
# (2) 請讓使用者輸入一個浮點數 a
#     然後對 a 以格式化 : * 填充, 靠右對齊, 最小欄位14, 三位一組, 小數點後5位, 浮點數來輸出
a = float(input("a = "))
print("{:*^14,.5f}".format(a))



print("\n(3)")
# (3) 如果想讓圓周率的倒數(1/math.pi)輸出如下, 該如何格式化輸出?
#     ---31.831%---
import math
print("{:-^13.3%}".format(1/math.pi))



print("\n(4)")
# (4) 下面的程式，讓使用者輸入實數b與c的值，請輸出直線y=bx+c與y軸,x軸的交點
# 此題請使用 *字串插值* 的方式輸出, 輸出交點以格式化方式輸出小數點後2位
b = float(input("b = "))
c = float(input("c = "))
x = -c/b
print(f"y = {b}x + {c} 與 y 軸交點為 (0, {c})")
print(f"y = {b}x + {c} 與 x 軸交點為 ({x:.2f}, 0)")



