#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 請依註解提示完成程式


# (1) 假設 F 是正整數中小於 100 且是 2 的倍數的集合
#     假設 G 是正整數中小於 100 且是 3 的倍數的集合
#     請用群集集合的概念, 分別列印出下面此四個數出來
#     (a) 小於100的正整數中是2的倍數有幾個?
#     (b) 小於100的正整數中是3的倍數有幾個?
#     (c) 小於100的正整數中是2或3的倍數有幾個?
#     (d) 小於100的正整數中同時是2和3的倍數有幾個?
#     用布林恆等式驗證是否 F聯集G個數 = F個數+G個數-F交集G個數
print("\n(1)\n")
F = {x for x in range(1, 100) if x % 2 == 0}
G = {x for x in range(1, 100) if x % 3 == 0}
print(f"小於100的正整數中是2的倍數有 {len(F)} 個")
print(f"小於100的正整數中是3的倍數有 {len(G)} 個")
print(f"小於100的正整數中是2或3的倍數有 {len(F | G)} 個")
print(f"小於100的正整數中同時是2和3的倍數有 {len(F & G)} 個")
print("布林恆等式驗證：", len(F | G) == len(F) + len(G) - len(F & G))


# (2) 假設有兩個集合 S 與 T, 定義 SxT 是元組(序對)的集合如下
#     SxT = {(s,t)|s在S中, t在T中}
#     如果 S 與 T 的定義如下, 如何才能得到 SxT ?
print("\n(2)\n")
S = {1,2,3}
T = {'do','rei','me','fa','so'}
SxT = {(s, t) for s in S for t in T}
print(f"SxT = {SxT}")


# (3) 威力彩是一種樂透型遊戲，其選號分為兩區，您必須從第1個選號區中的
#     01~38 的號碼中任選6個號碼，並從第2個選號區中的01~08的號碼中任選
#     1個號碼進行投注，這6個+1個號碼即為您的投注號碼。開獎時，開獎單位
#     將從第1區01~38的號碼中隨機開出六個號碼，再從第2區01~08的號碼中隨
#     機開出一個號碼，這一組六個+一個號碼，就是該期威力彩的中獎號碼。
#
#     請利用群集的不重覆特性寫出模擬威力彩的開獎號碼第一區38選6+第二區8選1
print("\n(3)\n")
import random
first_area = set()
while len(first_area) < 6:
    first_area.add(random.randint(1, 38))
second_area = random.choice(list(range(1, 9)))
print("威力彩開獎號碼:")
print("第一區:", sorted(first_area))
print("第二區:", second_area)