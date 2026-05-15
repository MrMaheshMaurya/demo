"""
Pattern with Functions
Function बनाओ जो pattern print करे।
"""

# def pattern():
#     num = 5
#     for i in range(0, num + 1):
#         for j in range(0, i):
#             print("*", end=" ")
#         print()


def pattern():
    num = 5
    for i in range(0, num + 1):
        for j in range(0, i):
            print("*", end=" ")
        print()


pattern()
