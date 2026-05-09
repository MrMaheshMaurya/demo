# def total_marks(hin: int, eng: int, math: int, sst: int, com: int) -> int:
#    return hin + eng + math + sst + com


# t = total_marks(23, 45, 56, 34, 34)
# print(t)


def total_marks(hin: int, eng: int, math: int, sst: int, com: int) -> int:
    return hin + eng + math + sst + com


t = total_marks(23, 45, 56, 34, 34)
print(t)


def calculate(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div


add, sub, mul, div = calculate(20, 34)
print("add is = ", add)
print("sub is = ", sub)
print("mul is = ", mul)
print("div is = ", div)
