# list1 = [23, 4, 67, 34, 21, 22]

# list2 = list1
# print(id(list1))
# print(id(list2))

# list1.append(100)
# print(f"list1 = {list1}")
# print(f"list2 = {list2}")

list1 = [23, 4, 67, [1, 2, 3, 4], 34, 21, 22]  # coppy

list2 = list1.copy()  # shallow  copy | bahar bahar se change kre
print(id(list1))
print(id(list2))
print("-------")
# print(id(list2))
print(id(list1[3][2]))
print(id(list2[3][2]))


list1[3][2] = 100
print(f"list1 = {list1}")
print(f"list2 = {list2}")

from copy import deepcopy

list1 = [23, 4, 67, [1, 2, 3, 4], 34, 21, 22]  # deep copy | ander se bhi change kr de

list2 = deepcopy(list1)
print(id(list1))
print(id(list2))
print("-------")
# print(id(list2))
print(id(list1[3][2]))
print(id(list2[3][2]))


list1[3][2] = 100
print(f"list1 = {list1}")
print(f"list2 = {list2}")
