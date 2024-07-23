#recursion
def fact(n):
    if(n<0):
        print("invalid")
    elif(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a num"))
f=fact(n)
print(f)

