def main():
    dictionary = {}
    while True:
        user_input = input("請輸入英文:中文字典翻譯字彙(輸入0:0結束) -> ")
        if user_input == "0:0":
            break
        if ":" in user_input:
            en, zh = user_input.split(":", 1)
            dictionary[en] = zh
    if dictionary:
        max_len = max(len(k) for k in dictionary.keys())
        for en, zh in dictionary.items():
            print(f"{en.rjust(max_len)} | {zh}")

# main
if __name__ == "__main__":
    main()