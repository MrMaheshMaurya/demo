"""
4. Maximum Number Function
3 numbers me se bada number return karo.
"""


def max_num():
    num1 = int(input("enter first number = "))
    num2 = int(input("enter second number = "))
    num3 = int(input("enter third number = "))
    if num1 > num2 and num1 > num3:
        print("num1 number is maximum")
    elif num2 > num3 and num2 > num1:
        print("num2 number is maximum")
    else:
        print("num3 number is maximum")


max_num()
