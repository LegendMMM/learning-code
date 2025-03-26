#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 請依註解提示完成程式

# 請由下列元組中用切片運算符取出 "who" 並列印出來 
a = 1, "yes", (0.3, 2, "no", 68.2, ("who", "u two", 23), (3,4)), "where"
print(a[2][4][0])


# 下面 b 是小學一年五班學生名單的元組
# 這學期來了個轉學生小噹, 想把它插在小安跟小雄中間, 要怎麼做?
# 請列印出來
b = "小明", "小華", "小惠", "小福", "小安", "小雄", "小強"
b = b[:5] + ("小噹",) + b[5:]
print(b)

# 想造一個名為 Score 的具名元組型態, 用來存學生成績, 欄位如下 :
# name=姓名, math=數學, eng=英語, chi=國語,
# 請用 collections.namedtuple 來宣告這個 Score 型態
import collections
Score = collections.namedtuple("Score", ["name", "math", "eng", "chi"])


# 指定兩筆成績 :
# 姓名 數學 英語 國語
# -----------------
# 大明  60  78  55
# 佳佳  88  62  74
# 請模仿投影片用 data 儲存這兩筆資料成為 Score 元組
data = [Score("大明", 60, 78, 55), Score("佳佳", 88, 62, 74)]


# 請用 for...in 算出這三科的平均成績, 小數點取兩位
sum = 0
for i in data:
    sum += i.math
math_avg = sum / len(data)
sum = 0
for i in data:
    sum += i.eng
eng_avg = sum / len(data)
sum = 0
for i in data:
    sum += i.chi
chi_avg = sum / len(data)
print(f"數學平均為: {math_avg:.2f}")
print(f"英語平均為: {eng_avg:.2f}")
print(f"國語平均為: {chi_avg:.2f}")

