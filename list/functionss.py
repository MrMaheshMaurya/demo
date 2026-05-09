from typing import List


def func(lst: List[int]):
    print(f"inside func = {lst}")
    print(f"ID of lst = {id(lst)}")
    lst.append(100)
    print(f"After the appending lst = {lst}")


list1 = [23, 84, 83, 98, 45]
print(f"Id of list1 = {id (list1)}")
func(list1)
print(f"Outside func={list1}")
# pass by refrence
