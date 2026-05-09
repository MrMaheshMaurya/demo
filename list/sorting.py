# my_list = [12, 45, 3, 76, 38]
# # my_list.sort()
# x = sorted(my_list)
# print(x)
# print(my_list)


def func(x):
    return x[1]


my_list1 = [[1, 3, 772], [32, 78, 7], [56, 44, 23], [32, 44, 99]]  # uniform list

# my_list1.sort(key=lambda x: x[1])
my_list1.sort(key=func)

print(my_list1)
