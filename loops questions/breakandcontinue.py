total = 0
while True:
    num = int(input("enter the number = "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num

print(total)
