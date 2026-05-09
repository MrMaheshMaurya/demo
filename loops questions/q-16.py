"""
accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself.
Ex - 6 = 1, 2, 3 = 6
"""

num = int(input("enter the your input -> "))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += i


sum = count - num
if sum == num:
    print(f"{num} nunber is a perfect number")
else:
    print(f"{num} nunber is not a perfect number")
