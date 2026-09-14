# create a simple calculator
try:
    a = float(input("enter first num :"))
    b = float(input("enter second num :"))
except ValueError:
    print("Invalid number input")
    print("thank you for using calculator")
    raise SystemExit

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
try:
    c = int(input("enter your choice :"))
except ValueError:
    print("invalid choice")
    print("thank you for using calculator")
    raise SystemExit

if c==1:
    print("addition is : ", a+b)
elif c==2:
    print("sub is :", a-b)
elif c==3:
    print("multiplication is :", a*b)
elif c==4:
    try:
        print("division is :", a/b)
    except ZeroDivisionError:
        print("Error: division by zero")
else:
    print("invalid choice")

print("thank you for using calculator")