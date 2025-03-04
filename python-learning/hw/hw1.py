# hw_example.py

# 1. 輸入學生姓名
name = input("請輸入學生姓名：")

# 2. 輸入筆試分數 (轉成 float 以便處理小數)
test_score = float(input("請輸入筆試分數："))

# 3. 輸入行動分數 (轉成 float 以便處理小數)
action_score = float(input("請輸入行動分數："))

# 4. 計算平均分數
average_score = (test_score + action_score) / 2

# 5. 將三項分數及平均分數顯示在一行
print(f"{name} 的筆試分數: {test_score}, 行動分數: {action_score}, 平均成績為: {average_score}")