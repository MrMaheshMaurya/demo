"""
9. Count Vowels Function
String me vowels count karo.
"""


def vowels():
    str = "mahesh"
    count = 0
    for i in range(0, len(str)):
        # print(str[i])
        if (
            str[i] == "a"
            or str[i] == "e"
            or str[i] == "i"
            or str[i] == "o"
            or str[i] == "u"
        ):
            count += 1
            print(str[i])
    print(count)


vowels()
