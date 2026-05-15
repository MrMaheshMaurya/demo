"""
digits ka sum of qube krne ka funtion bnao
"""


def digit_qube():
    i = int(input("enter your number = "))
    sum = 0
    while i > 0:
        sum = sum + (i % 10) * (i % 10) * (i % 10)
        i = i // 10
    print(sum)


digit_qube()
