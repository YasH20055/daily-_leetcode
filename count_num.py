a = int(input("Enter number: "))
count = 0

while a > 0:
    count += 1
    a = a // 10

print(count)