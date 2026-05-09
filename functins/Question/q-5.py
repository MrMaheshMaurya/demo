"""
5. Factorial Function
Number ka factorial find karo using function.
"""


def fact():
    num = int(input("enter the your input = "))
    factorial = 1
    for i in range(num, 0, -1):
        factorial = factorial * i
    print(factorial)


fact()
