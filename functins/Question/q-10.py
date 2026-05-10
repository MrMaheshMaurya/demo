"""
Sum of Digits
Number ke sabhi digits ka sum nikalo
"""


def sum():
    num = int(input("enter the number = "))
    sum_digit = 0
    while num > 0:
        sum_digit = sum_digit + num % 10
        num = num // 10

    print(sum_digit)


sum()
