"""
1
12
123
1234
"""

# for i in range(1, 5):
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     print(" ")

"""
1
22
333
4444
55555
666666
7777777
"""
n = 7

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="-")
    print("")
