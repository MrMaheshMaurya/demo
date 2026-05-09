# 1 se N tak me kitne numbers 7 se divisible hain


# n = int(input("please Enter the your input number = "))

# for i in range(1, n + 1):
#     if i % 7 == 0:
#         print(i)


n = int(input("please Enter the your input number = "))
i = 0

while i < n:
    if i % 7 == 0:
        print(i)
    i += 1
