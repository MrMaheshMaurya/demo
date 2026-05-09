# Count karo ki kisi number me kitne digits hain


num = int(input("Enter your Number = "))
count = 0
while num != 0:
    num //= 10
    count += 1

print(count)
