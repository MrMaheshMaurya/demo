# 1 se 100 tak numbers print karo jo 3 se divisible ho


for i in range(1, 100 + 1):
    if i % 3 == 0:
        print(i)


i = 1
n = 100

while i < n:
    if i % 3 == 0:
        print(i)
    i += 1
