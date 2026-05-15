"""
Check Anagram
ek funtion bnao jo check kre 2 stinrg anagram hai ya nhi.
"""


def check_anagram():
    str1 = input("enter the first string = ")
    str2 = input("enter the second string = ")
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if len(str1) == len(str2):
        if sorted_str1 == sorted_str2:
            print("this string anagram")
        else:
            print("this string not anagram")
    else:
        print("this string not anagram")


check_anagram()
