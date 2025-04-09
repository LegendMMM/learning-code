#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (1) 建造 trans 字典: 簡體字 : 繁體字
trans = {
    "守护": "守護",
    "丢弃": "丟棄",
    "回忆": "回憶"
}

# (2) 這句簡體字的句子
word = "守护你是我最后的希望,束缚着的是思念,丢弃的是无奈,最后我会留下一个圈摆放你我的回忆,直到我也干枯,你也远去!"
print(word)
trans["最后"] = "最後"
trans["束缚"] = "束縛"
trans["着"]   = "著"
trans["无奈"] = "無奈"
trans["会"]   = "會"
trans["摆"]   = "擺"
trans["干枯"] = "乾枯"
trans["远去"] = "遠去"
trans["个"]   = "個"

print("------------------------------------------------------------")
# (3) 列出 trans 所有的 key
for k in trans:
    print(k, end=" ")
print()

print("------------------------------------------------------------")
# (4) 列出 trans 所有的 value 值
for v in trans.values():
    print(v, end=" ")
print()

print("------------------------------------------------------------")
# (5) 利用 trans 將 word 翻譯成繁體字用語
word_fixed = ""
i = 0
while i < len(word):
    replaced = False
    for k in trans:
        if word[i:i+len(k)] == k:
            word_fixed += trans[k]  
            i += len(k)             
            replaced = True
            break
    if not replaced:
        word_fixed += word[i]  
        i += 1

print(word_fixed)