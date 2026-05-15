# """
# *
# **
# ***
# ****
# """

# for i in range(1, 6):
#     for j in range(0, i):
#         print("*", end=" ")
#     print(" ")
# print()

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(1, 6):
#     for j in range(0, 5):
#         print("*", end=" ")
#     print()
# print()


"""
* * * * *
* * * *
* * *
* *
*
"""
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     print()
# print()


"""
          *
        * *
      * * *
    * * * *
  * * * * *
"""
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print(" ", end=" ")

#     for k in range((5 + 1) - i):
#         print("*", end=" ")
#     print()
# print()


"""
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
"""

# for i in range(0, 4):
#     for j in range(4):
#         print("1", end=" ")
#     print()
# print()


"""
1
1 2
1 2 3
1 2 3 4
"""

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print()


"""
1
2 2
3 3 3
4 4 4 4
"""

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()
# print()


"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


"""
        *
      * *
    * * *
  * * * *
* * * * *
"""


# for i in range(1, 6):

#     for j in range(1, 6 - i):
#         print(" ", end=" ")

#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()


"""
        *
      * * *
    * * * * *
  * * * * * * *
"""

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     for l in range(1, i):
#         print("*", end=" ")
#     for h in range(1, 6 - i):
#         print(" ", end=" ")
#     print()


"""
* * * * * * *
  * * * * *
    * * *
      *
"""

# for i in range(1, 5):

#     for j in range(1, i):
#         print(" ", end=" ")

#     for j in range(1, 6 - i):
#         print("*", end=" ")

#     for k in range(1, 5 - i):
#         print("*", end=" ")

#     for l in range(1, i):
#         print(" ", end=" ")
#     print()


"""
    *
   * *
  * * *
 * * * *
  * * *
   * *
    *
"""

for i in range(1, 5):
    for j in range(1, 5 - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(3, 0, -1):
    for j in range(1, 5 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(3, 0, -1):

    for j in range(1, 5 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print("*", end=" ")

    print()

# Upper Part
for i in range(1, 5):

    for j in range(1, 5 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print("*", end=" ")

    print()


# Lower Part
for i in range(3, 0, -1):

    for j in range(1, 5 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print("*", end=" ")

    print()
