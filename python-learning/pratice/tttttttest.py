list = input("Input numbers (integers) list to sort:" )
list = list[1:-1].split(",")
sorting_list = []
sorted_list = []
while True:
        try:
            for i in list:
                sorting_list.append(int(i))
            break
        except ValueError:
            print("Please input integers.")
            list = input("Input numbers (integers) list to sort:" )
            list = list[1:-1].split(",")
            continue
l = len(sorting_list)
print(sorted_list , " | " , sorting_list)
for j in range(l):   
    for i in range(len(sorting_list)-1):
        if sorting_list[-i-2] > sorting_list[-i-1]:
            sorting_list[-i-2],sorting_list[-i-1] = sorting_list[-i-1],sorting_list[-i-2]
    sorted_list.append(sorting_list[0])
    sorting_list.pop(0)
    print(sorted_list , "|" , sorting_list)
print("----------------------------")
print("After sorted:")
print(sorted_list)