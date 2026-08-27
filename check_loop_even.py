a = int(input("Enter number: "))

t = 0
c=0

while a > 0:
    d=a%10
    t=d
    a=a//10
    if t%2==0:
        c+=1
    # get digit
    # add digit to total
    # remove digit

print(c)