a=int(input("enter a num:"))
c=0

for i in range(1, a+1):
    if i%3==0:
        c+=i
print(c)
