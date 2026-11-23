print("        A BASIC CALCULATOR")
a=int(input("ENTER 1st NUMBER:"))
b=int(input("ENTER 2nd NUMBER:"))
c=input("ENTER A OPERATOR:")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("invalid operator")
