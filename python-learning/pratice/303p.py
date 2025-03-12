user_input = input("請輸入一個數字: ")
value = complex(user_input)
if value.imag == 0:
    if value.real.is_integer():
        print(f"{user_input} 是一個整數")
    else:
        print(f"{user_input} 是一個實數")
elif value.real == 0:
    print(f"{user_input} 是一個純虛數")
else:
    print(f"{user_input} 是一個複數")