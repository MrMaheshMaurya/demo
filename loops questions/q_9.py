# Ek number lo aur check karo prime hai ya nahi


# num = int(input("please enter the your number = "))

# for i in "num":
#     for j in "num":
#         if i % j == 0:
#             break
#     else:
#         print(i)

# for i in range(2, num):
#     if num % 2 == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")


# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


num = int(input("Enter tell your number ->"))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print(count)

if count == 2:
    print(f"number is a prime number ")
else:
    print(f"number is not a prime number ")
