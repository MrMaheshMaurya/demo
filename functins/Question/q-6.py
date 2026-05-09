"""
6. Prime Number Function
Check karo number prime hai ya nahi
"""


def prime():
    num = int(input("Enter the your number = "))
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    print(count)

    if count == 2:
        print("prime number")
    else:
        print("not prime number")


prime()
