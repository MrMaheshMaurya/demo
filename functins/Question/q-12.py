"""Armstrong Number

Function बनाओ जो Armstrong number check करे।

"""


def armstrong():
    i = int(input("enter the number = "))
    org = i
    sum = 0
    while i > 0:
        sum = sum + (i % 10) * (i % 10) * (i % 10)
        i = i // 10

    if org == sum:
        print("armstrong number")
    else:
        print("not armstrong number")


armstrong()
