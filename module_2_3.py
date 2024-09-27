my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
flag = int(len(my_list))
index_ = 0
while flag >= 0:
    flag = flag - 1
    if my_list[index_] == 0:
        index_ = index_ + 1
        continue
    elif my_list[index_] >= 0:
        print(my_list[index_])
        index_ = index_ + 1
# print('Вышел из цикла')
