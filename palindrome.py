a = int(input("Enter number: "))
p=a
reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

print(reverse)
if p==reverse:
    print("palindrome")
    

else:
     print("not palindrome")