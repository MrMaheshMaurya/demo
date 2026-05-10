"""
3. Even Odd Function
Function check kare number even hai ya odd.
"""


def even_odd():
    num = int(input("Enter your number ="))
    if num % 2 == 0:
        print(f"{num} = Even number ")
    else:
        print(f"{num} = Odd number ")


even_odd()
