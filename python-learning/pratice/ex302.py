num1 = input("輸入第一個數字: ")
num2 = input("輸入第二個數字: ")
num1 = int(num1)
num2 = int(num2)
real_num1 = num1
real_num2 = num2

temp = 0
# 84
#36
while True:
    temp = num1 % num2
    if temp == 0:
        break
    num1 = num2
    num2 = temp
print(f"{real_num1}與{real_num2}的最大公因數是 {num2}")