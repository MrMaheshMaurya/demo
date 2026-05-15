# 1 se 10 tak numbers print karo using loop


# for i in range(1, 11):
#     print(i)


# i = 0

# while i < 10:
#     print(i)
#     i = i + 1


n = int(input("enter the your number = "))

i = 1
while i <= 10:
    print(
        i,
        "*",
        n,
        "=",
        i * n,
    )
    i += 1
    print()
