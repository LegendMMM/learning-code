#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 作業 hw0201
# 學號 41340116S
# 姓名 林景堯

# 以下程式開始

name = input("請輸入姓名：")
score1 = float(input("請輸入儀器分析成績："))
score2 = float(input("請輸入有機特論成績："))
score3 = float(input("請輸入溶液論成績："))
score4 = float(input("請輸入工業化學成績："))
score5 = float(input("請輸入分子模擬成績："))
average_score = (score1 + score2 + score3 + score4 + score5) / 5
print(f"{name} 的平均成績為: {average_score}")
