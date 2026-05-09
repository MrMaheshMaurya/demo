"""
7. Palindrome Function
String palindrome hai ya nahi
"""


def pilin():
    name = input("enter the you string name = ")
    reverse = name[::-1]
    print(name)
    print(reverse)
    if name == reverse:
        print(f"{name} is a palindrome")
    else:
        print(f"{name} is not a palindrome")


pilin()
