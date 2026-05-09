# from typing import List

my_list1: list[int] = [23, 45, 33, 56]
my_list: list[int | str] = [23, 45, 33, 56]

my_list.extend(["mahesh", 12])
print(my_list)
my_list1.append(12)
print(my_list1)
