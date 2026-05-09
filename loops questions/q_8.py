# Factorial find karo (e.g., 5! = 120

fact = 1
n = int(input("please Enter the your number = "))
for i in range(n, 0, -1):
    fact *= i

print(fact)
